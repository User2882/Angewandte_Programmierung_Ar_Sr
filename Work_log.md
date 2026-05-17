# Work Log

**Student Name:** ARASH SARKHAB

Dieses Worklog fasst meine Learnings, Herausforderungen sowie die dazugehörigen Lösungen von Tag 1 bis Tag 7 übersichtlich zusammen.

## Template:

---

## 1. ✅ What did I accomplish?

_Reflect on the activities, exercises, and work you completed today._

**Guiding questions:**
- What topics or concepts did you work with?
- What exercises or projects did you complete?
- What tools or technologies did you use?
- What did you learn or practice?



---

## 2. 🚧 What challenges did I face?

_Describe any difficulties, obstacles, or confusing moments you encountered._

**Guiding questions:**
- What was difficult to understand?
- Where did you get stuck?
- What errors or problems did you face?
- What felt frustrating or confusing?




---

## 3. 💡 How did I overcome them?

_Explain how you overcame the challenges or what help you needed._

**Guiding questions:**
- What strategies did you try?
- Who or what helped you (instructor, classmates, documentation)?
- What did you learn from solving the problem?
- What questions do you still have?


---

## Week 1

### Day 1

#### 1. ✅ What did I accomplish?

Als erstes habe ich meine Arbeitsumgebung vorbereitet und mich mit den grundlegenden Konzepten von APIs sowie dem Framework FastAPI beschäftigt. Dafür installierte ich zunächst Git, Visual Studio Code und den Paketmanager uv. Anschließend legte ich mein erstes Projekt mit FastAPI an.
Im praktischen Teil entwickelte ich eine einfache Anwendung und richtete drei GET-Endpunkte ein: /, /status und /about. Diese testete ich mithilfe der automatisch erzeugten Dokumentation unter /docs. Dadurch bekam ich ein besseres Verständnis dafür, wie FastAPI aufgebaut ist und wie Daten im JSON-Format über eine API bereitgestellt werden.

---

#### 2. 🚧 What challenges did I face?

Zu Beginn hatte ich Schwierigkeiten mit der Einrichtung und dem Starten der API. Einige Terminal‑Befehle wurden nicht erkannt, außerdem kam es zu Fehlern durch falsche Verzeichnisse und einen nicht passenden Dateinamen der Python‑Datei. Zusätzlich musste ich aufgrund meiner gesundheitlichen Situation den gesamten Lernstoff selbstständig von zu Hause aus anhand von Präsentationen erarbeiten. Wenn Inhalte unklar waren, habe ich ergänzend auf YouTube, Stack Overflow und KI‑basierte Hilfsmittel zurückgegriffen. Eine besondere Herausforderung bestand darin, dass diese Quellen häufig unterschiedliche Lösungsansätze für dasselbe Problem lieferten, was sehr zeitaufwendig war. Gleichzeitig führte dies dazu, dass ich mehrere Lösungswege für ein einzelnes Problem kennenlernte. Ein konkretes Beispiel hierfür war der Fehler „error: Failed to spawn: fastapi“, für den es in den verschiedenen Quellen keine einheitliche Lösung gab, sondern mehrere alternative Vorgehensweisen.

---

#### 3. 💡 How did I overcome them?

Ich habe die Probleme gelöst, indem ich konkrete, überprüfbare Schritte umgesetzt habe. Zunächst habe ich mein Projekt in ein beschreibbares Verzeichnis verschoben und die Projektstruktur korrekt eingerichtet. Anschließend habe ich fehlende Abhängigkeiten mit uv installiert und den Startbefehl an den tatsächlichen Dateinamen angepasst.
Bei widersprüchlichen Lösungsansätzen aus verschiedenen Quellen habe ich jeweils nur eine Änderung gleichzeitig vorgenommen und das Ergebnis direkt getestet. Dadurch konnte ich gezielt feststellen, welche Maßnahme das Problem behebt. So habe ich den Fehler „error: Failed to spawn: fastapi“ letztlich durch die korrekte Installation von FastAPI und den Wechsel auf den passenden Startbefehl mit uvicorn behoben.

---

### Day 2

#### 1. ✅ What did I accomplish?

FÜr diesen Abschnitt habe ich eine Note‑Taking‑API mit FastAPI umgesetzt und meine Python‑Grundlagen angewendet. Ich habe GET‑ und POST‑Endpoints erstellt, mit Pydantic Datenmodelle definiert und JSON als Datenaustauschformat genutzt. Zusätzlich habe ich File‑Persistenz implementiert, sodass Notizen in einer JSON‑Datei gespeichert und nach einem Neustart weiterhin verfügbar sind. Die API habe ich über /docs und /redoc getestet.

---

#### 2. 🚧 What challenges did I face?

Während der Umsetzung traten mehrere Fehler auf, darunter 500 Internal Server Error und 422 Unprocessable Entity. Probleme entstanden unter anderem durch Änderungen am Datenmodell, alte gespeicherte Daten ohne neue Felder sowie durch Routing‑Konflikte zwischen allgemeinen und spezifischen Endpoints. Zudem war es zeitlich herausfordernd, alle Aufgaben im vorgegebenen Zeitrahmen zu bearbeiten.

---

#### 3. 💡 How did I overcome them?

Ich habe die Fehler gelöst, indem ich Fehlermeldungen analysiert, Requests gezielt über /docs getestet und die Reihenfolge der Endpoints angepasst habe. Bei Modelländerungen habe ich gespeicherte Daten bereinigt oder neu erstellt. Durch strukturiertes Vorgehen, besseres Zeitmanagement und regelmäßiges Speichern der Dateien konnte ich die API erfolgreich fertigstellen.

---

### Day 3

#### 1. ✅ What did I accomplish?

Ich habe meine Note-Taking-API schrittweise erweitert und dabei die zentralen Konzepte von REST-APIs praktisch vertieft. Dazu implementierte ich die vollständige CRUD-Funktionalität und ergänzte die Anwendung um zusätzliche Endpoints für das Erstellen, Auslesen, Aktualisieren und Löschen von Notizen. Auf diese Weise konnte ich den Einsatz von GET-, POST-, PUT-, PATCH- und DELETE-Requests nachvollziehen und ein besseres Verständnis für ihre jeweilige Funktion entwickeln.
Ein Schwerpunkt lag auf der Erweiterung von GET‑Endpunkten durch Query‑Parameter. Ich habe Filter für Kategorie, Suchbegriffe, Tags sowie einen Datumsbereich implementiert und gelernt, wie mehrere Filter gleichzeitig kombiniert werden können. Zusätzlich habe ich Statistik‑Endpunkte erstellt, um aggregierte Informationen wie die Anzahl von Notizen pro Kategorie und häufig genutzte Tags bereitzustellen.
Darüber hinaus habe ich Resource‑Beziehungen umgesetzt, indem separate Endpoints für Tags und Kategorien eingeführt wurden. Dadurch konnte ich besser verstehen, wie REST‑konforme URL‑Strukturen aufgebaut sind und wie zusammengehörige Ressourcen logisch miteinander verknüpft werden.

---

#### 2. 🚧 What challenges did I face?

Während der Umsetzung kam es zu mehreren Problemen, insbesondere durch das parallele Arbeiten an verschiedenen Aufgaben. Die größte Herausforderung war die klare Trennung zwischen dateibasierter Persistenz (JSON) und der später eingeführten Datenbank‑Migration. Dabei wurde deutlich, wie wichtig eine saubere Struktur und schrittweises Vorgehen sind, um bestehende Funktionalitäten nicht zu beschädigen.

---

#### 3. 💡 How did I overcome them?

Ich habe gelernt, dass komplexere Erweiterungen wie Datenbank‑Migrationen einen grundlegenden Architekturwechsel darstellen und deshalb getrennt von funktionalen Erweiterungen umgesetzt werden sollten. Außerdem habe ich mein Verständnis für REST‑Design, Filterlogik und strukturierte Fehlerbehandlung vertieft. Insgesamt habe ich gelernt, systematischer vorzugehen und Änderungen schrittweise zu testen.

---

## Week 2

### Day 4

#### 1. ✅ What did I accomplish?

Ich habe mich mit dem Erstellen von POST‑Endpunkten und dem Testen von APIs beschäftigt. Ich habe gelernt, wie neue Daten über einen POST‑Request an eine API gesendet werden und wie Pydantic‑Modelle zur Validierung von Eingaben genutzt werden. Außerdem habe ich nachvollzogen, wie Daten über JSON‑Dateien gespeichert und wieder geladen werden können.
Der Schwerpunkt der Hausarbeit lag auf dem Schreiben von Tests mit pytest. Dafür habe ich eine Testsuite (test_notes.py) für die bestehende Notes‑API aus Tag 2 und Tag 3 erstellt. Die Tests decken CRUD‑Operationen, Filterfunktionen, Fehlerfälle sowie zusätzliche Endpunkte wie Statistik‑ und Kategorie‑Routen ab. Die Tests wurden mit der requests‑Bibliothek umgesetzt und folgen dem Arrange‑Act‑Assert‑Prinzip.

---

#### 2. 🚧 What challenges did I face?

Während der Arbeit war es zunächst schwierig, den Überblick zwischen verschiedenen APIs (Notes und Courses) zu behalten. Besonders wichtig war es, darauf zu achten, dass die Tests gegen den richtigen Server ausgeführt werden. Außerdem musste klar unterschieden werden, welche Aufgaben Lerninhalt waren und welche tatsächlich abgegeben werden sollten.

---

#### 3. 💡 How did I overcome them?

Ich habe gelernt, dass Tests ein zentrales Werkzeug sind, um die Funktionalität einer API systematisch zu überprüfen. Durch das Schreiben der Tests wurde deutlich, dass für die Bewertung nicht die Testergebnisse selbst, sondern die Struktur und Vollständigkeit der Testfälle entscheidend sind.

---

### Day 5

#### 1. ✅ What did I accomplish?

Die bestehende Notes-API wurde mithilfe von Pydantic weiter abgesichert und die Datenvalidierung deutlich strenger gestaltet.Ziel war es, ungültige Eingaben konsequent abzulehnen und gültige Daten zu normalisieren, ohne zusätzliche Logik in den Endpoints zu implementieren. Dafür wurden feste Feld‑Constraints definiert und bestehende Modelle angepasst.
Zusätzlich wurden benutzerdefinierte Validatoren eingesetzt, um Regeln umzusetzen, die über einfache Typ‑ und Längenprüfungen hinausgehen. Dazu zählten unter anderem die Prüfung erlaubter Kategorien, die Bereinigung von Tags sowie eine Cross‑Field‑Regel, bei der Abhängigkeiten zwischen mehreren Feldern berücksichtigt werden. Für PATCH‑Requests wurde ein separates Update‑Modell verwendet, bei dem alle Felder optional sind, die Validierung jedoch weiterhin greift, sobald ein Feld gesetzt wird.
Abschließend wurde mit einer eigenen Testdatei (test_validation.py) überprüft, dass alle Validierungsregeln korrekt funktionieren. Die Tests decken sowohl erfolgreiche Requests als auch erwartete Fehlerfälle (HTTP 422) ab und bestätigen damit die Stabilität der API.

---

#### 2. 🚧 What challenges did I face?

Eine Herausforderung bestand darin, Feld‑Validierung und Modell‑Validierung korrekt voneinander abzugrenzen und die passende Validator‑Art einzusetzen. Außerdem war es notwendig, die Validierungslogik schrittweise aufzubauen, bevor aussagekräftige Tests geschrieben werden konnten.

---

#### 3. 💡 How did I overcome them?

Durch die Arbeit an Tag 5 wurde deutlich, dass saubere Datenvalidierung ein zentraler Bestandteil robuster APIs ist. Pydantic‑Modelle können als verbindlicher Vertrag dienen, der Fehler frühzeitig verhindert und den Code in den Endpoints deutlich vereinfacht. Tests helfen dabei, diese Regeln nachvollziehbar und überprüfbar zu machen.

---

### Day 6

#### 1. ✅ What did I accomplish?

Am Tag 6 wurde mit einer vorgegebenen Referenz‑Test‑Suite gearbeitet, um die bestehende Notes‑API testsicher zu machen. Dazu wurde die Datei test_main.py in das Projekt integriert und mit pytest ausgeführt. Relevante Tests liefen erfolgreich, während optionale Tests (z. B. für nicht implementierte Features) korrekt übersprungen wurden.
Die bestehende main.py wurde als zentrale Referenz verwendet und nur minimal angepasst, um ein konsistentes Verhalten gegenüber der Test‑Suite sicherzustellen. Ziel war es, keine neuen Funktionen zu implementieren, sondern die vorhandene API kompatibel zur Test‑Suite zu halten. Am Ende liefen alle relevanten Tests ohne Fehler oder Fehlschläge durch, womit die Anforderungen für Tag 6 erfüllt waren.

---

#### 2. 🚧 What challenges did I face?

Eine Herausforderung bestand darin, zwischen tatsächlich relevanten Tests und bewusst übersprungenen Tests zu unterscheiden. Zudem war es wichtig zu verstehen, welche main.py von der Test‑Suite importiert wird, um sicherzustellen, dass der richtige Code geprüft wird.

---

#### 3. 💡 How did I overcome them?

Ich habe gelernt, dass automatisierte Tests ein zentrales Werkzeug zur Überprüfung der API‑Stabilität sind und dass „SKIPPED“‑Tests kein Fehler, sondern ein bewusstes Design der Test‑Suite sein können. Außerdem wurde deutlich, wie wichtig eine klare Projektstruktur ist, damit externe Tests zuverlässig mit dem eigenen Code arbeiten können.

---

## Week 3

### Day 7

#### 1. ✅ What did I accomplish?

Ich habe ein einfaches Frontend für die bestehende Notes‑API mit Streamlit umgesetzt. Das Frontend ermöglicht es, alle vorhandenen Notes vom Backend abzurufen, eine Liste der Note‑Titel anzuzeigen und die Details einer ausgewählten Note (Inhalt, Kategorie und Tags) darzustellen. Zusätzlich können neue Notes über ein Formular erstellt werden, die nach dem Absenden direkt in der Liste erscheinen.

---

#### 2. 🚧 What challenges did I face?

Eine Herausforderung war die korrekte Kommunikation zwischen Frontend und Backend, insbesondere die richtige Reihenfolge beim Laden und Verwenden von Daten, um Laufzeitfehler zu vermeiden. Außerdem führte das automatische Neuladen von Streamlit dazu, dass Variablen sauber initialisiert werden mussten. Auch das parallele Arbeiten mit zwei Terminals (Backend und Frontend) erforderte Aufmerksamkeit.

---

#### 3. 💡 How did I overcome them?

Ich habe die Probleme gelöst, indem ich Variablen konsequent initialisiert und den Code klar strukturiert habe, sodass Daten immer erst geladen werden, bevor sie verwendet werden. Durch den Einsatz von Streamlit‑Forms konnte die Eingabe neuer Notes zuverlässig gesteuert werden. Schrittweises Testen der einzelnen Funktionen stellte sicher, dass sowohl das Anzeigen als auch das Erstellen von Notes korrekt funktioniert.

---

### Day 8

#### 1. ✅ What did I accomplish?

Ich habe selbstständig an der Finalisierung des Projekts gearbeitet. Dabei habe ich alle relevanten Dateien aus den vorherigen Tagen strukturiert, bereinigt und übersichtlich organisiert. Anschließend habe ich das vollständige Projekt inklusive Backend, Frontend, Tests und Worklogs in ein GitHub‑Repository hochgeladen.
