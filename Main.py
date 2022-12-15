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
    global current_location


    print_slow("Would you like to travel, or enter your inventory? \n\n 1. Inventory    2. Travel \n\n", TEST)
    choice = int(input("Choice: "))
     

    if choice == 1:
        #INVENTORY

        print("inventory")
    elif choice == 2:
        #TRAVEL

        print_slow("Where would you like to travel?", TEST)
        sleep(0.5)

        temporary_locations = list(L.locations)
        if current_location != "":
            temporary_locations.pop(L.locations.index(current_location))

            #WEIGHTS MÅSTE VARA SAMMA LÄNGD SOM L.locations, 0 = shop, 0 = eldorado, 100 = resten, DET HÄR ÄR BARA FÖR FÖRSTA GÅNGEN TRAVEL() KALLAS
            location1 = rand.choices(temporary_locations, weights=[0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()  
            temporary_locations.remove(location1)
            location2 = rand.choices(temporary_locations, weights=[0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
            temporary_locations.remove(location2)
            location3 = rand.choices(temporary_locations, weights=[0, 0, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
        else:
            #WEIGHTS MÅSTE VARA SAMMA LÄNGD SOM L.locations, 60 = shop, 20 = eldorado, 100 = resten
            location1 = rand.choices(temporary_locations, weights=[60, 20, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
            temporary_locations.remove(location1)
            location2 = rand.choices(temporary_locations, weights=[60, 20, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
            temporary_locations.remove(location2)
            location3 = rand.choices(temporary_locations, weights=[60, 20, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()

        print(f"\n1: {location1} \n2: {location2}\n3: {location3}\n")


        location_choice = int(input("Choice: "))
        
        if location_choice == 1:
            current_location = location1
        elif location_choice == 2:
            current_location = location2
        elif location_choice == 3:
            current_location = location3
        
        if player == pangloss:
            print_slow(L.TravelDescription(current_location, True), TEST)
        else:
            print_slow(L.TravelDescription(current_location, False), TEST)

        if current_location == "eldorado":
            #ELDORADO
            print("eldorado")
        elif current_location == "shop":
            #SHOP
            print("")
        else:
            Fight()


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
    #FIGHT

    #WEIGHTS MÅSTE VARA LIKA LÅNG SOM E.Enemy_list, 1Bandit, 2cannibal, 3långöron, 4goblin, 5bulgar, 6råtta, 7traveler,
    chosen_enemy = E.Enemy_list.pop(E.Enemy_list.index(E.Enemy_list.pop(rand.choices(E.Enemy_list, weights=[100, 100, 90, 110, 70, 100, 50] , k=1)))) 

    print(E.fight_begin_description(chosen_enemy))

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
cacambo.hp = 800
cacambo.str = 20
cacambo.spd = 20
cacambo.gold = 40
cacambo.exp = 0

#Candide
candide = P.Player()
candide.hp = 500
candide.str = 15
candide.spd = 15
candide.gold = 10
candide.exp = 0

#Pangloss
pangloss = P.Player()
pangloss.hp = 300
pangloss.str = 10
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
    player.str = candide.str
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

player.level = 0

# player.level.limit = required EXP to level up, base value = 500 EXP
def level_up():
    player.level += 1
    player.level_limit += (player.level_limit*0.5)
    player.hp = player.hp*1.25
    player.str = player.str*1.25
    player.spd = player.spd*1.25
    player.exp = 0
    E.Enemy_levelup()


if player.exp >= player.level_limit:
    level_up()

# End arguments to call upon functions
intro()
current_location = ""

while True:
    travel()
