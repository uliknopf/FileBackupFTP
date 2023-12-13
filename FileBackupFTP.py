#Python Script zum Backup einer Datei auf dem FTP-Server
# eventuell easygui auf der Console einbinden: >pip install easygui 

# Bibliotheken einbinden
from ftplib import FTP 
from datetime import datetime
import easygui
import os

# individuelle Parameter zum Selbereinstellen vorweg:
FTP_Adresse = "192.168.1.1" # Bsp:"o2.box" , "192.168.178.1"
OrtWoGespeichertWird = "/Backup/" # SpeicherOrt muß existieren.
FTP_UserName = "user"  # bei anonymer Anmeldung muß die Funktion login (Zeile 42/43) mit Kommentarzeichen versehen werden.
FTP_Password = "password" 
#------------------------------------------------------------



# Funktion Datei auswählen
def select_file():
    file_path = easygui.fileopenbox(title="Wähle Datei zum Speichern.")
    if file_path:
        return file_path
    else :
        print ("keine Datei ausgewählt, daher Beendigung")
        exit()

def folderExist(folder):
    try:
        ftp.cwd(OrtWoGespeichertWird)
        return True
    except:
        return False

# Datumsobjekt
now = datetime.now();
zeit= now.strftime('%d.%m.%Y')

# Verbindung zum FTP-Server herstellen
ftp = FTP(host=FTP_Adresse)
print(ftp.getwelcome()); # Status anzeigen
ftpResponseMessage=ftp.login(user=FTP_UserName, passwd=FTP_Password)
print(ftpResponseMessage); # Status anzeigen
# mit easygui wird der DateiOrt der zu speichernden Datei ausgewählt.
OrtDerZuSpeicherndenDatei=select_file()
# mit os wird der Name der zu speichernden Datei ermittelt.
filename = os.path.basename(OrtDerZuSpeicherndenDatei)
# Datei die gespeichert wird, wird mit Zeitstempel versehen.
DateiNameDieGespeichertWird=zeit+filename

if folderExist(OrtWoGespeichertWird):
    ftpResponseMessage = ftp.cwd(OrtWoGespeichertWird)
    print(ftpResponseMessage);
    # Backup Datei speichern
    try:
        with open(OrtDerZuSpeicherndenDatei, "rb") as file:
            ftp.storbinary(f'STOR {DateiNameDieGespeichertWird}', file)
        print("Backup Datei gespeichert.")
    except:
        print("Die Datei kann nicht geschrieben werden.")
else :
    print("Der Ordner existiert nicht!")

# Verbindung zum FTP-Server trennen
ftp.quit()
print('Script beendet.')
