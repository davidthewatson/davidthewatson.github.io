#!/usr/bin/env python3
# build.py
import os
from pathlib import Path

import markdown

from staticjinja import Site

markdowner = markdown.Markdown(output_format="html5")


def resume_context(template):
    markdown_content = Path(template.filename).read_text()
    return {"post_content_html": markdowner.convert(markdown_content)}

def render_resume(site, template, **kwargs):
    # i.e. posts/post1.md -> build/posts/post1.html
    out = site.outpath / Path(template.name).with_suffix(".html")

    # Compile and stream the result
    os.makedirs(out.parent, exist_ok=True)
    site.get_template("_resume_base.html").stream(**kwargs).dump(str(out), encoding="utf-8")

print('rendering resume')

resume = Site.make_site(
    searchpath="resume",
    outpath="docs/resume",
    contexts=[(r".*\.md", resume_context)],
    rules=[(r".*\.md", render_resume)],
)

resume.render()