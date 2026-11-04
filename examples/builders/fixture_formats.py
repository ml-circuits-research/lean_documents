"""Deterministic native-format synthetic fixtures (not runtime dependencies).

PDF and DOCX writers use the standard library. Raster scan generation uses PIL.
Visible markers are document content, not answers or expected audit outcomes.
"""
from pathlib import Path
import io
import textwrap
import zipfile
from xml.sax.saxutils import escape


def _pdf(path, objects):
    output = bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
    offsets = [0]
    for index, obj in enumerate(objects, 1):
        offsets.append(len(output))
        output.extend(f'{index} 0 obj\n'.encode() + obj + b'\nendobj\n')
    start = len(output)
    output.extend(f'xref\n0 {len(objects)+1}\n0000000000 65535 f \n'.encode())
    for offset in offsets[1:]: output.extend(f'{offset:010d} 00000 n \n'.encode())
    output.extend(f'trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{start}\n%%EOF\n'.encode())
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_bytes(output)


def _lines(text, width=92):
    lines = []
    for line in text.splitlines():
        lines.extend(textwrap.wrap(line, width=width, replace_whitespace=False) or [''])
    return lines


def write_pdf(path, pages):
    """Write searchable PDF; long supplied pages overflow into additional pages."""
    sheets = []
    for text in pages:
        lines = _lines(text)
        sheets.extend(lines[i:i+52] for i in range(0, len(lines), 52))
    objects = [b'<< /Type /Catalog /Pages 2 0 R >>', b'', b'<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>']
    ids = []
    for sheet in sheets:
        page = len(objects)+1; ids.append(page)
        objects.append(f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 3 0 R >> >> /Contents {page+1} 0 R >>'.encode())
        content = ['BT /F1 9 Tf 12 TL 35 755 Td']
        for line in sheet:
            value = line.encode('ascii', 'replace').decode().replace('\\','\\\\').replace('(','\\(').replace(')','\\)')
            content.append(f'({value}) Tj T*')
        stream = ('\n'.join(content)+'\nET\n').encode()
        objects.append(f'<< /Length {len(stream)} >>\nstream\n'.encode()+stream+b'endstream')
    objects[1]=f'<< /Type /Pages /Count {len(ids)} /Kids [{" ".join(str(i)+" 0 R" for i in ids)}] >>'.encode()
    _pdf(path,objects)


def write_docx(path, paragraphs):
    """Write paragraphs; nested list items represent table rows/cells."""
    def para(text):return '<w:p><w:r><w:t xml:space="preserve">'+escape(str(text))+'</w:t></w:r></w:p>'
    body=[]
    for item in paragraphs:
        if isinstance(item,list):
            body.append('<w:tbl>'+''.join('<w:tr>'+''.join('<w:tc>'+para(cell)+'</w:tc>' for cell in row)+'</w:tr>' for row in item)+'</w:tbl>')
        else:body.append(para(item))
    xml='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'+''.join(body)+'<w:sectPr/></w:body></w:document>'
    types='<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>'
    rels='<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>'
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
        for name,text in [('[Content_Types].xml',types),('_rels/.rels',rels),('word/document.xml',xml)]:
            entry=zipfile.ZipInfo(name,date_time=(2026,11,4,0,0,0));entry.compress_type=zipfile.ZIP_DEFLATED;z.writestr(entry,text)


def write_scan_pdf(path,pages,*,faint_contains=None):
    """Image-only PDF; optional phrase rendered pale to exercise OCR uncertainty."""
    from PIL import Image,ImageDraw,ImageFont
    import subprocess
    fontfile=subprocess.check_output(['fc-match','monospace','-f','%{file}'],text=True).strip()
    font=ImageFont.truetype(fontfile,24)
    sheets=[]
    for text in pages:
        lines=_lines(text,width=85)
        for i in range(0,len(lines),50):
            canvas=Image.new('RGB',(1800,2400),'white');draw=ImageDraw.Draw(canvas)
            for j,line in enumerate(lines[i:i+50]):
                shade=(205,205,205) if faint_contains and faint_contains in line else (20,20,20)
                draw.text((70,80+j*43),line,font=font,fill=shade)
            sheets.append(canvas)
    objects=[b'<< /Type /Catalog /Pages 2 0 R >>',b''];ids=[]
    for canvas in sheets:
        page=len(objects)+1;ids.append(page)
        objects.append(f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 600 800] /Resources << /XObject << /Scan {page+2} 0 R >> >> /Contents {page+1} 0 R >>'.encode())
        stream=b'q 600 0 0 800 0 0 cm /Scan Do Q\n'
        objects.append(f'<< /Length {len(stream)} >>\nstream\n'.encode()+stream+b'endstream')
        out=io.BytesIO();canvas.save(out,format='JPEG',quality=95);raw=out.getvalue()
        objects.append(f'<< /Type /XObject /Subtype /Image /Width 1800 /Height 2400 /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length {len(raw)} >>\nstream\n'.encode()+raw+b'\nendstream')
    objects[1]=f'<< /Type /Pages /Count {len(ids)} /Kids [{" ".join(str(i)+" 0 R" for i in ids)}] >>'.encode()
    _pdf(path,objects)
