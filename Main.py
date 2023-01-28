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
import logbook as Log

pygame.mixer.init()



#SOUND EFFECTS
start_music = 'sounds/pococurante theme.mp3'
battle_music = ['sounds/battle_theme_jojo.mp3', 'sounds/battle_theme_rude_buster.mp3']
idle_music = ['sounds/idle_music_1.mp3']

print_sfx = pygame.mixer.Sound('sounds/print_sfx_2.mp3')
UI_sfx = pygame.mixer.Sound('sounds/UI sound effect.mp3')
healing_sfx = pygame.mixer.Sound('sounds/healingpotion.mp3')

TEST = 0.02
PUNCTUATION_PAUSE_TIME = 0.4
COMMA_PAUSE_TIME = 0.15
SEMICOLON_PAUSE_TIME = 0.6

ELDORADO_MONEY_BONUS = 9999999999

current_location = ""
total_turns = 0
good_ending = False
true_ending = False
bad_ending = False

game_over = False

def start():

    print("\n\n\n")
    sleep(0.6)

    is_exiting = False
    for line in A.start:
        print(line)
        sleep(0.08)
    sleep(0.6)

    while is_exiting == False:
        print('''
1. Start
2. Start (No intro cutscene)
3. Quick tutorial
4. Exit
''')

        while True:
            start_choice = input("Choice: ")
            if start_choice == "1":
                print(A.castle)
                sleep(0.2)
                print_slow(L.intro_description, TEST)
                is_exiting = True
                break
            elif start_choice == "2":
                is_exiting = True
                break
            elif start_choice == "3":
                #Tutorial
                print_slow(L.tutorial_description, TEST)
                sleep(0.8)
                break
            elif start_choice == "4":
                quit()
            else:
                print("\n[Enter correct input by pressing either 1, 2, 3, or 4. Then press enter]\n")
    

def return_location_rarity(temporary_locations, total_turns):
    rarity_list = []
    for location in temporary_locations:
        if total_turns == 0 and location.name == L.eldorado.name:
            rarity_list.append(0)
        elif total_turns == 0 and location.name == L.shop.name:
            rarity_list.append(0)
        else:
            rarity_list.append(location.rarity)
    return rarity_list



def travel():
    #HÄR GÖRS EN RESA, FUNKTIONEN SKA VÄLJA ETT STÄLLE OCH VÄLJA EN HÄNDELSE I DET STÄLLET,
    #VI MÅSTE RÄKNA HUR MÅNGA RUM MAN HAR VARIT I
    global current_location
    global total_turns
    global game_over
    global good_ending

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
            elif total_turns == 7:
                bossfight_baronen()
                break
            elif total_turns == 10:
                bossfight_kunigunda()
                break
            else:

                print_slow("Where would you like to travel?", TEST)
                sleep(0.5)

                temporary_locations = copy.deepcopy(L.locations)

                location1 = rand.choices(temporary_locations, weights=return_location_rarity(temporary_locations, total_turns), k=1).pop()  
                temporary_locations.remove(location1)
                location2 = rand.choices(temporary_locations, weights=return_location_rarity(temporary_locations, total_turns), k=1).pop()
                temporary_locations.remove(location2)
                location3 = rand.choices(temporary_locations, weights=return_location_rarity(temporary_locations, total_turns), k=1).pop()

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
                trap_chance = rand.randint(1, 100)
                if trap_chance == 1 and current_location != "Eldorado":
                    trap(current_location)
                    
                if game_over == False:  

                    #HÄR SKRIVS BESKRIVNINGEN AV SIN RESA UT
                    if player == pangloss and chosen_description == L.lissabon1:
                
                        pygame.mixer.music.play(L.lissabon_special.music)
                        print_slow(L.lissabon_special.description, TEST)
                    else:
                        print_slow(chosen_description.description, TEST)

                


                    if current_location.name == L.eldorado.name:
                        #ELDORADO----------------------------------------------------------------------------------------------------------
                        
                        print_slow("\n                     Stay                  Leave\n", 0.1)
                        
                        print_slow("\nChoice: ", 0.18)

                        while True:
                            eldorado_ending_choice = input()

                            if eldorado_ending_choice.lower() == "stay":
                                pygame.mixer.music.load('sounds/ruinds.mp3')
                                pygame.mixer.music.play()
                                print_slow(L.eldorado_stay_description, TEST)

                                good_ending = True
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
                    elif current_location.name == L.shop.name:

                        print(A.shop)

                        shop_items = copy.deepcopy(I.item_list)
                        temp_rarity_list = copy.deepcopy(I.item_rarity_list)
                        available_shop_items = []

                        shop_item_indicator_1 = rand.choices(shop_items, temp_rarity_list, k=1).pop()
                        shop_item_index_1 = shop_items.index(shop_item_indicator_1)
                        temp_rarity_list.pop(shop_item_index_1)
                        shop_items.remove(shop_item_indicator_1)
                        shop_item_1 = I.create_item(shop_item_indicator_1)
                        available_shop_items.append(shop_item_1)

                        shop_item_indicator_2 = rand.choices(shop_items, temp_rarity_list, k=1).pop()
                        shop_item_index_2 = shop_items.index(shop_item_indicator_2)
                        temp_rarity_list.pop(shop_item_index_2)
                        shop_items.remove(shop_item_indicator_2)
                        shop_item_2 = I.create_item(shop_item_indicator_2)
                        available_shop_items.append(shop_item_2)

                        shop_item_indicator_3 = rand.choices(shop_items, temp_rarity_list, k=1).pop()
                        shop_item_index_3 = shop_items.index(shop_item_indicator_3)
                        temp_rarity_list.pop(shop_item_index_3)
                        shop_items.remove(shop_item_indicator_3)
                        shop_item_3 = I.create_item(shop_item_indicator_3)
                        available_shop_items.append(shop_item_3)
                        
                        shop_item_4 = I.create_item(rand.choice(I.healing_item_list))
                        available_shop_items.append(shop_item_4)
                        while True:
                            sleep(1)
                            print(f'''
Current gold: {player.gold}

Thee can purchaseth the following items:
''')
                            j = 1
                            for item in available_shop_items:
                                print(j, ". ", item.name, "; ", item.cost, " Gold", sep="")
                                if item.type == "healing":
                                    print(f"[Healed HP: {item.hp_bonus}]\n")
                                else:
                                    print(f"[HP: {item.max_hp_bonus} STR: {item.str_bonus} SPD: {item.spd_bonus}]\n")

                                if j == len(available_shop_items):
                                    print(j+1, " Leave shop", sep="")

                                j += 1
                            
                            

                            j = 1
                            while True:
                                while True:
                                    try:
                                        shop_input = int(input("\nChoice: "))
                                        pygame.mixer.Sound.play(UI_sfx)
                                    except:
                                        print("\n[Please enter a number]\n")
                                        continue
                                    else:
                                        break

                                
                                for item in available_shop_items:
                                    if shop_input == j:
                                        chosen_item = item
                                        break
                                    elif shop_input == len(available_shop_items) + 1:
                                        break
                                    elif shop_input < 1 and shop_input < len(available_shop_items):
                                        print("\n[Please enter correct input]")
                                        continue
                                    else:
                                        j += 1
                                        continue
                                break
                            
                            if shop_input == len(available_shop_items) + 1 and len(available_shop_items) == 4:
                                print_slow("\nThee no more brain than stone clotpole sandwich, nev'r cometh backeth!\nYou hastily leave the store.\n", TEST)
                                break
                            elif shop_input == len(available_shop_items) + 1 and len(available_shop_items) > 1:
                                print_slow("\nThanketh thee f'r being a custom'r at mine own st're, seeth thee again lief!\n", TEST)
                                break


                            if chosen_item.cost <= player.gold:
                                player.gold -= chosen_item.cost
                                player.inventory.append(chosen_item)
                                available_shop_items.remove(chosen_item)
                                print_slow(f"\nThanketh thee f'r purchasing {chosen_item.name}!", TEST)
                            else: 
                                print_slow("\nThee has't not enow wage! Buyeth something else shall ya, If't be true thee did get the wage f'r t.", TEST)
                                continue

                            if len(available_shop_items) == 0:
                                print_slow("\nThee hath bought mine own entire st'rage! I desire we meeteth again at which hour mine own stock is refilled!\n", TEST)
                                break
                            else:
                                print_slow(" Wouldst thee liketh to buyeth something m're?\n", TEST)





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
5. Open the Logbook
6. Exit inventory
''')    
            while has_equipped_item == False:

                item_change_choice = input("Choice: ")
                pygame.mixer.Sound.play(UI_sfx)

                if item_change_choice == "1":
                    #ÄNDRAR VAPEN-------------------------------------------------------------------------------------------------------
                    inventory_item_change("weapon", has_equipped_item)
                    break
                elif item_change_choice == "2":
                    #ÄNDRAR ARMOR----------------------------------------------------------------------------------------------------
                    inventory_item_change("armor", has_equipped_item)
                    break
                elif item_change_choice == "3":
                    #ÄNDRAR ACCESSORY----------------------------------------------------------------------------------------------------
                    inventory_item_change("accessory", has_equipped_item)
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
                                    pygame.mixer.Sound.play(healing_sfx)
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
                    Log.logbook_menu()
                    break

                elif item_change_choice == "6":
                    break
                else:
                    print("\n[Please enter correct input; 1. Armor, 2. Weapon, 3. Accessory, 4. Item, 5. Logbook, 6. Exit]\n")    
                    
                 
                
            break
            

        elif inventory_choice == "2":
            break    
        else:
            print("\n[Please enter correct input; 1. Change equipment, 2. Go back]")
        

def inventory_item_change(item_type, has_equipped_item):
    #ÄNDRAR VAPEN-------------------------------------------------------------------------------------------------------

    temp_inventory = []
    for i in player.inventory:
        if i.type == item_type:
            temp_inventory.append(i)

    if item_type == "weapon":
        player_equipped_item = player.equipped_weapon
    elif item_type == "armor":
        player_equipped_item = player.equipped_armor
    elif item_type == "accessory":
        player_equipped_item = player.equipped_accessory

    if len(temp_inventory) > 0:

        print(f"\nCurrent weapon: {player_equipped_item.name}")

        print_slow(f"\nWhat {item_type} would you like to equip?\n", TEST)

        #HÄR PRINTAS LISTAN MED ALLA VAPEN I ENS INVENTORY
        j = 1
        for i in temp_inventory:
            if i != player_equipped_item:
                if i.name == "None":
                    i.name = f"Unequip {item_type}"
                print(j, ". ", i.name, f"\n[HP: {i.max_hp_bonus}, STR: {i.str_bonus}, SPD: {i.spd_bonus}]\n",sep='')
                j += 1
            if j-1 == len(temp_inventory):
                print(j, ". Change nothing / Exit inventory", sep='')
            
        while has_equipped_item == False:

            while True:
            
                try:
                    item_equip_choice = int(input("\nChoice: "))
                    pygame.mixer.Sound.play(UI_sfx)
                except:
                    print("[Please enter a number]")
                else:
                    break

            #HÄR KOLLAR DEN VILKET VAPEN MAN EQUIPAR
            if item_equip_choice == len(temp_inventory) + 1:
                has_equipped_item = True
                break
            else:
                for i in range(len(temp_inventory)):
                    
                    if item_equip_choice == i + 1:
                        #HÄR TAS GAMLA WEAPONSTATS BORT
                        player.max_hp -= player_equipped_item.max_hp_bonus
                        player.hp -= player_equipped_item.max_hp_bonus
                        player.str -= player_equipped_item.str_bonus
                        player.spd -= player_equipped_item.spd_bonus
                        player.inventory.append(player_equipped_item)

                        player_equipped_item = temp_inventory[i]
                        player.inventory.remove(player_equipped_item)

                        if item_type == "weapon":
                            player.equipped_weapon = player_equipped_item
                        elif item_type == "armor":
                            player.equipped_armor = player_equipped_item
                        elif item_type == "accessory":
                            player.equipped_accessory = player_equipped_item

                        if player_equipped_item == I.fists:
                            print_slow("You holstered your weapon.\n", TEST)
                        elif player_equipped_item == I.empty_armor:
                            print_slow("You took off your armor.\n", TEST)
                        elif player_equipped_item == I.empty_accessory:
                            print_slow("You put your accessory back in your backpack.\n", TEST)
                        else:
                            print_slow(f"\nYou equipped {player_equipped_item.name}.\n", TEST)
                                                        
                            
                        #HÄR LÄGGS NYA  STATS PÅ NÄR MAN HAR EQUIPAT ETT VAPEN
                        player.max_hp += player_equipped_item.max_hp_bonus
                        player.hp += player_equipped_item.max_hp_bonus
                        player.str += player_equipped_item.str_bonus
                        player.spd += player_equipped_item.spd_bonus

                        has_equipped_item = True
                        break
                    elif i == len(temp_inventory) - 1:
                        print("[Please choose an item to equip, or exit inventory]")
                        

    else:
        print_slow(f"\nNo {item_type} in inventory to equip.\n", TEST)


def enemy_level_multiplier(player_level):
    multiplier = 1
    multiplier *= (1.25**(player_level-1))
    return multiplier
    


#----------------------------------------------------------FIGHT-METHODS---------------------------------------------------------------

def fight(chosen_description):
    global game_over
    #FIGHT

    pygame.mixer.music.load(rand.choice(battle_music))
    pygame.mixer.music.play(-1, 0, 0)

    chosen_enemy_indicator = rand.choice(chosen_description.possible_enemies)

    chosen_enemy = E.create_enemy(chosen_enemy_indicator)

    print_slow(E.fight_begin_description(chosen_enemy.name), TEST)

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

    combat_sequence(chosen_enemy, "Enemy")

    sleep(0.8)
    print("\n")

    if game_over != True:

        print_slow(f"\n\n{chosen_enemy.name} died!\n", TEST)

        player.gold += chosen_enemy.gold_dropped
        print_slow(f"\nThe enemy dropped {chosen_enemy.gold_dropped} gold!", TEST)

        player.exp += chosen_enemy.exp_dropped
        print_slow(f"\nYou gained {chosen_enemy.exp_dropped} exp!\n", TEST)

        loot("enemy drop")

def combat_sequence(chosen_enemy, enemy_name):
    global game_over

    while player.hp > 0 or chosen_enemy.hp > 0:


        temp_player_attack_list = copy.deepcopy(P.ATTACK_MOVE_LIST)

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
            
            player_attack(chosen_attack, chosen_enemy, player.equipped_weapon.effect, enemy_name)

            if player.equipped_weapon.effect == "quickstep" and rand.randint(1, 4) == 1:
                print_slow(I.baronen_knife_effect_description(), TEST)
                bonus_damage = rand.randint(10, 30)
                print_slow(f"\n    - You dealt {bonus_damage} damage!", TEST)
                chosen_enemy.hp -= bonus_damage
                if chosen_enemy.hp <= 0:
                    break
            else:                   
                if chosen_enemy.hp > 0:
                    print_boss_voice_lines(chosen_enemy)
                    enemy_attack(chosen_enemy, enemy_name)
                else:
                    break

        elif first_attack_move == "enemy":
            print_slow(f"\nEnemy struck first!", TEST)

            print_boss_voice_lines(chosen_enemy)
            enemy_attack(chosen_enemy, enemy_name)

            if player.hp > 0:
                player_attack(chosen_attack, chosen_enemy, player.equipped_weapon.effect, enemy_name)
                if chosen_enemy.hp <= 0:
                    break
            else:
                game_over = True
                break

        sleep(0.8)
        print("\n")

def print_boss_voice_lines(enemy):
    if enemy == E.pococurante:
        print_slow(E.pococurante_voice_lines(), TEST)
    elif enemy == E.baronen:
        print_slow(E.baronen_voice_lines(), TEST)
    elif enemy == E.kunigunda:
        print_slow(E.kunigunda_voice_lines_phase_1(), TEST)
    elif enemy == E.kunigunda_2:
        print_slow(E.kunigunda_voice_lines_phase_2(), TEST)
    


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
        print_slow(f"\n   - You dealt {extra_damage} damage!\n", 0.01)

    if chosen_enemy.hp > 0:
        print_slow(f"\n   - {enemy_name} health: {chosen_enemy.hp} / {chosen_enemy.max_hp}\n", TEST)
    else:
        print_slow(f"\n   - {enemy_name} health: 0 / {chosen_enemy.max_hp}\n", TEST)

def enemy_attack(chosen_enemy, enemy_name):
    global game_over

    enemy_damage = rand.randint(chosen_enemy.str -5 , chosen_enemy.str + 5)
    player.hp -= enemy_damage

    if chosen_enemy == E.pococurante:
        print_slow(E.pococurante_attacks(), TEST)
    elif chosen_enemy == E.baronen:
        print_slow(E.baronen_attacks(), TEST)
    elif chosen_enemy == E.kunigunda:
        print_slow(E.kunigunda_attacks_phase_1(), TEST)
    elif chosen_enemy == E.kunigunda_2:
        print_slow(E.kunigunda_attacks_phase_2(), TEST)
    else:
        print_slow("\n" + E.enemy_attack_description(chosen_enemy, player.name), TEST)
    print_slow(f"\n   - {enemy_name} dealt {enemy_damage} damage!", TEST)
    if player.hp >= 0:
        print_slow(f"\n   - {player.name}'s health: {player.hp} / {player.max_hp}\n", TEST)
    else:
        print_slow(f"\n   - {player.name}'s health: 0 / {player.max_hp}\n", TEST)
        game_over = True

def bossfight_pococurante():
    global game_over
    global total_turns
    pygame.mixer.music.stop()
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

    combat_sequence(E.pococurante, "Pococurante")

    if player.hp <= 0:
        game_over = True
    else:
        sleep(1)
        print("\n")

        pygame.mixer.music.stop()

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
            print_slow(f"\nYou walked up to Pococurante's body and took '{I.pococurante_cane.name}'.\n", TEST)

    total_turns += 1


def bossfight_baronen():
    global game_over
    global total_turns
    pygame.mixer.music.stop()
    print_slow(L.baronen_description, 0.02)

    pygame.mixer.music.load('sounds/baronen_theme.mp3')
    pygame.mixer.music.play()

    print_slow(f"\nBaronen, the mad brother, acrimony of love, baron of Thunder-ten-tronckh, towers over you.", 0.1)
    sleep(PUNCTUATION_PAUSE_TIME)
    print(f'''
HP: {E.baronen.hp} / {E.baronen.max_hp}
STR: {E.baronen.str}
SPD: {E.baronen.spd}
    ''')

    sleep(2)

    #TAR BORT HP OCH VAPEN PÅ GRUND AV VAD SOM HÄNDER I STORYN
    player.hp /= 1.4
    player.hp = round(player.hp)

    player.max_hp -= player.equipped_weapon.max_hp_bonus
    player.hp -= player.equipped_weapon.max_hp_bonus
    player.str -= player.equipped_weapon.str_bonus
    player.spd -= player.equipped_weapon.spd_bonus

    player.equipped_weapon = I.baronen_knife

    player.max_hp += player.equipped_weapon.max_hp_bonus
    player.hp += player.equipped_weapon.max_hp_bonus
    player.str += player.equipped_weapon.str_bonus
    player.spd += player.equipped_weapon.spd_bonus

    combat_sequence(E.baronen, "Baronen")

    if player.hp <= 0:
        game_over = True
    else:

        sleep(1)
        print("\n")

        pygame.mixer.music.stop()

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

            total_turns += 1

def bossfight_kunigunda():
    global game_over
    global true_ending
    global bad_ending

    pygame.mixer.music.stop()

    #INTRO------------------------------------------------------------------------------
    # print_slow(L.kunigunda_description_intro, TEST)
    print_slow("\n                      ", 0.001)
    print_slow("Accept", 0.4)
    print_slow("                        ", 0.001)
    print_slow("Refuse", 0.4)
    sleep(1)


    while True:
        marriage_choice = input("\n\n\nChoice: ")
        if marriage_choice.lower() == "accept":
            #TRUE ENDING------------------------------------------------------------------------------------
            pygame.mixer.music.load('sounds/true ending.mp3')
            pygame.mixer.music.play()
            print_slow(L.kunigunda_description_accept + "\n\n\n", TEST)
            print_slow("This is truly, the truest of all possible worlds.", 0.2)

            game_over = True
            true_ending = True
            break
        elif marriage_choice.lower() == "refuse":
            #BAD ENDING - BOSS FIGHT--------------------------------    ----------------------------------------

            pygame.mixer.music.load('sounds/kunigunda theme.mp3')
            pygame.mixer.music.play(-1, 0, 0)

            print_slow(L.kunigunda_description_refuse + "\n\n\n", TEST)

            print_slow(f"\nYour love ", 0.1)
            sleep(1)
            print_slow(f"Kunigunda", 0.2)
            sleep(0.9)
            print_slow(f" stands before you.", 0.1)
            sleep(PUNCTUATION_PAUSE_TIME)
            print(f'''
HP: {E.kunigunda.hp} / {E.kunigunda.max_hp}
STR: {E.kunigunda.str}
SPD: {E.kunigunda.spd}
            ''')

            sleep(2)

            combat_sequence(E.kunigunda, "Kunigunda")

            if player.hp <= 0:
                game_over = True
                break
            else:
                print("\n")
                pygame.mixer.music.stop()
                print_slow(L.kunigunda_description_revive,TEST)

                pygame.mixer.music.load('sounds/kunigunda_second_phase.mp3')
                pygame.mixer.music.play(-1, 0, 0)

                print(f"\n\n\nKunigunda HP: 0 / {E.kunigunda.max_hp}")
                sleep(3.6)

                for i in range(E.kunigunda_2.max_hp):
                    sleep(0.008)
                    E.kunigunda_2.hp += 1
                    print(f"Kunigunda HP: {E.kunigunda_2.hp} / {E.kunigunda_2.max_hp}")
                    i+=1

                sleep(1)
                print_slow("\n\n??? remains.", 0.3)

                sleep(0.8)
                print(A.entity)

                sleep(1)
                print(f'''

{E.kunigunda_2.name} stats:

HP: {E.kunigunda_2.hp} / {E.kunigunda_2.max_hp}
STR: {E.kunigunda_2.str}
SPD: {E.kunigunda_2.spd}
                ''')

                sleep(2)

                combat_sequence(E.kunigunda_2, "???")

                if player.hp <= 0:
                    game_over = True
                    break
                else:
                    

                    pygame.mixer.music.load('sounds/kunigunda death.mp3')
                    pygame.mixer.music.play()

                    print_slow(L.kunigunda_description_death, TEST)
                    game_over = True
                    bad_ending = True

                    break
        else:
            print_slow("\n\nMake your choice.", 0.25)
    
#--------------------------------------------------------------------------------------------------------------------------------------

def print_slow(str, write_speed):
    global print_sfx
    sound_play = 1
    sound_speed = 3

    if write_speed < 0.001:
        sound_speed = 30
    elif write_speed < 0.005:
        sound_speed = 5
    elif write_speed < 0.02:
        sound_speed = 3
    elif write_speed < 0.08:
        sound_speed = 2 
    else:
        sound_speed = 1

    for letter in str:
        if sound_play % sound_speed == 0:
            pygame.mixer.Sound.play(print_sfx)
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(write_speed)
        if letter == "." or letter == "?" or letter == "!":
            sleep(PUNCTUATION_PAUSE_TIME)
        elif letter == ",":
            sleep(COMMA_PAUSE_TIME)
        elif letter == ";":
            sleep(SEMICOLON_PAUSE_TIME)
        sound_play += 1


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

    print_slow(L.trap_description(player.name, location.name, trap_type), TEST)

    damage = rand.randint(15, 45)
    player.hp -= damage

    if trap_type == "gold":
        if player.gold == 0:
            print_slow("\nYou were broke asf anyways so you didn't lose anything!", TEST)
        elif player.gold - gold_lost <= 0:
            player.gold = 0
            print_slow("\nYou lost the rest of your gold!", TEST)
        else:
            player.gold -= gold_lost
            print_slow(f"   - You lost {gold_lost} gold!  Gold: {player.gold}", TEST)

    if player.hp >= 0:
        print_slow(f"   - You took {damage} damage!  HP: {player.hp} / {player.max_hp}\n", TEST)
    else:
        print_slow(f"   - You took {damage} damage!  HP: 0 / {player.max_hp}\n", TEST)
        game_over = True
    
    sleep(0.8)

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
cacambo.gold = 40000

#Candide
candide = P.Player()
candide.name = "Candide"
candide.max_hp = 600
candide.str = 35
candide.spd = 15
candide.gold = 10

#Pangloss
pangloss = P.Player()
pangloss.name = "Pangloss"
pangloss.max_hp = 450
pangloss.str = 20
pangloss.spd = 5
pangloss.gold = 0

#------------------------------------------------------HÄR KÖRS HUVUDDELEN AV PROGRAMMET-------------------------------------------------------------------------------------------------------

start()

sleep(0.6)
print_slow("Who will be the one to deliver the kiss?", 0.01)
sleep(1)

print(f'''

1. Cacambo! [Difficulty easy]
    HP  :  {cacambo.max_hp}
    STR :  {cacambo.str}
    SPD :  {cacambo.spd}
    Gold:  {cacambo.gold}


2. Candide! [Difficulty medium]
    HP  :   {candide.max_hp}
    STR :   {candide.str}
    SPD :   {candide.spd}
    Gold:   {candide.gold}


3. Pangloss! [Difficulty hard] 
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
            print("\nYou chose Cacambo!\n")
            sleep(0.8)
            print("\n\n" + A.gigachad + "\n\n")
            sleep(0.8)
            print_slow("Cacambo sets out on the journey!", TEST)
        elif player_choice == 2: #CANDIDE
            player = candide
            player.name = candide.name
            player.hp = candide.hp
            player.str = candide.str
            player.spd = candide.spd
            player.gold = candide.gold
            player.exp = candide.exp
            print("\nYou chose Candide!\n")
            sleep(0.8)
            print("\n\n" + A.candide + "\n\n")
            sleep(0.8)
            print_slow("Candide sets out on the journey!", TEST)
        elif player_choice == 3: #PANGLOSS
            player = pangloss
            player.name = pangloss.name
            player.hp = pangloss.hp
            player.str = pangloss.str
            player.spd = pangloss.spd
            player.gold = pangloss.gold
            player.exp = pangloss.exp
            print("\nYou chose Pangloss! Good luck lol\n")
            sleep(0.8)
            print("\n\n" + A.pangloss + "\n\n")
            sleep(0.8)
            print_slow("Pangloss instantly contracted syphilis! He sets out on the journey anyways!", TEST)

        player.level = 1
        player.exp = 0
        player.hp = player.max_hp
        player.inventory = []

    except:
        print("\n[Please enter a correct input; 1. Cacambo, 2. Candide, 3. Pangloss]")
    else:
        break


#DEN STÖRRE SPELLOOPEN----------------------------------------------------------------
while True:

    pygame.mixer.music.load(rand.choice(idle_music))
    pygame.mixer.music.play(-1, 0, 5)
    travel()

    if len(player.inventory) != 0:
        if player.exp >= player.level_limit:
            level_up()

    if game_over == True:
        if good_ending == True:
            print_slow("\n\n\n\n[Good ending]", 0.1)
            break
        elif true_ending == True:
            print_slow("\n\n\n\n[True ending]", 0.1)
            break
        elif bad_ending == True:
            print_slow("\n\n\n\n[Bad ending]", 0.1)
            break
        else:
            pygame.mixer.music.load('sounds/you died.mp3')
            pygame.mixer.music.play()
            print_slow("\n\n\n\n[You died]", 0.1)
            break

game_summary()

input()