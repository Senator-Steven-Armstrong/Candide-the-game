import Art
from time import sleep
import sys,time
import Player_module as P
import Location_and_description_storage as L
import Enemy_module as E
import Item_module as I
import random as rand



TEST = 0.00000000000000000000000000000000000000000000000000001
PUNCTUATION_PAUSE_TIME = 0.4
COMMA_PAUSE_TIME = 0.15

ELDORADO_MONEY_BONUS = 9999999999

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


    print_slow("\nWould you like to travel, or enter your inventory? \n\n 1. Inventory    2. Travel \n\n", TEST)

    
    while True:
        choice = input("Choice: ")
        
        if choice == "1":
            #INVENTORY
            inventory()
            
            break
        elif choice == "2":
            
            #TRAVEL-------------------------------------------------------------------------------------------------------------
            
            print_slow("Where would you like to travel?", TEST)
            sleep(0.5)

            temporary_locations = list(L.locations)

            #ELDORADO KAN BARA BESÖKAS EN GÅNG, OM DEN BESÖKS KOMMER DEN INTE LÄNGRE VARA MED I LISTAN L.Locations OCH DÄRMED KÖRS KODEN:
            if L.locations.count("Eldorado") == 0:
                location1 = rand.choices(temporary_locations, weights=[60, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()  
                temporary_locations.remove(location1)
                location2 = rand.choices(temporary_locations, weights=[60, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
                temporary_locations.remove(location2)
                location3 = rand.choices(temporary_locations, weights=[60, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
            else:
                if current_location != "":
                    temporary_locations.pop(L.locations.index(current_location))

                    #WEIGHTS MÅSTE VARA SAMMA LÄNGD SOM L.locations, 60 = shop, 20 = eldorado, 100 = resten 
                    location1 = rand.choices(temporary_locations, weights=[60, 99999999, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()  
                    temporary_locations.remove(location1)
                    location2 = rand.choices(temporary_locations, weights=[60, 20, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
                    temporary_locations.remove(location2)
                    location3 = rand.choices(temporary_locations, weights=[60, 20, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
                else:
                    #WEIGHTS MÅSTE VARA SAMMA LÄNGD SOM L.locations, 0 = shop, 0 = eldorado, 100 = resten, DET HÄR ÄR BARA FÖR FÖRSTA GÅNGEN TRAVEL() KALLAS
                    location1 = rand.choices(temporary_locations, weights=[0, 999999999, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
                    temporary_locations.remove(location1)
                    location2 = rand.choices(temporary_locations, weights=[0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
                    temporary_locations.remove(location2)
                    location3 = rand.choices(temporary_locations, weights=[0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()

            print(f'''

1: {location1} 
2: {location2}
3: {location3}
            ''')


            while True:
                location_choice = input("Choice: ")
                
                if location_choice == "1":
                    current_location = location1
                    break
                elif location_choice == "2":
                    current_location = location2
                    break
                elif location_choice == "3":
                    current_location = location3
                    break
                else:
                    print(f"\n[Please enter correct input; 1. {location1}, 2. {location2}, 3. {location3}]")   
            


            #HÄR KOLLAS DET HUR OM MAN HAR COE OCH DÄREFTER TAS PENGAR BORT
            if player.curse_of_eldorado > 0:
                print_slow(L.eldorado_lost_gold_description(player.curse_of_eldorado), TEST)

                if player.curse_of_eldorado > 1:
                    player.gold -= int(ELDORADO_MONEY_BONUS / 3 )

                    print_slow(f"    - You lost {int(ELDORADO_MONEY_BONUS/3)} gold!\n\n", TEST)
                    sleep(0.5) 
                elif player.curse_of_eldorado == 1:
                    player.gold = 0

                    print_slow(f"   - You lost all of your money!\n\n", TEST)
                    sleep(0.8)

                player.curse_of_eldorado -= 1



            #HÄR KOLLAS DET OM MAN HAMNAR I EN FÄLLA ELLER INTE
            trap_chance = rand.randint(1, 1)
            if trap_chance == 1 and current_location != "Eldorado":
                trap(current_location)  

            #HÄR SKRIVS BESKRIVNINGEN AV SIN RESA UT
            if player == pangloss:
                print_slow(L.TravelDescription(current_location, True), TEST)
            else:
                print_slow(L.TravelDescription(current_location, False), TEST)

        


            if current_location == "Eldorado":
                #ELDORADO----------------------------------------------------------------------------------------------------------
                
                print_slow("\n                     Stay                  Leave\n", 0.1)
                
                print_slow("\nChoice: ", 0.18)

                while True:
                    eldorado_ending_choice = input()

                    if eldorado_ending_choice.lower() == "stay":
                        print("You decide to stay. good ending")

                        break
                    elif eldorado_ending_choice.lower() == "leave":
                        
                        print_slow('''
You decide to leave, to journey out and take back Kunigunda once and for all!

You are taken to the outskirts of the deep valley that Eldorado resides in. 
The "King" offers you riches to help with you quest, and you gladly accept. 
102 sheep packed full with gold and jewels will accompany you. 
You leave richer than all of the European kings combined, but something feels off.
Final goodbyes are said and you get one last glimpse of paradise. 
You start to wander once more, your spirit and pockets bigger than ever.
''', TEST)

                        player.curse_of_eldorado = 3
                        player.gold = ELDORADO_MONEY_BONUS
                        L.locations.remove("Eldorado")
                        break
                    else:
                        print_slow("\nLeave or stay, choose: ", 0.15)
                

            elif current_location == "Shop":
                #SHOP
                print("")
            else:
                #HÄR KAN EN FIGHT SKE------------------------------------------------------------------------

                fight()

            if total_turns == 10:
                print("Bossfight")
            elif total_turns == 20:
                print("Bossfight")
            elif total_turns == 30:
                print("Bossfight")
            
            break
        else:
            print("\n[Please enter correct input; 1. Inventory, 2. Travel]")



    


def inventory():
    is_equipped_item = False

    print_slow("\nYou opened your backpack.", TEST)

    print(f'''

--------------------------------------------------------------------------------------------------------------------------

PLAYER STATS:

{player.name} level {player.level}
EXP: {player.exp} / {player.level_limit}

HP: {player.hp} / {player.max_hp}
STR: {player.str}
SPD: {player.spd}
Gold: {player.gold}
Debuffs: {player.debuffs}

INVENTORY:''')
    print(player.shown_inventory)

    print(f'''

EQUIPPED ITEMS:
Weapon: {player.equipped_weapon.name}
Armor: {player.equipped_armor.name}
Accessory: {player.equipped_accessory.name}

--------------------------------------------------------------------------------------------------------------------------
    ''')



    print_slow("\nWhat would you like to do?", TEST)

    print('''
1. Change Equipment
2. Go back
        ''')

    while is_equipped_item == False:    
        inventory_choice = input("Choice: ")
        
        if inventory_choice == "1":
            #CHANGE EQUIPMENT
            sleep(0.5)
            
            print('''
Pick an equipment to change:
1. Weapon
2. Armor
3. Accessory

4. Exit inventory
''')    
            while is_equipped_item == False:

                item_change_choice = input("Choice: ")

                if item_change_choice == "1":
                    #ÄNDRAR VAPEN-------------------------------------------------------------------------------------------------------
                    
                    temp_weapon_inventory = []
                    for i in player.inventory:
                        if i.type == "weapon":
                            temp_weapon_inventory.append(i)

                    if len(temp_weapon_inventory) > 0:

                        print(f"\nCurrent weapon: {player.equipped_weapon.name}")

                        print_slow("\nWhat weapon would you like to equip?\n", TEST)

                        #HÄR PRINTAS LISTAN MED ALLA VAPEN I ENS INVENTORY
                        j = 1
                        for i in temp_weapon_inventory:
                            if i != player.equipped_weapon:
                                print(j, ". ", i.name, f"\n[HP: {i.max_hp_bonus}, STR: {i.str_bonus}, SPD: {i.spd_bonus}]\n",sep='')
                                j += 1
                            if j-1 == len(temp_weapon_inventory):
                                print(j, ". Change nothing / Exit inventory", sep='')
                            
                        

                        while is_equipped_item == False:

                            while True:
                            
                                try:
                                    weapon_equip_choice = int(input("\nChoice: "))
                                except:
                                    print("[Please enter a number]")
                                else:
                                    break

                            #HÄR KOLLAR DEN VILKET VAPEN MAN EQUIPAR
                            if weapon_equip_choice == len(temp_weapon_inventory) + 1:
                                break
                            else:
                                for i in range(len(temp_weapon_inventory)):
                                    
                                    if weapon_equip_choice == i + 1:
                                        #HÄR TAS GAMLA WEAPONSTATS BORT
                                        player.max_hp -= player.equipped_weapon.max_hp_bonus
                                        player.hp -= player.equipped_weapon.hp_bonus
                                        player.str -= player.equipped_weapon.str_bonus
                                        player.spd -= player.equipped_weapon.spd_bonus
                                        player.inventory.append(player.equipped_weapon)

                                        player.equipped_weapon = temp_weapon_inventory[i]
                                        player.equipped_weapon.name = player.equipped_weapon.name
                                        player.inventory.pop(player.inventory.index(player.equipped_weapon))

                                        if player.equipped_weapon == I.fists:
                                            print_slow("You holstered your weapon.\n", TEST)
                                        else:
                                            print_slow(f"\nYou equipped {player.equipped_weapon.name}.\n", TEST)
                                                                        
                                            
                                        #HÄR LÄGGS NYA  STATS PÅ NÄR MAN HAR EQUIPAT ETT VAPEN
                                        player.max_hp += player.equipped_weapon.max_hp_bonus
                                        player.hp += player.equipped_weapon.hp_bonus
                                        player.str += player.equipped_weapon.str_bonus
                                        player.spd += player.equipped_weapon.spd_bonus

                                        is_equipped_item = True
                                        break
                                    else:
                                        if i == len(temp_weapon_inventory) - 1:
                                            print("[Please choose a weapon to equip, or exit inventory]")
 

                    else:
                        print_slow("\nNo weapons in inventory to equip\n", TEST)
                        break
                    
                    
                
                elif item_change_choice == "2":
                    #ÄNDRAR ARMOR----------------------------------------------------------------------------------------------------
                 
                    temp_armor_inventory = []
                    for i in player.inventory:
                        if i.type == "armor":
                            temp_armor_inventory.append(i)

                    if len(temp_armor_inventory) > 0:

                        print(f"\nCurrent armor: {player.equipped_armor.name}")

                        print_slow("\nWhat armor would you like to equip?\n", TEST)

                        #HÄR PRINTAS LISTAN MED ALLA ARMORPIECES I ENS INVENTORY
                        j = 1
                        for i in temp_armor_inventory:
                            if i != player.equipped_armor:
                                print(j, ". ", i.name, f"\n[HP: {i.max_hp_bonus}, STR: {i.str_bonus}, SPD: {i.spd_bonus}]\n",sep='')
                                j += 1
                            if j-1 == len(temp_armor_inventory):
                                print(j, ". Change nothing / Exit inventory", sep='')
                            
                        

                        while is_equipped_item == False:

                            while True:
                            
                                try:
                                    armor_equip_choice = int(input("\nChoice: "))
                                except:
                                    print("[Please enter a number]")
                                else:
                                    break

                            #HÄR KOLLAR DEN VILKEN ARMOR MAN EQUIPAR
                            if armor_equip_choice == len(temp_armor_inventory) + 1:
                                break
                            else:
                                for i in range(len(temp_armor_inventory)):
                                    
                                    if armor_equip_choice == i + 1:
                                        #HÄR TAS GAMLA armorSTATS BORT
                                        player.max_hp -= player.equipped_armor.max_hp_bonus
                                        player.hp -= player.equipped_armor.hp_bonus
                                        player.str -= player.equipped_armor.str_bonus
                                        player.spd -= player.equipped_armor.spd_bonus
                                        player.inventory.append(player.equipped_armor)

                                        player.equipped_armor = temp_armor_inventory[i]
                                        player.equipped_armor.name = player.equipped_armor.name
                                        player.inventory.pop(player.inventory.index(player.equipped_armor))

                                        if player.equipped_armor == I.fists:
                                            print_slow("You took off your armor.\n", TEST)
                                        else:
                                            print_slow(f"\nYou equipped {player.equipped_armor.name}.\n", TEST)
                                                                        
                                            
                                        #HÄR LÄGGS NYA  STATS PÅ NÄR MAN HAR EQUIPAT EN ARMORPIECE
                                        player.max_hp += player.equipped_armor.max_hp_bonus
                                        player.hp += player.equipped_armor.hp_bonus
                                        player.str += player.equipped_armor.str_bonus
                                        player.spd += player.equipped_armor.spd_bonus

                                        is_equipped_item = True
                                        break
                                    else:
                                        if i == len(temp_armor_inventory) - 1:
                                            print("[Please choose an armorpiece to equip, or exit inventory]")

                            if is_equipped_item == True:
                                break  

                    else:
                        print_slow("\nNo armorpieces in inventory to equip\n", TEST)
                        break
                    
                    
                
                elif item_change_choice == "3":
                    #ÄNDRAR ACCESSORY----------------------------------------------------------------------------------------------------
                    temp_accessory_inventory = []
                    for i in player.inventory:
                        if i.type == "accessory":
                            temp_accessory_inventory.append(i)

                    if len(temp_accessory_inventory) > 0:

                        print(f"\nCurrent accessory: {player.equipped_accessory.name}")

                        print_slow("\nWhich accessory would you like to equip?\n", TEST)

                        #HÄR PRINTAS LISTAN MED ALLA ACCESSORIES I ENS INVENTORY
                        j = 1
                        for i in temp_accessory_inventory:
                            if i != player.equipped_accessory:
                                print(j, ". ", i.name, f"\n[HP: {i.max_hp_bonus}, STR: {i.str_bonus}, SPD: {i.spd_bonus}]\n",sep='')
                                j += 1
                            if j-1 == len(temp_accessory_inventory):
                                print(j, ". Change nothing / Exit inventory", sep='')
                            
                        

                        while is_equipped_item == False:

                            while True:
                            
                                try:
                                    accessory_equip_choice = int(input("\nChoice: "))
                                except:
                                    print("[Please enter a number]")
                                else:
                                    break

                            #HÄR KOLLAR DEN VILKEN ACCESSORY MAN EQUIPAR
                            if accessory_equip_choice == len(temp_accessory_inventory) + 1:
                                break
                            else:
                                for i in range(len(temp_accessory_inventory)):
                                    
                                    if accessory_equip_choice == i + 1:
                                        #HÄR TAS GAMLA accessorySTATS BORT
                                        player.max_hp -= player.equipped_accessory.max_hp_bonus
                                        player.hp -= player.equipped_accessory.hp_bonus
                                        player.str -= player.equipped_accessory.str_bonus
                                        player.spd -= player.equipped_accessory.spd_bonus
                                        player.inventory.append(player.equipped_accessory)

                                        player.equipped_accessory = temp_accessory_inventory[i]
                                        player.equipped_accessory.name = player.equipped_accessory.name
                                        player.inventory.pop(player.inventory.index(player.equipped_accessory))

                                        if player.equipped_accessory == I.fists:
                                            print_slow("You put your accessory back in your backpack.\n", TEST)
                                        else:
                                            print_slow(f"\nYou equipped {player.equipped_accessory.name}.\n", TEST)
                                                                        
                                            
                                        #HÄR LÄGGS NYA  STATS PÅ NÄR MAN HAR EQUIPAT EN ACCESSORY
                                        player.max_hp += player.equipped_accessory.max_hp_bonus
                                        player.hp += player.equipped_accessory.hp_bonus
                                        player.str += player.equipped_accessory.str_bonus
                                        player.spd += player.equipped_accessory.spd_bonus

                                        is_equipped_item = True
                                        break
                                    else:
                                        if i == len(temp_accessory_inventory) - 1:
                                            print("[Please choose an accessory to equip, or exit inventory]")

                            if is_equipped_item == True:
                                break  

                    else:
                        print_slow("\nNo accessories in inventory to equip\n", TEST)
                        break
                
                elif item_change_choice == 4:
                    break
                else:
                    print("\n[Please enter correct input; 1. Armor, 2. Weapon, 3. Accessory, 4. Exit]")    
                    
                 
                
            break
            

        elif inventory_choice == "2":
            break
        else:
            print("\n[Please enter correct input; 1. Change equipment, 2. Go back]")
        

    


def fight():
    #FIGHT

    temp_enemy_list = [E.bandit, E.cannibal, E.långöron, E.goblin, E.bulgar, E.råtta, E.traveler] #FIXA DET HÄR, VARFÖR ÄNDRAS TEMP MEN OCKSÅ DEN I ENEMY MODULE??? temporär lösning atm


    #WEIGHTS MÅSTE VARA LIKA LÅNG SOM E.Enemy_list, 1Bandit, 2cannibal, 3långöron, 4goblin, 5bulgar, 6råtta, 7traveler,
    chosen_enemy = temp_enemy_list.pop(temp_enemy_list.index(rand.choices(temp_enemy_list, weights=[100, 100, 90, 110, 70, 100, 50], k=1).pop()))

    E.create_enemy(chosen_enemy)

    print_slow(E.fight_begin_description(chosen_enemy), TEST)

    chosen_enemy.hp = chosen_enemy.max_hp

    print_slow("\nEnemy stats: ", TEST)
    sleep(PUNCTUATION_PAUSE_TIME)
    print(f'''
HP: {chosen_enemy.hp} / {chosen_enemy.max_hp}
STR: {chosen_enemy.str}
SPD: {chosen_enemy.spd}
''')
    sleep(2)

    while player.hp > 0 or chosen_enemy.hp > 0:


        temp_player_attack_list = [P.attack_move_name_1, P.attack_move_name_2, P.attack_move_name_3, P.attack_move_name_4, P.attack_move_name_5, P.attack_move_name_6, P.attack_move_name_7, P.attack_move_name_8]

        player_damage = rand.randint(player.str - 5, player.str + 5)
        enemy_damage = rand.randint(chosen_enemy.str -5 , chosen_enemy.str + 5)

        #VÄLJER VEM SOM FÅR ATTACKERA FÖRST
        first_attack_move = rand.choices(["player", "enemy", "player", "enemy"], weights=[player.spd, chosen_enemy.spd, 140, 140], k=1).pop()

        attack_1 = rand.choice(temp_player_attack_list)
        temp_player_attack_list.remove(attack_1)
        attack_2 = rand.choice(temp_player_attack_list)
        temp_player_attack_list.remove(attack_2)
        attack_3 = rand.choice(temp_player_attack_list)

        print_slow("What attack will you use?", TEST)
        print(f'''

    1: {attack_1}
    2: {attack_2}
    3: {attack_3}
        ''')

        while True:
            while True:
                try:
                    attack_choice = int(input("Choice: "))
                except:
                    print("\n[Please enter a number]")
                else:
                    break

            if attack_choice == 1:
                chosen_attack = attack_1
                break
            elif attack_choice == 2:
                chosen_attack = attack_2
                break
            elif attack_choice == 3:
                chosen_attack = attack_3
                break
            else:
                print(f"\n[Please enter a valid input; 1. {attack_1}, 2. {attack_2}, 3. {attack_3}]")

        chosen_enemy.hp -= player_damage
        player.hp -= enemy_damage

        if first_attack_move == "player":
            print_slow("\n" + P.attack_move_description(chosen_attack, player.name, player.equipped_weapon.name, chosen_enemy.name), TEST)

            print_slow(f"\n   - You dealt {player_damage} damage!", TEST)
            if chosen_enemy.hp > 0:
                print_slow(f"\n   - Enemy health: {chosen_enemy.hp} / {chosen_enemy.max_hp}", TEST)
            else:
                print_slow(f"\n   - Enemy health: 0 / {chosen_enemy.max_hp}", TEST)
                break
            
            print_slow("\n" + E.enemy_attack_description(chosen_enemy, player.name), TEST)
            print_slow(f"\n   - Enemy dealt {enemy_damage} damage!", TEST)
            print_slow(f"\n   - {player.name}'s health: {player.hp} / {player.max_hp}", TEST)

        elif first_attack_move == "enemy":
            print_slow(f"\nEnemy struck first!", TEST)
            print_slow(E.enemy_attack_description(chosen_enemy, player.name), TEST)
            print_slow(f"\n   - Enemy dealt {enemy_damage} damage!", TEST)
            print_slow(f"\n   - {player.name}'s health: {player.hp} / {player.max_hp}.\n", TEST)
            
            #IF STATEMENT HÄR OM DU DOG ELLER INTE

            print_slow(P.attack_move_description(chosen_attack, player.name, player.equipped_weapon.name, chosen_enemy.name), TEST)
            
            print_slow(f"\n   - You dealt {player_damage} damage!", TEST)
            if chosen_enemy.hp > 0:
                print_slow(f"\n   - Enemy health: {chosen_enemy.hp} / {chosen_enemy.max_hp}", TEST)
            else:
                print_slow(f"\n   - Enemy health: 0 / {chosen_enemy.max_hp}.", TEST)
                break

        sleep(0.8)
        print("\n")

    print_slow(f"\n\n{chosen_enemy.name} died!\n", TEST)

    loot("enemy drop")

def print_slow(str, write_speed):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(write_speed)
        if letter == "." or letter == "?" or letter == "!":
            sleep(PUNCTUATION_PAUSE_TIME)
        elif letter == ",":
            sleep(COMMA_PAUSE_TIME)

def loot(type):
    if type == "enemy drop":
        weapon_drop_chance = rand.randint(1, 1)
        if weapon_drop_chance == 1:
            print_slow("\nThe enemy dropped an item!", TEST)

            dropped_weapon_index = rand.choices(I.item_list, weights=I.item_rarity_list, k=1).pop()
            dropped_weapon = I.create_item(dropped_weapon_index)
            print_slow(f"\nYou picked up {dropped_weapon.name}.\n", TEST)
            player.inventory.append(dropped_weapon)
            player.shown_inventory.append(dropped_weapon.name)
             

def trap(location):
    trap_type = rand.choice(["gold", "damage"])
    gold_lost = rand.randint(20, 80)

    if player.gold == 0 or player.gold - gold_lost <= 0:
        player.gold = 0
        trap_type = "damage"
    elif player.curse_of_eldorado > 0:
        trap_type = "damage"

    print_slow(L.trap_description(player.name, location, trap_type), TEST)

    damage = rand.randint(15, 45)
    player.hp -= damage

    if trap_type == "gold":
        player.gold -= gold_lost

        print_slow(f"   - You lost {gold_lost} gold!  Gold: {player.gold}", TEST)
        print_slow(f"\n   - You took {damage} damage!  HP: {player.hp} / {player.max_hp}\n", TEST)

    elif trap_type == "damage":
        
        print_slow(f"   - You took {damage} damage!  HP: {player.hp} / {player.max_hp}\n", TEST)
    
    sleep(0.8)


    

def intro():
    print(Art.start)


# player.level.limit = required EXP to level up, base value = 500 EXP
def level_up():
    player.level += 1
    player.level_limit += (player.level_limit*0.5)
    player.hp = player.hp*1.25
    player.str = player.str*1.25
    player.spd = player.spd*1.25
    player.exp = 0
    E.enemy_levelup()

#Cacambo
cacambo = P.Player()
cacambo.name = "Cacambo"
cacambo.max_hp = 800
cacambo.str = 60000
cacambo.spd = 20000
cacambo.gold = 40

#Candide
candide = P.Player()
candide.name = "Candide"
candide.max_hp = 500
candide.str = 35
candide.spd = 15
candide.gold = 10

#Pangloss
pangloss = P.Player()
pangloss.name = "Pangloss"
pangloss.max_hp = 300
pangloss.str = 20
pangloss.spd = 5
pangloss.gold = 1

#------------------------------------------------------HÄR KÖRS HUVUDDELEN AV PROGRAMMET-------------------------------------------------------------------------------------------------------

print_slow("Choose your character!", 0.01)
sleep(0.5)

print(f'''

1. Cacambo! (Easy)
    HP  :  {cacambo.max_hp}
    STR :  {cacambo.str}
    SPD :  {cacambo.spd}
    Gold:  {cacambo.gold}


2. Candide! (Medium)
    HP  :   {candide.max_hp}
    STR :   {candide.str}
    SPD :   {candide.spd}
    Gold:   {candide.gold}


3. Pangloss! (Hard) 
    HP  :  {pangloss.max_hp}
    STR :  {pangloss.str}
    SPD :  {pangloss.spd}
    Gold:  {pangloss.gold}
    Debuffs: Syphilis, Static mindset
''')



while True:
    try:
        player_choice = int(input("Choice: "))

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

        player.level = 1
        player.hp = player.max_hp
        player.inventory = []
        player.shown_inventory = []
    except:
        print("\n[Please enter a correct input; 1. Cacambo, 2. Candide, 3. Pangloss]")
    else:
        break


# if player.exp >= player.level_limit:
#     level_up()

# End arguments to call upon functions



intro()

current_location = ""

for i in range(10):
    weapon_choice = rand.choice(I.item_list)
    player.inventory.append(I.create_item(weapon_choice))


for i in player.inventory:
    player.shown_inventory.append(i.name)


while True:

    travel()