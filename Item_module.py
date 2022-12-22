import random as rand

class Item:
    hp_bonus = 0
    str_bonus = 0
    spd_bonus = 0
    name = ""
    type = ""
    effect = ""

#WEAPONS------------------------------------------------
dagger = Item()
dagger.type = "weapon"
dagger.name = "small dagger"
dagger.str_bonus = 4
dagger.spd_bonus = 5

bow = Item()
bow.type = "weapon"
bow.name = "longbow"
bow.str_bonus = 6
bow.spd_bonus = 3

sword = Item()
sword.type = "weapon"
sword.name = "shortsword"
sword.str_bonus = 8

explosive = Item()
explosive.type = "weapon"
explosive.name = "highly volatile explosive"
explosive.str_bonus = 20
explosive.effect = "explosion" #GÖR SKADA PÅ SIG SJÄLV






resource_string = ["iron", "guldbagge", "wood", "stone", "bread", "meat"]
weapon_string = ["bow", "dagger", "sword", "explosive"]
    