# Netzwerktechnik

## OSI-Modell

Das OSI-Modell beschreibt die Kommunikation in 7 Schichten:

| Schicht | Name | Beispiele |
|---------|------|-----------|
| 7 | Anwendung | HTTP, FTP, DNS |
| 6 | Darstellung | SSL/TLS, JPEG |
| 5 | Sitzung | NetBIOS |
| 4 | Transport | TCP, UDP |
| 3 | Vermittlung | IP, ICMP |
| 2 | Sicherung | Ethernet, MAC |
| 1 | Bitübertragung | Kabel, WLAN |

> **Merksatz:** Alle Deutschen Studenten Trinken Verschiedene Sorten Bier

---

## IP-Adressen

### IPv4

- 32 Bit lang, aufgeteilt in 4 Oktette
- Beispiel: `192.168.1.1`
- Private Bereiche:
    - `10.0.0.0/8`
    - `172.16.0.0/12`
    - `192.168.0.0/16`

### Subnetting

```
IP-Adresse:  192.168.1.0
Subnetzmaske: 255.255.255.0  (/24)
Netzadresse:  192.168.1.0
Broadcast:    192.168.1.255
Hosts:        192.168.1.1 - 192.168.1.254  (254 Hosts)
```

!!! tip "Formel für Hostanzahl"
    Anzahl Hosts = 2^(32 - Präfixlänge) - 2

---

## TCP vs. UDP

| Eigenschaft | TCP | UDP |
|-------------|-----|-----|
| Verbindung | Verbindungsorientiert | Verbindungslos |
| Zuverlässigkeit | Ja (Bestätigung) | Nein |
| Geschwindigkeit | Langsamer | Schneller |
| Einsatz | HTTP, SSH, FTP | DNS, VoIP, Streaming |
