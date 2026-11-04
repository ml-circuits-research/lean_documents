"""Versioned, resumable corpus ingestion and on-disk evidence retrieval.

No semantic verdict is produced here. Search results never establish coverage.
All original bytes, converter artifacts, and previous revisions are retained.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import shutil
import sqlite3
import tempfile
import time
from datetime import datetime, timezone
from extractors import extract_document
import contracts


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''): h.update(block)
    return h.hexdigest()


def save(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')


def read(path): return json.loads(Path(path).read_text())
def stamp(): return datetime.now(timezone.utc).isoformat()


class ClosingConnection(sqlite3.Connection):
    def __exit__(self, exc_type, exc_value, traceback):
        try:
            return super().__exit__(exc_type, exc_value, traceback)
        finally:
            self.close()


def connection(root, writable=False):
    path = Path(root) / 'input/index.sqlite3'
    return sqlite3.connect(path if writable else f'file:{path}?mode=ro', uri=not writable, factory=ClosingConnection)


def manifest(root):
    files = {p.relative_to(root).as_posix(): {'sha256': sha(p), 'bytes': p.stat().st_size}
             for p in sorted((root/'input').rglob('*')) if p.is_file() and p != root/'input/manifest.json'}
    value = {'schema_version': 2, 'algorithm': 'sha256', 'index': 'input/index.sqlite3', 'files': files}
    save(root/'input/manifest.json', value); save(root/'manifest.json', value)


def verify(root):
    root = Path(root)
    value = read(root/'manifest.json')
    if value != read(root/'input/manifest.json'): raise ValueError('Manifest copies disagree')
    actual = {p.relative_to(root).as_posix() for p in (root/'input').rglob('*') if p.is_file() and p != root/'input/manifest.json'}
    if actual != set(value['files']): raise ValueError('Input inventory changed outside a recorded revision')
    for rel, info in value['files'].items():
        p=(root/rel).resolve()
        if not p.is_relative_to(root.resolve()) or sha(p)!=info['sha256']: raise ValueError(f'Input integrity mismatch: {rel}')
    lock=root/'extraction-lock.json'
    if not lock.exists() and (root/'extraction').exists() and any(p.is_file() for p in (root/'extraction').rglob('*')):
        raise ValueError('Missing extraction integrity lock; explicit recovery is required')
    if lock.exists():
        expected=read(lock)['files']
        actual={p.relative_to(root).as_posix() for p in (root/'extraction').rglob('*') if p.is_file()}
        if actual!=set(expected):raise ValueError('Extraction artifact inventory changed')
        for rel,digest in expected.items():
            p=(root/rel).resolve()
            if not p.is_relative_to(root.resolve()) or sha(p)!=digest:raise ValueError(f'Extraction artifact changed: {rel}')
    return value


def _schema(db):
    db.executescript('''
    PRAGMA journal_mode=DELETE;
    CREATE TABLE documents(id TEXT PRIMARY KEY, role TEXT, original TEXT, logical TEXT UNIQUE,
      external TEXT, original_sha TEXT, status TEXT, warnings TEXT, tools TEXT, extraction_sha TEXT);
    CREATE TABLE segments(path TEXT, anchor TEXT, document_id TEXT, quote TEXT, locator TEXT,
      method TEXT, uncertainty TEXT, PRIMARY KEY(path,anchor));
    CREATE TABLE chunks(id INTEGER PRIMARY KEY, path TEXT, anchor TEXT, document_id TEXT,
      start_char INTEGER, end_char INTEGER, text TEXT);
    CREATE VIRTUAL TABLE search USING fts5(text, content='chunks', content_rowid='id');
    ''')


def prepare(args):
    temp_root=Path(args.temp_root or Path.cwd()/'tmp').resolve();temp_root.mkdir(parents=True,exist_ok=True)
    sources=[Path(p).resolve() for p in args.sources]
    for source in sources:
        if not source.exists(): raise ValueError(f'Missing source: {source}')
        if source.is_dir() and temp_root.is_relative_to(source):
            raise ValueError('Temporary root must be outside supplied source directories to avoid recursive ingestion')
    brief = getattr(args, 'brief', None)
    inventory=([('brief',Path(brief).resolve(),'input/brief.md')] if brief else []) + [('report',Path(args.report).resolve(),'input/report.md')]
    used=set()
    for n,source in enumerate(sources,1):
        paths=sorted(p for p in source.rglob('*') if p.is_file()) if source.is_dir() else [source]
        for p in paths:
            rel=p.relative_to(source).as_posix() if source.is_dir() else p.name
            if p.suffix.lower() not in {'.md','.markdown','.txt','.text','.csv'}: rel+='.md'
            candidate=rel; serial=0
            while any(candidate==x or candidate.startswith(x+'/') or x.startswith(candidate+'/') for x in used):
                serial+=1;candidate=f'source-{n}-{serial}/{rel}'
            used.add(candidate);inventory.append(('source',p,'input/sources/'+candidate))
    if any(not p.is_file() for _,p,_ in inventory): raise ValueError('Brief/report must be files')
    root=Path(tempfile.mkdtemp(prefix='claim-audit-',dir=temp_root));(root/'input/originals').mkdir(parents=True);(root/'models').mkdir()
    db=connection(root,True);_schema(db)
    catalog=[]
    for n,(role,path,logical) in enumerate(inventory,1):
        ident=f'D{n:05d}';original=f'input/originals/{ident}{path.suffix.lower()}'
        shutil.copyfile(path,root/original)
        db.execute('INSERT INTO documents VALUES (?,?,?,?,?,?,?,?,?,?)',
            (ident,role,original,logical,str(path),sha(root/original),'pending','[]','{}',None))
        catalog.append({'id':ident,'role':role,'original':original,'logical':logical,'external':str(path),'original_sha':sha(root/original)})
    db.commit();db.close()
    save(root/'input/catalog.json',catalog)
    save(root/'run.json',{'schema_version':2,'workspace':str(root),'created_at':stamp(),
        'retention':'Retain until explicit user cleanup request','extraction':{
        'ocr_language':getattr(args,'ocr_language','eng'),'timeout':getattr(args,'extract_timeout',60),
        'max_pages':getattr(args,'max_pages',None)},'limitations':'Retrieval is not exhaustive semantic review; extraction is not authenticity.'})
    save(root/'input/audit-policy.json', {'contract_version':2, 'brief_origin':'provided' if brief else 'inferred',
        'default_mandate':'Audit every material report claim and its justification against the supplied sources; derive and disclose criteria without assuming the claim.'})
    manifest(root)
    return resume(root,max_documents=getattr(args,'max_documents',None),max_seconds=getattr(args,'max_seconds',None))


def resume(root,*,max_documents=None,max_seconds=None,retry=False,max_pages=None,recover=False):
    root=Path(root).resolve()
    if recover:recover_workspace(root)
    verify(root);prior_manifest_sha=sha(root/'manifest.json');started=time.monotonic()
    if max_documents is not None and max_documents<1: raise ValueError('max_documents must be positive')
    if max_seconds is not None and max_seconds<=0: raise ValueError('max_seconds must be positive')
    settings=read(root/'run.json')['extraction']
    if max_pages is not None: settings['max_pages']=max_pages
    db=connection(root,True);db.row_factory=sqlite3.Row
    candidates=db.execute("SELECT * FROM documents WHERE status='pending'"+(" OR status IN ('blocked','partial')" if retry else '')+" ORDER BY id").fetchall()
    processed=[]
    for row in candidates:
        if (max_documents is not None and len(processed)>=max_documents) or (max_seconds is not None and time.monotonic()-started>=max_seconds): break
        original=root/row['original']
        if sha(original)!=row['original_sha']: db.close();raise ValueError('Original snapshot changed')
        attempt=root/'extraction'/row['id'];attempt.mkdir(parents=True,exist_ok=True)
        artifact=Path(tempfile.mkdtemp(prefix='attempt-',dir=attempt))
        result=extract_document(original,artifact,**settings)
        segments=[]
        for seg in result['segments']:
            locator={**seg['locator'],'original':row['original'],'original_sha256':row['original_sha'],'artifact_directory':artifact.relative_to(root).as_posix()}
            segments.append({**seg,'locator':locator})
        anchors={seg['anchor'] for seg in segments}
        retained=[]
        for prior in db.execute("SELECT * FROM segments WHERE document_id=? AND method='manual-transcription' ORDER BY rowid",(row['id'],)):
            locator=json.loads(prior['locator'])
            if locator.get('original_sha256')!=row['original_sha']:
                result['warnings'].append(f"Manual transcription {prior['anchor']} was invalidated by changed original bytes; its authored snapshot and parent workspace remain retained.")
                continue
            if prior['anchor'] in anchors:
                db.close()
                # Keep the rejected converter attempt without changing its raw output.
                save(root/'extraction-lock.json',{'files':{p.relative_to(root).as_posix():sha(p) for p in sorted((root/'extraction').rglob('*')) if p.is_file()}})
                raise ValueError(f"Extraction anchor collides with retained manual transcription: {prior['anchor']}")
            anchors.add(prior['anchor'])
            retained.append({'anchor':prior['anchor'],'quote':prior['quote'],'locator':locator,
                'method':prior['method'],'uncertainty':json.loads(prior['uncertainty'])})
        # Reviewed overlays retain their original coordinates and review bindings.
        # The new converter artifact remains an unmodified machine extraction.
        derived=result['text']+''.join(f'\n\n<a id="{seg["anchor"]}"></a>\n{seg["quote"]}\n' for seg in retained)
        segments.extend(retained)
        target=root/row['logical'];target.parent.mkdir(parents=True,exist_ok=True);target.write_text(derived)
        old=db.execute('SELECT id,text FROM chunks WHERE document_id=?',(row['id'],)).fetchall()
        for c in old:db.execute("INSERT INTO search(search,rowid,text) VALUES('delete',?,?)",(c['id'],c['text']))
        db.execute('DELETE FROM chunks WHERE document_id=?',(row['id'],));db.execute('DELETE FROM segments WHERE document_id=?',(row['id'],))
        for seg in segments:
            locator=seg['locator']
            db.execute('INSERT INTO segments VALUES (?,?,?,?,?,?,?)',(row['logical'],seg['anchor'],row['id'],seg['quote'],json.dumps(locator),seg['method'],json.dumps(seg['uncertainty'])))
            # Overlap preserves boundary context; original segment remains available.
            text=seg['quote']
            for start in range(0,len(text),1800):
                end=min(start+2000,len(text));chunk=text[start:end]
                cur=db.execute('INSERT INTO chunks(path,anchor,document_id,start_char,end_char,text) VALUES(?,?,?,?,?,?)',(row['logical'],seg['anchor'],row['id'],start,end,chunk))
                db.execute('INSERT INTO search(rowid,text) VALUES(?,?)',(cur.lastrowid,chunk))
        db.execute('UPDATE documents SET status=?,warnings=?,tools=?,extraction_sha=? WHERE id=?',(result['status'],json.dumps(result['warnings']),json.dumps(result['tools']),sha(target),row['id']))
        db.commit();processed.append(row['id'])
        # Atomic per-document checkpoint: a killed converter leaves pending work;
        # committed records are preserved even if the batch stops afterward.
    rows=[dict(r) for r in db.execute('SELECT * FROM documents ORDER BY id')]
    with (root/'source-ledger.jsonl').open('w') as stream:
        for seg in db.execute('SELECT * FROM segments ORDER BY document_id,anchor'):
            record=dict(seg);record['locator']=json.loads(record['locator']);record['uncertainty']=json.loads(record['uncertainty'])
            stream.write(json.dumps(record,ensure_ascii=False)+'\n')
    report={r['anchor']:r['quote'] for r in db.execute("SELECT anchor,quote FROM segments WHERE path='input/report.md'")}
    save(root/'input/report-ledger.json',report)
    db.close();manifest(root)
    current_manifest_sha=sha(root/'manifest.json')
    if current_manifest_sha!=prior_manifest_sha and (root/'semantic-review.md').is_file():
        history=root/'history';history.mkdir(exist_ok=True)
        prior_review=Path(tempfile.mkdtemp(prefix='ingestion-review-',dir=history))
        shutil.move(root/'semantic-review.md',prior_review/'semantic-review.md')
        save(prior_review/'invalidation.json',{
            'reason':'Ingestion changed the reviewed corpus; a new semantic review is required before export.',
            'prior_manifest_sha256':prior_manifest_sha, 'current_manifest_sha256':current_manifest_sha,
            'processed_documents':processed, 'at':stamp()})
    if (root/'input/audit-policy.json').is_file(): contracts.initialize(root)
    coverage={'updated_at':stamp(),'total_documents':len(rows),'processed_this_batch':processed,
        'complete':all(r['status']=='ready' for r in rows),'documents':[
        {k:json.loads(r[k]) if k in {'warnings','tools'} else r[k] for k in ('id','role','original','logical','external','original_sha','status','warnings','tools','extraction_sha')} for r in rows],
        'elapsed_seconds':time.monotonic()-started,'budget':{'max_documents':max_documents,'max_seconds':max_seconds},
        'coverage_meaning':'Extraction coverage only, not claim review completeness or OCR accuracy'}
    save(root/'ingestion.json',coverage)
    save(root/'extraction-lock.json',{'files':{p.relative_to(root).as_posix():sha(p) for p in sorted((root/'extraction').rglob('*')) if p.is_file()}})
    return {'workspace':str(root),'coverage':coverage,'source_index':'input/index.sqlite3','report_ledger':'input/report-ledger.json'}


def passage(root,path,anchor):
    with connection(root) as db:
        row=db.execute('SELECT quote,locator,method,uncertainty,document_id FROM segments WHERE path=? AND anchor=?',(path,anchor)).fetchone()
    if row is None:return None
    return dict(quote=row[0],locator=json.loads(row[1]),method=row[2],uncertainty=json.loads(row[3]),document_id=row[4])


def search(root,query,limit=20,offset=0):
    root=Path(root).resolve();verify(root)
    if not 1<=limit<=500 or offset<0:raise ValueError('Use limit 1..500 and nonnegative offset')
    with connection(root) as db:
        db.row_factory=sqlite3.Row
        total=db.execute('SELECT count(*) FROM search WHERE search MATCH ?',(query,)).fetchone()[0]
        matches=[dict(r) for r in db.execute('SELECT chunks.*,bm25(search) AS rank FROM search JOIN chunks ON chunks.id=search.rowid WHERE search MATCH ? ORDER BY rank,chunks.id LIMIT ? OFFSET ?',(query,limit,offset))]
    result={'query':query,'total_matching_chunks':total,'offset':offset,'limit':limit,'results':matches,
        'limitations':'Ranked retrieval is not exhaustive semantic review; inspect full passages and inventory for exceptions.'}
    with (root/'search-history.jsonl').open('a') as f:f.write(json.dumps({'at':stamp(),**result})+'\n')
    return result


def inventory(root):
    with connection(root) as db:
        db.row_factory=sqlite3.Row
        return [dict(r) for r in db.execute('SELECT * FROM documents ORDER BY id')]


def assert_reviewable(root,findings):
    root=Path(root)
    incomplete=[d for d in inventory(root) if d['status']!='ready']
    acknowledgements=read(root/'coverage-acknowledgement.json') if (root/'coverage-acknowledgement.json').exists() else {}
    acknowledged={x.get('document_id') for x in acknowledgements.get('documents',[]) if x.get('reason') and x.get('impact')}
    if any(d['id'] not in acknowledged for d in incomplete):
        raise ValueError('Incomplete ingestion must be resumed or explicitly accounted for in coverage-acknowledgement.json (document_id, reason, impact)')
    reviews=read(root/'extraction-review.json').get('reviews',[]) if (root/'extraction-review.json').exists() else []
    for finding in findings:
        for evidence in finding['evidence']+[{'path':'input/report.md','anchor':finding['report_anchor']}]:
            seg=passage(root,evidence['path'],evidence['anchor'])
            if not seg or not seg['uncertainty']:continue
            accepted=any(r.get('path')==evidence['path'] and r.get('anchor')==evidence['anchor'] and r.get('decision')=='accepted' and r.get('reviewer') and r.get('reason') and r.get('source_sha256')==seg['locator']['original_sha256'] and r.get('segment_sha256')==hashlib.sha256(seg['quote'].encode()).hexdigest() for r in reviews)
            if not accepted and finding['formal_status'] in {'proved','refuted'}:
                raise ValueError(f'{finding["claim_id"]}: uncertain extraction requires explicit original-source review before direct formal verdict')
    invalidation=root/'invalidation.json'
    if invalidation.exists():
        state=read(invalidation);review=read(root/'revision-review.json') if (root/'revision-review.json').exists() else {}
        if review.get('revision_manifest_sha256')!=sha(root/'manifest.json') or not set(state['affected_claims'])<=set(review.get('reviewed_claims',[])):
            raise ValueError('Changed dependencies require revision-review.json with current manifest hash and every affected claim')


def _affected_claims(findings, documents, selected, mapping):
    """Narrow invalidation only with a complete, consistent dependency map.

    Search inspections can underpin support-gap conclusions without appearing in
    positive evidence. Declared claim dependencies propagate source changes to
    every dependent claim. Malformed maps never justify narrowing the review.
    """
    ids={finding['claim_id'] for finding in findings}
    fallback=(set(ids),'No complete, consistent dependency map: conservatively invalidate every finding.')
    if selected['role']!='source' or not isinstance(mapping,dict) or mapping.get('coverage')!='complete':
        return fallback
    graph=mapping.get('claims')
    if not isinstance(graph,dict) or set(graph)!=ids or len(ids)!=len(findings):return fallback
    document_ids={document['id'] for document in documents}
    by_path={document['logical']:document['id'] for document in documents}
    def checked_ids(value, allowed):
        if not isinstance(value,list) or any(not isinstance(item,str) for item in value):
            raise ValueError('Dependency IDs must be a list of strings')
        if len(value)!=len(set(value)) or not set(value)<=allowed:
            raise ValueError('Dependency IDs must be distinct and known')
        return set(value)
    try:
        global_documents=checked_ids(mapping.get('global_documents',[]),document_ids)
        direct={cid:checked_ids(value,document_ids) for cid,value in graph.items()}
        dependencies={}
        for finding in findings:
            cid=finding['claim_id']
            search=finding.get('support_search',{})
            argument=finding.get('argument_audit',{})
            if not isinstance(search,dict) or not isinstance(argument,dict):return fallback
            evidence=finding.get('evidence',[]);inspected=search.get('inspected',[])
            if not isinstance(evidence,list) or not isinstance(inspected,list):return fallback
            footprint={by_path[item['path']] for item in evidence+inspected}
            if not footprint<=direct[cid]|global_documents:return fallback
            dependencies[cid]=checked_ids(argument.get('claim_dependencies',[]),ids)
        # Reject circular or self-dependent declarations before narrowing scope.
        pending={cid:set(deps) for cid,deps in dependencies.items()}
        reverse={cid:set() for cid in ids}
        for cid,deps in dependencies.items():
            for dependency in deps:reverse[dependency].add(cid)
        ready=[cid for cid,deps in pending.items() if not deps];visited=set()
        while ready:
            cid=ready.pop();visited.add(cid)
            for dependent in reverse[cid]:
                pending[dependent].discard(cid)
                if not pending[dependent]:ready.append(dependent)
        if visited!=ids:return fallback
        affected={cid for cid,deps in direct.items() if selected['id'] in deps|global_documents}
        queue=list(affected)
        while queue:
            for dependent in reverse[queue.pop()]:
                if dependent not in affected:
                    affected.add(dependent);queue.append(dependent)
        return affected,('Affected semantic claims selected from complete source and search dependencies '
                         'and their transitive claim dependents; all technical proofs still require rechecking.')
    except (KeyError,TypeError,ValueError):
        return fallback


def refresh(root,document_id,replacement,*,temp_root=None):
    root=Path(root).resolve();verify(root);replacement=Path(replacement).resolve()
    if not replacement.is_file():raise ValueError('Replacement must be a file')
    docs=inventory(root);selected=next((d for d in docs if d['id']==document_id),None)
    if not selected:raise ValueError('Unknown document ID')
    parent=Path(temp_root or root.parent).resolve()
    if parent==root or parent.is_relative_to(root):raise ValueError('Revision destination must be outside the source workspace')
    if replacement.suffix.lower()!=Path(selected['original']).suffix.lower():raise ValueError('Replacement format must match original')
    parent.mkdir(parents=True,exist_ok=True)
    target=Path(tempfile.mkdtemp(prefix='claim-audit-revision-',dir=parent))
    shutil.copytree(root,target,dirs_exist_ok=True,ignore=shutil.ignore_patterns('.lake','attempts','history','export-manifest.json'))
    history=target/'history/parent';history.mkdir(parents=True)
    for name in ('proof-results.json','logs','checks','audit-report.md','coverage.md','semantic-review.md'):
        p=target/name
        if p.exists():shutil.move(p,history/name)
    original=target/selected['original']
    # Preserve format identity; converting between formats needs a new document.
    if replacement.suffix.lower()!=original.suffix.lower():raise ValueError('Replacement format must match original')
    shutil.copyfile(replacement,original)
    catalog=read(target/'input/catalog.json')
    for entry in catalog:
        if entry['id']==document_id:entry.update(original_sha=sha(original),external=str(replacement))
    save(target/'input/catalog.json',catalog)
    with connection(target,True) as db:
        db.execute("UPDATE documents SET status='pending',original_sha=?,external=? WHERE id=?",(sha(original),str(replacement),document_id))
    old_findings=read(target/'findings.json') if (target/'findings.json').exists() else []
    try:
        mapping=read(target/'dependencies.json') if (target/'dependencies.json').exists() else {}
    except (OSError,ValueError):
        mapping={}
    affected,reason=_affected_claims(old_findings,docs,selected,mapping)
    with connection(target) as db:
        invalidated_manual=[r[0] for r in db.execute("SELECT anchor FROM segments WHERE document_id=? AND method='manual-transcription'",(document_id,))] if selected['original_sha']!=sha(original) else []
    save(target/'invalidation.json',{'parent_workspace':str(root),'changed_document':document_id,'old_sha256':selected['original_sha'],'new_sha256':sha(original),'affected_claims':sorted(affected),'invalidated_manual_transcriptions':invalidated_manual,'technical_results':'all invalidated','reason':reason})
    meta=read(target/'run.json');meta.update(workspace=str(target),parent_workspace=str(root),revised_at=stamp());save(target/'run.json',meta)
    manifest(target)
    result=resume(target);result['invalidation']=read(target/'invalidation.json');return result


def recover_workspace(root):
    """Rebuild interrupted derived state only from intact snapshotted originals.

    Recovery is explicit, preserves the failed state, discards all technical
    successes, and requires semantic review again before publication.
    """
    root=Path(root).resolve();old=read(root/'input/manifest.json')
    if old!=read(root/'manifest.json'):raise ValueError('Recovery requires matching prior manifest copies')
    protected=['input/catalog.json'] + (['input/audit-policy.json'] if 'input/audit-policy.json' in old['files'] else []) +[rel for rel in old['files'] if rel.startswith('input/originals/')]
    for rel in protected:
        if rel not in old['files'] or sha(root/rel)!=old['files'][rel]['sha256']:
            raise ValueError(f'Cannot recover modified original/catalog: {rel}')
    catalog=read(root/'input/catalog.json')
    for entry in catalog:
        if entry['original'] not in protected or sha(root/entry['original'])!=entry['original_sha']:
            raise ValueError('Catalog does not match protected original bytes')
    history=root/'history';history.mkdir(exist_ok=True)
    target=Path(tempfile.mkdtemp(prefix='interrupted-',dir=history));(target/'input').mkdir()
    for p in list((root/'input').iterdir()):
        if p.name not in {'originals','catalog.json','manifest.json','audit-policy.json'}:shutil.move(p,target/'input'/p.name)
    for name in ('extraction','extraction-lock.json','proof-results.json','logs','checks','semantic-review.md','audit-report.md','coverage.md'):
        p=root/name
        if p.exists():shutil.move(p,target/name)
    db=connection(root,True);_schema(db)
    for entry in catalog:
        db.execute('INSERT INTO documents VALUES (?,?,?,?,?,?,?,?,?,?)',tuple(entry[k] for k in ('id','role','original','logical','external','original_sha'))+('pending','[]','{}',None))
    db.commit();db.close()
    data=read(root/'findings.json') if (root/'findings.json').exists() else []
    save(root/'invalidation.json',{'affected_claims':[f['claim_id'] for f in data],
        'reason':'Explicit recovery rebuilt derived state from intact original snapshots; all previous results require review.',
        'technical_results':'all invalidated','previous_state':target.relative_to(root).as_posix()})
    manifest(root)
