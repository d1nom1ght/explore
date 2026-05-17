# Auftrag: WordPress-Seite bonsbalance.de komplett ausbauen

Brief für die Ausführung durch einen agentischen Workflow (Cowork o.ä.) auf
der bestehenden WordPress-Installation `bonsbalance.de`.

## 0. Vor dem Start

- **Backup** anlegen via UpdraftPlus (oder vorhandenes Backup-Plugin). Erst nach erfolgreichem Backup weitermachen.
- Prüfen, ob folgende Plugins installiert/aktiv sind, sonst installieren:
  - **Yoast SEO** oder **RankMath** (SEO)
  - **Contact Form 7** oder **WPForms Lite** (Kontaktformular)
  - **Complianz** oder **Borlabs Cookie** (Cookie-Banner + Datenschutzgenerator)
  - **UpdraftPlus** (Backups)

## 1. Login

- URL: `bonsbalance.de/wp-admin`
- Zugangsdaten: _vom Auftraggeber einfügen_

## 2. Theme

- **Kadence Theme** mit **Yoga Starter Template** ist installiert — darauf aufbauen, nicht neu importieren.

## 3. Farben (Kadence → Customizer → Farben)

- **Primär:** `#1B2A4A` (Dunkelblau)
- **Hintergrund:** `#F9F5EF` (Cremeweiß)
- **Akzent:** `#C9A84C` (Gold)
- **Textfarbe:** dunkles Grau `#2C2C2C` (nicht reines Schwarz)

## 4. Typografie

- Headings: serifenlos, ruhig (z.B. **Inter** oder **Lato**)
- Body: gleiche Familie, normales Gewicht, Zeilenhöhe 1.6

## 5. Navigation (Hauptmenü)

Reihenfolge: **Start | Über mich | Leistungen | Preise | Kontakt**
Footer-Menü: **Impressum | Datenschutz**

## 6. Startseite

**Hero-Headline:** „Dein Weg zu innerer Balance"
**Unterzeile:** „Hypnosetherapeut in Castrop-Rauxel. Ich begleite dich auf dem Weg zu mehr Wohlbefinden, Klarheit und innerer Stärke."
**Primärer CTA-Button:** „Kostenloses Erstgespräch vereinbaren" → verlinkt auf `/kontakt`

**Sektionen darunter:**

1. Kurzvorstellung (2–3 Sätze + Foto)
2. Leistungen-Teaser (3–4 Karten mit Icons)
3. Ablauf / „So arbeite ich" (3 Schritte: Erstgespräch → Sitzung → Integration)
4. Zweiter CTA-Block „Lass uns sprechen"

## 7. Über mich

> Mein Name ist Bastian Bons. Als **Hypnosetherapeut in Ausbildung zum Heilpraktiker (sektoral, Psychotherapie)** verbinde ich wissenschaftlich fundierte Methoden mit einem tiefen Verständnis für den Menschen als Ganzes. Hypnose ist kein Zaubertrick, sondern ein bewährtes therapeutisches Werkzeug, das dir helfen kann, festgefahrene Muster zu lösen und neue Wege zu gehen. Ich freue mich darauf, dich auf deinem Weg zu begleiten.

> ⚠️ **Wichtig:** Die Berufsbezeichnung „Heilpraktiker" darf erst nach bestandener Überprüfung beim Gesundheitsamt geführt werden. Bitte exakt diese Formulierung verwenden, NICHT „angehender Heilpraktiker" auf der Live-Seite.

## 8. Leistungen

Einzelne Karten/Abschnitte für:

- **Hypnosetherapie** (Begleitung bei Stress, Schlafproblemen, belastenden Gewohnheiten)
- **Raucherentwöhnung**
- **Stressmanagement**
- **Persönlichkeitsentwicklung**
- **Kostenloses Erstgespräch**

> ⚠️ **HWG-Compliance:** Keine Heilversprechen. Statt „heilt Ängste" → „Begleitung bei belastenden Gefühlen". Keine Vorher/Nachher-Bilder, keine Erfolgsgarantien, keine Testimonials zu konkreten Krankheitsbildern.

## 9. Preise

- Erstgespräch: **kostenlos** (30 Min.)
- Einzelsitzung: **90 €** (60 Min.)
- Hypnosesitzung: **120 €** (90 Min.)
- 5er-Paket: **400 €**

Hinweis darunter: „Preise inkl. gesetzl. MwSt. Zahlung per Überweisung oder bar nach der Sitzung."

## 10. Kontakt

**Inhalte:**

- E-Mail: `info@bonsbalance.de`
- Telefon: _wird noch ergänzt — Platzhalter „Auf Anfrage"_
- Öffnungszeiten: Mo–Fr 9:00–18:00 Uhr / Sa 10:00–14:00 Uhr
- Adresse: Castrop-Rauxel _(genaue Adresse vom Auftraggeber)_

**Kontaktformular** (Contact Form 7 / WPForms):

- Felder: Name\*, E-Mail\*, Telefon, Nachricht\*, Datenschutz-Checkbox\*
- Checkbox-Text: „Ich habe die [Datenschutzerklärung](/datenschutz) gelesen und stimme zu."
- E-Mail-Empfänger: `info@bonsbalance.de`

## 11. Impressum (Pflichtseite nach §5 TMG)

Anlegen unter `/impressum`. Inhalte:

- Vollständiger Name, Adresse
- Telefon, E-Mail
- Berufsbezeichnung (siehe oben)
- Zuständige Aufsichtsbehörde: Gesundheitsamt Kreis Recklinghausen
- Berufsrechtliche Regelungen: HeilprG, ggf. Verweis auf Berufsverband
- Berufshaftpflichtversicherung: Name + Geltungsbereich
- USt-IdNr. (falls vorhanden) oder Hinweis Kleinunternehmer §19 UStG
- Haftungsausschluss + Urheberrechtshinweis

Vorlage: Impressum-Generator von [e-recht24.de](https://www.e-recht24.de) nutzen, Daten manuell prüfen.

## 12. Datenschutzerklärung (Pflicht nach DSGVO)

Anlegen unter `/datenschutz`. Generieren via **Complianz** oder e-recht24.de. Muss abdecken:

- Verantwortlicher
- Hosting-Provider (Webhoster nennen)
- Kontaktformular (Speicherung, Zweck)
- Server-Logs
- Cookies (falls verwendet)
- Rechte der Betroffenen (Auskunft, Löschung, Widerspruch)
- Besondere Sensibilität bei Gesundheitsdaten erwähnen

## 13. Cookie-Banner

Mit **Complianz** konfigurieren. Nur essentielle Cookies vorauswählen, alle anderen (Analytics etc.) opt-in.

## 14. Footer

- Spalte 1: Kurzinfo + Logo
- Spalte 2: Quick-Links (Leistungen, Preise, Kontakt)
- Spalte 3: Kontakt + Öffnungszeiten
- Untere Leiste: © 2026 Bons Balance | Impressum | Datenschutz

## 15. Bilder

- Quelle: **unsplash.com** (Lizenz-Doku: für kommerzielle Nutzung frei, kein Credit-Pflicht, aber URL der Quelle in einer privaten Notiz mitführen)
- Suchbegriffe: `meditation`, `therapy`, `wellness`, `calm`, `nature`
- **Bildgrößen:**
  - Hero: 1920×1080 (max. 300 KB nach Kompression)
  - Sektion/Karte: 800×600
  - Über-mich-Porträt-Platzhalter: 600×800 (Hochformat)
- **Alt-Texte für jedes Bild** (Pflicht): beschreibend, deutsch, z.B. „Person meditiert ruhig im Sonnenlicht"
- Kompression vorher via [tinypng.com](https://tinypng.com) oder Smush-Plugin

## 16. SEO (Yoast / RankMath)

Pro Seite setzen:

- **SEO-Title** (max. 60 Zeichen, Hauptkeyword vorn)
- **Meta-Description** (max. 155 Zeichen, Handlungsaufforderung)
- **H1** nur 1× pro Seite (= Seitentitel)
- Beispiel Startseite:
  - Title: „Hypnosetherapie Castrop-Rauxel | Bons Balance"
  - Description: „Hypnosetherapie & Stressmanagement in Castrop-Rauxel. Kostenloses Erstgespräch vereinbaren. Begleitung bei Ängsten, Schlaf und Gewohnheiten."

## 17. Abnahme-Checkliste (am Ende durchgehen)

- [ ] Alle Seiten in beiden Menüs erreichbar
- [ ] Jede Seite auf Desktop UND Mobile geprüft
- [ ] Kontaktformular sendet Test-Mail erfolgreich
- [ ] Cookie-Banner erscheint beim ersten Aufruf
- [ ] Impressum & Datenschutz vollständig und verlinkt
- [ ] Keine Heilversprechen / HWG-Wording überall sauber
- [ ] Alle Bilder mit Alt-Texten
- [ ] Seitenladezeit unter 3 s (Test: pagespeed.web.dev)
- [ ] Favicon gesetzt
- [ ] SEO-Titles + Descriptions auf allen Seiten
- [ ] Backup nach Fertigstellung anlegen

## 18. Reporting

Nach Abschluss: kurzer Bericht mit

- Liste aller angelegten/geänderten Seiten + URLs
- Offene Punkte (z.B. Telefonnummer fehlt, Adresse fehlt)
- Screenshot-Links der Hauptseiten
