import Art
from time import sleep
import sys,time
import P




TEST = 0.000000000000000000000000000000000001

total_turns = 0

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

    if total_turns == 10:
        print("Bossfight")
    elif total_turns == 20:
        print("Bossfight")
    elif total_turns == 30:
        print("Bossfight")

    #Väljer vilken plats att resa till
    

    print()

def Fight():
    
    

    print("")

def Inventory():
    #FUNKTIONEN ÖPPNAR ENS INVENTORY OCH VISAR ENS STATS, SAMT HUR MÅNGA RUM MAN HAR VARIT I
    ASD


def print_slow(str, timee):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(timee)

def intro():
    print(Art.start)

    print_slow("Välj din spelare!", 0.01)
    sleep(0.5)
    spelare = int(input('''

    1. Cacambo! (Easy)
        HP  :  200
        STR :  
        SPD :
        Gold:  15


    2. Candide! (Medium)
        HP  :  100
        STR :
        SPD :
        Gold:  


    3. Pangloss! (Hard) 
        HP  :  50
        STR :
        SPD :
        Gold:  20
        (syfilis)

    Ditt val --> '''))
    
    if spelare == 1:       
        cacambo = P.Player()
        cacambo.hp = 200
        cacambo.str = 20
        cacambo.spd = 20
    elif spelare == 2:
        candide = P.Player()
        candide.hp = 100
        candide.str = 10
        candide.spd = 15
    elif spelare == 3:
        pangloss = P.Player()
        pangloss.hp = 50
        pangloss.str = 15
        pangloss.spd = 5

intro()