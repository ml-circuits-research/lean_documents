"""Exercise real extraction tools and preserve fixtures/logs under repository tmp/."""
import importlib.util
import json
from pathlib import Path
import shutil
import struct
import sys
import tempfile
import unittest
from unittest import mock
import zipfile
import zlib

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('extractors', REPO / 'skills/evidence-to-proof-review/scripts/extractors.py')
extractors = importlib.util.module_from_spec(spec)
spec.loader.exec_module(extractors)
CAPABILITIES = {name: shutil.which(name) for name in ('pdftotext', 'pdfinfo', 'pdfimages', 'pdftoppm', 'tesseract')}
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


def write_pdf(path, pages):
    """Create real uncompressed text PDFs without third-party dependencies."""
    objects = [b'', b'']
    objects.append(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>')
    page_ids = []
    for text in pages:
        stream = ('BT /F1 18 Tf 50 750 Td (' + text.replace('\\','\\\\').replace('(','\\(').replace(')','\\)') + ') Tj ET').encode('ascii')
        content_id = len(objects)+1
        objects.append(b'<< /Length '+str(len(stream)).encode()+b' >>\nstream\n'+stream+b'\nendstream')
        page_id = len(objects)+1
        objects.append(f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 3 0 R >> >> /Contents {content_id} 0 R >>'.encode())
        page_ids.append(page_id)
    objects[0] = b'<< /Type /Catalog /Pages 2 0 R >>'
    objects[1] = ('<< /Type /Pages /Count '+str(len(pages))+' /Kids ['+' '.join(f'{p} 0 R' for p in page_ids)+'] >>').encode()
    _pdf_objects(path, objects)


def _pdf_objects(path, objects):
    data = bytearray(b'%PDF-1.4\n')
    offsets = []
    for index, obj in enumerate(objects, 1):
        offsets.append(len(data)); data.extend(f'{index} 0 obj\n'.encode()+obj+b'\nendobj\n')
    xref = len(data)
    data.extend(f'xref\n0 {len(objects)+1}\n0000000000 65535 f \n'.encode())
    for offset in offsets: data.extend(f'{offset:010d} 00000 n \n'.encode())
    data.extend(f'trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode())
    path.write_bytes(data)


def write_docx(path, body, extra=None):
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as package:
        package.writestr('[Content_Types].xml', '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>')
        package.writestr('word/document.xml', f'<w:document xmlns:w="{W}"><w:body>{body}</w:body></w:document>')
        for name, value in (extra or {}).items(): package.writestr(name,value)


class ExtractorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (REPO/'tmp').mkdir(exist_ok=True)
        cls.run_root = Path(tempfile.mkdtemp(prefix='extractor-tests-',dir=REPO/'tmp'))
        (cls.run_root/'capabilities.json').write_text(json.dumps(CAPABILITIES,indent=2)+'\n')
        print('\nExtractor test artifacts retained at '+str(cls.run_root), flush=True)
        print('Actual converter availability: '+json.dumps(CAPABILITIES), flush=True)

    def setUp(self):
        self.root = self.run_root/self._testMethodName; self.root.mkdir()

    def extract(self, path, **kwargs):
        return extractors.extract_document(path,self.root/'artifacts',**kwargs)

    def test_markdown_keeps_explicit_anchors_and_exact_coordinates(self):
        path=self.root/'source.md'
        content='# Title\r\n\r\n<a id="C-1"></a>\r\nFirst paragraph.\r\n\r\nSecond line.\r\n'
        path.write_bytes(content.encode())
        result=self.extract(path)
        self.assertEqual(result['status'],'ready')
        self.assertEqual([s['anchor'] for s in result['segments']],['document-preamble','C-1'])
        segment=result['segments'][1]
        self.assertEqual(segment['locator']['start_line'],4)
        self.assertEqual(segment['quote'],'First paragraph.\r\n\r\nSecond line.')
        loc=segment['locator']
        self.assertEqual(content[loc['start_character']:loc['end_character']],segment['quote'])

    def test_unanchored_text_has_stable_paragraph_offsets(self):
        path=self.root/'source.txt';path.write_text('Repeated.\n\nRepeated.\n\nLast.')
        result=self.extract(path)
        self.assertEqual([s['anchor'] for s in result['segments']],['P01','P02','P03'])
        self.assertEqual([s['locator']['start_line'] for s in result['segments']],[1,3,5])
        self.assertEqual(result['segments'][1]['locator']['start_character'],11)

    def test_duplicate_text_anchor_blocked(self):
        path=self.root/'source.md';path.write_text('<a id="A"></a>one\n<a id="A"></a>two')
        result=self.extract(path)
        self.assertEqual(result['status'],'blocked')
        self.assertIn('Duplicate',' '.join(result['warnings']))

    def test_invalid_utf8_and_unsupported_formats_are_explicit(self):
        for index, suffix in enumerate(('.txt','.bin')):
            path=self.root/f'source{suffix}';path.write_bytes(b'\xff\xfe\x00')
            result=extractors.extract_document(path,self.root/f'artifacts-{index}')
            self.assertEqual(result['status'],'blocked');self.assertFalse(result['complete'])
            self.assertTrue(result['warnings'])

    def test_docx_order_tables_headers_footnotes_and_comments(self):
        path=self.root/'source.docx'
        body='<w:p><w:r><w:t>Before table.</w:t></w:r></w:p><w:tbl><w:tr><w:tc><w:p><w:r><w:t>Amount</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>275000</w:t></w:r></w:p></w:tc></w:tr></w:tbl><w:p><w:r><w:t>After table.</w:t><w:footnoteReference w:id="2"/></w:r></w:p>'
        extra={'word/header1.xml':f'<w:hdr xmlns:w="{W}"><w:p><w:r><w:t>Header.</w:t></w:r></w:p></w:hdr>',
               'word/footer1.xml':f'<w:ftr xmlns:w="{W}"><w:p><w:r><w:t>Footer.</w:t></w:r></w:p></w:ftr>',
               'word/footnotes.xml':f'<w:footnotes xmlns:w="{W}"><w:footnote w:id="2"><w:p><w:r><w:t>Footnote.</w:t></w:r></w:p></w:footnote></w:footnotes>',
               'word/comments.xml':f'<w:comments xmlns:w="{W}"><w:comment w:id="3" w:author="Reviewer"><w:p><w:r><w:t>Check total.</w:t></w:r></w:p></w:comment></w:comments>'}
        write_docx(path,body,extra)
        result=self.extract(path)
        self.assertEqual(result['status'],'ready')
        self.assertEqual([s['quote'] for s in result['segments']],['Before table.','Amount','275000','After table.','Header.','Footer.','Footnote.','Check total.'])
        amount=result['segments'][2]
        self.assertEqual(amount['anchor'],'docx-table-0001-r0001-c0002-p0001')
        self.assertEqual(amount['locator']['cell'],2)
        self.assertIn('/w:tc[2]/w:p[1]',amount['locator']['xml_path'])
        self.assertEqual(result['segments'][3]['locator']['footnote_ids'],['2'])
        self.assertIn('Reviewer',' '.join(result['segments'][-1]['uncertainty']))

    def test_docx_tracked_changes_and_objects_mark_partial(self):
        path=self.root/'source.docx'
        body='<w:p><w:del><w:r><w:delText>Old.</w:delText></w:r></w:del><w:ins><w:r><w:t>New.</w:t></w:r></w:ins><w:r><w:drawing/></w:r></w:p>'
        write_docx(path,body)
        result=self.extract(path)
        self.assertEqual(result['status'],'partial');self.assertFalse(result['complete'])
        self.assertEqual(result['segments'][0]['quote'],'Old.New.')
        self.assertIn('Tracked changes',' '.join(result['segments'][0]['uncertainty']))
        self.assertIn('Unsupported',' '.join(result['segments'][0]['uncertainty']))

    def test_corrupt_docx_is_blocked(self):
        path=self.root/'source.docx';path.write_bytes(b'not a zip')
        self.assertEqual(self.extract(path)['status'],'blocked')

    def test_docx_table_revision_properties_propagate_to_evidence(self):
        properties = {
            'row-deleted': ('', '<w:trPr><w:del w:id="1"/></w:trPr>', ''),
            'cell-deleted': ('', '', '<w:tcPr><w:cellDel w:id="2"/></w:tcPr>'),
            'cell-inserted': ('', '', '<w:tcPr><w:cellIns w:id="3"/></w:tcPr>'),
            'table-properties': ('<w:tblPr><w:tblPrChange w:id="4"><w:tblPr/></w:tblPrChange></w:tblPr>', '', ''),
        }
        for name, (table, row, cell) in properties.items():
            with self.subTest(name=name):
                path=self.root/(name+'.docx')
                write_docx(path, '<w:tbl>'+table+'<w:tr>'+row+'<w:tc>'+cell+'<w:p><w:r><w:t>Approval was denied.</w:t></w:r></w:p></w:tc></w:tr></w:tbl>')
                result=extractors.extract_document(path,self.root/('artifacts-'+name))
                self.assertEqual(result['status'],'partial')
                self.assertEqual(result['segments'][0]['quote'],'Approval was denied.')
                self.assertIn('Tracked', ' '.join(result['segments'][0]['uncertainty']))

    def test_deleted_docx_row_cannot_support_direct_proof_without_revision_review(self):
        from types import SimpleNamespace
        sys.path.insert(0,str(REPO/'skills/evidence-to-proof-review/scripts'))
        import corpus
        source=self.root/'deleted-row.docx'
        write_docx(source,'<w:tbl><w:tr><w:trPr><w:del w:id="1"/></w:trPr><w:tc><w:p><w:r><w:t>Approval was denied.</w:t></w:r></w:p></w:tc></w:tr></w:tbl>')
        brief=self.root/'brief.md';brief.write_text('Check the approval claim.')
        report=self.root/'report.md';report.write_text('<a id="R"></a>Approval was denied.')
        prepared=corpus.prepare(SimpleNamespace(brief=brief,report=report,sources=[source],temp_root=self.root/'runs'))
        root=Path(prepared['workspace']);document=next(d for d in corpus.inventory(root) if d['role']=='source')
        corpus.save(root/'coverage-acknowledgement.json',{'documents':[{'document_id':document['id'],'reason':'Tracked deletion retained.','impact':'Revision meaning requires original-source review.'}]})
        claim={'claim_id':'C','report_anchor':'R','formal_status':'proved','evidence':[{'path':document['logical'],'anchor':'docx-table-0001-r0001-c0001-p0001'}]}
        with self.assertRaisesRegex(ValueError,'uncertain extraction'):
            corpus.assert_reviewable(root,[claim])

    def test_entity_definition_is_not_interpreted(self):
        path=self.root/'source.docx'
        with zipfile.ZipFile(path,'w') as z:
            z.writestr('word/document.xml','<!DOCTYPE foo [<!ENTITY bad "expanded">]><foo>&bad;</foo>')
        result=self.extract(path)
        self.assertEqual(result['status'],'blocked')
        self.assertIn('DTD/entity',' '.join(result['warnings']))

    @unittest.skipUnless(CAPABILITIES['pdftotext'] and CAPABILITIES['pdfinfo'],'Real Poppler unavailable; recorded in capabilities.json')
    def test_real_pdf_page_text_and_word_boxes(self):
        path=self.root/'source.pdf';write_pdf(path,['Exact total 275000 cents.','Second page evidence.'])
        result=self.extract(path)
        self.assertEqual(result['status'],'ready')
        self.assertEqual([s['anchor'] for s in result['segments']],['pdf-page-0001','pdf-page-0002'])
        self.assertEqual(result['segments'][0]['quote'],'Exact total 275000 cents.')
        word=result['segments'][0]['locator']['words'][0]
        self.assertEqual(word['text'],'Exact');self.assertGreater(word['bbox'][2],word['bbox'][0])
        self.assertTrue((self.root/'artifacts/pdf-page-0001.bbox.xhtml').exists())

    @unittest.skipUnless(CAPABILITIES['pdftotext'] and CAPABILITIES['pdfinfo'],'Real Poppler unavailable; recorded in capabilities.json')
    def test_real_pdf_page_limit_is_partial(self):
        path=self.root/'source.pdf';write_pdf(path,['Page one.','Page two.'])
        result=self.extract(path,max_pages=1)
        self.assertEqual(result['status'],'partial');self.assertFalse(result['complete'])
        self.assertEqual(len(result['segments']),1)
        self.assertIn('extracted 1 of 2',' '.join(result['warnings']))

    def test_missing_optional_tool_explicitly_blocks(self):
        path=self.root/'source.pdf';write_pdf(path,['Text.'])
        with mock.patch.object(extractors.shutil,'which',return_value=None):
            result=self.extract(path)
        self.assertEqual(result['status'],'blocked')
        self.assertEqual(result['tools']['pdfinfo'],'unavailable')

    def test_synthetic_low_confidence_tsv_is_partial(self):
        # Unit fixture only: these rows are explicitly synthetic, not a tool run.
        ctx=extractors.Context(self.root/'synthetic-artifacts',60)
        tsv=ctx.artifacts/'synthetic-page.tsv'
        tsv.write_text('level\tpage_num\tblock_num\tpar_num\tline_num\tword_num\tleft\ttop\twidth\theight\tconf\ttext\n5\t1\t1\t1\t1\t1\t10\t20\t30\t40\t12.5\tuncertain\n')
        with mock.patch.object(ctx,'tool',return_value='synthetic-unit-test-tool'), mock.patch.object(ctx,'command',return_value=(b'',b'')):
            extractors._ocr(self.root/'unit-input.png',ctx,'synthetic-page',page=1,language='eng',origin={'unit_fixture':True})
        result=ctx.result()
        self.assertEqual(result['status'],'partial')
        locator=result['segments'][0]['locator']
        self.assertEqual(locator['mean_word_confidence'],12.5)
        self.assertEqual(locator['low_confidence_words'],1)
        self.assertEqual(locator['words'][0]['bbox'],[10,20,30,40])

    def test_synthetic_tsv_literal_opening_quote_does_not_merge_rows(self):
        # Tesseract TSV text is literal, not CSV-quoted. The first token below
        # deliberately begins an unmatched quote; following rows stay separate.
        ctx=extractors.Context(self.root/'synthetic-artifacts',60)
        header='level\tpage_num\tblock_num\tpar_num\tline_num\tword_num\tleft\ttop\twidth\theight\tconf\ttext\n'
        rows=['5\t1\t1\t1\t1\t1\t10\t20\t30\t40\t99\t"For\n',
              '5\t1\t1\t1\t1\t2\t45\t20\t60\t40\t98\tapproval\n',
              '5\t1\t1\t1\t2\t1\t10\t70\t40\t40\t97\tNext\n']
        (ctx.artifacts/'synthetic-page.tsv').write_text(header+''.join(rows))
        with mock.patch.object(ctx,'tool',return_value='synthetic-unit-test-tool'), mock.patch.object(ctx,'command',return_value=(b'',b'')):
            extractors._ocr(self.root/'unit-input.png',ctx,'synthetic-page',page=1,language='eng',origin={'unit_fixture':True})
        segment=ctx.result()['segments'][0]
        self.assertEqual(segment['quote'],'"For approval\nNext')
        self.assertEqual([word['text'] for word in segment['locator']['words']],['"For','approval','Next'])
        self.assertEqual(segment['locator']['word_count'],3)
        self.assertNotIn('\t',segment['quote'])
        self.assertEqual(segment['locator']['words'][-1]['line_id'],[1,1,2])

    def test_missing_ocr_dependency_is_blocked(self):
        path=self.root/'input.png';path.write_bytes(b'unit fixture: dependency checked before image decode')
        with mock.patch.object(extractors.shutil,'which',return_value=None):
            result=self.extract(path)
        self.assertEqual(result['status'],'blocked')
        self.assertEqual(result['tools']['tesseract'],'unavailable')
        self.assertIn('tesseract',' '.join(result['warnings']))

    @unittest.skipUnless(CAPABILITIES['pdfinfo'],'Real Poppler unavailable; recorded in capabilities.json')
    def test_corrupt_pdf_is_blocked_with_actual_failure_log(self):
        path=self.root/'corrupt.pdf';path.write_bytes(b'not a PDF')
        result=self.extract(path)
        self.assertEqual(result['status'],'blocked')
        records=[json.loads(p.read_text()) for p in (self.root/'artifacts').glob('*-pdfinfo.json')]
        self.assertEqual(len(records),1)
        self.assertNotEqual(records[0]['returncode'],0)

    def test_command_timeout_records_actual_failure(self):
        ctx=extractors.Context(self.root/'artifacts',0.02)
        with self.assertRaisesRegex(extractors.ExtractionFailure,'timed out'):
            ctx.command([sys.executable,'-c','import time; time.sleep(2)'],'timeout-test')
        log=json.loads(next((self.root/'artifacts').glob('*.json')).read_text())
        self.assertEqual(log['error'],'timeout')

    @unittest.skipUnless(all(CAPABILITIES.values()),'Real PDF/OCR dependencies unavailable; recorded in capabilities.json')
    def test_real_scanned_pdf_and_image_ocr(self):
        # Rendering a text-only PDF creates an actual image with no text layer.
        path=self.root/'original.pdf';write_pdf(path,['TOTAL 275000 EURO CENTS'])
        ctx=extractors.Context(self.root/'raster-build',60)
        prefix=self.root/'scan'
        ctx.command([CAPABILITIES['pdftoppm'],'-f','1','-singlefile','-r','200','-png',path,prefix],'render-test-image')
        image=prefix.with_suffix('.png')
        result=self.extract(image)
        self.assertIn(result['status'],{'ready','partial'})
        self.assertIn('275000',result['text'])
        segment=result['segments'][0]
        self.assertEqual(segment['method'],'tesseract-tsv')
        self.assertIsNotNone(segment['locator']['mean_word_confidence'])
        self.assertTrue(segment['locator']['words'])
        self.assertIn('recognized text only',' '.join(segment['uncertainty']))
        # Use the raster's actual pixel bytes to build a scanned PDF.
        width,height,pixels=_read_rgb_png(image)
        scanned=self.root/'scanned.pdf';_write_image_pdf(scanned,width,height,pixels)
        scan=extractors.extract_document(scanned,self.root/'scan-artifacts')
        self.assertIn('275000',scan['text'])
        self.assertEqual(scan['segments'][0]['anchor'],'pdf-page-0001')
        self.assertEqual(scan['segments'][0]['locator']['origin']['format'],'pdf')
        self.assertTrue((self.root/'scan-artifacts/pdf-page-0001-raster.png').exists())

    @unittest.skipUnless(all(CAPABILITIES.values()),'Real PDF/OCR dependencies unavailable; recorded in capabilities.json')
    def test_mixed_native_and_scanned_page_keeps_both(self):
        path=self.root/'original.pdf';write_pdf(path,['SCANNED BODY 75000 CENTS'])
        ctx=extractors.Context(self.root/'raster-build',60);prefix=self.root/'scan'
        ctx.command([CAPABILITIES['pdftoppm'],'-f','1','-singlefile','-r','100','-png',path,prefix],'render-mixed-image')
        width,height,pixels=_read_rgb_png(prefix.with_suffix('.png'))
        mixed=self.root/'mixed.pdf';_write_image_pdf(mixed,width,height,pixels,native='NATIVE HEADER')
        result=self.extract(mixed)
        self.assertEqual([s['anchor'] for s in result['segments']],['pdf-page-0001','pdf-page-0001-ocr'])
        self.assertIn('NATIVE HEADER',result['segments'][0]['quote'])
        self.assertIn('75000',result['segments'][1]['quote'])


def _read_rgb_png(path):
    """Decode actual pdftoppm RGB PNG including standard row filters, stdlib only."""
    raw=path.read_bytes();offset=8;packed=b''
    while offset<len(raw):
        size=struct.unpack('>I',raw[offset:offset+4])[0];kind=raw[offset+4:offset+8];data=raw[offset+8:offset+8+size];offset+=size+12
        if kind==b'IHDR':
            width,height,depth,color,_,_,interlace=struct.unpack('>IIBBBBB',data)
            if (depth,color,interlace)!=(8,2,0):raise ValueError('Fixture renderer must emit noninterlaced RGB8 PNG')
        if kind==b'IDAT':packed+=data
    filtered=zlib.decompress(packed);stride=width*3;previous=bytearray(stride);pixels=bytearray();offset=0
    for _ in range(height):
        filter_type=filtered[offset];offset+=1;row=bytearray(filtered[offset:offset+stride]);offset+=stride
        for x in range(stride):
            left=row[x-3] if x>=3 else 0;above=previous[x];upper_left=previous[x-3] if x>=3 else 0
            if filter_type==1:predictor=left
            elif filter_type==2:predictor=above
            elif filter_type==3:predictor=(left+above)//2
            elif filter_type==4:
                prediction=left+above-upper_left;distances=[abs(prediction-left),abs(prediction-above),abs(prediction-upper_left)]
                predictor=(left,above,upper_left)[distances.index(min(distances))]
            elif filter_type==0:predictor=0
            else:raise ValueError('Unsupported PNG filter')
            row[x]=(row[x]+predictor)&255
        pixels+=row;previous=row
    return width,height,bytes(pixels)


def _write_image_pdf(path,width,height,pixels,native=None):
    packed=zlib.compress(pixels)
    stream=b'q 612 0 0 792 0 0 cm /Im0 Do Q'
    if native:stream+=f'\nBT /F1 12 Tf 50 780 Td ({native}) Tj ET'.encode()
    objects=[b'<< /Type /Catalog /Pages 2 0 R >>',b'<< /Type /Pages /Count 1 /Kids [3 0 R] >>',
        b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /XObject << /Im0 4 0 R >> /Font << /F1 6 0 R >> >> /Contents 5 0 R >>',
        f'<< /Type /XObject /Subtype /Image /Width {width} /Height {height} /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /FlateDecode /Length {len(packed)} >>\nstream\n'.encode()+packed+b'\nendstream',
        f'<< /Length {len(stream)} >>\nstream\n'.encode()+stream+b'\nendstream',
        b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>']
    _pdf_objects(path,objects)


if __name__=='__main__':unittest.main()
