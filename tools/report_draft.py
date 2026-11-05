#!/usr/bin/env python3
"""Check retained report draft structure; never certify substantive conclusions."""
from pathlib import Path
import argparse
import re
import sys
from urllib.parse import unquote, urlsplit


def confined(root, value):
    path = root / value
    if path.is_absolute() and not path.is_relative_to(root):
        raise ValueError(f'Path is outside the generation workspace: {value}')
    for part in [path, *path.parents]:
        if part == root.parent:
            break
        if part.is_symlink():
            raise ValueError(f'Symlink is not a retained generation artifact: {value}')
    resolved = path.resolve()
    if not resolved.is_relative_to(root) or not resolved.is_file():
        raise ValueError(f'Missing or external retained file: {value}')
    return resolved


def validate(workspace):
    supplied = Path(workspace).absolute()
    if any(part.is_symlink() for part in [supplied, *supplied.parents]):
        raise ValueError('The generation workspace must not traverse a symlink')
    root = supplied.resolve()
    documents = {}
    for name in ('report.md', 'generation-notes.md'):
        path = confined(root, name)
        text = path.read_text(encoding='utf-8')
        if len(text.strip()) < 80 or not re.match(r'^# [^\n]+\n', text):
            raise ValueError(f'{name} needs a Markdown title and substantive readable prose')
        if re.search(r'^\s*(?:<!DOCTYPE|<html|```json)', text, re.I | re.M):
            raise ValueError(f'{name} must be a narrative Markdown document')
        documents[name] = text
    report = documents['report.md']
    headings = list(re.finditer(r'^## (R\d{2,})\s+[—:-]\s+(.+)$', report, re.M))
    if not headings:
        raise ValueError('The report needs at least one substantive R01-style finding heading')
    if [m[1] for m in headings] != [f'R{i:02d}' for i in range(1, len(headings) + 1)]:
        raise ValueError('Report finding anchors must be unique and sequential from R01')
    for index, heading in enumerate(headings):
        section = report[heading.end():headings[index + 1].start() if index + 1 < len(headings) else len(report)].strip()
        paragraphs = [p for p in re.split(r'\n\s*\n', section) if p.strip()]
        if len(section) < 60 or len(paragraphs) < 2:
            raise ValueError(f'{heading[1]} needs a substantive claim and a separate rationale paragraph')
        citations = re.findall(r'\[([^\]]*\bS\d+\b[^\]]*)\]\(([^)]+)\)', section)
        if not citations:
            raise ValueError(f'{heading[1]} needs a descriptive source-ID citation')
        for label, target in citations:
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path or not url.fragment:
                raise ValueError(f'{heading[1]} needs retained local source links with anchors')
            source = confined(root, unquote(url.path))
            if source.name in documents:
                raise ValueError('A generated report or its notes cannot be cited as independent source evidence')
            text = source.read_text(encoding='utf-8')
            for ident in re.findall(r'\bS\d+\b', label):
                if not re.search(r'\b' + re.escape(ident) + r'\b', text):
                    raise ValueError(f'Cited source ID {ident} is absent from {source.name}')
    return f'Validated {len(headings)} anchored findings and both retained Markdown documents. This structural check does not certify source correspondence or substantive correctness.'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True)
    args = parser.parse_args(argv)
    try:
        print(validate(args.workspace))
    except (ValueError, OSError) as error:
        print(f'Draft validation failed: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
