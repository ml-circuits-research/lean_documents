"""Native extraction with readable Markdown provenance and no JSON artifacts.

The caller retains original source bytes. Converter output is evidence for human
inspection, not an authentication or correctness guarantee.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import re
import shlex

import extractors


def _title(value):
    return str(value).replace('_', ' ').replace('-', ' ').capitalize()


def _literal(value):
    text = str(value)
    fence = '`' * max(3, 1 + max((len(x) for x in re.findall(r'`+', text)), default=0))
    return f'{fence}\n{text}\n{fence}'


def _cell(value):
    if isinstance(value, (list, tuple)):
        value = ', '.join(str(item) for item in value)
    return str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '&#124;').replace('\n', '<br>')


def _render(value, level=2):
    """Render nested provenance as ordinary sections, lists and coordinate tables."""
    if isinstance(value, dict):
        return '\n\n'.join('#' * min(level, 6) + ' ' + _title(key) + '\n\n' + _render(item, level + 1)
                            for key, item in value.items()) or 'None recorded.'
    if isinstance(value, list):
        if not value:
            return 'None recorded.'
        if all(isinstance(item, dict) and all(not isinstance(v, dict) and (not isinstance(v, list) or all(not isinstance(part, (dict, list)) for part in v)) for v in item.values()) for item in value):
            columns = list(dict.fromkeys(key for item in value for key in item))
            rows = ['| ' + ' | '.join(_cell(_title(key)) for key in columns) + ' |',
                    '| ' + ' | '.join('---' for _ in columns) + ' |']
            rows += ['| ' + ' | '.join(_cell(item.get(key, '')) for key in columns) + ' |' for item in value]
            return '\n'.join(rows)
        if all(not isinstance(item, (dict, list)) for item in value):
            return '\n'.join('- ' + _cell(item) for item in value)
        return '\n\n'.join('#' * min(level, 6) + f' Item {index}\n\n' + _render(item, level + 1)
                            for index, item in enumerate(value, 1))
    if isinstance(value, bool):
        return 'Yes' if value else 'No'
    if value is None:
        return 'Not available.'
    return _literal(value)


class MarkdownContext(extractors.Context):
    record_suffix = '.md'

    def __init__(self, artifact_dir, timeout, source):
        super().__init__(artifact_dir, timeout)
        self.source = Path(source)
        self.source_sha256 = hashlib.sha256(self.source.read_bytes()).hexdigest() if self.source.is_file() else None

    def write_record(self, path, record):
        path = Path(path)
        if path.name == 'extraction.md':
            record = {'original_file': self.source.name, 'original_sha256': self.source_sha256,
                      'inspection_limit': 'Extraction and coordinates are converter output. Review the original source; completeness does not authenticate it or guarantee OCR accuracy.',
                      **record}
            title = 'Document extraction'
        elif 'command' in record:
            record = {'command': shlex.join(record['command']), **{key: value for key, value in record.items() if key != 'command'}}
            title = 'Converter execution'
        else:
            title = 'Source coordinates'
        path.write_text('# ' + title + '\n\n' + _render(record) + '\n', encoding='utf-8')

    def result(self):
        result = super().result()
        result['source_sha256'] = self.source_sha256
        return result


def extract_markdown(path, artifact_dir, *, ocr_language='eng', timeout=60, max_pages=None):
    """Return native extractor data in memory and retain only Markdown records.

    Raw XML, images and TSV remain available as technical extraction artifacts.
    Use a distinct artifact directory per extraction; existing artifacts are not
    deleted. The result includes original source_sha256, segments, locators,
    uncertainty, tools, warnings, coverage status and recovered text.
    """
    source = Path(path).resolve()
    return extractors.extract_document(source, Path(artifact_dir), ocr_language=ocr_language,
                                      timeout=timeout, max_pages=max_pages,
                                      context_factory=lambda directory, seconds: MarkdownContext(directory, seconds, source))
