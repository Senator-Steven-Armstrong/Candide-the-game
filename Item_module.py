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

#DEFAULT WEAPON ÄR FISTS:
fists = Item()
fists.type = "weapon"
fists.name = "Fists"

#DEFAULT ARMOR ÄR NONE
empty_armor = Item()
empty_armor.type = "armor"
empty_armor.name = "None"

item_list=["dagger", "bow", "sword", "explosive", "ultra_greatsword", "crusader helm", "leather boots"]
item_rarity_list = [100, 100, 100, 60, 20, 100, 100]



def create_item(choice):


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
        ultra_greatsword.cost = rand.randint(420,480) 
        return ultra_greatsword
    
    #ARMOR-----------------------------------------------------
    elif choice == "crusader helm":
        crusader_helm = Item()
        crusader_helm.type = "armor"
        crusader_helm.name = "Crusader helm"
        crusader_helm.max_hp_bonus = rand.randint(50,70)
        crusader_helm.cost = rand.randint(70, 80)
        return crusader_helm
    elif choice == "Leather boots":
        boots = Item()
        boots.type = "armor"
        boots.name = "Leather boots"
        boots.max_hp_bonus = rand.randint(40, 50)
        boots.spd_bonus = rand.randint(3, 6)
        boots.cost = rand.randint(60, 70)
        return boots



    


#HÄR LÄGGS ALLT TILL I DE OLIKA LISTORNA





resource_string = ["iron", "guldbagge", "wood", "stone", "bread", "meat"]
    