import Art
from time import sleep
import sys,time
import Player_module as P
import Location_storage as L
import Enemy_module as E
import random as rand




TEST = 0.0000000000000000000000000000000000000000001
PUNCTUATION_PAUSE_TIME = 0.4
COMMA_PAUSE_TIME = 0.15

total_turns = 0



def start():
    startbutton = input("Welcome! Press Y to start, or N to quit.")
    while True:
        if startbutton == "Y" or "y":
            break
        elif startbutton == "N" or "n":
            raise SystemExit(0)
        else:
            print("Försök igen.")
            continue



def travel():
    #HÄR GÖRS EN RESA, FUNKTIONEN SKA VÄLJA ETT STÄLLE OCH VÄLJA EN HÄNDELSE I DET STÄLLET,
    #VI MÅSTE RÄKNA HUR MÅNGA RUM MAN HAR VARIT I

    current_location = ""


    print_slow("Would you like to travel, or enter your inventory? \n\n 1. Inventory    2. Travel \n\n", TEST)
    choice = int(input("Choice: "))
     

    if choice == 1:
        Inventory()
    elif choice == 2:
        #travel

        print_slow("Where would you like to travel?", TEST)
        sleep(0.5)

        temporary_locations = list(L.locations)

        location1 = rand.choice(temporary_locations)
        temporary_locations.remove(location1)
        location2 = rand.choice(temporary_locations)
        temporary_locations.remove(location2)
        location3 = rand.choice(temporary_locations)

        print(f"\n1: {location1} \n2: {location2}\n3: {location3}\n")
        

        location_choice = int(input("Val: "))
        
        if location_choice == 1:
            current_location = location1
        elif location_choice == 2:
            current_location = location2
        elif location_choice == 3:
            current_location = location3

        print_slow(L.TravelDescription(current_location), TEST)

    else:
        print("please enter 1 or 2.")

    if total_turns == 10:
        print("Bossfight")
    elif total_turns == 20:
        print("Bossfight")
    elif total_turns == 30:
        print("Bossfight")
    

    print()

def Fight():
    
    

    print("")

def Inventory():
    #FUNKTIONEN ÖPPNAR ENS INVENTORY OCH VISAR ENS STATS, SAMT HUR MÅNGA RUM MAN HAR VARIT I
    print("uuh")



def print_slow(str, write_speed):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(write_speed)
        if letter == "." or letter == "?" or letter == "!":
            sleep(PUNCTUATION_PAUSE_TIME)
        elif letter == ",":
            sleep(COMMA_PAUSE_TIME)

#Cacambo
cacambo = P.Player()
cacambo.hp = 200
cacambo.str = 20
cacambo.spd = 20
cacambo.gold = 40
cacambo.exp = 0

#Candide
candide = P.Player()
candide.hp = 100
candide.str = 10
candide.spd = 15
candide.gold = 10
candide.exp = 0

#Pangloss
pangloss = P.Player()
pangloss.hp = 50
pangloss.str = 15
pangloss.spd = 5
pangloss.gold = 1
pangloss.exp = 10



def intro():
    print(Art.start)

print_slow("Choose your character!", 0.01)
sleep(0.5)
player_choice = int(input(f'''

1. Cacambo! (Easy)
    HP  :  {cacambo.hp}
    STR :  {cacambo.str}
    SPD :  {cacambo.spd}
    Gold:  {cacambo.gold}


2. Candide! (Medium)
    HP  :   {candide.hp}
    STR :   {candide.str}
    SPD :   {candide.spd}
    Gold:   {candide.gold}


3. Pangloss! (Hard) 
    HP  :  {pangloss.hp}
    STR :  {pangloss.str}
    SPD :  {pangloss.spd}
    Gold:  {pangloss.gold}
    Debuffs: Syphilis, Static mindset

Your choice --> '''))

if player_choice == 1:       
    player = cacambo
    player.hp = cacambo.hp
    player.str = cacambo.str
    player.spd = cacambo.spd
    player.gold = cacambo.gold
    player.exp = cacambo.exp
    print("You chose Cacambo, good choice!")
elif player_choice == 2:
    player = candide
    player.hp = candide.hp
    player.st = candide.str
    player.spd = candide.spd
    player.gold = candide.gold
    player.exp = candide.exp
    print("You chose Candide, good luck!")
elif player_choice == 3:
    player = pangloss
    player.hp = pangloss.hp
    player.str = pangloss.str
    player.spd = pangloss.spd
    player.gold = pangloss.gold
    player.exp = pangloss.exp
    print("You chose Pangloss, ha ha ha😬.")


# player_choice = player 
# # player.level.limit = required xp to level up
# player.level.limit = 500


# def level_up():
#     if player.exp >= player.level.limit:
#         player.level += 1
#     player.level.limit += (player.level.limit*0.5)

intro()

travel()