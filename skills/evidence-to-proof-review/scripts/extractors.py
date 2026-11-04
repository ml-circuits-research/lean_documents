#!/usr/bin/env python3
"""Coordinate-preserving document extraction; optional converters are never simulated.

This module extracts evidence for inspection, not verified truth. OCR quotes match
recognized text only and always need comparison with the original visual source.
Converter command arrays never execute instructions found inside documents.
"""
from __future__ import annotations
import csv
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile

OCR_CONFIDENCE_THRESHOLD = 85.0
MAX_XML_MEMBER_BYTES = 20 * 1024 * 1024
MAX_DOCX_TOTAL_BYTES = 100 * 1024 * 1024
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


class ExtractionFailure(Exception):
    pass


class Context:
    def __init__(self, artifact_dir, timeout):
        self.artifacts = Path(artifact_dir)
        self.artifacts.mkdir(parents=True, exist_ok=True)
        self.timeout = timeout
        self.tools = {'python-stdlib': sys.version.split()[0]}
        self.warnings = []
        self.segments = []
        self.complete = True
        self.command_index = 0

    def gap(self, message):
        self.complete = False
        if message not in self.warnings:
            self.warnings.append(message)

    def warn(self, message):
        if message not in self.warnings:
            self.warnings.append(message)

    def command(self, args, label):
        self.command_index += 1
        log = self.artifacts / f'{self.command_index:03d}-{label}.json'
        record = {'command': [str(a) for a in args], 'timeout_seconds': self.timeout}
        try:
            result = subprocess.run([str(a) for a in args], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, timeout=self.timeout)
            record.update(returncode=result.returncode,
                          stdout=result.stdout.decode('utf-8', errors='replace'),
                          stderr=result.stderr.decode('utf-8', errors='replace'))
        except subprocess.TimeoutExpired as exc:
            record.update(error='timeout', stdout=_decode(exc.stdout), stderr=_decode(exc.stderr))
            log.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
            raise ExtractionFailure(f'{label} timed out after {self.timeout} seconds; see {log.name}') from exc
        except OSError as exc:
            record.update(error=str(exc))
            log.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
            raise ExtractionFailure(f'{label} could not execute: {exc}') from exc
        log.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
        if result.returncode:
            raise ExtractionFailure(f'{label} failed with exit code {result.returncode}; see {log.name}')
        return result.stdout, result.stderr

    def tool(self, name):
        executable = shutil.which(name)
        if not executable:
            self.tools[name] = 'unavailable'
            raise ExtractionFailure(f'Optional dependency unavailable: {name}')
        if name not in self.tools:
            flag = '--version' if name == 'tesseract' else '-v'
            stdout, stderr = self.command([executable, flag], name + '-version')
            self.tools[name] = (_decode(stdout) + '\n' + _decode(stderr)).strip().splitlines()[0]
        return executable

    def segment(self, anchor, quote, locator, method, uncertainty=None):
        self.segments.append({'anchor': anchor, 'quote': quote, 'locator': locator,
                              'method': method, 'uncertainty': uncertainty or []})

    def result(self):
        text = '\n\n'.join(f'<a id="{s["anchor"]}"></a>\n{s["quote"]}' for s in self.segments)
        has_text = any(s['quote'].strip() for s in self.segments)
        status = 'ready' if self.complete and has_text else 'partial' if has_text else 'blocked'
        if not has_text:
            self.gap('No nonempty text segments were recovered; inspect the original document.')
        result = {'text': text + ('\n' if text else ''), 'segments': self.segments,
                  'tools': self.tools, 'warnings': self.warnings, 'complete': self.complete,
                  'status': status}
        (self.artifacts / 'extraction.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        return result


def _decode(value):
    return value.decode('utf-8', errors='replace') if isinstance(value, bytes) else value or ''


def _parse_xml(raw):
    if b'<!DOCTYPE' in raw.upper() or b'<!ENTITY' in raw.upper():
        raise ExtractionFailure('XML declarations with DTD/entity definitions are not accepted')
    try:
        return ET.fromstring(raw)
    except ET.ParseError as exc:
        raise ExtractionFailure(f'Invalid XML: {exc}') from exc


def _text(path, ctx):
    try:
        # Preserve original newlines: coordinates are offsets in decoded source.
        raw = path.read_bytes().decode('utf-8-sig')
    except UnicodeError as exc:
        raise ExtractionFailure('Text input is not valid UTF-8; no encoding was guessed') from exc
    matches = list(re.finditer(r'<a\s+id=["\']([^"\']+)["\']\s*>\s*</a>', raw))
    spans = []
    if matches:
        prefix = raw[:matches[0].start()]
        if prefix.strip():
            preamble_anchor = 'document-preamble'
            explicit_ids = {match.group(1) for match in matches}
            while preamble_anchor in explicit_ids:
                preamble_anchor += '-preamble'
            spans.append((preamble_anchor, 0, matches[0].start()))
        used = {anchor for anchor, _, _ in spans}
        for index, match in enumerate(matches):
            anchor = match.group(1)
            if not re.fullmatch(r'[A-Za-z0-9_.:-]+', anchor):
                raise ExtractionFailure(f'Unsupported explicit anchor syntax: {anchor}')
            if anchor in used:
                raise ExtractionFailure(f'Duplicate source anchor: {anchor}')
            used.add(anchor)
            end = matches[index+1].start() if index+1 < len(matches) else len(raw)
            spans.append((anchor, match.end(), end))
    else:
        for index, match in enumerate(re.finditer(r'\S[\s\S]*?(?=\r?\n[ \t]*\r?\n|\Z)', raw), 1):
            spans.append((f'P{index:02d}', match.start(), match.end()))
    for anchor, start, end in spans:
        passage = raw[start:end]
        left = len(passage) - len(passage.lstrip())
        quote = passage.strip()
        start += left
        end = start + len(quote)
        ctx.segment(anchor, quote, {'kind': 'text', 'start_line': raw.count('\n', 0, start)+1,
                    'end_line': raw.count('\n', 0, max(start, end-1))+1,
                    'start_character': start, 'end_character': end,
                    'coordinate_unit': 'Unicode code points after UTF-8 BOM removal'}, 'utf8')
    if not ctx.segments:
        ctx.gap('The text file contains no non-whitespace content.')


def _local(tag):
    return tag.rsplit('}', 1)[-1]


def _pdf_page(raw, page_number):
    # Poppler's XHTML has a fixed external DTD declaration. Remove that declaration
    # before the strict parser; ElementTree never resolves it or fetches a URL.
    raw = re.sub(br'<!DOCTYPE[^>]*>', b'', raw, count=1)
    document = _parse_xml(raw)
    pages = [node for node in document.iter() if _local(node.tag) == 'page']
    if len(pages) != 1:
        raise ExtractionFailure(f'Expected one bbox page for PDF page {page_number}; got {len(pages)}')
    page = pages[0]
    words, lines = [], []
    for line_index, line in enumerate((n for n in page.iter() if _local(n.tag) == 'line'), 1):
        line_words = []
        for node in line:
            if _local(node.tag) != 'word':
                continue
            text = ''.join(node.itertext())
            line_words.append(text)
            words.append({'text': text, 'line': line_index,
                          'bbox': [float(node.attrib[k]) for k in ('xMin', 'yMin', 'xMax', 'yMax')]})
        if line_words:
            lines.append(' '.join(line_words))
    return '\n'.join(lines), {'kind': 'pdf', 'page': page_number,
        'page_width_points': float(page.attrib['width']), 'page_height_points': float(page.attrib['height']),
        'coordinate_unit': 'PDF points; origin at top-left', 'words': words,
        'text_reconstruction': 'Words in Poppler line order, joined by one space; lines joined by newline.'}


def _ocr(image, ctx, anchor, *, page, language, origin):
    tesseract = ctx.tool('tesseract')
    prefix = ctx.artifacts / anchor
    ctx.command([tesseract, image, prefix, '-l', language, '--psm', '3', '-c', 'tessedit_create_tsv=1', '-c', 'tessedit_create_txt=0'], anchor + '-tesseract')
    tsv = prefix.with_suffix('.tsv')
    if not tsv.is_file():
        raise ExtractionFailure(f'OCR returned no TSV artifact for {anchor}')
    words, line_groups = [], {}
    # Tesseract's text column contains literal quote characters. It is TSV,
    # not CSV quoting: a token such as '"For' must not consume later rows.
    for row in csv.DictReader(io.StringIO(tsv.read_text(encoding='utf-8')), delimiter='\t', quoting=csv.QUOTE_NONE):
        if row.get('level') != '5' or not row.get('text', '').strip():
            continue
        try:
            confidence = float(row['conf'])
            box = [int(row[k]) for k in ('left', 'top', 'width', 'height')]
            line_key = tuple(int(row[k]) for k in ('block_num', 'par_num', 'line_num'))
        except (ValueError, KeyError) as exc:
            raise ExtractionFailure(f'Malformed OCR coordinates in {tsv.name}') from exc
        word = {'text': row['text'], 'confidence': confidence, 'bbox': box,
                'line_id': list(line_key)}
        words.append(word)
        line_groups.setdefault(line_key, []).append(row['text'])
    quote = '\n'.join(' '.join(items) for items in line_groups.values())
    confidence = sum(w['confidence'] for w in words) / len(words) if words else None
    uncertain = ['OCR is a probabilistic transcription; quote matching verifies the recognized text only. Visually compare every material quotation with the original image.']
    low_words = sum(w['confidence'] < OCR_CONFIDENCE_THRESHOLD for w in words)
    if not words:
        ctx.gap(f'{anchor}: OCR recognized no words; the page may be blank, unreadable, or contain unsupported content.')
        uncertain.append('No recognized words; original inspection is required.')
    elif low_words:
        ctx.gap(f'{anchor}: {low_words}/{len(words)} OCR words are below confidence {OCR_CONFIDENCE_THRESHOLD:g}.')
        uncertain.append(f'Low-confidence words: {low_words}; review original bounding boxes before relying on text.')
    locator = {'kind': 'ocr', 'page': page, 'origin': origin,
               'coordinate_unit': 'raster pixels; origin at top-left; bbox = left, top, width, height',
               'image_artifact': image.name, 'tsv_artifact': tsv.name,
               'ocr_language': language, 'ocr_page_segmentation_mode': 3,
               'mean_word_confidence': confidence, 'minimum_word_confidence': min((w['confidence'] for w in words), default=None),
               'confidence_threshold': OCR_CONFIDENCE_THRESHOLD, 'low_confidence_words': low_words,
               'word_count': len(words), 'words': words}
    ctx.segment(anchor, quote, locator, 'tesseract-tsv', uncertain)
    ctx.warn('OCR text is not independently verified against the original visual source, regardless of confidence.')


def _pdf(path, ctx, language, max_pages):
    pdfinfo = ctx.tool('pdfinfo')
    stdout, _ = ctx.command([pdfinfo, path], 'pdfinfo')
    info = _decode(stdout)
    match = re.search(r'^Pages:\s*(\d+)\s*$', info, re.M)
    if not match:
        raise ExtractionFailure('pdfinfo did not supply a page count')
    page_count = int(match.group(1))
    pages_to_read = min(page_count, max_pages) if max_pages is not None else page_count
    if pages_to_read < page_count:
        ctx.gap(f'Page limit: extracted {pages_to_read} of {page_count} PDF pages; omitted pages {pages_to_read+1}–{page_count}.')
    image_pages = set()
    try:
        pdfimages = ctx.tool('pdfimages')
        image_list, _ = ctx.command([pdfimages, '-list', path], 'pdfimages-list')
        for line in _decode(image_list).splitlines():
            fields = line.split()
            if len(fields) > 2 and fields[0].isdigit() and fields[1].isdigit():
                image_pages.add(int(fields[0]))
    except ExtractionFailure as exc:
        # Without image detection every page needs raster inspection/OCR so a text
        # header cannot cause scanned body content to be silently omitted.
        ctx.warn(str(exc) + '; attempt raster OCR on every page to cover possible mixed content.')
        image_pages = set(range(1, pages_to_read+1))
    pdftotext = ctx.tool('pdftotext')
    for page in range(1, pages_to_read+1):
        anchor = f'pdf-page-{page:04d}'
        bbox_path = ctx.artifacts / (anchor + '.bbox.xhtml')
        text = ''
        native_failed = False
        try:
            ctx.command([pdftotext, '-f', str(page), '-l', str(page), '-bbox-layout', '-enc', 'UTF-8', path, bbox_path], anchor + '-bbox')
            text, locator = _pdf_page(bbox_path.read_bytes(), page)
            locator.update(bbox_artifact=bbox_path.name, total_pages=page_count)
            (ctx.artifacts / (anchor + '.words.json')).write_text(json.dumps(locator, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
            if text.strip():
                uncertainty = ['PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.']
                if page in image_pages:
                    uncertainty.append('This page also contains raster images; OCR is preserved as a separate supplement and may overlap native text.')
                ctx.segment(anchor, text, locator, 'poppler-bbox-layout', uncertainty)
        except (ExtractionFailure, OSError, ValueError, KeyError) as exc:
            native_failed = True
            ctx.warn(f'{anchor}: native text extraction failed: {exc}; attempting OCR.')
        if native_failed or not text.strip() or page in image_pages:
            try:
                pdftoppm = ctx.tool('pdftoppm')
                prefix = ctx.artifacts / (anchor + '-raster')
                ctx.command([pdftoppm, '-f', str(page), '-l', str(page), '-singlefile', '-r', '200', '-png', path, prefix], anchor + '-raster')
                raster = prefix.with_suffix('.png')
                if not raster.is_file():
                    raise ExtractionFailure('PDF rasterization produced no PNG')
                ocr_anchor = anchor + '-ocr' if text.strip() else anchor
                _ocr(raster, ctx, ocr_anchor, page=page, language=language,
                     origin={'format': 'pdf', 'page': page, 'raster_dpi': 200,
                             'pixel_to_pdf_points': 'coordinate * 72 / 200', 'total_pages': page_count})
            except (ExtractionFailure, OSError, ValueError) as exc:
                ctx.gap(f'{anchor}: OCR coverage unavailable: {exc}')
                if not text.strip():
                    ctx.segment(anchor, '', {'kind': 'pdf', 'page': page, 'total_pages': page_count},
                                'unavailable', [str(exc), 'No readable text recovered for this page.'])


def _paragraph_text(element):
    values = []
    for node in element.iter():
        if node.tag in {W+'t', W+'delText'}:
            values.append(node.text or '')
        elif node.tag == W+'tab':
            values.append('\t')
        elif node.tag in {W+'br', W+'cr'}:
            values.append('\n')
    return ''.join(values)


def _docx(path, ctx):
    ctx.tools['docx-zip-xml'] = 'Python zipfile and ElementTree ' + sys.version.split()[0]
    with zipfile.ZipFile(path) as package:
        members = package.infolist()
        if len({item.filename for item in members}) != len(members):
            raise ExtractionFailure('DOCX has duplicate ZIP member names; interpretation is ambiguous')
        if sum(item.file_size for item in members) > MAX_DOCX_TOTAL_BYTES:
            raise ExtractionFailure('DOCX exceeds the 100 MiB uncompressed extraction bound')
        names = set(package.namelist())
        if 'word/document.xml' not in names:
            raise ExtractionFailure('DOCX is missing word/document.xml')
        desired = ['word/document.xml'] + sorted(n for n in names if re.fullmatch(r'word/header\d+\.xml', n))
        desired += sorted(n for n in names if re.fullmatch(r'word/footer\d+\.xml', n))
        desired += [n for n in ('word/footnotes.xml', 'word/endnotes.xml', 'word/comments.xml') if n in names]
        ctx.warn('DOCX segments follow body XML order, then header/footer members and notes/comments in member order. This is not rendered pagination or the placement of repeated page headers; no page coordinates are inferred.')
        if any(n.startswith('word/embeddings/') or n.endswith('vbaProject.bin') for n in names):
            ctx.gap('DOCX contains embedded objects or macros; these are not executed or interpreted.')
        raw_dir = ctx.artifacts / 'docx-xml'; raw_dir.mkdir(exist_ok=True)
        for member in desired:
            info = package.getinfo(member)
            if info.file_size > MAX_XML_MEMBER_BYTES:
                ctx.gap(f'{member} exceeds the 20 MiB XML member bound; skipped.')
                continue
            raw = package.read(member)
            (raw_dir / Path(member).name).write_bytes(raw)
            document = _parse_xml(raw)
            story = Path(member).stem
            prefix = 'docx' if story == 'document' else 'docx-' + story
            context_uncertainty = []
            if story.startswith(('header', 'footer')):
                context_uncertainty.append('Header/footer story; the extraction does not resolve page/section repetition or visibility.')
            if story == 'comments':
                context_uncertainty.append('Comment annotation, not main document assertions; preserve author attribution.')
            index = {'p': 0, 'table': 0}

            def paragraph(node, xpath, *, anchor=None, extra=None, inherited=None):
                index['p'] += 1
                if anchor is None:
                    anchor = f'{prefix}-p-{index["p"]:04d}'
                quote = _paragraph_text(node)
                tags = {_local(n.tag) for n in node.iter()}
                uncertain = list(context_uncertainty) + list(inherited or [])
                if tags & {'ins', 'del', 'moveFrom', 'moveTo', 'pPrChange', 'rPrChange'}:
                    uncertain.append('Tracked changes are present; inserted and deleted text are both transcribed in XML order. No accepted revision is selected.')
                    ctx.gap(f'{anchor}: tracked changes require a revision interpretation.')
                if tags & {'commentRangeStart', 'commentRangeEnd', 'commentReference'}:
                    uncertain.append('Comment markers present; consult the separately extracted comments story and original range.')
                if tags & {'instrText', 'fldChar', 'fldSimple'}:
                    uncertain.append('Field instructions are not evaluated; only stored textual field results are transcribed.')
                    ctx.warn(f'{anchor}: field values may be stale; inspect the original field context.')
                unsupported = tags & {'drawing', 'pict', 'object', 'altChunk', 'oMath', 'oMathPara', 'txbxContent'}
                if unsupported:
                    uncertain.append('Unsupported visual/embedded content: ' + ', '.join(sorted(unsupported)) + '. Text alone does not cover it.')
                    ctx.gap(f'{anchor}: unsupported objects require original inspection.')
                if tags & {'vanish', 'webHidden'}:
                    uncertain.append('Hidden text formatting is present; XML text may differ from rendered visibility.')
                locator = {'kind': 'docx', 'member': member, 'xml_path': xpath,
                           'paragraph_index_in_story': index['p'], 'story': story,
                           'raw_xml_artifact': 'docx-xml/' + Path(member).name,
                           'footnote_ids': [n.get(W+'id') for n in node.iter(W+'footnoteReference')],
                           'endnote_ids': [n.get(W+'id') for n in node.iter(W+'endnoteReference')],
                           'comment_ids': [n.get(W+'id') for n in node.iter(W+'commentReference')]}
                if extra: locator.update(extra)
                # Empty layout paragraphs do not manufacture content. Empty objects
                # still get a segment so their extraction gap remains coordinateable.
                if quote or uncertain:
                    ctx.segment(anchor, quote, locator, 'docx-xml', uncertain)

            def table(node, xpath, inherited=None):
                index['table'] += 1
                table_number = index['table']
                def revision_context(properties, label, inherited_context):
                    uncertain = list(inherited_context or [])
                    tags = {_local(n.tag) for prop in properties if prop is not None for n in prop.iter()}
                    changes = tags & {'ins', 'del', 'moveFrom', 'moveTo', 'tblPrChange', 'tblGridChange',
                                      'trPrChange', 'tcPrChange', 'cellIns', 'cellDel', 'cellMerge'}
                    if changes:
                        uncertain.append('Tracked ' + label + ' changes: ' + ', '.join(sorted(changes)) + '; no accepted revision selected.')
                        ctx.gap(f'{member}: tracked {label} changes require a revision interpretation.')
                    return uncertain
                table_uncertain = revision_context([node.find(W+'tblPr'), node.find(W+'tblGrid')], 'table', inherited)
                for row_number, row in enumerate(node.findall(W+'tr'), 1):
                    row_uncertain = revision_context([row.find(W+'trPr')], 'table row', table_uncertain)
                    for cell_number, cell in enumerate(row.findall(W+'tc'), 1):
                        cell_info = {'table_index': table_number, 'row': row_number, 'cell': cell_number}
                        grid_span = cell.find('./'+W+'tcPr/'+W+'gridSpan')
                        merge = cell.find('./'+W+'tcPr/'+W+'vMerge')
                        if grid_span is not None: cell_info['grid_span'] = grid_span.get(W+'val')
                        if merge is not None: cell_info['vertical_merge'] = merge.get(W+'val', 'continue')
                        cell_uncertain = revision_context([cell.find(W+'tcPr')], 'table cell', row_uncertain)
                        if grid_span is not None or merge is not None:
                            cell_uncertain.append('Merged table cell; row/cell positions are XML positions, not inferred visual columns.')
                        paragraph_number = 0
                        for child in cell:
                            tag = _local(child.tag)
                            if tag == 'p':
                                paragraph_number += 1
                                paragraph(child, f'{xpath}/w:tr[{row_number}]/w:tc[{cell_number}]/w:p[{paragraph_number}]',
                                    anchor=f'{prefix}-table-{table_number:04d}-r{row_number:04d}-c{cell_number:04d}-p{paragraph_number:04d}',
                                    extra=cell_info, inherited=cell_uncertain)
                            elif tag == 'tbl':
                                table(child, f'{xpath}/w:tr[{row_number}]/w:tc[{cell_number}]/w:tbl', cell_uncertain + ['Nested table; inspect parent cell layout.'])
                            elif tag not in {'tcPr'}:
                                ctx.gap(f'{member}: unsupported table-cell element {tag}.')

            def walk(container, xpath, inherited=None):
                counts = {}
                for child in container:
                    tag = _local(child.tag)
                    counts[tag] = counts.get(tag, 0) + 1
                    child_path = f'{xpath}/w:{tag}[{counts[tag]}]'
                    if tag == 'p': paragraph(child, child_path, inherited=inherited)
                    elif tag == 'tbl': table(child, child_path, inherited)
                    elif tag in {'ins', 'del', 'moveFrom', 'moveTo'}:
                        ctx.gap(f'{member}: tracked block changes require a revision interpretation.')
                        walk(child, child_path, list(inherited or []) + ['Tracked block change: ' + tag + '; no accepted revision selected.'])
                    elif tag == 'sdt':
                        content = child.find(W+'sdtContent')
                        if content is not None: walk(content, child_path+'/w:sdtContent', inherited)
                        ctx.warn(f'{member}: content control text is extracted without evaluating bindings.')
                    elif tag not in {'sectPr', 'bookmarkStart', 'bookmarkEnd', 'proofErr', 'permStart', 'permEnd'}:
                        ctx.gap(f'{member}: unsupported block element {tag}; inspect original.')
            if story == 'document':
                body = document.find(W+'body')
                if body is None: raise ExtractionFailure('DOCX main document has no body')
                walk(body, '/w:document/w:body')
            elif story in {'footnotes', 'endnotes', 'comments'}:
                for note in document:
                    ident = note.get(W+'id', '')
                    if ident.startswith('-') or note.get(W+'type') in {'separator', 'continuationSeparator'}:
                        continue
                    attribution = []
                    if story == 'comments':
                        attribution.append(f'Comment author: {note.get(W+"author", "unspecified")}; date: {note.get(W+"date", "unspecified")}.')
                    walk(note, f'/w:{story}/w:{_local(note.tag)}[@w:id="{ident}"]', attribution)
            else:
                walk(document, '/w:'+_local(document.tag))


def extract_document(path: Path, artifact_dir: Path, *, ocr_language='eng', timeout=60, max_pages=None):
    """Extract inspected text and original coordinates, preserving raw artifacts.

    ``complete`` describes coverage/recoverability, not source authenticity or OCR
    correctness. ``partial`` retains usable portions plus explicit coverage gaps;
    ``blocked`` means no nonempty text was recovered. Caller preserves originals.
    Existing artifacts are not deleted; callers must use a distinct run directory.
    """
    ctx = Context(artifact_dir, timeout)
    path = Path(path).resolve()
    try:
        if not path.is_file(): raise ExtractionFailure(f'Input file does not exist: {path}')
        if timeout <= 0: raise ExtractionFailure('timeout must be positive')
        if max_pages is not None and (not isinstance(max_pages, int) or max_pages < 1):
            raise ExtractionFailure('max_pages must be a positive integer')
        if not re.fullmatch(r'[A-Za-z0-9_+-]+', ocr_language):
            raise ExtractionFailure('Invalid OCR language identifier')
        extension = path.suffix.lower()
        if extension in {'.md', '.markdown', '.txt', '.text', '.csv'}:
            _text(path, ctx)
        elif extension == '.pdf':
            _pdf(path, ctx, ocr_language, max_pages)
        elif extension == '.docx':
            if max_pages is not None:
                ctx.warn('max_pages does not apply to DOCX XML stories: rendered pagination is unavailable; all supported XML stories are extracted.')
            _docx(path, ctx)
        elif extension in {'.png', '.jpg', '.jpeg'}:
            image = ctx.artifacts / ('image-original' + extension)
            shutil.copyfile(path, image)
            _ocr(image, ctx, 'image-page-0001', page=1, language=ocr_language,
                 origin={'format': extension.lstrip('.'), 'original_file': path.name})
        else:
            raise ExtractionFailure(f'Unsupported document format: {extension or "no extension"}')
    except (ExtractionFailure, OSError, ValueError, KeyError, zipfile.BadZipFile, RuntimeError) as exc:
        ctx.gap(str(exc))
    return ctx.result()
