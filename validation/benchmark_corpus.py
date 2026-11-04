#!/usr/bin/env python3
"""Executed scale/resume/retrieval benchmark, separate from semantic accuracy."""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import sys
import tempfile
import time
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'skills/evidence-to-proof-review/scripts'))
import corpus


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--documents',type=int,default=1000)
    args=parser.parse_args()
    if args.documents<20:parser.error('At least 20 documents are required for this benchmark')
    base=Path(tempfile.mkdtemp(prefix='scale-benchmark-',dir=ROOT/'tmp'));sources=base/'sources';sources.mkdir()
    (base/'brief.md').write_text('Exercise ingestion, bounded batches and full-text retrieval. This is not a semantic audit.\n')
    (base/'report.md').write_text('<a id="LOAD-01"></a>\n**LOAD-01.** All supplied records have been available for inspection.\n')
    for n in range(args.documents):
        paragraphs=[]
        for part in range(24):
            body=(f'Record {n:04d} section {part:02d} documents the named station, review interval, measured quantity and custody scope. '
                'A reading is evidence for this station only. It supplies no unobserved event history and must be joined with the applicable version and exception list. '
                'The custodian records provenance independently of the amount. Repeated context tests chunk boundaries without establishing additional findings. ')*4
            if n==args.documents-3 and part==23:body+=' CROSSBOUNDARY_EXCEPTION applies to station Z-997 and supersedes the general threshold only during its named interval.'
            paragraphs.append(f'<a id="P{part:03d}"></a>\n{body}')
        (sources/f'record-{n:04d}.md').write_text('\n\n'.join(paragraphs)+'\n')
    supplied_bytes=sum(p.stat().st_size for p in sources.iterdir());start=time.monotonic()
    prepared=corpus.prepare(SimpleNamespace(brief=base/'brief.md',report=base/'report.md',sources=[sources],temp_root=ROOT/'tmp',
        max_documents=100,max_seconds=None,ocr_language='eng',extract_timeout=60,max_pages=None))
    workspace=Path(prepared['workspace']);first_elapsed=time.monotonic()-start
    assert not prepared['coverage']['complete']
    absent=corpus.search(workspace,'CROSSBOUNDARY_EXCEPTION')
    assert absent['total_matching_chunks']==0
    batches=[{'documents_processed':len(prepared['coverage']['processed_this_batch']),'elapsed_seconds':first_elapsed}]
    while not prepared['coverage']['complete']:
        tick=time.monotonic();prepared=corpus.resume(workspace,max_documents=250)
        batches.append({'documents_processed':len(prepared['coverage']['processed_this_batch']),'elapsed_seconds':time.monotonic()-tick})
    found=corpus.search(workspace,'CROSSBOUNDARY_EXCEPTION',limit=5)
    assert found['total_matching_chunks']>0
    hit=found['results'][0];full=corpus.passage(workspace,hit['path'],hit['anchor'])
    assert 'supersedes the general threshold' in full['quote']
    before=hashlib.sha256((workspace/'input/index.sqlite3').read_bytes()).hexdigest()
    noop=corpus.resume(workspace)
    assert not noop['coverage']['processed_this_batch']
    assert hashlib.sha256((workspace/'input/index.sqlite3').read_bytes()).hexdigest()==before
    with corpus.connection(workspace) as db:
        segments=db.execute('SELECT count(*) FROM segments').fetchone()[0]
        chunks=db.execute('SELECT count(*) FROM chunks').fetchone()[0]
    result={'scope':'Synthetic ingestion/index/retrieval benchmark; no semantic accuracy or unlimited-scale claim',
        'input_documents':args.documents+2,'source_bytes':supplied_bytes,'segments':segments,'chunks':chunks,
        'elapsed_seconds_total':time.monotonic()-start,'peak_process_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'rss_platform_note':'Linux ru_maxrss in KiB; includes this benchmark generator and Python processing, not a universal capacity estimate',
        'batches':batches,'partial_search_was_not_treated_as_complete':True,'late_exception_retrieved':True,
        'no_op_resume_preserved_index_hash':True,'workspace':str(workspace),'fixture_directory':str(base),
        'index_bytes':(workspace/'input/index.sqlite3').stat().st_size,
        'legacy_in_memory_ledger_absent':not (workspace/'input/source-ledger.json').exists()}
    target=ROOT/'validation/extended';target.mkdir(parents=True,exist_ok=True)
    (target/'scale.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
