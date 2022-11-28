import Art
from time import sleep
import sys,time

gold=0
xp=0
hp=0
attack=0
speed=0

print(Art.start)

TEST = 0.000000000000000000000000000000000001

def start():
    startbutton = input("Välkommen! Tryck Y för att starta spelet, och tryck N för att avsluta det.")
    while True:
        if startbutton == "Y" or "y":
            break
        elif startbutton == "N" or "n":
            raise SystemExit(0)
        else:
            print("Försök igen.")
            continue

def Travel():
    #HÄR GÖRS EN RESA, FUNKTIONEN SKA VÄLJA ETT STÄLLE OCH VÄLJA EN HÄNDELSE I DET STÄLLET,
    #VI MÅSTE RÄKNA HUR MÅNGA RUM MAN HAR VARIT I
    print()

def Fight():
    #HÄR UTFÖR VI STRIDEN, EN FIENDE SOM SKA GE OCH TA SKADA, SKA GE EXPERIENCE OCH GULD EFTER FIGHTEN, 
    
    print("")

def Inventory():
    #FUNKTIONEN ÖPPNAR ENS INVENTORY OCH VISAR ENS STATS, SAMT HUR MÅNGA RUM MAN HAR VARIT I
    ASD


def print_slow(str, timee):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(timee)


