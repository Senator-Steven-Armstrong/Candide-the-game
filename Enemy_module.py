import random as rand

class Enemy():
    
    name = ""
    max_hp = 0
    hp = 0
    spd = 0
    str = 0
    exp_dropped = 0
    gold_dropped = 0


# Kanske dodgeroll / block, och combat kan kanske vara baserad på tur för varje runda eller annars är spd bara till för första rundan som i pokemans 



# OUTLINE
# variable = Enemy()
# .hp = rand.randint()
# .spd = rand.randint()
# .str = rand.randint()
# .exp_dropped = rand.randint()
# .gold_dropped = rand.randint()

bandit = Enemy()
cannibal = Enemy()
långöron = Enemy()
goblin = Enemy()
bulgar = Enemy()
råtta = Enemy()
traveler = Enemy()

#TEXTER SOM VISAS NÄR EN FIGHT BÖRJAR


def create_enemy(enemy_name):
    # Below are the base stats of enemies that can be encountered and fought in the game

    if enemy_name == bandit:
        # Bandit stats
        bandit.name = "bandit"
        bandit.max_hp = rand.randint(80, 120)
        bandit.spd = rand.randint(5, 15)
        bandit.str = rand.randint(5, 15)
        bandit.exp_dropped = rand.randint(100, 150)
        bandit.gold_dropped = rand.randint(40, 70)
    elif enemy_name == cannibal:
        # Cannibal stats
        cannibal.name = "cannibal"
        cannibal.max_hp = rand.randint(50, 90)
        cannibal.spd = rand.randint(10, 20)
        cannibal.str = rand.randint(10, 20)
        cannibal.exp_dropped = rand.randint(120, 190)
        cannibal.gold_dropped = rand.randint(10, 30)
    elif enemy_name == långöron:
        # Långöron
        långöron.name = "långöron"
        långöron.max_hp = rand.randint(90, 130)
        långöron.spd = rand.randint(15, 25)
        långöron.str = rand.randint(15, 30)
        långöron.exp_dropped = rand.randint(150, 220)
        långöron.gold_dropped = rand.randint(20, 40)
    elif enemy_name == goblin:
        # Goblin
        goblin.name = "goblin"
        goblin.max_hp = rand.randint(40, 80)
        goblin.spd = rand.randint(27, 40)
        goblin.str = rand.randint(4, 10)
        goblin.exp_dropped = rand.randint(100, 140)
        goblin.gold_dropped = rand.randint(40, 70)
    elif enemy_name == bulgar:
        # Bulgar
        bulgar.name = "bulgar"
        bulgar.max_hp = rand.randint(120, 160)
        bulgar.spd = rand.randint(10, 14)
        bulgar.str = rand.randint(25, 32)
        bulgar.exp_dropped = rand.randint(120, 300)
        bulgar.gold_dropped = rand.randint(45, 75)
    elif enemy_name == råtta:   
        # Råtta
        råtta.name = "råtta"
        råtta.max_hp = rand.randint(1, 50)
        råtta.spd = rand.randint(20, 30)
        råtta.str = rand.randint(20, 25)
        råtta.exp_dropped = rand.randint(40, 100)
        råtta.gold_dropped = rand.randint(10, 20)
    elif enemy_name == traveler:
        # traveler
        traveler.name = "traveler"
        traveler.max_hp = rand.randint(160, 220)
        traveler.spd = rand.randint(5, 10)
        traveler.str = rand.randint(35, 45)
        traveler.exp_dropped = rand.randint(150, 350)
        traveler.gold_dropped = rand.randint(85, 150)

def fight_begin_description(chosen_enemy):

    enemy_name = chosen_enemy.name

    fight_begins_1 = f'''
{enemy_name.capitalize()} blocks your way!
'''

    fight_begins_2 = f'''
{enemy_name.capitalize()} stands in your way!
'''

    fight_begins_3 = f'''
{enemy_name.capitalize()} has appeared!
'''

    fight_begins_4 = f'''
{enemy_name.capitalize()} breaks down on the dancefloor!
'''

    fight_begins_5 = f'''
It's time to fucking eradicate {enemy_name}!
'''

    fight_description_list = [fight_begins_1, fight_begins_2, fight_begins_3, fight_begins_4, fight_begins_5]

    return rand.choice(fight_description_list)


enemy_list = [bandit, cannibal, långöron, goblin, bulgar, råtta, traveler]
print(type(bandit))

def Enemy_levelup():
    
    hp = hp*1.125
    spd = spd*1.125

    str = str*1.125
    exp_dropped = exp_dropped*1.125
    gold_dropped = gold_dropped*1.125