import random as rand

class Item:
    max_hp_bonus = 0
    hp_bonus = 0
    str_bonus = 0
    spd_bonus = 0
    name = ""
    type = ""
    rarity = 100 #100 ÄR DEFAULT, DET KOMMER SKRIVAS IN I "weights" I rand.choices()
    cost = 0

#WEAPONS------------------------------------------------
dagger = Item()
dagger.type = "weapon"
dagger.name = "Small dagger"
dagger.str_bonus = 4
dagger.spd_bonus = 5
dagger.cost = 60

bow = Item()
bow.type = "weapon"
bow.name = "Longbow"
bow.str_bonus = 6
bow.spd_bonus = 3
bow.cost = 65


sword = Item()
sword.type = "weapon"
sword.name = "Shortsword"
sword.str_bonus = 8
sword.cost = 70

explosive = Item()
explosive.type = "weapon"
explosive.name = "Highly volatile explosive"
explosive.str_bonus = 20
explosive.rarity = 70
explosive.cost = 120


item_list = [dagger, bow, sword, explosive]
item_name_list = []
weapon_list = []

#HÄR LÄGGS ALLT TILL I DE OLIKA LISTORNA
for i in item_list:
    item_name_list.append(i)
    if i.type == "weapon":
        weapon_list.append(i)




resource_string = ["iron", "guldbagge", "wood", "stone", "bread", "meat"]
    