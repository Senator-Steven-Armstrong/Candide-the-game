import Art as A
from time import sleep
import sys,time
import Player_module as P
import Location_and_description_storage as L
import Enemy_module as E
import Item_module as I
import random as rand
import copy
import pygame

pygame.mixer.init()



#SOUND EFFECTS
start_music = 'sounds/pococurante theme.mp3'
UI_sfx = pygame.mixer.Sound('sounds/UI sound effect.mp3')

TEST = 0.02
PUNCTUATION_PAUSE_TIME = 0.4
COMMA_PAUSE_TIME = 0.15
SEMICOLON_PAUSE_TIME = 0.6

ELDORADO_MONEY_BONUS = 9999999999

current_location = ""
total_turns = 0
good_ending = False

game_over = False

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
    global total_turns
    global game_over


    print_slow("\nWould you like to travel, or enter your inventory? \n\n 1. Inventory    2. Travel \n\n", TEST)

    
    while True:
        choice = input("Choice: ")
        pygame.mixer.Sound.play(UI_sfx)
        
        if choice == "1":
            #INVENTORY
            inventory()
            
            break
        elif choice == "2":
            
            #TRAVEL-------------------------------------------------------------------------------------------------------------
            
            if total_turns == 3:
                bossfight_pococurante()
                break
            elif total_turns == 6:
                bossfight_baronen()
                break
            elif total_turns == 999999:
                bossfight_kunigunda()
                break
            else:

                print_slow("Where would you like to travel?", TEST)
                sleep(0.5)

                temporary_locations = copy.deepcopy(L.locations)

                #ELDORADO KAN BARA BESÖKAS EN GÅNG, OM DEN BESÖKS KOMMER DEN INTE LÄNGRE VARA MED I LISTAN L.Locations OCH DÄRMED KÖRS KODEN:
                if L.locations.count(L.eldorado) == 0:
                    location1 = rand.choices(temporary_locations, weights=[60, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()  
                    temporary_locations.remove(location1)
                    location2 = rand.choices(temporary_locations, weights=[60, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
                    temporary_locations.remove(location2)
                    location3 = rand.choices(temporary_locations, weights=[60, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
                else:
                    if current_location != "":
                        temporary_locations.remove(current_location)

                        #WEIGHTS MÅSTE VARA SAMMA LÄNGD SOM L.locations, 60 = shop, 20 = eldorado, 100 = resten 
                        location1 = rand.choices(temporary_locations, weights=[60, 20, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()  
                        temporary_locations.remove(location1)
                        location2 = rand.choices(temporary_locations, weights=[60, 20, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
                        temporary_locations.remove(location2)
                        location3 = rand.choices(temporary_locations, weights=[60, 20, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
                    else:
                        #WEIGHTS MÅSTE VARA SAMMA LÄNGD SOM L.locations, 0 = shop, 0 = eldorado, 100 = resten, DET HÄR ÄR BARA FÖR FÖRSTA GÅNGEN TRAVEL() KALLAS
                        location1 = rand.choices(temporary_locations, weights=[0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
                        temporary_locations.remove(location1)
                        location2 = rand.choices(temporary_locations, weights=[0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()
                        temporary_locations.remove(location2)
                        location3 = rand.choices(temporary_locations, weights=[0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100], k=1).pop()

                print(f'''

    1: {location1.name} 
    2: {location2.name}
    3: {location3.name}
                ''')


                while True:
                    location_choice = input("Choice: ")
                    pygame.mixer.Sound.play(UI_sfx)
                    
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
                
                chosen_description = L.choose_description(current_location)

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
                    
                if game_over == False:  

                    #HÄR SKRIVS BESKRIVNINGEN AV SIN RESA UT
                    if player == pangloss:
                        # pygame.mixer.music.play(L.lissabon_special.music)
                        print_slow(L.lissabon_special.description)
                    else:
                        print_slow(chosen_description.description, TEST)

                


                    if current_location == "Eldorado":
                        #ELDORADO----------------------------------------------------------------------------------------------------------
                        
                        print_slow("\n                     Stay                  Leave\n", 0.1)
                        
                        print_slow("\nChoice: ", 0.18)

                        while True:
                            eldorado_ending_choice = input()

                            if eldorado_ending_choice.lower() == "stay":
                                print_slow(L.eldorado_stay_description, TEST)

                                game_over = True
                                break
                            elif eldorado_ending_choice.lower() == "leave":
                                
                                print_slow(L.eldorado_leave_description, TEST)

                                player.curse_of_eldorado = 3
                                player.gold = ELDORADO_MONEY_BONUS
                                L.locations.remove("Eldorado")
                                break
                            else:
                                print_slow("\nLeave or stay, choose: ", 0.15)
                        
                        
                    #----------------------------------------------SHOP------------------------------------------------------------
                    elif current_location == "Shop":

                        print(A.shop)

                        shop_items = copy.deepcopy(I.item_list)

                        shop_item_indicator_1 = rand.choices(shop_items, I.item_rarity_list, k=1).pop()
                        shop_item_index_1 = shop_items.index(shop_item_indicator_1)
                        I.item_rarity_list.pop(shop_item_index_1)
                        shop_items.remove(shop_item_indicator_1)
                        shop_item_1 = I.create_item(shop_item_indicator_1)

                        shop_item_indicator_2 = rand.choices(shop_items, I.item_rarity_list, k=1).pop()
                        shop_item_index_2 = shop_items.index(shop_item_indicator_2)
                        I.item_rarity_list.pop(shop_item_index_2)
                        shop_items.remove(shop_item_indicator_2)
                        shop_item_2 = I.create_item(shop_item_indicator_2)

                        shop_item_indicator_3 = rand.choices(shop_items, I.item_rarity_list, k=1).pop()
                        shop_item_index_3 = shop_items.index(shop_item_indicator_3)
                        I.item_rarity_list.pop(shop_item_index_3)
                        shop_items.remove(shop_item_indicator_3)
                        shop_item_3 = I.create_item(shop_item_indicator_3)

                        while True:
                            sleep(1)
                            print(f'''
Current gold: {player.gold}

Thee can purchaseth one of the following three items:

    1.{shop_item_1.name}; {shop_item_1.cost} Gold
    [HP: {shop_item_1.max_hp_bonus} STR: {shop_item_1.str_bonus} SPD: {shop_item_1.spd_bonus}]

    2.{shop_item_2.name}; {shop_item_2.cost} Gold
    [HP: {shop_item_2.max_hp_bonus} STR: {shop_item_2.str_bonus} SPD: {shop_item_2.spd_bonus}]

    3.{shop_item_3.name}; {shop_item_3.cost} Gold
    [HP: {shop_item_3.max_hp_bonus} STR: {shop_item_3.str_bonus} SPD: {shop_item_3.spd_bonus}]

    4. None (go back)
                            ''')

                            while True:
                                shop_input = input("Choice: ")
                                pygame.mixer.Sound.play(UI_sfx)

                                if shop_input == "1":
                                    chosen_item = shop_item_1
                                    break
                                elif shop_input == "2":
                                    chosen_item = shop_item_2
                                    break
                                elif shop_input == "3":
                                    chosen_item = shop_item_3
                                    break
                                elif shop_input == "4":
                                    print_slow("\nThee no more brain than stone clotpole sandwich, nev'r cometh backeth!\You hastily leave the store.", TEST)
                                    break
                                else:
                                    print("\n[Please enter correct input]")
                                    continue
                            
                            if shop_input == "4":
                                break
                            elif chosen_item.cost <= player.gold:
                                player.gold -= chosen_item.cost
                                print_slow(f"\nThanketh thee f'r purchasing {chosen_item.name}, desire thee has't a t'rrible day!\n", TEST)
                                player.inventory.append(chosen_item)
                                break
                            else: 
                                print_slow("\nThee has't not enow wage! Buyeth something else shall ya, If 't be true thee did get the wage f'r t.", TEST)
                                continue





                    else:
                        #HÄR KAN EN FIGHT SKE------------------------------------------------------------------------

                        fight(chosen_description)

                

                    total_turns += 1

                break
        else:
            print("\n[Please enter correct input; 1. Inventory, 2. Travel]")





def inventory():
    has_equipped_item = False

    print_slow("\nYou opened your backpack.", TEST)

    print(f'''

--------------------------------------------------------------------------------------------------------------------------

PLAYER STATS:

{player.name} level {player.level}
EXP: {player.exp} / {int(player.level_limit)}

HP: {player.hp} / {player.max_hp}
STR: {player.str}
SPD: {player.spd}
Gold: {player.gold}
Debuffs: {player.debuffs}

INVENTORY:''')
    
    #PRINTAR INVENTORYN
    if len(player.inventory) == 0:
        print("[Empty]")
    j = 1
    inventory_row = ""
    for i in player.inventory:
        if j-1 == 0 or (j-1) % 3 == 0:
            inventory_row = i.name
        elif j-1 % 3 != 0:
            inventory_row = inventory_row + " || " + i.name
        
        if j % 3 == 0 or j == len(player.inventory):
            print("|| " + inventory_row + " ||")

        j += 1

    print(f'''
EQUIPPED ITEMS:
Weapon: {player.equipped_weapon.name}
Armor: {player.equipped_armor.name}
Accessory: {player.equipped_accessory.name}

Countries traveled: {total_turns}

--------------------------------------------------------------------------------------------------------------------------
    ''')



    print_slow("\nWhat would you like to do?", TEST)

    print('''
1. Change Equipment or use items
2. Go back
        ''')

    while has_equipped_item == False:    
        inventory_choice = input("Choice: ")
        pygame.mixer.Sound.play(UI_sfx)
        
        if inventory_choice == "1":
            #CHANGE EQUIPMENT
            sleep(0.5)
            
            print('''
Choose an action:
1. Weapon
2. Armor
3. Accessory

4. Use items

5. Exit inventory
''')    
            while has_equipped_item == False:

                item_change_choice = input("Choice: ")
                pygame.mixer.Sound.play(UI_sfx)

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
                            
                        

                        while has_equipped_item == False:

                            while True:
                            
                                try:
                                    weapon_equip_choice = int(input("\nChoice: "))
                                    pygame.mixer.Sound.play(UI_sfx)
                                except:
                                    print("[Please enter a number]")
                                else:
                                    break

                            #HÄR KOLLAR DEN VILKET VAPEN MAN EQUIPAR
                            if weapon_equip_choice == len(temp_weapon_inventory) + 1:
                                has_equipped_item = True
                                break
                            else:
                                for i in range(len(temp_weapon_inventory)):
                                    
                                    if weapon_equip_choice == i + 1:
                                        #HÄR TAS GAMLA WEAPONSTATS BORT
                                        player.max_hp -= player.equipped_weapon.max_hp_bonus
                                        player.hp -= player.equipped_weapon.max_hp_bonus
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
                                        player.hp += player.equipped_weapon.max_hp_bonus
                                        player.str += player.equipped_weapon.str_bonus
                                        player.spd += player.equipped_weapon.spd_bonus

                                        has_equipped_item = True
                                        break
                                    else:
                                        if i == len(temp_weapon_inventory) - 1:
                                            print("[Please choose a weapon to equip, or exit inventory]")
 

                    else:
                        print_slow("\nNo weapons in inventory to equip.\n", TEST)
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
                            
                        

                        while has_equipped_item == False:

                            while True:
                            
                                try:
                                    armor_equip_choice = int(input("\nChoice: "))
                                    pygame.mixer.Sound.play(UI_sfx)
                                except:
                                    print("[Please enter a number]")
                                else:
                                    break

                            #HÄR KOLLAR DEN VILKEN ARMOR MAN EQUIPAR
                            if armor_equip_choice == len(temp_armor_inventory) + 1:
                                has_equipped_item = True
                                break
                            else:
                                for i in range(len(temp_armor_inventory)):
                                    
                                    if armor_equip_choice == i + 1:
                                        #HÄR TAS GAMLA armorSTATS BORT
                                        player.max_hp -= player.equipped_armor.max_hp_bonus
                                        player.hp -= player.equipped_armor.max_hp_bonus
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
                                        player.hp += player.equipped_armor.max_hp_bonus
                                        player.str += player.equipped_armor.str_bonus
                                        player.spd += player.equipped_armor.spd_bonus

                                        has_equipped_item = True
                                        break
                                    else:
                                        if i == len(temp_armor_inventory) - 1:
                                            print("[Please choose an armorpiece to equip, or exit inventory]")

                            if has_equipped_item == True:
                                break  

                    else:
                        print_slow("\nNo armorpieces in inventory to equip.\n", TEST)
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
                            
                        

                        while has_equipped_item == False:

                            while True:
                            
                                try:
                                    accessory_equip_choice = int(input("\nChoice: "))
                                    pygame.mixer.Sound.play(UI_sfx)
                                except:
                                    print("[Please enter a number]")
                                else:
                                    break

                            #HÄR KOLLAR DEN VILKEN ACCESSORY MAN EQUIPAR
                            if accessory_equip_choice == len(temp_accessory_inventory) + 1:
                                has_equipped_item = True
                                break
                            else:
                                for i in range(len(temp_accessory_inventory)):
                                    
                                    if accessory_equip_choice == i + 1:
                                        #HÄR TAS GAMLA accessorySTATS BORT
                                        player.max_hp -= player.equipped_accessory.max_hp_bonus
                                        player.hp -= player.equipped_accessory.max_hp_bonus
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
                                                                        
                                            
                                        #HÄR LÄGGS NYA STATS PÅ NÄR MAN HAR EQUIPAT EN ACCESSORY
                                        player.max_hp += player.equipped_accessory.max_hp_bonus
                                        player.hp += player.equipped_accessory.max_hp_bonus
                                        player.str += player.equipped_accessory.str_bonus
                                        player.spd += player.equipped_accessory.spd_bonus

                                        has_equipped_item = True
                                        break
                                    else:
                                        if i == len(temp_accessory_inventory) - 1:
                                            print("[Please choose an accessory to equip, or exit inventory]")

                            if has_equipped_item == True:
                                break  

                    else:
                        print_slow("\nNo accessories in inventory to equip.\n", TEST)
                        break
                
                elif item_change_choice == "4":
                    temp_item_inventory = []
                    for i in player.inventory:
                        if i.type == "consumable" or i.type == "healing":
                            temp_item_inventory.append(i)



                    if len(temp_item_inventory) > 0:
                        print_slow("\nWhich item would you like to use? The effect is permanent, and the item will be lost.\n", TEST)

                        j = 1
                        for i in temp_item_inventory:
                            if i.type == "healing":
                                print(j, ". ", i.name, f"\n[Healed HP: {i.hp_bonus}]\n",sep='')
                            else:
                                print(j, ". ", i.name, f"\n[HP: {i.max_hp_bonus}, STR: {i.str_bonus}, SPD: {i.spd_bonus}]\n",sep='')
                            j += 1
                            if j-1 == len(temp_item_inventory):
                                print(j, ". Change nothing / Exit inventory", sep='')

                        
                        while True:
                            try:
                                item_use_choice = int(input("\nChoice: "))
                                pygame.mixer.Sound.play(UI_sfx)
                            except:
                                print("[Please enter a number]")
                            else:
                                break

                        if item_use_choice == len(temp_item_inventory) + 1:
                            break
                        else:
                            for i in range(len(temp_item_inventory)):
                                if item_use_choice == i + 1 and temp_item_inventory[i].type == "consumable":
                                    print_slow(f"You used {temp_item_inventory[i].name}.\n", TEST)

                                    player.max_hp += temp_item_inventory[i].max_hp_bonus
                                    player.hp += temp_item_inventory[i].max_hp_bonus
                                    player.str += temp_item_inventory[i].str_bonus
                                    player.spd += temp_item_inventory[i].spd_bonus

                                    player.inventory.remove(temp_item_inventory[i])

                                    has_equipped_item = True
                                    break
                                elif item_use_choice == i + 1 and temp_item_inventory[i].type == "healing":
                                    print_slow(f"You used {temp_item_inventory[i].name}, healing {temp_item_inventory[i].hp_bonus}.\n", TEST)

                                    if player.hp + temp_item_inventory[i].hp_bonus > player.max_hp:
                                        player.hp = player.max_hp
                                    else:
                                        player.hp += temp_item_inventory[i].hp_bonus

                                    player.inventory.remove(temp_item_inventory[i])

                                    has_equipped_item = True
                                    break

                                elif i == len(temp_item_inventory) - 1:
                                    print("[Please choose an item to use, or exit inventory]")
                    else:
                        has_equipped_item = True
                        print_slow("\nNo consumables in inventory.\n", TEST)

                elif item_change_choice == "5":
                    break
                else:
                    print("\n[Please enter correct input; 1. Armor, 2. Weapon, 3. Accessory, 4. Item, 5. Exit]\n")    
                    
                 
                
            break
            

        elif inventory_choice == "2":
            break    
        else:
            print("\n[Please enter correct input; 1. Change equipment, 2. Go back]")
        

def enemy_level_multiplier(player_level):
    multiplier = 1
    multiplier *= (1.25**(player_level-1))
    return multiplier
    


#----------------------------------------------------------FIGHT-METHODS---------------------------------------------------------------

def fight(chosen_description):
    global game_over
    #FIGHT

    chosen_enemy = rand.choice(chosen_description.possible_enemies)

    E.create_enemy(chosen_enemy)

    print_slow(E.fight_begin_description(chosen_enemy), TEST)

    chosen_enemy.max_hp *= enemy_level_multiplier(player.level)
    chosen_enemy.str *= enemy_level_multiplier(player.level)
    chosen_enemy.spd *= enemy_level_multiplier(player.level)
    chosen_enemy.exp_dropped *= enemy_level_multiplier(player.level)
    chosen_enemy.gold_dropped *= enemy_level_multiplier(player.level)

    chosen_enemy.max_hp = int(chosen_enemy.max_hp)
    chosen_enemy.str = int(chosen_enemy.str)
    chosen_enemy.spd = int(chosen_enemy.spd)
    chosen_enemy.exp_dropped = int(chosen_enemy.exp_dropped)
    chosen_enemy.gold_dropped = int(chosen_enemy.gold_dropped)

    
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


        temp_player_attack_list = copy.deepcopy(P.ATTACK_MOVE_LIST)

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

    1: {attack_1.name}
    2: {attack_2.name}
    3: {attack_3.name}
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

        #HÄR SKER SJÄLVA ATTACKERNA----------------------------------------------------------------------------------
        if first_attack_move == "player":
            
            player_attack(chosen_attack, chosen_enemy, player.equipped_weapon.effect, "Enemy")

            if player.equipped_weapon.effect == "quickstep" and rand.randint(1, 4) == 1:
                print_slow(I.baronen_knife_effect_description(), TEST)
                bonus_damage = rand.randint(10, 30)
                print_slow(f"\n    - You dealt {bonus_damage} damage!", TEST)
                chosen_enemy.hp -= bonus_damage
                if chosen_enemy.hp <= 0:
                    break
            else:                   
                if chosen_enemy.hp > 0:
                    enemy_attack(chosen_enemy, "Enemy")
                else:
                    break

        elif first_attack_move == "enemy":
            print_slow(f"\nEnemy struck first!", TEST)

            enemy_attack(chosen_enemy, "Enemy")

            if player.hp > 0:
                player_attack(chosen_attack, chosen_enemy, player.equipped_weapon.effect, "Enemy")
                if chosen_enemy.hp <= 0:
                    break
            else:
                game_over = True
                break

        sleep(0.8)
        print("\n")

    if game_over != True:

        print_slow(f"\n\n{chosen_enemy.name} died!\n", TEST)

        player.gold += chosen_enemy.gold_dropped
        print_slow(f"\nThe enemy dropped {chosen_enemy.gold_dropped} gold!", TEST)

        player.exp += chosen_enemy.exp_dropped
        print_slow(f"\nYou gained {chosen_enemy.exp_dropped} exp!\n", TEST)

        loot("enemy drop")


def player_attack(chosen_attack, chosen_enemy, weapon_effect, enemy_name):
    player_damage = rand.randint(player.str - 5, player.str + 5)
    chosen_enemy.hp -= player_damage

    print_slow(P.attack_move_description(chosen_attack, player.name, player.equipped_weapon.name, chosen_enemy.name), TEST)

    print_slow(f"\n   - You dealt {player_damage} damage!", TEST)

    #EFFECTS
    if weapon_effect == "explosion":
        extra_damage = rand.randint(20, 30)
        print_slow(f"\n\nUsing the {player.equipped_weapon.name} to attack, the explosion from it was big enough to hurt you too!", 0.01)
        player.hp -= extra_damage
        print_slow(f"\n   - You took {extra_damage} damage!", 0.01)

    if chosen_enemy.hp > 0:
        print_slow(f"\n   - {enemy_name} health: {chosen_enemy.hp} / {chosen_enemy.max_hp}\n", TEST)
    else:
        print_slow(f"\n   - {enemy_name} health: 0 / {chosen_enemy.max_hp}\n", TEST)

def enemy_attack(chosen_enemy, enemy_name):
    global game_over

    enemy_damage = rand.randint(chosen_enemy.str -5 , chosen_enemy.str + 5)
    player.hp -= enemy_damage

    print_slow("\n" + E.enemy_attack_description(chosen_enemy, player.name), TEST)
    print_slow(f"\n   - {enemy_name} dealt {enemy_damage} damage!", TEST)
    if player.hp >= 0:
        print_slow(f"\n   - {player.name}'s health: {player.hp} / {player.max_hp}\n", TEST)
    else:
        print_slow(f"\n   - {player.name}'s health: 0 / {player.max_hp}\n", TEST)
        game_over = True

def bossfight_pococurante():
    global game_over
    print_slow(L.pococurante_description, 0.02)

    pygame.mixer.music.load('sounds/pococurante theme.mp3')
    pygame.mixer.music.play()

    print_slow(f"\nLord Pococurante, the dreadful art collector stands before you.", 0.1)
    sleep(PUNCTUATION_PAUSE_TIME)
    print(f'''
HP: {E.pococurante.hp} / {E.pococurante.max_hp}
STR: {E.pococurante.str}
SPD: {E.pococurante.spd}
    ''')

    sleep(2)

    while player.hp > 0 or E.pococurante.hp > 0:

            temp_player_attack_list = copy.deepcopy(P.ATTACK_MOVE_LIST)
            player_damage = rand.randint(player.str - 5, player.str + 5)
            enemy_damage = rand.randint(E.pococurante.str -5 , E.pococurante.str + 5)

            #VÄLJER VEM SOM FÅR ATTACKERA FÖRST
            first_attack_move = rand.choices(["player", "enemy", "player", "enemy"], weights=[player.spd, E.pococurante.spd, 140, 140], k=1).pop()

            attack_1 = rand.choice(temp_player_attack_list)
            temp_player_attack_list.remove(attack_1)
            attack_2 = rand.choice(temp_player_attack_list)
            temp_player_attack_list.remove(attack_2)
            attack_3 = rand.choice(temp_player_attack_list)

            print_slow("\nWhat attack will you use?", TEST)
            print(f'''

    1: {attack_1.name}
    2: {attack_2.name}
    3: {attack_3.name}
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

            E.pococurante.hp -= player_damage
            player.hp -= enemy_damage

            if first_attack_move == "player":
                player_attack(chosen_attack, E.pococurante, player.equipped_weapon.effect, "Pococurante")

                if E.pococurante.hp > 0:
                    print_slow(E.pococurante_voice_lines(),TEST)
                    enemy_attack(E.pococurante, "Pococurante")
                else:
                    break
                    
            elif first_attack_move == "enemy":
                print_slow(f"\nEnemy struck first!", TEST)

                print_slow(E.pococurante_voice_lines(),TEST)
                enemy_attack(E.pococurante, "Pococurante")

                if player.hp > 0:
                    player_attack(chosen_attack, E.pococurante, player.equipped_weapon.effect, "Pococurante")
                    if E.pococurante.hp <= 0:
                        break
                    else:
                        game_over = True
                        break
                else:
                    print_slow(f"\n   - {player.name}'s health: 0 / {player.max_hp}", TEST)
                    game_over = True
                    break

    sleep(1)
    print("\n")

    if game_over == False:
        print_slow('''\n"Now I see... Optimism.. Positivity.. Maybe... All of the art wasn't bad...."''', 0.1)
        sleep(PUNCTUATION_PAUSE_TIME*1.5)

        print_slow(f"\n\nYou have slayn {E.pococurante.name}.\n", 0.04)
        sleep(PUNCTUATION_PAUSE_TIME*1.5)

        player.gold += E.pococurante.gold_dropped
        print_slow(f"\nPococurante dropped {E.pococurante.gold_dropped} gold!", TEST)

        player.exp += E.pococurante.exp_dropped
        print_slow(f"\nYou gained {E.pococurante.exp_dropped} exp!", TEST)

        player.inventory.append(I.pococurante_cane)
        print_slow(f"\nYou walked up to Pococurante and took {I.pococurante_cane.name}\n", TEST)


def bossfight_baronen():
    global game_over
    print_slow(L.baronen_description, 0.02)

    print_slow(f"\nBaronen, the mad brother, acrimony of love, baron of Thunder-ten-tronckh, towers over you.", 0.1)
    sleep(PUNCTUATION_PAUSE_TIME)
    print(f'''
HP: {E.baronen.hp} / {E.baronen.max_hp}
STR: {E.baronen.str}
SPD: {E.baronen.spd}
    ''')

    sleep(2)

    player.hp /= 1.5
    int(player.hp)

    player.max_hp -= player.equipped_weapon.max_hp_bonus
    player.hp -= player.equipped_weapon.max_hp_bonus
    player.str -= player.equipped_weapon.str_bonus
    player.spd -= player.equipped_weapon.spd_bonus

    player.equipped_weapon = I.baronen_knife

    player.max_hp += player.equipped_weapon.max_hp_bonus
    player.hp += player.equipped_weapon.max_hp_bonus
    player.str += player.equipped_weapon.str_bonus
    player.spd += player.equipped_weapon.spd_bonus

    while player.hp > 0 or E.baronen.hp > 0:

            temp_player_attack_list = copy.deepcopy(P.ATTACK_MOVE_LIST)
            player_damage = rand.randint(player.str - 5, player.str + 5)
            enemy_damage = rand.randint(E.baronen.str -5 , E.baronen.str + 5)

            #VÄLJER VEM SOM FÅR ATTACKERA FÖRST
            first_attack_move = rand.choices(["player", "enemy", "player", "enemy"], weights=[player.spd, E.baronen.spd, 140, 140], k=1).pop()

            attack_1 = rand.choice(temp_player_attack_list)
            temp_player_attack_list.remove(attack_1)
            attack_2 = rand.choice(temp_player_attack_list)
            temp_player_attack_list.remove(attack_2)
            attack_3 = rand.choice(temp_player_attack_list)

            print_slow("\nWhat attack will you use?", TEST)
            print(f'''

    1: {attack_1.name}
    2: {attack_2.name}
    3: {attack_3.name}
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

            E.baronen.hp -= player_damage
            player.hp -= enemy_damage

            if first_attack_move == "player":
                print_slow(P.attack_move_description(chosen_attack, player.name, player.equipped_weapon.name, E.baronen.name), TEST)

                print_slow(f"\n   - You dealt {player_damage} damage!", TEST)
                if E.baronen.hp > 0:
                    print_slow(f"\n   - Baronen health: {E.baronen.hp} / {E.baronen.max_hp}", TEST)
                else:
                    print_slow(f"\n   - Baronen health: 0 / {E.baronen.max_hp}", TEST)
                    break
                
                print_slow("\n" + E.baronen_voice_lines(), TEST)
                print_slow(E.baronen_attacks(), TEST)
                print_slow(f"\n   - Baronen dealt {enemy_damage} damage!", TEST)
                if player.hp >= 0:
                    print_slow(f"\n   - {player.name}'s health: {player.hp} / {player.max_hp}", TEST)
                else:
                    print_slow(f"\n   - {player.name}'s health: 0 / {player.max_hp}", TEST)
                    game_over = True
                    break
            elif first_attack_move == "enemy":
                print_slow(f"Baronen struck first!", TEST)
                print_slow("\n" + E.baronen_voice_lines(), TEST)
                print_slow(E.baronen_attacks(), TEST)
                print_slow(f"\n   - Baronen dealt {enemy_damage} damage!", TEST)
                
                if player.hp >= 0:
                    print_slow(f"\n   - {player.name}'s health: {player.hp} / {player.max_hp}", TEST)

                    print_slow("\n" + P.attack_move_description(chosen_attack, player.name, player.equipped_weapon.name, E.baronen.name), TEST)
                    
                    print_slow(f"\n   - You dealt {player_damage} damage!", TEST)
                    if E.baronen.hp > 0:
                        print_slow(f"\n   - Baronen health: {E.baronen.hp} / {E.baronen.max_hp}", TEST)
                    else:
                        print_slow(f"\n   - Baronen health: 0 / {E.baronen.max_hp}.", TEST)
                        break
                        
                else:
                    print_slow(f"\n   - {player.name}'s health: 0 / {player.max_hp}", TEST)
                    game_over = True
                    break


    sleep(1)
    print("\n")

    if game_over == False:
        print_slow('''\n"Just.. treat.. treat her good... please..."''', 0.1)
        sleep(PUNCTUATION_PAUSE_TIME*1.5)

        print_slow(f"\n\nYou have slayn {E.baronen.name}.\n", 0.04)
        sleep(PUNCTUATION_PAUSE_TIME*1.5)

        player.gold += E.baronen.gold_dropped
        print_slow(f"\nBaronen dropped {E.baronen.gold_dropped} gold!", TEST)

        player.exp += E.baronen.exp_dropped
        print_slow(f"\nYou gained {E.baronen.exp_dropped} exp!", TEST)

        print_slow(f"\nYou held onto {I.baronen_knife.name}.\n", TEST)

        player.inventory.append(I.baronen_greatsword)
        print_slow(f"\nFrom the corpse of Baronen, you took {I.baronen_greatsword.name}.\n", TEST)


def bossfight_kunigunda():
    print_slow('''

    ''', TEST)
    



#--------------------------------------------------------------------------------------------------------------------------------------

def print_slow(str, write_speed):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(write_speed)
        if letter == "." or letter == "?" or letter == "!":
            sleep(PUNCTUATION_PAUSE_TIME)
        elif letter == ",":
            sleep(COMMA_PAUSE_TIME)
        elif letter == ";":
            sleep(SEMICOLON_PAUSE_TIME)

def loot(type):
    if type == "enemy drop":
        weapon_drop_chance = rand.randint(1, 1)
        if weapon_drop_chance == 1:
            print_slow("\nThe enemy dropped an item!", TEST)

            dropped_weapon_index = rand.choices(I.item_list, weights=I.item_rarity_list, k=1).pop()
            dropped_weapon = I.create_item(dropped_weapon_index)
            print_slow(f"\nYou picked up {dropped_weapon.name}.\n", TEST)
            player.inventory.append(dropped_weapon)
             

def trap(location):
    global game_over
    trap_type = rand.choice(["gold", "damage"])
    gold_lost = rand.randint(20, 80)

    if player.gold == 0 or player.gold - gold_lost <= 0 or player.curse_of_eldorado > 0:
        trap_type = "damage"

    print_slow(L.trap_description(player.name, location.name, trap_type), TEST)

    damage = rand.randint(15, 45)
    player.hp -= damage

    if trap_type == "gold":
        if player.gold == 0:
            print_slow("You were broke asf anyways so you didn't lose anything!", TEST)
        elif player.gold - gold_lost <= 0:
            player.gold = 0
            print_slow("You lost the rest of your gold!", TEST)
        else:
            player.gold -= gold_lost
            print_slow(f"   - You lost {gold_lost} gold!  Gold: {player.gold}", TEST)

    if player.hp >= 0:
        print_slow(f"   - You took {damage} damage!  HP: {player.hp} / {player.max_hp}\n", TEST)
    else:
        print_slow(f"   - You took {damage} damage!  HP: 0 / {player.max_hp}\n", TEST)
        game_over = True
    
    sleep(0.8)


    

def intro():
    print(A.start)

def game_summary():
    
    sleep(1)
    print_slow("\nGAME SUMMARY:", 0.05)
    sleep(0.5)

    print(f'''
PLAYER CHARARACTER: {player.name}
LEVEL: {player.level}

Max HP: {player.max_hp}
STR: {player.str}
SPD: {player.spd}

WEAPON: {player.equipped_weapon.name}
ARMOR: {player.equipped_armor.name}
ACCESSORY: {player.equipped_accessory.name}

COUNTRIES TRAVERSED: {total_turns}
    ''')

# player.level.limit = required EXP to level up, base value = 500 EXP
def level_up():
    player.level += 1
    player.level_limit += (player.level_limit*0.5)
    player.max_hp = int(player.max_hp*1.25)
    player.hp = int(player.hp*1.25)
    player.str = int(player.str*1.25)
    player.spd = int(player.spd*1.25)
    player.exp = 0

    print_slow("\nYou leveled up!", TEST)
    print_slow(f"\n{player.name} level: {player.level-1} --> {player.level}\n", TEST)
    print_slow(f"\nYou feel your strength increase!\n", TEST)

#Cacambo
cacambo = P.Player()
cacambo.name = "Cacambo"
cacambo.max_hp = 800
cacambo.str = 40000
cacambo.spd = 20000
cacambo.gold = 40000#40

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
pangloss.max_hp = 1000#300
pangloss.str = 20
pangloss.spd = 1#5
pangloss.gold = 1

#------------------------------------------------------HÄR KÖRS HUVUDDELEN AV PROGRAMMET-------------------------------------------------------------------------------------------------------

print_slow("Choose your character!", 0.01)
sleep(1)

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
        pygame.mixer.Sound.play(UI_sfx)

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
        player.exp = 0
        player.hp = player.max_hp
        player.inventory = []

        player.inventory.append(I.create_item("health potion"))
        player.inventory.append(I.create_item("roids"))

    except:
        print("\n[Please enter a correct input; 1. Cacambo, 2. Candide, 3. Pangloss]")
    else:
        break



intro()


# # TEMPORÄR TILLÄG AV ITEMS
# for i in range(10):
#     weapon_choice = rand.choice(I.item_list)
#     player.inventory.append(I.create_item(weapon_choice))

player.inventory.append(I.baronen_knife)

#DEN STÖRRE SPELLOOPEN----------------------------------------------------------------
while True:

    travel()

    if len(player.inventory) != 0:
        if player.exp >= player.level_limit:
            level_up()

    if game_over == True:
        print_slow("\n\n\n\n[You died]", 0.1)
        break
    elif good_ending == True:
        print_slow("\n\n\n\n[Good ending]", 0.1)
        break

game_summary()

input()