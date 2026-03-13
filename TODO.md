# Haikara Wiki – Roadmap & Ideen

## In Arbeit / Nächste Schritte

- [ ] Ersten echten Inhalt erstellen (Berufsschul-Notizen aus input/)
- [ ] Editor-Workflow klären: git-basiert oder Web-GUI zum Bearbeiten von Seiten

## Account & Auth

- [x] Authentik auf 24/7-PC deployed
- [x] auth.networkhybrid.de eingerichtet
- [x] OAuth2/PKCE Login-Widget im Wiki-Header
- [x] Avatar, Name, E-Mail, Abmelden funktionieren
- [x] Gruppen angelegt: `wiki-admin`, `wiki-editor`, `wiki-viewer-berufsschule`
- [x] Persönlicher User angelegt (Editor-Rolle)
- [x] Berufsschule-Tab + Startseiten-Link per Gruppen-Check ausgeblendet (JS + Authentik Groups-Claim)
- [ ] Server-seitiger Schutz für /berufsschule/ via NPM + Authentik Forward Auth (aktuell nicht funktionsfähig — embedded Outpost synct Provider-Config nicht zuverlässig bei NPM auf separatem RPi → Authentik auf 24/7-PC; NPM Config wurde geleert um 500-Fehler zu vermeiden)
- [ ] Weiterer Viewer-User zum Testen anlegen (z.B. für wiki-viewer-berufsschule ohne editor)

## Wiki Features

- [x] Custom Dark Theme
- [x] Suche in Tabs-Leiste
- [x] Account-Widget oben rechts
- [x] Berufsschule-Tab + Startseiten-Link client-seitig versteckt (JS)
- [ ] Server-seitiger Schutz /berufsschule/ (direkte URL ohne Login momentan erreichbar)
- [ ] Weitere geschützte Bereiche bei Bedarf
- [ ] Web-GUI zum Erstellen/Bearbeiten von Seiten (ohne Terminal)

## Infrastruktur

- [x] Auto-Rebuild via Cron (jede Minute)
- [x] XAMPP auf 24/7-PC, Reverse Proxy via NPM
- [x] Wildcard-SSL *.networkhybrid.de
- [ ] Zentrale Landing Page (www.networkhybrid.de) mit Service-Übersicht
- [ ] Status-Seite für Services

## Ideen / Langfristig

- [ ] Seitenübergreifendes Account-System (networkhybrid.de SSO)
- [ ] Release Notes / Changelog auf der Landing Page
- [ ] db.networkhybrid.de und weitere Subdomains
