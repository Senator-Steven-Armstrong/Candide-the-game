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

            #WEIGHTS MÅSTE VARA SAMMA LÄNGD SOM L.locations, 60 = shop, 20 = eldorado, 100 = resten, DET HÄR ÄR BARA FÖR FÖRSTA GÅNGEN TRAVEL() KALLAS
            location1 = rand.choices(temporary_locations, weights=[60, 20, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()  
            temporary_locations.remove(location1)
            location2 = rand.choices(temporary_locations, weights=[60, 20, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
            temporary_locations.remove(location2)
            location3 = rand.choices(temporary_locations, weights=[60, 20, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
        else:
            #WEIGHTS MÅSTE VARA SAMMA LÄNGD SOM L.locations, 0 = shop, 0 = eldorado, 100 = resten
            location1 = rand.choices(temporary_locations, weights=[0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
            temporary_locations.remove(location1)
            location2 = rand.choices(temporary_locations, weights=[0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
            temporary_locations.remove(location2)
            location3 = rand.choices(temporary_locations, weights=[0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()

        print(f'''
        1: {location1} 
        2: {location2}
        3: {location3}
        ''')


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

    temp_enemy_list = [E.bandit, E.cannibal, E.långöron, E.goblin, E.bulgar, E.råtta, E.traveler] #FIXA DET HÄR, VARFÖR ÄNDRAS TEMP MEN OCKSÅ DEN I ENEMY MODULE??? temporär lösning atm


    #WEIGHTS MÅSTE VARA LIKA LÅNG SOM E.Enemy_list, 1Bandit, 2cannibal, 3långöron, 4goblin, 5bulgar, 6råtta, 7traveler,
    chosen_enemy = temp_enemy_list.pop(temp_enemy_list.index(rand.choices(temp_enemy_list, weights=[100, 100, 90, 110, 70, 100, 50], k=1).pop()))

    E.create_enemy(chosen_enemy)

    print_slow(E.fight_begin_description(chosen_enemy), TEST)


    while player.hp > 0 or chosen_enemy.hp > 0:

        temp_attack_list = [P.attack_move_name_1, P.attack_move_name_2, P.attack_move_name_3, P.attack_move_name_4, P.attack_move_name_5, P.attack_move_name_6, P.attack_move_name_7, P.attack_move_name_8]

        player_damage = rand.randint(player.str - 5, player.str + 5)
        enemy_damage = rand.randint(chosen_enemy.str -5 , chosen_enemy.str + 5)

        attack_1 = rand.choice(temp_attack_list)
        temp_attack_list.remove(attack_1)
        attack_2 = rand.choice(temp_attack_list)
        temp_attack_list.remove(attack_2)
        attack_3 = rand.choice(temp_attack_list)

        print_slow("What will you do?", TEST)
        print(f'''

        1: {attack_1}
        2: {attack_2}
        3: {attack_3}
        ''')

        attack_choice = int(input("Choice: "))

        if attack_choice == 1:
            chosen_attack = attack_1
        elif attack_choice == 2:
            chosen_attack = attack_2
        elif attack_choice == 3:
            chosen_attack = attack_3

        print_slow(P.attack_move_description(chosen_attack, player.name, "Excalibur", chosen_enemy.name) + "\n", TEST)
        



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
cacambo.name = "Cacambo"
cacambo.hp = 800
cacambo.str = 20
cacambo.spd = 20
cacambo.gold = 40
cacambo.exp = 0

#Candide
candide = P.Player()
candide.name = "Candide"
candide.hp = 500
candide.str = 15
candide.spd = 15
candide.gold = 10
candide.exp = 0

#Pangloss
pangloss = P.Player()
pangloss.name = "Pangloss"
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

if player_choice == 1: #CACAMBO   
    player = cacambo
    player.name = cacambo.name
    player.hp = cacambo.hp
    player.str = cacambo.str
    player.spd = cacambo.spd
    player.gold = cacambo.gold
    player.exp = cacambo.exp
    print("You chose Cacambo, good choice!")
elif player_choice == 2: #CANDIDE
    player = candide
    player.name = candide.name
    player.hp = candide.hp
    player.str = candide.str
    player.spd = candide.spd
    player.gold = candide.gold
    player.exp = candide.exp
    print("You chose Candide, good luck!")
elif player_choice == 3: #PANGLOSS
    player = pangloss
    player.name = pangloss.name
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
