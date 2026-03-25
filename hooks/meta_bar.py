"""
Fügt nach dem ersten <h1> eine Metadaten-Zeile ein (Datum, Autor, Wörter).
"""
import re


def on_page_content(html, page, **kwargs):
    meta = page.meta or {}
    date = meta.get('date', '')
    author = meta.get('author', '')

    md_text = page.markdown or ''
    md_text = re.sub(r'^---[\s\S]*?---\s*', '', md_text)
    md_text = re.sub(r'```[\s\S]*?```', '', md_text)
    md_text = re.sub(r'`[^`]+`', '', md_text)
    md_text = re.sub(r'[#*_\[\]()!>|~`]', ' ', md_text)
    words = len(md_text.split())

    parts = []
    if date:
        parts.append(f'<span class="nh-hero-meta-item">📅 {date}</span>')
    if author:
        parts.append(f'<span class="nh-hero-meta-item">✍ {author}</span>')
    parts.append(f'<span class="nh-hero-meta-item">📖 {words} Wörter</span>')

    bar = f'<div class="nh-doc-meta">{"".join(parts)}</div>'

    return bar + html
