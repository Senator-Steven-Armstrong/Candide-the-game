import random as rand

class Item:
    max_hp_bonus = 0
    hp_bonus = max_hp_bonus #KAN ÄNDRAS INDIVIDUELLT, DEFAULT ÄR ATT DE ÄR SAMMA
    str_bonus = 0
    spd_bonus = 0
    name = ""
    type = ""
    cost = 0
    effect = "none"

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

#BOSS ITEMS
pococurante_cane = Item()
pococurante_cane.type = "weapon"
pococurante_cane.name = "Pococurante's cane"
pococurante_cane.str_bonus = 40
pococurante_cane.max_hp_bonus = 200
pococurante_cane.effect = "books"

baronen_knife = Item()
baronen_knife.type = "weapon"
baronen_knife.name = "The knife of the mad brother"
baronen_knife.spd_bonus = 100
baronen_knife.str_bonus = 20
baronen_knife.effect = "quickstep"
baronen_knife_effect_text_1 = "\n\nThe knife vibrates, everything seems to slow down around you.\nA rushing jolt sends you body forward, avoiding the enemy attack, and seemingly stepping through the enemy.\nYou turn around, facing the back of your foe, and stab it in the back!"
baronen_knife_effect_text_2 = "\n\nThe knife radiates, you feel a rush of speed, jolt backwards and \nin a swift dash stab the enemy before it has a chance to attack!,"
baronen_knife_effect_text_3 = "\n\nThe knife sends an electric shock through your body and like lightning \nyou zap around the enemy slicing it multiple times without a chance to counter-attack!"
baronen_knife_effect_text_list = [baronen_knife_effect_text_1, baronen_knife_effect_text_2, baronen_knife_effect_text_3]

def baronen_knife_effect_description():
    return rand.choice(baronen_knife_effect_text_list)



baronen_greatsword = Item()
baronen_greatsword.type = "weapon"
baronen_greatsword.name = "Moonlight greatsword of animosity"
baronen_greatsword.str_bonus = 50
baronen_greatsword.spd_bonus = 20
baronen_greatsword.max_hp_bonus = 300




item_list=          ["dagger", "sword", "explosive", "ultra_greatsword", "springfield rifle", "rocket launcher", "knight helm", "leather boots", "philosophy book", "voltaire's pencil", "shackles", "health potion", "roids"]
item_rarity_list =  [100,       100,     60,          20,                 60,                  10,                100,           100,             100,               100,                 100,        80,              80]

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
        explosive.str_bonus = rand.randint(30, 40)
        explosive.cost = rand.randint(410,460)
        explosive.effect = "explosion"
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
    elif choice == "knight helm":
        knight_helm = Item()
        knight_helm.type = "armor"
        knight_helm.name = "Knight helm"
        knight_helm.max_hp_bonus = rand.randint(50,70)
        knight_helm.cost = rand.randint(70, 80)
        return knight_helm
    elif choice == "leather boots":
        boots = Item()
        boots.type = "armor"
        boots.name = "Leather boots"
        boots.max_hp_bonus = rand.randint(40, 50)
        boots.spd_bonus = rand.randint(3, 6)
        boots.cost = rand.randint(60, 70)
        return boots
    elif choice == "shackles":
        shackles = Item()
        shackles.type = "armor"
        shackles.name = "Prisoner's shackles"
        shackles.max_hp_bonus = 100
        shackles.spd_bonus = rand.randint(-12, -2)
        shackles.cost = rand.randint(20, 60)
        return shackles

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
        pencil.max_hp_bonus = rand.randint(10, 15)
        pencil.str_bonus = pencil.max_hp_bonus
        pencil.spd_bonus = pencil.max_hp_bonus
        pencil.cost = pencil.max_hp_bonus * 10
        return pencil

    #HEALING------------------------------------------------------
    elif choice == "health potion":
        health_potion = Item()
        health_potion.type = "healing"
        health_potion.name = "Health potion"
        health_potion.hp_bonus = 200
        return health_potion
    elif choice == "calypso":
        calypso = Item()
        calypso.type = "healing"
        calypso.name = "Calypso [Minging]"
        calypso.hp_bonus = 100

    #CONSUMABLE-------------------------------------------------------
    elif choice == "roids":
        roids = Item()
        roids.type = "consumable"
        roids.name = "Roids"
        roids.str_bonus = rand.randint(10, 20)
        roids.spd_bonus = rand.randint(-10, -5)
        return roids

        



    


#HÄR LÄGGS ALLT TILL I DE OLIKA LISTORNA





resource_string = ["iron", "guldbagge", "wood", "stone", "bread", "meat"]
    