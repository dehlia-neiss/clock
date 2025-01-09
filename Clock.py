#import moduls
from datetime import datetime, timedelta

#user input
while True:
    try:
        user_input = input("Entrez l'heure actuelle dans le bon format (format : YYYY-MM-DD HH:MM:SS) : ")
        current_time = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
        break 
    except ValueError:
        print("Entrez le bon format avec les tirets et les 2 points...")

#Validation de la saisie
print("Vous avez entrez", current_time)

#start clock
import time
while True:
    print("\rhorloge :", current_time.strftime("%Y-%m-%d %H:%M:%S"), end="")
    current_time += timedelta(seconds=1)
    time.sleep(1)






