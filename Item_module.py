import random as rand

class Item:
    max_hp_bonus = 0
    hp_bonus = max_hp_bonus #KAN ÄNDRAS INDIVIDUELLT, DEFAULT ÄR ATT DE ÄR SAMMA
    str_bonus = 0
    spd_bonus = 0
    name = ""
    type = ""
    cost = 0

#DEFAULT WEAPON ÄR FISTS:
fists = Item()
fists.type = "weapon"
fists.name = "Fists"

#DEFAULT ARMOR ÄR NONE:
empty_armor = Item()
empty_armor.type = "armor"
empty_armor.name = "None"

#DEFAULT ACCESSORY ÄR NONE:
empty_accessory = Item()
empty_accessory.type = "accessory"
empty_accessory.name = "None"

item_list=          ["dagger", "sword", "explosive", "ultra_greatsword", "springfield rifle", "rocket launcher", "crusader helm", "leather boots", "philosophy book", "voltaire's pencil"]
item_rarity_list =  [100,       100,     60,          20,                 60,                  1099999999,       100,             100,             100,               100]



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
        explosive.cost = rand.randint(410,460)
        return explosive
    elif choice == "ultra_greatsword":
        ultra_greatsword = Item()
        ultra_greatsword.type = "weapon"
        ultra_greatsword.name = "Voltaire's Ultra Greatsword"
        ultra_greatsword.str_bonus = rand.randint(25,30)
        ultra_greatsword.spd_bonus = rand.randint(-9, -6)
        ultra_greatsword.cost = rand.randint(620,880) 
        return ultra_greatsword
    elif choice == "springfield rifle":
        springfield_rifle = Item()
        springfield_rifle.type = "weapon"
        springfield_rifle.name = "M1903 Springfield .30 Cal Rifle"
        springfield_rifle.str_bonus = rand.randint(12, 18)
        springfield_rifle.spd_bonus = rand.randint(4, 6)
        springfield_rifle.cost = rand.randint(280, 340)
        return springfield_rifle
    elif choice == "rocket launcher":
        rocket_launcher = Item()
        rocket_launcher.type = "weapon"
        rocket_launcher.name = "1970 US Northrop Corporation; 4 rocket clip M202A1 FLASH incendiary TPA Rocket Launcher"
        rocket_launcher.str_bonus = rand.randint(42, 60)
        rocket_launcher.cost = rand.randint(1000, 1200)
        return rocket_launcher
    #ARMOR-----------------------------------------------------
    elif choice == "crusader helm":
        crusader_helm = Item()
        crusader_helm.type = "armor"
        crusader_helm.name = "Crusader helm"
        crusader_helm.max_hp_bonus = rand.randint(50,70)
        crusader_helm.cost = rand.randint(70, 80)
        return crusader_helm
    elif choice == "leather boots":
        boots = Item()
        boots.type = "armor"
        boots.name = "Leather boots"
        boots.max_hp_bonus = rand.randint(40, 50)
        boots.spd_bonus = rand.randint(3, 6)
        boots.cost = rand.randint(60, 70)
        return boots

    #ACCESSORY------------------------------------------------------
    elif choice == "philosophy book":
        philosophy_book = Item()
        philosophy_book.type = "accessory"
        philosophy_book.name = '''Pangloss`s "Metaphysiology collection" book'''
        philosophy_book.max_hp_bonus = rand.randint(30, 40)
        philosophy_book.str_bonus = rand.randint(-8, -2)
        philosophy_book.spd_bonus = rand.randint(5, 8)
        philosophy_book.cost = rand.randint(1, 5)
        return philosophy_book
    elif choice == "voltaire's pencil":
        pencil = Item()
        pencil.type = "accessory"
        pencil.name = "Voltaire's pencil"
        pencil.str_bonus = rand.randint(8, 14)
        pencil.spd_bonus = rand.randint(6, 10)
        pencil.cost = rand.randint(90, 100)
        return pencil
        



    


#HÄR LÄGGS ALLT TILL I DE OLIKA LISTORNA





resource_string = ["iron", "guldbagge", "wood", "stone", "bread", "meat"]
    