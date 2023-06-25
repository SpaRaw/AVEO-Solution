# AVEO-Solution-Bewerbung
## Vorname zu Geschlecht

### Aufgabe
Erstelle eine eigenständige und einfache Webanwendung/Web-API, die das wahrscheinliche 
Geschlecht für einen bestimmten Vornamen ausgeben kann. Du kannst dir die UI als eine einzelne 
Textzeile vorstellen, die beim Abschicken das Geschlecht (male/female/unknown) der Eingabe 
ermittelt und die Ergebnisse zurückgibt.

### app.py
Hierbei Handelt es sich um die Ausführbare Datei. Es wird Python in der Version 3.10 Verwendet. Dabei wird mittels dem Framwork Flask ein Webserver gestartet.
Ebenso werden die Zulässigen URL definiert. Diese sind:
<ul> 
<li>/ : Landing Page mit der Testdokumentation 
<li>/WebApp 
<li>/API 
</ul>


### DataHandler.py
Hier ist die Klasse DataHandler deklariert. Diese kümmert sich um die Auswertung der Namen
