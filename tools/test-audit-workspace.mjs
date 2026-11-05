import {spawn} from 'node:child_process';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
import vm from 'node:vm';

// Read-only browser regression against the existing local audit server.
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const origin='http://127.0.0.1:8787';
const dir=await fs.mkdtemp(path.join(root,'tmp/workspace-browser-'));
const profile=path.join(dir,'profile');
const sourceHTML=await fs.readFile(path.join(root,'tools/audit-ui.html'),'utf8');
const renderer=vm.createContext({});
vm.runInContext(sourceHTML.split('<script>')[1].split('async function catalog()')[0],renderer);
const rendered=vm.runInContext("markdown('# Heading\\n\\n- One\\n- Two\\n\\n> Quote\\n\\n###### Small\\n\\n| Column | Other |\\n| --- | --- |\\n| Value | Entry |\\n\\n[Evidence](../input/source.md)\\n\\n```lean\\ntheorem demo : True := by trivial\\n```')",renderer);
for(const tag of ['<h1','<ul>','<blockquote>','<h6','<thead>','<th>','<code>','data-md-link='])assert(rendered.includes(tag),'Markdown element missing: '+tag);
assert(!vm.runInContext("inline('[Bad](javascript:alert)')",renderer).includes('<a'),'Executable links are not rendered');
const anchored=vm.runInContext("markdown('## S01 — Chapter 1\\n\\nSource text\\n\\n## R01 — Conclusion')",renderer);
assert(anchored.includes('id="md-s01"')&&anchored.includes('id="md-r01"'),'Short source and report citations have stable section anchors');
assert.equal(vm.runInContext("resolveDocumentLink('work/a/traces/step.md','../input/source.md').path",renderer),'work/a/input/source.md');
assert.throws(()=>vm.runInContext("resolveDocumentLink('one.md','../../outside.md')",renderer));
const catalogResponse=await fetch(origin+'/api/examples');
const catalog=await catalogResponse.json();
assert(catalogResponse.ok&&Array.isArray(catalog),'Catalog unavailable: '+JSON.stringify(catalog));
const requested=process.argv[2];
const example=requested?catalog.find(x=>x.id===requested):catalog.find(x=>(x.language||'en')==='en'&&x.runs.some(r=>r.status==='finished'))||catalog.find(x=>x.runs.some(r=>r.status==='finished'));
assert(example,'A real completed example is required (optional argument: example ID)');
const requestedReport=process.argv[3];
const report=requestedReport?example.reports.find(r=>r.path===requestedReport):example.reports.find(r=>example.runs.some(x=>x.reportPath===r.path&&x.status==='finished'))||example.reports[0];
assert(report,'The selected example must have an input report');
const source=example.files.find(f=>f.role==='source');
const runs=example.runs.filter(r=>r.reportPath===report.path).sort((a,b)=>b.created.localeCompare(a.created));
const finished=runs.find(r=>r.status==='finished');
assert(source&&finished,'A source and a real finished verification are required');
const runData=await (await fetch(origin+'/api/runs/'+finished.id)).json();
assert(runData.findings?.length,'The real run must contain findings');
const claim=runData.findings.find(f=>f.proofs?.length)||runData.findings[0];
const chrome=spawn('google-chrome',['--headless','--no-sandbox','--disable-gpu','--no-first-run','--no-default-browser-check','--disable-dev-shm-usage','--remote-debugging-port=0','--user-data-dir='+profile,'--disk-cache-dir='+path.join(dir,'cache'),'about:blank'],{cwd:root,stdio:['ignore','ignore','pipe']});
let chromeLog='',ws;
chrome.stderr.on('data',c=>chromeLog+=c);
const sleep=ms=>new Promise(r=>setTimeout(r,ms)),errors=[],mutations=[];
try{
 let port;
 for(let i=0;i<100;i++){try{port=Number((await fs.readFile(path.join(profile,'DevToolsActivePort'),'utf8')).split('\n')[0]);if(port)break;}catch{}await sleep(100);}
 assert(port,'Chrome debugging endpoint unavailable: '+chromeLog);
 const targets=await (await fetch('http://127.0.0.1:'+port+'/json')).json();
 ws=new WebSocket(targets.find(t=>t.type==='page').webSocketDebuggerUrl);
 await new Promise((resolve,reject)=>{ws.addEventListener('open',resolve,{once:true});ws.addEventListener('error',reject,{once:true});});
 let seq=0;const pending=new Map();
 ws.addEventListener('message',event=>{const m=JSON.parse(event.data);if(m.id){const p=pending.get(m.id);if(!p)return;pending.delete(m.id);clearTimeout(p.timer);m.error?p.reject(Error(JSON.stringify(m.error))):p.resolve(m.result);}else if(m.method==='Runtime.exceptionThrown')errors.push(m.params.exceptionDetails);else if(m.method==='Network.requestWillBeSent'&&m.params.request.url.startsWith(origin)&&!['GET','HEAD'].includes(m.params.request.method))mutations.push(m.params.request);});
 function cdp(method,params={}){return new Promise((resolve,reject)=>{const id=++seq,timer=setTimeout(()=>{pending.delete(id);reject(Error('CDP timeout: '+method));},20000);pending.set(id,{resolve,reject,timer});ws.send(JSON.stringify({id,method,params}));});}
 async function js(expression){const r=await cdp('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;}
 async function until(expression){for(let i=0;i<150;i++){if(await js(expression))return;await sleep(100);}throw Error('Timed out: '+expression);}
 async function clickNode(expression){
  const point=await js(`(()=>{const e=${expression};e.scrollIntoView({block:'nearest'});const r=e.getBoundingClientRect();return {x:r.x+Math.min(30,r.width/2),y:r.y+r.height/2};})()`);
  await cdp('Input.dispatchMouseEvent',{type:'mousePressed',button:'left',clickCount:1,...point});
  await cdp('Input.dispatchMouseEvent',{type:'mouseReleased',button:'left',clickCount:1,...point});
 }
 const quote=JSON.stringify;
 const node=`document.querySelector('#tree details[data-example-id="'+${quote(example.id)}+'"]')`;
 const reportButton=`${node}.querySelector('.report-file[data-report-path="'+${quote(report.path)}+'"]')`;
 const sourceButton=`${node}.querySelector('[data-input-files] .input-file[data-path="'+${quote(source.path)}+'"]')`;
 await cdp('Runtime.enable');await cdp('Page.enable');await cdp('Network.enable');
 await cdp('Emulation.setDeviceMetricsOverride',{width:1440,height:1000,deviceScaleFactor:1,mobile:false});
 await cdp('Page.navigate',{url:origin});await until(`${node}!==null`);
 assert.equal(await js("document.querySelectorAll('dialog,[role=dialog],#refresh,#run-history,#expand-verification').length"),0,'No popups, history, refresh or fullscreen navigation');
 await js("document.getElementById('new-example').click()");
 assert.deepEqual(await js("[...document.querySelectorAll('#example-language option')].map(o=>o.value).sort()"),['en','ro']);
 await clickNode(`${node}.querySelector('summary')`);await until(`${sourceButton}!==null`);
 await until(`${node}.open`);
 await clickNode(`${node}.querySelector('summary')`);await until(`!${node}.open`);
 await sleep(3300);assert(await js(`!${node}.open`),'Root remains collapsed after polling');
 await clickNode(`${node}.querySelector('summary')`);await until(`${node}.open`);
 assert(await js("!!document.getElementById('add-files') && !!document.getElementById('stop-example') && !!document.getElementById('generate-report')"),'Example-level actions exist');
 await js("document.getElementById('add-files').click()");assert(await js("!!document.querySelector('#upload-form select[name=role]')"),'Inline upload role selector');
 await js("document.getElementById('cancel-form').click();document.getElementById('generate-report').click()");
 assert.deepEqual(await js("[...document.querySelectorAll('#generate-form select[name=mode] option')].map(o=>o.value)"),['grounded','with_errors']);
 await js("document.getElementById('cancel-form').click()");
 const inputs=`${node}.querySelector('[data-input-files]')`;
 await clickNode(`${inputs}.querySelector('summary')`);
 await until(`${inputs}.open && ${sourceButton}.getBoundingClientRect().height>0`);
 await sleep(3300);
 assert(await js(`${inputs}.open`),'Input files stays expanded after polling');
 await clickNode(`${inputs}.querySelector('summary')`);
 await until(`!${inputs}.open`);
 await sleep(3300);
 assert(await js(`!${inputs}.open`),'Input files stays collapsed after polling');
 await js(`${inputs}.querySelector('summary').focus()`);
 await cdp('Input.dispatchKeyEvent',{type:'keyDown',key:'Enter',code:'Enter',windowsVirtualKeyCode:13,text:'\r'});
 await cdp('Input.dispatchKeyEvent',{type:'keyUp',key:'Enter',code:'Enter',windowsVirtualKeyCode:13});
 await until(`${inputs}.open && ${sourceButton}.getBoundingClientRect().height>0`);
 await clickNode(sourceButton);await until(`document.getElementById('verification-document').dataset.artifactPath===${quote(source.path)}`);
 await clickNode(reportButton);await until(`document.getElementById('content').dataset.runId===${quote(finished.id)}`);
 assert.equal(await js("document.querySelectorAll('#add-files,#stop-example,#generate-report').length"),0,'Example-only actions do not leak into report');
 assert(await js("!!document.getElementById('start')"),'Report verification action');
 const reportNode=`${node}.querySelector('details[data-report-path="'+${quote(report.path)}+'"]')`;
 await clickNode(reportButton);
 await until(`!${reportNode}.open`);
 await sleep(3300);
 assert(await js(`!${reportNode}.open`),'Selected report stays collapsed after polling');
 await clickNode(reportButton);
 await until(`${reportNode}.open`);

 const finding=`${node}.querySelector('details[data-report-path="'+${quote(report.path)}+'"] .finding-file[data-claim-id="'+${quote(claim.claim_id)}+'"]')`;
 await until(`${finding}!==null`);await clickNode(finding);
 await until(`document.getElementById('content')?.dataset.claimId===${quote(claim.claim_id)}`);
 await until(`document.getElementById('verification-document')?.dataset.artifactPath===${quote(claim.path)}`);
 assert.equal(await js("document.querySelectorAll('#content details,#content [role=tab],#content nav,#verification-documents,dialog').length"),0,'All navigation is in the tree; right pane is a plain document');
 const statusCases={supported:'Supported',refuted:'Refuted',undetermined:'Undetermined',both:'Conflicting',pending:'Pending',not_applicable:'Not applicable'};
 for(const [state,label] of Object.entries(statusCases)){const result=await js(`findingStatus(${quote(state)})`);assert.equal(result.label,label);assert(result.icon&&result.description,'Every state has an icon and explanation');}
 assert.equal((await js('findingStatus(undefined)')).state,'pending','Missing verdict cannot appear supported');
 for(const phase of ['queued','running','finalizing','failed','interrupted','incomplete','stopped']){const draft=await js(`findingStatus('supported',${quote(phase)})`);assert.equal(draft.state,'pending','Nonfinished drafts cannot appear supported');assert(draft.description.includes('provisional'));}
 assert.equal(await js(`${reportButton}.querySelector('.report-status').dataset.status`),finished.status,'Report exposes execution status');
 assert(await js("[...document.querySelectorAll('#tree details[data-report-path]')].every(d=>d.querySelector(':scope > summary .report-status')?.dataset.status==='finished'||[...d.querySelectorAll('.finding-file')].every(f=>f.dataset.semanticState==='pending'))"),'Every unfinished report shows provisional finding badges');
 for(const f of runData.findings){const state=Object.hasOwn(statusCases,f.semantic_state)?f.semantic_state:'pending';const summary=`${reportNode}.querySelector('.finding-file[data-claim-id="'+${quote(f.claim_id)}+'"]')`;assert.equal(await js(`${summary}.dataset.semanticState`),state);assert.equal(await js(`${summary}.querySelector('.status-label').textContent`),statusCases[state]);assert(await js(`${summary}.querySelector('.finding-status').title.length>0 && ${summary}.querySelector('.status-icon').getAttribute('aria-hidden')==='true'`),'Visible text conveys the decorative icon status accessibly');}
 await clickNode(finding);await until(`!${finding}.parentElement.open`);await sleep(3300);
 assert(await js(`!${finding}.parentElement.open`),'Finding remains collapsed after polling');
 await clickNode(finding);await until(`${finding}.parentElement.open`);
 await until(`document.getElementById('verification-document')?.dataset.artifactPath===${quote(claim.path)}`);

 const narrative=await js("document.getElementById('verification-document').innerText");
 assert(!/&(?:amp|lt|gt|quot|#\d+);/.test(narrative),'No escaped entities');
 assert(!/"(?:claim_id|executive_summary|semantic_state)"\s*:/.test(narrative),'No internal JSON');
 if(example.language==='ro')assert(/[ăâîșțĂÂÎȘȚ]/.test(narrative),'Romanian diacritics');
 const steps=`${finding}.parentElement.querySelector('details')`;
 if(await js(`!!${steps}`)){await clickNode(`${steps}.querySelector('summary')`);await until(`${steps}.open`);}
 await js(`${finding}.scrollIntoView({block:'nearest'})`);
 await fs.writeFile(path.join(dir,'finding-narrative.png'),Buffer.from((await cdp('Page.captureScreenshot',{format:'png'})).data,'base64'));
 const docs=await js("[...document.querySelectorAll('#tree .document-link')].map(a=>a.dataset.path)");
 for(const e of runData.phases.filter(e=>e.claim_ids?.length===1&&e.claim_ids[0]===claim.claim_id&&e.claim_step))assert(docs.includes(e.path),'Individual step linked');
 const tracePath=runData.phases.find(e=>e.claim_ids?.length===1&&e.claim_ids[0]===claim.claim_id&&e.claim_step==='evidence').path;
 await js(`[...document.querySelectorAll('.document-link')].find(a=>a.dataset.path===${quote(tracePath)}).click()`);
 await until(`document.getElementById('verification-document').dataset.artifactPath===${quote(tracePath)}`);
 assert(await js("!!document.querySelector('#verification-document thead th')"),'Readable source table');
 const reference=await js("(()=>{const a=document.querySelector('#verification-document [data-md-link]');a.dataset.testLink='yes';return a.dataset.mdLink;})()");
 const linkedPath=path.posix.normalize(path.posix.join(path.posix.dirname(tracePath),decodeURIComponent(reference.split('#')[0])));
 await js("document.querySelector('[data-test-link=yes]').click()");await until(`document.getElementById('verification-document').dataset.artifactPath===${quote(linkedPath)}`);
 assert.equal(await js("document.getElementById('verification-document').dataset.sourceId"),finished.id);
 const fragment=decodeURIComponent(reference.split('#')[1]||'');
 if(fragment)assert(await js(`[...document.querySelectorAll('#verification-document [id]')].some(e=>e.id===${quote(fragment)}||e.id===headingId(${quote(fragment)}))`),'Evidence citation resolves to its exact section');

 await js("[...document.querySelectorAll('.document-link')].find(a=>a.dataset.path.endsWith('.lean')).click()");
 await until("document.getElementById('verification-document').dataset.artifactPath?.endsWith('.lean')");
 assert(await js("/theorem|namespace/.test(document.getElementById('verification-document').textContent)"),'Actual Lean code shown');
 const selectedArtifact=await js("document.getElementById('verification-document').dataset.artifactPath");
 const openedNodes=await js("[...document.querySelectorAll('#tree details[open]')].map(d=>d.dataset.key)");
 await sleep(3300);
 assert.equal(await js("document.getElementById('verification-document').dataset.artifactPath"),selectedArtifact,'Polling keeps selected document');
 const stillOpen=await js("[...document.querySelectorAll('#tree details[open]')].map(d=>d.dataset.key)");
 for(const key of openedNodes)assert(stillOpen.includes(key),'Polling preserves expanded tree nodes');
 assert(await js(`[...document.querySelectorAll('#tree .document-link.selected')].some(b=>b.dataset.path===${quote(selectedArtifact)})`),'Selected document stays highlighted after polling');
 const bounds=[];
 for(const [width,height] of [[1440,1000],[390,844]]){
  await cdp('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false});await sleep(150);
  assert(await js("document.documentElement.scrollWidth<=innerWidth+2"),'Page has no horizontal overflow');
  bounds.push({viewportWidth:width,viewportHeight:height,width,height});
  await js("document.querySelector('#tree .document-link.selected')?.scrollIntoView({block:'nearest'})");
  await fs.writeFile(path.join(dir,`verification-${width}x${height}.png`),Buffer.from((await cdp('Page.captureScreenshot',{format:'png'})).data,'base64'));
 }
 // Exercise real pointer toggles at every tree depth, including a redraw.
 await cdp('Emulation.setDeviceMetricsOverride',{width:1440,height:1000,deviceScaleFactor:1,mobile:false});
 async function checkToggle(summary,details,label){
  if(!await js(`${details}.open`))await clickNode(summary);
  await until(`${details}.open`);
  await clickNode(summary);
  await until(`!${details}.open`);
  await js('drawTree()');
  assert(await js(`!${details}.open`),label+' remains collapsed after tree redraw');
  await clickNode(summary);
  await until(`${details}.open`);
 }
 const findingNode=`${finding}.parentElement`;
 const stepsNode=`${findingNode}.querySelector('details')`;
 await checkToggle(`${stepsNode}.querySelector('summary')`,stepsNode,'Verification steps');
 await checkToggle(finding,findingNode,'Finding');
 await checkToggle(reportButton,reportNode,'Report');
 await checkToggle(`${node}.querySelector('summary')`,node,'Example');
 assert.deepEqual(errors,[],'No browser exceptions');assert.deepEqual(mutations,[],'This test must remain read-only');
 assert.equal(await js("document.getElementById('error')?.textContent.trim()||''"),'','No user-visible errors');
 await fs.writeFile(path.join(dir,'result.md'),'# Browser verification\n\nPassed: read-only real-server navigation, source preview, finding summary, Lean preview, Markdown links and responsive document bounds.\n\n- Example: '+example.id+'\n- Report: '+report.path+'\n- Run: '+finished.id+'\n- Claim: '+claim.claim_id+'\n\n## Viewports\n\n'+bounds.map(b=>'- '+b.viewportWidth+' × '+b.viewportHeight+': viewport '+b.width+' × '+b.height).join('\n')+'\n');
 console.log('PASS read-only audit workspace. Artifacts: '+dir);
}catch(e){await fs.writeFile(path.join(dir,'failure.md'),'# Browser verification failed\n\n```text\n'+e.stack+'\n```\n\nBrowser exceptions: '+errors.length+'\n\nUnexpected writes: '+mutations.length+'\n');throw e;}
finally{ws?.close();chrome.kill('SIGTERM');await fs.writeFile(path.join(dir,'chrome.md'),'# Browser diagnostics\n\n```text\n'+chromeLog+'\n```\n');}
