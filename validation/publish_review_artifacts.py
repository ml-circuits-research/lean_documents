#!/usr/bin/env python3
"""Publish offline, escaped text viewers for the retained flexibility review runs.

Run after copying reviewed run artifacts to docs/flexibility-data/. This script
reads only published copies; it needs no tmp workspace or external package.
"""
from html import escape
import os
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOCS = REPO / 'docs'
DATA = DOCS / 'flexibility-data'


def link(path, origin):
    return escape(os.path.relpath(path, origin.parent).replace(os.sep, '/'), quote=True)


def page(destination, title, content, back):
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>' + escape(title) + ' · Evidence-to-Proof Review</title>'
        '<link rel="stylesheet" href="' + link(DOCS / 'assets/style.css', destination) + '"></head>'
        '<body><a class="skip" href="#main">Skip to content</a><header>'
        '<a class="brand" href="' + link(DOCS / 'index.html', destination) + '">Evidence-to-Proof Review</a>'
        '<nav aria-label="Artifact navigation"><a href="' + link(back, destination) + '">Back to review</a>'
        '<a href="' + link(DOCS / 'examples/index.html', destination) + '">Example catalog</a></nav></header>'
        '<main id="main"><h1>' + escape(title) + '</h1>' + content + '</main>'
        '<footer>Preserved execution artifacts. Text viewers work offline and over HTTP.</footer></body></html>',
        encoding='utf-8')


def publish(name, title, raw_subdirectory=False):
    root = DATA / name
    source = root / 'raw' if raw_subdirectory else root
    if not source.is_dir():
        raise SystemExit('Missing reviewed artifact directory: ' + str(source))
    index = root / 'index.html'
    files = [p for p in source.rglob('*') if p.is_file()
             and '_views' not in p.relative_to(source).parts and p != index]
    rows = []
    for artifact in sorted(files):
        relative = artifact.relative_to(source)
        viewer = root / '_views' / (relative.as_posix() + '.html')
        try:
            body = artifact.read_text(encoding='utf-8')
            if '\0' in body:
                raise UnicodeError('Binary artifact')
        except UnicodeError:
            view = 'Binary artifact'
        else:
            page(viewer, artifact.name,
                 '<p><code>' + escape(relative.as_posix()) + '</code></p><p><a href="'
                 + link(artifact, viewer) + '">Open original file</a></p><pre><code>'
                 + escape(body) + '</code></pre>', index)
            view = '<a href="' + link(viewer, index) + '">Read text</a>'
        rows.append('<tr><td><code>' + escape(relative.as_posix()) + '</code></td><td>' + view
                    + '</td><td><a href="' + link(artifact, index) + '">Original</a></td></tr>')
    page(index, title,
         '<p>Inspect the selected input, source mappings, claims, models, exact-target checks, '
         'compiler logs and review records. Earlier failed attempts remain labelled as attempts; '
         'the final result identifies the delivered state.</p><div class="table-wrap"><table>'
         '<thead><tr><th>Artifact</th><th>Viewer</th><th>Preserved file</th></tr></thead><tbody>'
         + ''.join(rows) + '</tbody></table></div>', DOCS / 'flexibility-review.html')
    return len(files)


if __name__ == '__main__':
    print('Native artifacts:', publish('agent-native', 'Lean-only audit: evidence and arguments'))
    print('Portable artifacts:', publish('portable-audit', 'Copied-skill audit: complete workflow', True))
