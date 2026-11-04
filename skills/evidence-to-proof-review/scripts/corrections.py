"""Retained, attributed manual transcriptions layered over immutable extraction.

Calling transcribe explicitly attests that the named reviewer inspected the
original visual/XML source. The helper records that attestation; it cannot
perform or establish that inspection itself. Original passages remain available.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import corpus


LIMITATION = ('Manual transcription is a reviewer-attributed interpretation of the original source, '
              'not machine-certified textual fidelity or source authenticity. Inherited coordinates '
              'identify the original passage; inherited OCR words and confidence describe the '
              'uncorrected extraction, not the manually transcribed wording.')


def _nonempty(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{name} must be a nonempty string')
    return value.strip()


def transcribe(root, path, anchor, text_file, reviewer, reason):
    """Append a reviewed segment without replacing the original passage.

    The correction preserves original bytes, prior extraction artifacts and the
    author's exact UTF-8 file. Only outer whitespace/BOM is removed from the
    indexed quotation. A direct acceptance record covers the new segment alone.
    Existing proof outputs are archived and must be rerun. Partial document
    coverage remains partial; callers must separately address coverage gaps.
    """
    root = Path(root).resolve()
    reviewer = _nonempty(reviewer, 'reviewer')
    reason = _nonempty(reason, 'reason')
    path = _nonempty(path, 'path')
    anchor = _nonempty(anchor, 'anchor')
    corpus.verify(root)
    passage = corpus.passage(root, path, anchor)
    if passage is None:
        raise ValueError('The source passage does not exist in the verified corpus')
    locator = passage['locator']
    if not locator.get('original') or not locator.get('original_sha256'):
        raise ValueError('The passage lacks original-source coordinates and a source fingerprint')
    target = (root / path).resolve()
    original = (root / locator['original']).resolve()
    if Path(path).is_absolute() or not target.is_relative_to(root/'input') or not original.is_relative_to(root/'input/originals'):
        raise ValueError('The logical passage and original snapshot must stay inside their input directories')
    if corpus.sha(original) != locator['original_sha256']:
        raise ValueError('The original source fingerprint does not match the passage')
    documents = corpus.inventory(root)
    if any(document['status'] == 'pending' for document in documents):
        raise ValueError('Finish pending ingestion before recording a manual transcription')
    document = next(d for d in documents if d['id'] == passage['document_id'])
    manual_file = Path(text_file).resolve()
    if not manual_file.is_file():
        raise ValueError('Manual transcription text_file must be an existing UTF-8 file')
    raw_text = manual_file.read_bytes()
    try:
        quote = raw_text.decode('utf-8-sig').strip()
    except UnicodeError as exc:
        raise ValueError('Manual transcription must be valid UTF-8; no encoding is guessed') from exc
    if not quote:
        raise ValueError('Manual transcription text must not be empty')
    # Anchor markup inside the quote would make the derived Markdown ambiguous.
    # Literal plain quotes, tabs, and line breaks remain valid text.
    if '<a ' in quote or '<a\n' in quote:
        raise ValueError('Manual transcription must contain passage text, not HTML anchor definitions')
    review_file = root/'extraction-review.json'
    reviews = corpus.read(review_file) if review_file.exists() else {'reviews': []}
    if not isinstance(reviews, dict) or not isinstance(reviews.get('reviews'), list):
        raise ValueError('Existing extraction-review.json must contain a reviews array')
    with corpus.connection(root) as db:
        occupied = {row[0] for row in db.execute('SELECT anchor FROM segments WHERE path=?', (path,))}
    number = 1
    new_anchor = f'{anchor}-reviewed-{number:04d}'
    while new_anchor in occupied:
        number += 1
        new_anchor = f'{anchor}-reviewed-{number:04d}'
    text_sha = hashlib.sha256(raw_text).hexdigest()
    quote_sha = hashlib.sha256(quote.encode('utf-8')).hexdigest()
    snapshot_name = hashlib.sha256(new_anchor.encode('utf-8')).hexdigest()+'.txt'
    snapshot = root/'input/manual-transcriptions'/passage['document_id']/snapshot_name
    if snapshot.exists():
        raise ValueError('A transcription snapshot already exists for the new anchor')
    timestamp = corpus.stamp()
    source_anchor = locator.get('root_source_anchor', locator.get('source_anchor', anchor))
    corrected_locator = dict(locator)
    corrected_locator.update(source_anchor=anchor, root_source_anchor=source_anchor,
        reviewer=reviewer, reason=reason, reviewed_at=timestamp,
        transcription_snapshot=snapshot.relative_to(root).as_posix(),
        transcription_file_sha256=text_sha,
        transcription_normalization='UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.',
        coordinate_interpretation=LIMITATION)
    if path == 'input/report.md':
        corrected_locator['parent_report_anchor'] = source_anchor
    uncertainty = [LIMITATION]
    acceptance = {'path': path, 'anchor': new_anchor, 'decision': 'accepted',
        'reviewer': reviewer, 'reason': reason, 'source_sha256': locator['original_sha256'],
        'segment_sha256': quote_sha, 'reviewed_at': timestamp,
        'attestation': 'The caller explicitly attests original-source inspection for this manual transcription.',
        'source_anchor': anchor}
    action = {'action': 'manual-transcription', 'at': timestamp, 'path': path,
        'source_anchor': anchor, 'root_source_anchor': source_anchor, 'new_anchor': new_anchor,
        'document_id': passage['document_id'], 'reviewer': reviewer, 'reason': reason,
        'source_sha256': locator['original_sha256'], 'source_segment_sha256': hashlib.sha256(passage['quote'].encode('utf-8')).hexdigest(),
        'new_segment_sha256': quote_sha, 'transcription_file_sha256': text_sha,
        'transcription_snapshot': snapshot.relative_to(root).as_posix(),
        'interpretation_limit': LIMITATION,
        'technical_results': 'Prior successes invalidated; no new proof check has been run.'}
    old_derived = target.read_bytes()
    addition = ('\n\n<a id="'+new_anchor+'"></a>\n'+quote+'\n').encode('utf-8')
    new_derived = old_derived + addition
    # Retain an operation journal even if filesystem/SQLite mutation is interrupted.
    operation_dir = Path(tempfile.mkdtemp(prefix='transcription-', dir=_history_directory(root)))
    corpus.save(operation_dir/'action.json', {**action, 'state': 'started'})
    shutil.copyfile(root/'manifest.json', operation_dir/'prior-manifest.json')
    (operation_dir/'prior-derived-text.md').write_bytes(old_derived)
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    snapshot.write_bytes(raw_text)
    with corpus.connection(root, True) as db:
        db.execute('BEGIN IMMEDIATE')
        db.execute('INSERT INTO segments VALUES (?,?,?,?,?,?,?)',
            (path, new_anchor, passage['document_id'], quote, json.dumps(corrected_locator),
             'manual-transcription', json.dumps(uncertainty)))
        for start in range(0, len(quote), 1800):
            end = min(start+2000, len(quote))
            cursor = db.execute('INSERT INTO chunks(path,anchor,document_id,start_char,end_char,text) VALUES(?,?,?,?,?,?)',
                (path, new_anchor, passage['document_id'], start, end, quote[start:end]))
            db.execute('INSERT INTO search(rowid,text) VALUES(?,?)', (cursor.lastrowid, quote[start:end]))
        target.write_bytes(new_derived)
        db.execute('UPDATE documents SET extraction_sha=? WHERE id=?',
                   (hashlib.sha256(new_derived).hexdigest(), passage['document_id']))
    reviews['reviews'].append(acceptance)
    corpus.save(review_file, reviews)
    with (root/'manual-transcriptions.jsonl').open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(action, ensure_ascii=False)+'\n')
    # Old reports/logs are evidence of earlier executions, never current success.
    archived = []
    for name in ('proof-results.json', 'logs', 'checks', 'environment.lock',
                 'audit-report.md', 'coverage.md', 'semantic-review.md'):
        existing = root/name
        if existing.exists():
            shutil.move(str(existing), str(operation_dir/name))
            archived.append(name)
    corpus.manifest(root)
    refreshed = corpus.resume(root)
    if refreshed['coverage']['processed_this_batch']:
        raise ValueError('Unexpected pending ingestion processed while recording transcription')
    corpus.save(operation_dir/'action.json', {**action, 'state': 'recorded', 'archived': archived})
    corpus.verify(root)
    return {'workspace': str(root), 'path': path, 'source_anchor': anchor,
        'anchor': new_anchor, 'method': 'manual-transcription', 'source_sha256': locator['original_sha256'],
        'segment_sha256': quote_sha, 'document_status': document['status'],
        'transcription_snapshot': snapshot.relative_to(root).as_posix(),
        'history': operation_dir.relative_to(root).as_posix(), 'archived': archived,
        'review_attestation_recorded': True, 'proof_check_status': 'not_run',
        'limitations': LIMITATION}


def _history_directory(root):
    history = root/'history'
    history.mkdir(exist_ok=True)
    return history
