#!/usr/bin/env python3
"""Inline data/ into app/template.html -> app/index.html and docs/index.html (the GitHub Pages site)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
read = lambda p: json.loads((root / p).read_text(encoding="utf-8"))
data = {
    "site": read("data/site.json"),
    "problems": read("data/problems.json"),
    "national": read("data/national.json"),
    "states": read("data/states.json"),
    "cities": [json.loads(p.read_text(encoding="utf-8")) for p in sorted((root / "data/cities").glob("*.json"))],
}
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
template = (root / "app/template.html").read_text(encoding="utf-8")
assert "/*__DATA__*/" in template, "placeholder missing"
html = template.replace("/*__DATA__*/", blob)
# GitHub Pages serves a full document, so add the head the artifact viewer would otherwise add
page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="description" content="Find which office is responsible for a civic problem in your city, how to complain, and how to escalate.">\n'
        '</head>\n<body>\n' + html + '\n</body>\n</html>\n')
(root / "app/index.html").write_text(html, encoding="utf-8")
(root / "docs/index.html").write_text(page, encoding="utf-8")
print(f"Built app/index.html and docs/index.html: {len(data['cities'])} cities, {len(data['problems']['problems'])} problem types")
