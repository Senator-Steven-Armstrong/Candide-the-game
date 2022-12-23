import random as rand

class Item:
    max_hp_bonus = 0
    hp_bonus = max_hp_bonus #KAN ÄNDRAS INDIVIDUELLT, DEFAULT ÄR ATT DE ÄR SAMMA
    str_bonus = 0
    spd_bonus = 0
    name = ""
    type = ""
    rarity = 100 #100 ÄR DEFAULT, DET KOMMER SKRIVAS IN I "weights" I rand.choices()
    cost = 0

#DEFAULT ÄR BARE FISTS:
fists = Item()
fists.type = "weapon"
fists.name = "Fists"

weapon_list=["dagger", "bow", "sword", "explosive", "ultra_greatsword"]
weapon_rarity_list = [100, 100, 100, 60, 20]

def create_weapon(choice):


    #WEAPONS------------------------------------------------
    if choice == "dagger":
        dagger = Item()
        dagger.type = "weapon"
        dagger.name = "Small dagger"
        dagger.str_bonus = rand.randint(3, 5)
        dagger.spd_bonus = rand.randint(5, 6)
        dagger.cost = rand.randint(50,66)
        return dagger
    elif choice == "bow":
        bow = Item()
        bow.type = "weapon"
        bow.name = "Longbow"
        bow.str_bonus = rand.randint(5,7)
        bow.spd_bonus = rand.randint(2,3)
        bow.cost = rand.randint(76,88)
        return bow
    elif choice == "sword":
        sword = Item()
        sword.type = "weapon"
        sword.name = "Shortsword"
        sword.str_bonus = rand.randint(8,9)
        sword.cost = rand.randint(88,100)
        return sword
    elif choice == "explosive":
        explosive = Item()
        explosive.type = "weapon"
        explosive.name = "Highly volatile explosive"
        explosive.str_bonus = rand.randint(19, 22)
        explosive.cost = rand.randint(210,230)
        return explosive
    elif choice == "ultra_greatsword":
        ultra_greatsword = Item()
        ultra_greatsword.type = "weapon"
        ultra_greatsword.name = "Voltaire's Ultra Greatsword"
        ultra_greatsword.str_bonus = rand.randint(25,30)
        ultra_greatsword.spd_bonus = rand.randint(-9, -6)
        ultra_greatsword.cost = rand.randint(420,460) 
        return ultra_greatsword


    


#HÄR LÄGGS ALLT TILL I DE OLIKA LISTORNA





resource_string = ["iron", "guldbagge", "wood", "stone", "bread", "meat"]
    