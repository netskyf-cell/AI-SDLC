"""Convert the Thiga dojo page (dojo/ai-sdlc.html) into Markdown files.

The HTML is a single-page app: each lesson is a <section class="site-page">.
This script writes, into docs/dojo/:
- one Markdown file per module (Plan, Design, Build...) plus a README.md index;
- lessons.json, the lesson HTML the docs/index.html reader loads.

Screenshots come from docs/dojo/img/, made by docs/screenshot_dojo.mjs
(run it first). Its manifest.json lists each lesson's images in page order.

Usage: python3 docs/convert_dojo.py [input.html] [output_dir]
"""
import json
import re
import sys
from pathlib import Path

import markdown
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
# Screen mockups and diagrams, replaced by their screenshot.
VISUALS = ".reader-screen, .reader-panel"
# Visual-only elements: code/styling, UI mockups, navigation, copy buttons.
DROP = [
    "script", "style", "svg", "noscript", "button", "form",
    "[role=img]", ".pagination", ".module-pagination", ".copy-status", ".journey-number",
]
NOTICE = (
    "<!-- Converted from thiga-co/dojo-ai-native-sdlc-from-the-tranches "
    "(ai-sdlc.html). MIT License, Copyright (c) 2026 Thiga. -->\n\n"
)


def swap_visuals(soup, root, images):
    """Replace each mockup or diagram with an <img> of its screenshot."""
    for visual, name in zip(root.select(VISUALS), images):
        caption = visual.find("figcaption")
        activity = visual.find_parent(class_="activity")
        heading = activity.find(["h2", "h3"]) if activity else None
        alt = (caption or heading).get_text(" ", strip=True) if (caption or heading) else "Capture d’écran"
        img = soup.new_tag("img", src=f"img/{name}", alt=alt)
        para = soup.new_tag("p")
        para.append(img)
        if caption:
            em = soup.new_tag("em")
            em.string = alt
            para.append(soup.new_tag("br"))
            para.append(em)
        visual.replace_with(para)


def lesson_to_md(soup, section, images):
    root = section.find("main") or section
    swap_visuals(soup, root, images)
    for sel in DROP:
        for tag in root.select(sel):
            tag.decompose()
    text = md(str(root), heading_style="ATX", bullets="-")
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def main():
    soup = BeautifulSoup(SRC.read_text(encoding="utf-8"), "html.parser")
    pages = soup.select("section.site-page")
    titles = {n["id"]: n["title"] for n in json.loads(soup.find(id="navigation-data").string)}
    blurbs = {
        a.find(["h3", "h2", "a"]).get_text(strip=True).lower(): a.find("p").get_text(strip=True)
        for a in soup.select("#course .modules article")
        if a.find("p")
    }
    manifest_path = OUT / "img" / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    OUT.mkdir(parents=True, exist_ok=True)

    index = [NOTICE + "# AI-Native SDLC from the trenches — Dojo\n"]
    site = []
    for prefix, filename, title in MODULES:
        lessons = [p for p in pages if p["id"].split("-")[0] == prefix]
        parts = []
        entry = {
            "id": prefix,
            "title": title.split(" · ")[-1],
            "number": title.split(" · ")[0].replace("Module ", "") if "·" in title else "",
            "blurb": blurbs.get(prefix, ""),
            "lessons": [],
        }
        for p in lessons:
            text = lesson_to_md(soup, p, manifest.get(p["id"], []))
            parts.append(text)
            body = re.sub(r"^## .*\n+", "", text, count=1)  # the reader shows its own title
            entry["lessons"].append({
                "id": p["id"],
                "title": titles.get(p["id"], "Introduction"),
                "html": markdown.markdown(body.replace("](img/", "](dojo/img/"), extensions=["tables"]),
            })
        site.append(entry)
        path = OUT / f"{filename}.md"
        path.write_text(f"{NOTICE}# {title}\n\n" + "\n\n---\n\n".join(parts) + "\n", encoding="utf-8")
        index.append(f"- [{title}]({path.name}) ({len(lessons)} lessons)")
        print(f"Wrote {path} ({len(lessons)} lessons)")

    (OUT / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    (OUT / "lessons.json").write_text(json.dumps(site, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Wrote {OUT / 'lessons.json'}")


if __name__ == "__main__":
    main()
