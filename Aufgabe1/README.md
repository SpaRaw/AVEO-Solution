# AVEO-Solution-Bewerbung
## IP4 zu Geolocation

### Aufgabe
Erstelle eine eigenständige und einfache Webanwendung/Web-API, die die Längen- und
Breitengrade (Longitude/Latitude) für eine bestimmte IP4-Adresse ausgeben kann. Du kannst dir die
UI als eine einzelne Textzeile vorstellen, die beim Abschicken die Geolocation der Eingabe ermittelt
und die Ergebnisse zurückgibt.

### app.py
Hierbei Handelt es sich um die Ausführbare Datei. Es wird Python in der Version 3.10 Verwendet. Dabei wird mittels dem Framwork Flask ein Webserver gestartet.
Ebenso werden die Zulässigen URL definiert. Diese sind:
<ul> 
<li>/ : Landing Page mit der Testdokumentation 
<li>/WebApp 
<li>/API 
</ul>


### DataHandler.py
Hier ist die Klasse DataHandler deklariert. Diese kümmert sich um die Auswertung der Ip Adressen

### Data/ip.db
Die Daten wurden zunächst auf https://dev.maxmind.com/geoip/geolite2-free-geolocation-data heruntergeladen. Es werden die Daten der City CSV benutzt.
Um den Zugriff zu Beschleunigen wurden die Daten in ein SqlLite Datenbank geshrieben