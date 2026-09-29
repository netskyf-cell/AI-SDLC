"""Convert the Thiga dojo page (dojo/ai-sdlc.html) into Markdown files.

The HTML is a single-page app: each lesson is a <section class="site-page">.
This script writes one Markdown file per module (Plan, Design, Build...)
into docs/dojo/, plus a README.md index.

Usage: python3 docs/convert_dojo.py [input.html] [output_dir]
"""
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as md

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "dojo/ai-sdlc.html")
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else "docs/dojo")

# Module order, keyed by the prefix of each lesson's section id.
MODULES = [
    ("course", "00-introduction", "Introduction"),
    ("plan", "01-plan", "Module 1 · Plan"),
    ("design", "02-design", "Module 2 · Design"),
    ("build", "03-build", "Module 3 · Build"),
    ("test", "04-test", "Module 4 · Test"),
    ("deploy", "05-deploy", "Module 5 · Deploy"),
    ("maintain", "06-maintain", "Module 6 · Maintain"),
    ("conclusion", "07-conclusion", "Module 7 · Conclusion"),
]
# Visual-only elements: code/styling, UI mockups, navigation, copy buttons.
DROP = [
    "script", "style", "svg", "noscript", "img", "button", "form",
    "[role=img]", ".pagination", ".module-pagination", ".copy-status", ".journey-number",
]
NOTICE = (
    "<!-- Converted from thiga-co/dojo-ai-native-sdlc-from-the-tranches "
    "(ai-sdlc.html). MIT License, Copyright (c) 2026 Thiga. -->\n\n"
)


def lesson_to_md(section):
    root = section.find("main") or section
    for sel in DROP:
        for tag in root.select(sel):
            tag.decompose()
    text = md(str(root), heading_style="ATX", bullets="-")
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def main():
    soup = BeautifulSoup(SRC.read_text(encoding="utf-8"), "html.parser")
    pages = soup.select("section.site-page")
    OUT.mkdir(parents=True, exist_ok=True)

    index = [NOTICE + "# AI-Native SDLC from the trenches — Dojo\n"]
    for prefix, filename, title in MODULES:
        lessons = [p for p in pages if p["id"].split("-")[0] == prefix]
        body = "\n\n---\n\n".join(lesson_to_md(p) for p in lessons)
        path = OUT / f"{filename}.md"
        path.write_text(f"{NOTICE}# {title}\n\n{body}\n", encoding="utf-8")
        index.append(f"- [{title}]({path.name}) ({len(lessons)} lessons)")
        print(f"Wrote {path} ({len(lessons)} lessons, {len(body):,} chars)")

    (OUT / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
