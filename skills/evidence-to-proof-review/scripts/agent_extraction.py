"""Import attributed extraction data without executing supplied tools or commands.

The caller supplies exact transcriptions with declared original coordinates.
Validation checks the data contract and hash binding, not transcription truth.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import corpus

LIMITATION = ('Agent-produced transcription and original coordinates require explicit material '
              'inspection of the original source before a direct formal verdict. Import validation '
              'does not establish fidelity, authenticity, semantic completeness, or truth.')


def _text(value, label):
    if not isinstance(value,str) or not value.strip():
        raise ValueError(label+' must be a nonempty string')
    return value


def _object(value, keys, label):
    if not isinstance(value,dict) or set(value)!=set(keys):
        raise ValueError(label+' must contain exactly: '+', '.join(keys))
    return value


def _strings(value,label,nonempty=False):
    if not isinstance(value,list) or (nonempty and not value):
        raise ValueError(label+' must be a '+('nonempty ' if nonempty else '')+'list')
    for item in value:_text(item,label+' item')
    return value


def _locator(value):
    if not isinstance(value,dict):raise ValueError('locator must be an object')
    kind=value.get('kind')
    fields={'line':('start_line','end_line'),'page':('page',),'section':('section',),
            'cell':('sheet','cell'),'sheet':('sheet',),'timestamp':('timestamp',),
            'byte':('start_byte','end_byte'),'other':('coordinate_system','coordinate')}
    if not isinstance(kind,str) or kind not in fields:
        raise ValueError('locator.kind must identify original line/page/section/cell/sheet/timestamp/byte/other coordinates')
    required={'kind',*fields[kind]}
    if not required<=set(value) or set(value)-required-{'description'}:
        raise ValueError('locator must contain its original coordinate fields and optional description')
    for key in fields[kind]:
        item=value[key]
        if kind in {'line','page','byte'}:
            if type(item) is not int or item < (0 if kind=='byte' else 1):
                raise ValueError('locator numeric coordinates must be valid original-source positions')
        else:_text(item,'locator.'+key)
    if kind=='line' and value['end_line']<value['start_line']:raise ValueError('Reversed original line range')
    if kind=='byte' and value['end_byte']<=value['start_byte']:raise ValueError('Empty or reversed original byte range')
    if 'description' in value:_text(value['description'],'locator.description')
    return value


def validate_bundle(value, original_sha):
    _object(value,('schema_version','original_sha256','method','tool','reviewer','coverage','segments'),'bundle')
    if type(value['schema_version']) is not int or value['schema_version']!=1:
        raise ValueError('Agent extraction schema_version must be 1')
    if value['original_sha256']!=original_sha:
        raise ValueError('Agent extraction original_sha256 does not match the immutable original snapshot')
    for key,fields in (('method',('name','description')),('tool',('name','version'))):
        _object(value[key],fields,key)
        for field in fields:_text(value[key][field],key+'.'+field)
    _text(value['reviewer'],'reviewer')
    coverage=_object(value['coverage'],('status','scope','limitations'),'coverage')
    if coverage['status'] not in ('complete','partial'):raise ValueError('coverage.status must be complete or partial')
    _text(coverage['scope'],'coverage.scope')
    _strings(coverage['limitations'],'coverage.limitations',True)
    if not isinstance(value['segments'],list) or not value['segments']:
        raise ValueError('segments must be a nonempty list; wholly unavailable extraction remains blocked')
    seen=set()
    for seg in value['segments']:
        _object(seg,('anchor','quote','locator','uncertainty'),'segment')
        anchor=_text(seg['anchor'],'anchor')
        if not re.fullmatch(r'[A-Za-z][A-Za-z0-9_.:-]{0,199}',anchor):raise ValueError('Unsafe extraction anchor')
        if anchor in seen:raise ValueError('Duplicate extraction anchor: '+anchor)
        seen.add(anchor)
        quote=_text(seg['quote'],'quote')
        if re.search(r'<a\s',quote,re.I):raise ValueError('Quote must not contain HTML anchor definitions')
        _locator(seg['locator']);_strings(seg['uncertainty'],'uncertainty')
    return value


def import_extraction(root,document_id,bundle_path):
    """Replace effective extraction, retaining originals and all prior attempts.

    This accepts source, report, and brief documents already in the catalog.
    Exact repetition is a no-op, including after native resume/retry. Every
    effective change invalidates prior proof results and semantic reviews.
    """
    root=Path(root).resolve();corpus.verify(root)
    docs=corpus.inventory(root)
    document=next((d for d in docs if d['id']==document_id),None)
    if document is None:raise ValueError('Unknown document ID')
    original=root/document['original']
    if corpus.sha(original)!=document['original_sha']:raise ValueError('Original snapshot changed')
    raw=Path(bundle_path).read_bytes()
    try:value=json.loads(raw.decode('utf-8'))
    except (UnicodeError,ValueError) as exc:raise ValueError('Bundle must be valid UTF-8 JSON') from exc
    validate_bundle(value,document['original_sha'])
    canonical=json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')
    digest=hashlib.sha256(canonical).hexdigest()
    prior_import=json.loads(document['tools']).get('agent_extraction',{})
    if prior_import.get('bundle_sha256')==digest:
        return {'workspace':str(root),'document_id':document_id,'changed':False,
                'coverage':corpus.read(root/'ingestion.json'),'proof_check_status':'unchanged'}
    target=(root/document['logical']).resolve()
    if not target.is_relative_to(root/'input'):raise ValueError('Unsafe catalog logical path')
    prior_manifest=corpus.sha(root/'manifest.json')
    history=root/'history';history.mkdir(exist_ok=True)
    operation=Path(tempfile.mkdtemp(prefix='agent-extraction-',dir=history))
    action={'action':'import-agent-extraction','document_id':document_id,'at':corpus.stamp(),
            'original_sha256':document['original_sha'],'bundle_sha256':digest,
            'prior_manifest_sha256':prior_manifest,'state':'started'}
    corpus.save(operation/'action.json',action)
    shutil.copyfile(root/'manifest.json',operation/'prior-manifest.json')
    if target.exists():shutil.copyfile(target,operation/'prior-derived-text.md')
    for name in ('findings.json','claims.json','source-ledger.jsonl','ingestion.json','invalidation.json'):
        if (root/name).exists():shutil.copyfile(root/name,operation/name)
    parent=root/'extraction'/document_id;parent.mkdir(parents=True,exist_ok=True)
    attempt=Path(tempfile.mkdtemp(prefix='agent-attempt-',dir=parent))
    (attempt/'bundle.json').write_bytes(raw)
    segments=[]
    for seg in value['segments']:
        locator={**seg['locator'],'original':document['original'],
                 'original_sha256':document['original_sha'],
                 'artifact_directory':attempt.relative_to(root).as_posix(),
                 'extraction_bundle_sha256':digest,'extraction_reviewer':value['reviewer'],
                 'coordinate_interpretation':'Declared original-source coordinates; fidelity requires original-source inspection.'}
        segments.append({**seg,'locator':locator,'uncertainty':[LIMITATION,*seg['uncertainty']]})
    derived=''.join('<a id="'+seg['anchor']+'"></a>\n'+seg['quote']+'\n\n' for seg in segments)
    (attempt/'extracted.md').write_text(derived,encoding='utf-8')
    status='ready' if value['coverage']['status']=='complete' else 'partial'
    metadata={'agent_extraction':{'original_sha256':document['original_sha'],'bundle_sha256':digest,
              'method':value['method'],'tool':value['tool'],'reviewer':value['reviewer'],
              'coverage':value['coverage'],'artifact_directory':attempt.relative_to(root).as_posix()}}
    with corpus.connection(root,True) as db:
        db.execute('BEGIN IMMEDIATE')
        for row in db.execute('SELECT id,text FROM chunks WHERE document_id=?',(document_id,)).fetchall():
            db.execute("INSERT INTO search(search,rowid,text) VALUES('delete',?,?)",row)
        db.execute('DELETE FROM chunks WHERE document_id=?',(document_id,))
        db.execute('DELETE FROM segments WHERE document_id=?',(document_id,))
        for seg in segments:
            db.execute('INSERT INTO segments VALUES (?,?,?,?,?,?,?)',(document['logical'],seg['anchor'],document_id,
                seg['quote'],json.dumps(seg['locator']),'agent-extraction',json.dumps(seg['uncertainty'])))
            for start in range(0,len(seg['quote']),1800):
                end=min(start+2000,len(seg['quote']));chunk=seg['quote'][start:end]
                cursor=db.execute('INSERT INTO chunks(path,anchor,document_id,start_char,end_char,text) VALUES(?,?,?,?,?,?)',
                    (document['logical'],seg['anchor'],document_id,start,end,chunk))
                db.execute('INSERT INTO search(rowid,text) VALUES(?,?)',(cursor.lastrowid,chunk))
        target.parent.mkdir(parents=True,exist_ok=True);target.write_text(derived,encoding='utf-8')
        db.execute('UPDATE documents SET status=?,warnings=?,tools=?,extraction_sha=? WHERE id=?',
            (status,json.dumps([LIMITATION,*value['coverage']['limitations']]),json.dumps(metadata),corpus.sha(target),document_id))
    archived=[]
    for name in ('proof-results.json','logs','checks','environment.lock','audit-report.md','coverage.md',
                 'semantic-review.md','extraction-review.json','revision-review.json','coverage-acknowledgement.json','export-manifest.json'):
        if (root/name).exists():
            shutil.move(root/name,operation/name);archived.append(name)
    findings=corpus.read(root/'findings.json') if (root/'findings.json').exists() else []
    corpus.save(root/'invalidation.json',{'changed_document':document_id,
        'affected_claims':sorted({f['claim_id'] for f in findings}),
        'technical_results':'all invalidated',
        'reason':'Agent extraction changed effective evidence; every finding requires renewed review.',
        'previous_state':operation.relative_to(root).as_posix()})
    result=corpus.finalize(root,[document_id],prior_manifest)
    corpus.save(operation/'action.json',{**action,'state':'recorded','archived':archived,
                'current_manifest_sha256':corpus.sha(root/'manifest.json')})
    corpus.verify(root)
    return {**result,'document_id':document_id,'changed':True,
            'history':operation.relative_to(root).as_posix(),'archived':archived,
            'extraction_bundle':(attempt/'bundle.json').relative_to(root).as_posix(),
            'proof_check_status':'not_run','limitations':LIMITATION}
