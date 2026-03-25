## Project Overview

Haikara Wiki is a personal knowledge wiki (German-language) built with MkDocs Material. It collects learning material, vocational school notes (Berufsschule), and general notes. The site has a custom dark theme (teal/blue/orange accent palette).

## Tech Stack

- **Generator:** MkDocs with the Material theme (`mkdocs-material`)
- **Language:** German (`de`)
- **Fonts:** Syne (body), JetBrains Mono (code) — loaded from Google Fonts
- **Theme:** Custom dark theme via `docs/stylesheets/extra.css` (slate scheme, `#0d0f14` background)
- **Markdown extensions:** admonition, pymdownx.details, pymdownx.superfences, pymdownx.highlight (with anchor line numbers), pymdownx.inlinehilite, pymdownx.snippets, attr_list, md_in_html, tables
- **Search:** Built-in MkDocs search plugin, German language

## Commands

- **Dev (Main-PC):** `~/.local/bin/uvx --with mkdocs-material mkdocs serve` → http://127.0.0.1:8000
- **Build:** `~/.local/bin/uvx --with mkdocs-material mkdocs build`
- **Deploy:** Automatisch – Cron-Job auf 24/7-PC baut jede Minute neu

## Architecture

```
mkdocs.yml                  Main config: nav, theme, plugins, extensions
docs/
  index.md                  Landing page
  berufsschule/
    index.md                Section index (Berufsschule)
    netzwerk.md             Networking content: OSI model, IPv4, subnetting, TCP/UDP
  notizen/
    index.md                Section index (general notes, mostly empty)
  stylesheets/
    extra.css               Full custom dark theme overrides for Material
input/
  lf93-statisches-routing.html  Source HTML that inspired the theme design
  Pasted Image.png          Reference image
site/                       Built output (auto-generated, not committed)
```

## Nav Structure (mkdocs.yml)

- Start → `index.md`
- Berufsschule → `berufsschule/index.md`
  - Netzwerktechnik → `berufsschule/netzwerk.md`
- Notizen → `notizen/index.md`

## Deployment (Hosting)

- **Produktiv-URL:** https://wiki.networkhybrid.de
- **24/7-PC:** 10.70.10.10 (Pop!OS), XAMPP Apache
- **Build-Skript:** `/home/networkhybrid/build-wiki.sh`
- **Output:** `/opt/lampp/htdocs/wiki`
- **Cron:** jede Minute (Root-Crontab: `* * * * *`), Log: `/home/networkhybrid/wiki-build.log`
- **Reverse Proxy:** NPM mit Wildcard-SSL *.networkhybrid.de
- **Nextcloud-Pfad auf 24/7-PC:** `/var/lib/docker/volumes/networkhybrid_nextcloud_data/_data/data/admin/files/projects/Haikara-Wiki`

## Input-Ordner Workflow

User legt Dateien in `input/` ab (txt, pdf, html, png...) und sagt Claude was damit gemacht werden soll. Claude liest die Datei und baut daraus eine fertige Wiki-Seite inkl. Nav-Eintrag.

## Gotchas

- MkDocs läuft via `uvx`, nicht als globales Kommando
- Nav in `mkdocs.yml` muss bei neuen Seiten manuell gepflegt werden
- Google Fonts in `extra.css` – offline kein Custom Font
