import os
from Encounter import One_V_One_Battle
try:
    HP_Bar = One_V_One_Battle.hp
    MHP = One_V_One_Battle.P_max
    HP_Appox = int((HP_Bar/MHP)*100)
except AttributeError:
    print("Whoops!!")
    HP_Appox = 100

def clear():
	os.system("cls")
        
if HP_Appox >= 100:
    Health =  ("||||||||||")
    
elif HP_Appox >= 90:
    Health =  ("|||||||||.")
    if HP_Appox >= 95:
        clear()
        Health =  ("|||||||||-")

elif HP_Appox >= 80:
    Health =  ("||||||||..")
    if HP_Appox >= 85:
        clear()
        Health =  ("||||||||-.")

elif HP_Appox >= 70:
    Health =  ("|||||||...")
    if HP_Appox >= 75:
        clear()
        Health =  ("|||||||-..")

elif HP_Appox >= 60:
    Health =  ("||||||....")
    if HP_Appox >= 65:
        clear()
        Health =  ("||||||-...")

elif HP_Appox >= 50:
    Health =  ("|||||.....")
    if HP_Appox >= 55:
        clear()
        Health =  ("|||||-....")

elif HP_Appox >= 40:
    Health =  ("||||......")
    if HP_Appox >= 45:
        clear()
        Health =  ("||||-.....")

elif HP_Appox >= 30:
    Health =  ("|||.......")
    if HP_Appox >= 35:
        clear()
        Health =  ("|||-......")

elif HP_Appox >= 20:
    Health =  ("||........")
    if HP_Appox >= 25:
        clear()
        Health =  ("||-.......")

elif HP_Appox >= 10:
    Health =  ("|.........")
    if HP_Appox >= 15:
        clear()
        Health = ("|-.......")

elif HP_Appox >= 1:
    Health =  ("-........")
print("Health: " + str(Health))