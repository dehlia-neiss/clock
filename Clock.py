import time
from datetime import datetime, timedelta
import pytz

def obtenir_heure_francaise():
    """
    Retourne l'heure actuelle en France.
    """
    fuseau_france = pytz.timezone('Europe/Paris')
    heure_france = datetime.now(fuseau_france)
    return heure_france.hour, heure_france.minute, heure_france.second

def afficher_heure(h):
    """
    Affiche l'heure sous la forme hh:mm:ss.
    """
    print(f"{h[0]:02}:{h[1]:02}:{h[2]:02}", end="\r")

def regler_alarme(alarme):
    """
    Active l'alarme lorsque l'heure actuelle correspond à l'heure réglée.
    """
    print(f"Alarme réglée à {alarme[0]:02}:{alarme[1]:02}:{alarme[2]:02}")
    while True:
        heure_actuelle = obtenir_heure_francaise()
        afficher_heure(heure_actuelle)
        if heure_actuelle == alarme:
            print("\n\u26A1 Alarme déclenchée ! \u26A1")
            break
        time.sleep(1)

# Exemple d'utilisation
if __name__ == "__main__":
    print("Horloge démarrée. Appuyez sur Ctrl+C pour arrêter.")
    alarme = (22, 14, 0)  # Réglage de l'alarme
    regler_alarme(alarme)