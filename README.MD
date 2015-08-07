# Twitterbot-Workshop 9. August 2015
## Was ist ein Twitterbot?
- Ein Programm, das automatisiert kurze Texte generiert und auf Twitter postet.
- Ein Twitterbot läuft idealerweise auf einem eigenen Twitteraccount.
- Der Phantasie sind keine Grenzen gesetzt!
- Mögliche Ansätze:
    - Bot, der Witze erzählt
    - Bot, der mit Emojis/Unicodezeichen "Bilder" oder ASCII-Art generiert
    - interaktiver Bot
    - Bot, der interessante Links postet
    - Bot, der Geschichten erzählt

## Twitterbot-Beispiele
- [Meine Lieblingsbots von anderen Autoren](https://twitter.com/ojahnn/lists/my-favourite-bots)
- [Meine fertigen Bots](https://twitter.com/ojahnn/lists/my-bots)
- [BotAlly](https://twitter.com/botALLY)

## Technische Anleitung
Um einen Twitterbot in Python zu erstellen, kann man das Modul [`tweepy`](http://tweepy.readthedocs.org/en/v3.2.0/) verwenden. Ihr könnt es mit `pip install tweepy` installieren.

Achtung: Wenn der Bot zum Schluss dauerhaft laufen und jede Stunde einen Tweet posten soll, muss man darauf achten, welche Pythonversion auf dem Server installiert ist. Auf meinem Webspace läuft momentan nur Python 2, der Server wird aber gerade umgestellt. Eure fertigen Bots können auch gerne von meinem Server aus laufen, dann müsst ihr von Anfang an in Python 2 arbeiten (oder euch gedulden, bis auch Python 3 darauf läuft, in wenigen Wochen). 

Um Bots auf einem Server laufen zu lassen, zu dem ihr ftp-Zugriff habt, legt ihr die Pythondatei(en) in einem Ordner ab und ergänzt eine php-Datei, die die Python-Datei aufruft. Für das Starten des php-Skripts kann man einen cronjob einrichten. (Dafür braucht man Admin-Rechte auf dem Server.)

Der Aufbau meiner Twitterbots ist fast immer folgendermaßen:
- Funktion, die für das Einloggen auf Twitter sorgt
- Funktion, die den Output (auf irgendeine Weise) zusammenbastelt
- Funktion, die einen Tweet abschickt
- Außerhalb der Funktionsdefinitionen ein einziger Aufruf als Einstieg in das Programm.
- Das Abfangen bzw. Vermeiden von Fehlern ist hier besonders wichtig, weil man schlecht intervenieren kann, wenn es Probleme gibt und das Programm nicht lokal läuft, sondern auf einem Server.

### OAuth
Um auf Twitter posten zu können, braucht euer Bot Zugangsdaten. Dafür genügen nicht Username und Passwort, sondern man muss OAuth2-Token generieren und sie zur Authentifizierung verwenden. Der Ablauf dafür sieht so aus:
- Einen normalen Account auf Twitter erstellen. Ihr braucht dafür eine Mailadresse, die noch mit keinem Twitteraccount assoziiert ist. Ein guter Trick dafür ist es, gmail-Adressen zu verwenden und darin an verschiedenen Stellen Punkte einzufügen - die Mails kommen im gleichen Postfach an, aber Twitter denkt, es wären verschiedene Adressen.
- Ihr müsst beim Registrieren eine Handynummer angeben. Sie wird benötigt, wenn wir die OAuth-Daten erzeugen wollen. Man kann danach die Handynummer wieder aus dem Account entfernen. (Eine Handynummer kann immer nur mit einem Account assoziiert sein.)
- Den Namen des Accounts kann man im Nachhinein ändern.
- Wenn der Account erstellt wurde, gehe auf [https://apps.twitter.com/](https://apps.twitter.com/). Diese Seite ermöglicht den Zugriff auf Twitter über Apps. Unsere Twitterbots sind Apps. Klicke auf Create New App und befolge die Anweisungen.
- Sobald die App erstellt wurde, können wir im Tab "Keys and Access Tokens" die OAuth-Zugangsdaten abrufen beziehungsweise erzeugen. Der Bot braucht vier Informationen: _Consumer Key_, _Consumer Secret_, _Access Token_, _Access Token Secret_.

### Hallo Welt!
Wenn ihr die Zugangsdaten bekommen habt, könnt ihr die Handynummer aus dem Account entfernen und anfangen zu programmieren. Ihr könnt in der Dokumentation zu `tweepy` oder im Code von einem meiner Bots nachsehen, wie die `tweepy`-Methoden verwendet werden. Mit dem Code aus meinem Beispiel könnt ihr einen ersten **Hallo Welt!**-Tweet absenden.

### Spielregeln
Bevor es weitergeht, gibt es ein paar Twitterbot-Spielregeln, die uns dabei helfen, nicht unnötig menschliche Twitternutzer zu verärgern. Einen [guten Text dazu](http://tinysubversions.com/2013/03/basic-twitter-bot-etiquette/) hat Darius Kazemi geschrieben, mein großes Twitterbot-Vorbild. Besonders wichtig:
- Nicht massenhaft fremde Tweets retweeten, favorisieren oder auf fremde Tweets antworten.
- Nicht massenhaft anderen Nutzern folgen.
- Vorsicht im Umgang mit existierenden Hashtags, nicht massenhaft einzelne Tags verwenden.
- Allgemein: Immer eine Verzögerung einbauen, die vermeidet, dass der Bot Twitter mit Posts bombardiert.

Wenn ihr eine oder mehrere Regeln missachtet, ist die Gefahr groß, dass der Account des Bots direkt von Twitter gebannt wird.

## Inhalt! Inhalt!
**Hallo Welt** ist natürlich erst der Anfang. Die nächste Aufgabe ist die, sich zu überlegen, was der Bot posten soll. Ihr könnt euch von den Beispielen oben inspirieren lassen oder versuchen, einen der Bots vom Englischen ins Deutsche zu übertragen. Ich habe auch noch eine To-Bot-Liste, die vielleicht als Inspiration dienen kann:
- Bot, der zufällige (englische) Hexameter generiert - am besten mit passender Part-of-Speech-Struktur.
- Bot, der Portmanteaus generiert, nach dem Muster _Randgruppenbild_ oder _Nebennierentisch_.
- Bot, der Wortbildungen mit "-splain" erzeugt, wie _mansplain_, _pilotsplain_ oder _frenchsplain_.
- Bot, der Wortbildungen mit "-athon" erzeugt, wie _hackathon_, _thinkathon_ oder _sleepathon_.
- Bot, der auf Twitter nach Tweets sucht, die mit nur einer Hand getippt werden können (nur Zeichen von der linken/rechten Tastaturseite).
- Bot, der berühmte Zitate falsch zuordnet.
- Bot, der berühmte oder einfach zu erkennende deutsche Sätze nimmt und durch eine anderssprachige Rechtschreibkorrektur schickt. Kann man am Output erkennen, welcher Satz ursprünglich gemeint war?
- Bot, der Wortspiele macht, die aus existierenden Witzen zusammengebastelt sind und dadurch nicht funktionieren. Datenbasis: [Pun of the Day](http://www.punoftheday.com/)
- Bot, der alle Tweets sucht, die mit "Actually, ..." beginnen, und sie retweetet (bzw den Text kopiert und ohne Accountname des ursprünglichen Users postet).
- Bot nach dem Vorbild des [Sprichwortrekombinators](http://sprichwortrekombinator.de/).

## Data is beautiful
Bots haben leider kein Gehirn und kein Weltwissen. Mit der richtigen Datenbasis können wir aber so tun, als ob. Es gibt viele Ressourcen, die für unterschiedliche Aufgaben geeignet sind und die vielleicht auch als Inspiration für eure Bots dienen können. Einige davon habe ich in meiner Präsentation ["Aspekte der Natural Language Generation"](http://de.slideshare.net/EstherSeyffarth/nlg-workshop) (ab Folie 22) verlinkt.

Je nach Art des Bots kann es sinnvoll sein, die Daten entweder direkt zur Laufzeit abzurufen oder sie vorzubereiten und dann zur Laufzeit nur noch aus einer Textdatei o.ä. zu lesen. Das Vorbereiten führt zu dem Problem, das [mein erster Twitterbot](https://twitter.com/parsextoto) seit einigen Monaten hat, dass irgendwann die interessanten Daten einfach alle sind. Das Abrufen zur Laufzeit kann zu dem Problem führen, dass ggf. die Ressource nicht immer verfügbar ist oder die Daten eine unerwartete Form annehmen. Welche Variante ihr wählt, ist euch überlassen.

Wenn ihr die Daten aus einer Webseite abruft, könnt ihr mit dem Pythonmodul `urllib2` (Python 2.x) oder `Requests` (Python 3.x) arbeiten. Falls ihr eine REST-API verwendet, empfehle ich:
- für json-Output `json` oder `simplejson`
- für html- oder xml-Output `xml.etree.ElementTree`

Wenn ihr meine [Datenbank deutscher Adjektive, Verben und Nomen mit morphologischen Annotationen](https://github.com/noeddl/parsextoto/blob/master/parsextoto.sqlite) verwenden wollt, braucht ihr das Modul `sqlite3`.

## Ergebnisse
Ich werde alle eure Bots in einer Twitterliste zusammenfassen, die dann alle lesen können. Außerdem fände ich es schön, wenn ihr mir euren Code zur Verfügung stellt, damit ich die fertigen Programme in GitHub hochladen kann. Ich gebe natürlich an, dass die Arbeit nicht von mir, sondern von euch stammt. Wenn ihr selbst einen GitHub-Account habt, könnt ihr auch einen Pull Request stellen.
Wenn ihr am Ende des Workshops noch keine zufriedenstellenden Ergebnisse erreicht habt, könnt ihr euch ja später nochmal bei mir melden, wenn ihr fertig seid.