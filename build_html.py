import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "index.md"
DOCS = ROOT / "docs"
LOGOS = ["comhis_logo.png", "hy_logo.png"]

CSS = """
:root { --ink:#1d2430; --muted:#5b6573; --accent:#1f4e79; --rule:#d8dde6; --tint:#f3f6fa; }
* { box-sizing: border-box; }
body { margin:0; font-family:"Source Sans 3","Source Sans Pro","Segoe UI",Helvetica,Arial,sans-serif;
  font-size:18px; line-height:1.6; color:var(--ink); background:#fff; }
header.site { border-bottom:1px solid var(--rule); background:#fff; }
.wrap { max-width:860px; margin:0 auto; padding:0 24px; }
.logos { display:flex; align-items:center; gap:24px; padding:16px 0; }
.logos img { height:48px; width:auto; }
.logos .sep { flex:1; }
.logos .tag { font-size:14px; color:var(--muted); letter-spacing:.04em; text-transform:uppercase; }
main { padding:32px 0 64px; }
h1 { font-size:2.4em; line-height:1.2; margin:0 0 .3em; color:var(--accent); font-weight:700; }
h2 { font-size:1.6em; margin:2.2em 0 .5em; color:var(--accent); border-bottom:1px solid var(--rule); padding-bottom:.25em; }
h3 { font-size:1.2em; margin:1.8em 0 .4em; color:var(--ink); }
h4 { font-size:1.05em; margin:1.4em 0 .3em; }
p, li { margin:.7em 0; }
a { color:var(--accent); }
em { color:var(--muted); }
blockquote { margin:1.4em 0; padding:14px 18px; background:var(--tint); border-left:4px solid var(--accent); }
blockquote p { margin:.4em 0; }
code { font-family:"JetBrains Mono",Consolas,monospace; font-size:.9em; background:var(--tint); padding:1px 4px; border-radius:3px; }
table { border-collapse:collapse; width:100%; margin:1.2em 0; font-size:.95em; }
th, td { border:1px solid var(--rule); padding:8px 10px; text-align:left; vertical-align:top; }
th { background:var(--tint); font-weight:600; }
img { max-width:100%; height:auto; display:block; margin:1.6em auto; }
hr { border:0; border-top:1px solid var(--rule); margin:2.4em 0; }
.toc { margin:1.6em 0 2em; padding:16px 20px; background:var(--tint); border-radius:6px; font-size:.95em; }
.toc summary { cursor:pointer; font-weight:600; color:var(--accent); }
.toc ul { margin:.5em 0 0; padding-left:1.2em; }
.toc li { margin:.2em 0; }
footer { border-top:1px solid var(--rule); color:var(--muted); font-size:.9em; padding:24px 0 48px; }
@media (max-width:600px) { body { font-size:16px; } h1 { font-size:1.9em; } }
"""


def clean_source(text: str) -> str:
    # The Markdown source escapes punctuation for GitHub-style rendering.
    # Python-Markdown does not need these escapes, and some would show literally.
    return re.sub(r"\\([!-/:-@\[-`{-~])", r"\1", text)


def main() -> None:
    body_md = clean_source(SRC.read_text(encoding="utf-8"))

    md = markdown.Markdown(
        extensions=["tables", "toc", "sane_lists", "attr_list"],
        extension_configs={"toc": {"permalink": False, "toc_depth": "2-3"}},
    )
    html_body = md.convert(body_md)
    toc = md.toc

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>From catalogue records to research data</title>
<meta name="description" content="A repeatable workflow for refining bibliographic metadata, with ESTC publication years and places as worked examples.">
<style>{CSS}</style>
</head>
<body>
<header class="site">
  <div class="wrap logos">
    <img src="comhis_logo.png" alt="COMHIS">
    <span class="sep"></span>
    <span class="tag">DARIAH-Campus learning material · Draft</span>
    <img src="hy_logo.png" alt="Helsingin yliopisto">
  </div>
</header>
<div class="wrap">
<main>
<details class="toc" open>
<summary>Contents</summary>
{toc}
</details>
{html_body}
</main>
<footer>
Draft for discussion and adaptation for DARIAH-Campus. ESTC is used as a case study; field structures and cataloguing practices vary between catalogues.
</footer>
</div>
</body>
</html>
"""

    DOCS.mkdir(exist_ok=True)
    (DOCS / "index.html").write_text(page, encoding="utf-8")
    for logo in LOGOS:
        shutil.copy2(ROOT / logo, DOCS / logo)
    print(f"wrote {DOCS / 'index.html'}")


if __name__ == "__main__":
    main()
