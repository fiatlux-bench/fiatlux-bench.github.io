#!/usr/bin/env python3
"""Stamp the stylesheet link with a content hash.

GitHub Pages sends cache-control: max-age=600 on every file and the header
cannot be configured. The HTML and the CSS therefore expire independently, so
for up to ten minutes a visitor can hold new markup against a cached old
stylesheet, or the reverse. Giving the stylesheet a content-derived query
string means updated CSS is a new URL, which no cache can satisfy from an old
entry. Run this after editing style.css, before committing.
"""
import hashlib, pathlib, re

root = pathlib.Path(__file__).parent
css = root / "static/css/style.css"
digest = hashlib.sha256(css.read_bytes()).hexdigest()[:10]

html_path = root / "index.html"
html = html_path.read_text(encoding="utf-8")
new, n = re.subn(r'href="static/css/style\.css(?:\?v=[0-9a-f]+)?"',
                 f'href="static/css/style.css?v={digest}"', html)
if n != 1:
    raise SystemExit(f"expected one stylesheet link, found {n}")
html_path.write_text(new, encoding="utf-8")
print(f"stylesheet stamped: ?v={digest}")
