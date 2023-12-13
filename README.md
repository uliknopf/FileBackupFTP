# FileBackupFTP
A python script to backup a file on FTP server (german language)
## Beschreibung ##
Wenn man zuhause an verschiedenen Rechnern arbeitet, möchte man gerne die ein oder andere bearbeitete Datei auch später vom anderen Rechner aus anschauen. Viele Router haben einen freien USB Port, an dem ein USB-Stick angeschlossen werden kann. Dieser dient dann als FTP-Server (Einrichtung des USB-Sticks steht im Handbuch des Routers), auf den alle angeschlossenen Geräte zugreifen können. Beim Ausführen des Python-Codes wird vom Anwender eine Datei ausgewählt, die dann in einen Ordner des FTP-Servers kopiert wird, so daß andere Geräte darauf zugreifen können. Sollte Python beim Ausführen ein Modul-Fehler liefern, muß eventuell noch auf der Console die Bibliothek easygui mit pip eingebunden werden: 
`>pip install easygui`
