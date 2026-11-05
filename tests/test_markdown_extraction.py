"""Execute native extraction and check Markdown-only provenance artifacts."""
import hashlib
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/evidence-to-proof-review/scripts'))
import markdown_extraction
import test_extractors as fixtures


class MarkdownExtractionTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / 'tmp/markdown-extraction-tests'
        base.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix='run-', dir=base))

    def check_artifacts(self, source, result):
        self.assertEqual(list(self.root.rglob('*.json')), [])
        self.assertEqual(list(self.root.rglob('*.jsonl')), [])
        self.assertEqual(result['source_sha256'], hashlib.sha256(source.read_bytes()).hexdigest())
        text = (self.root / 'artifacts/extraction.md').read_text()
        self.assertIn(result['source_sha256'], text)
        self.assertIn('## Original file', text)
        self.assertIn('## Segments', text)

    def test_docx_keeps_coordinates_and_original_hash(self):
        source = self.root / 'policy.docx'
        fixtures.write_docx(source, '<w:p><w:r><w:t>Charge limit is 50 credits.</w:t></w:r></w:p>')
        result = markdown_extraction.extract_markdown(source, self.root / 'artifacts')
        self.assertEqual(result['status'], 'ready')
        self.assertIn('Charge limit is 50 credits.', result['text'])
        self.assertTrue(result['segments'][0]['locator'])
        self.check_artifacts(source, result)

    @unittest.skipUnless(all(shutil.which(tool) for tool in ('pdfinfo', 'pdftotext', 'pdfimages')), 'PDF converters unavailable')
    def test_pdf_retains_word_table_and_page_limit(self):
        source = self.root / 'ledger.pdf'
        fixtures.write_pdf(source, ['First page amount 60', 'Second page amount 40'])
        result = markdown_extraction.extract_markdown(source, self.root / 'artifacts', max_pages=1)
        self.assertEqual(result['status'], 'partial')
        self.assertFalse(result['complete'])
        self.assertTrue(any('Page limit' in warning for warning in result['warnings']))
        self.assertTrue(result['segments'][0]['uncertainty'])
        words = (self.root / 'artifacts/pdf-page-0001.words.md').read_text()
        self.assertIn('|', words)
        self.assertIn('## Words', words)
        commands = list((self.root / 'artifacts').glob('*-bbox.md'))
        self.assertEqual(len(commands), 1)
        self.assertIn('## Returncode\n\n```\n0', commands[0].read_text())
        self.check_artifacts(source, result)

    @unittest.skipUnless(all(shutil.which(tool) for tool in ('pdfinfo', 'pdftotext', 'pdfimages', 'pdftoppm', 'tesseract')), 'OCR converters unavailable')
    def test_actual_scanned_receipt_retains_ocr_uncertainty(self):
        source = self.root / 'receipt.pdf'
        shutil.copyfile(ROOT / 'examples/15-native-revision/sources/03-receipt-scan.pdf', source)
        result = markdown_extraction.extract_markdown(source, self.root / 'artifacts')
        self.assertTrue(result['segments'])
        self.assertTrue(any(segment['locator'].get('kind') == 'ocr' for segment in result['segments']))
        self.assertTrue(any(segment['uncertainty'] for segment in result['segments']))
        self.assertTrue(list((self.root / 'artifacts').glob('*.tsv')))
        self.assertTrue(list((self.root / 'artifacts').glob('*.png')))
        self.check_artifacts(source, result)

    def test_missing_converter_returns_documented_blockage(self):
        source = self.root / 'ledger.pdf'
        fixtures.write_pdf(source, ['Amount 60'])
        with patch.object(markdown_extraction.extractors.shutil, 'which', return_value=None):
            result = markdown_extraction.extract_markdown(source, self.root / 'artifacts')
        self.assertEqual(result['status'], 'blocked')
        self.assertTrue(any('unavailable' in warning for warning in result['warnings']))
        self.check_artifacts(source, result)


if __name__ == '__main__':
    unittest.main()
