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

#BOSSES
kunigunda = Enemy()
kunigunda.name = "Kunigunda, the burned beauty"
kunigunda.max_hp = 1200
kunigunda.spd = 60
kunigunda.str = 70

baronen = Enemy()
baronen.name = "Baronen, the mad brother"
baronen.max_hp = 800
baronen.spd = 45
baronen.str = 45

pococurante = Enemy()
pococurante.name = "Lord Pococurante, the dreadful art collector"
pococurante.max_hp = 600
pococurante.spd = 10
pococurante.str = 50

def pococurante_attacks(player_name):
    
    boss_attack_1 = '''
Pococurante winds up his cane behind him, and releases with a huge swing!
'''

    boss_attack_2 = '''
Pococurante throws a book at you!
'''

    boss_attack_3 = '''

'''

    boss_attack_4 = '''
    
'''

    boss_attack_5 = '''
    
'''

    boss_attack_6 = '''
    
'''

    boss_attack_7 = '''
    
'''

    boss_attack_8 = '''
    
'''
    boss_attack_list = [boss_attack_1, boss_attack_2, boss_attack_3, boss_attack_4, boss_attack_5, boss_attack_6, boss_attack_7, boss_attack_8]
    return rand.choice(boss_attack_list)
    


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
You engage in combat with {enemy_name.capitalize()}, lets kill it!
'''

    fight_description_list = [fight_begins_1, fight_begins_2, fight_begins_3, fight_begins_4, fight_begins_5]

    return rand.choice(fight_description_list)

def enemy_attack_description(chosen_enemy, player_name):
   
    enemy_name = chosen_enemy.name

    enemy_attack_1 = f'''
{enemy_name.capitalize()} whipped out the AK and started blasting!'''
    
    enemy_attack_2 = f'''
{enemy_name.capitalize()} threw down some sick moves, {player_name} is in absolute awe!'''

    enemy_attack_3 = f'''
Enemy engaged in small talk, you couldn't handle the pressure!'''

    enemy_attack_4 = f'''
Enemy hit you in the face!'''

    enemy_attack_5 = f'''
Enemy threw some pebbles at you!'''

    enemy_attack_list = [enemy_attack_1, enemy_attack_2, enemy_attack_3, enemy_attack_4, enemy_attack_5]
    return rand.choice(enemy_attack_list)

enemy_list = [bandit, cannibal, långöron, goblin, bulgar, råtta, traveler]
print(type(bandit))

