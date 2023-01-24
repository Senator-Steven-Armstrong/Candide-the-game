import random as rand

class Enemy():
    
    name = ""
    max_hp = 0
    hp = 0
    spd = 0
    str = 0
    exp_dropped = 0
    gold_dropped = 0
    spawndialouge = ""


# Kanske dodgeroll / block, och combat kan kanske vara baserad på tur för varje runda eller annars är spd bara till för första rundan som i pokemans 



# OUTLINE
# variable = Enemy()
# .hp = rand.randint()
# .spd = rand.randint()
# .str = rand.randint()
# .exp_dropped = rand.randint()
# .gold_dropped = rand.randint()








#BOSSES
kunigunda = Enemy()
kunigunda.name = "Kunigunda"
kunigunda.max_hp = 1200
kunigunda.spd = 100
kunigunda.str = 100

#BARONEN----------------------------------------------------------------------------
baronen = Enemy()
baronen.name = "Baronen"
baronen.max_hp = 800
baronen.hp = baronen.max_hp
baronen.spd = 200
baronen.str = 60
baronen.gold_dropped = 800
baronen.exp_dropped = 1000

def baronen_attacks():
    
    boss_attack_1 = '''
Baronen swings his blade with incredible speed!'''

    boss_attack_2 = '''
Baronen dashes towards you, piercing you with the blade!'''

    boss_attack_3 = '''
Baronen point the blade at the moon and swings it down, shooting out a sharp projectile of light!'''

    boss_attack_4 = '''
Baronen disappears and reappears behind you, slashing you in the back!'''

    boss_attack_5 = '''
Baronen throws the blade, its spins in the air and hits you!'''

    boss_attack_6 = '''
Baronen slams the blade in the ground and starts running toward you, dragging the blade along the floor,
and then uppercuts you!'''

    boss_attack_7 = '''
Baronen forms two small moonlight knifes and throws them at you! '''

    boss_attack_8 = '''
Baronen spins his blade over his head and slices you!'''
    boss_attack_list = [boss_attack_1, boss_attack_2, boss_attack_3, boss_attack_4, boss_attack_5, boss_attack_6, boss_attack_7, boss_attack_8]
    return rand.choice(boss_attack_list)

def baronen_voice_lines():

    voice_line_chance = rand.randint(1, 3)

    line_1 = '''
"Leave her alone!"''' 
    line_2 = '''
"You don't deserve her!"''' 
    line_3 = '''
"You won't be able to keep up!"''' 
    line_4 = '''
"Why did you have to do this? We were a family!"''' 
    line_5 = '''
"Give up."''' 
    line_6 = '''
"How can you even keep up?!"''' 
    voice_line_list = [line_1, line_2, line_3, line_4, line_5, line_6]
    
    if voice_line_chance >= 1:
        return rand.choice(voice_line_list)


#POCOCURANTE------------------------------------------------------------------------
pococurante = Enemy()
pococurante.name = "Lord Pococurante"
pococurante.max_hp = 600
pococurante.hp = pococurante.max_hp
pococurante.spd = 20
pococurante.str = 50
pococurante.gold_dropped = 400
pococurante.exp_dropped = 600

def pococurante_attacks():
    
    boss_attack_1 = '''
Pococurante winds up his cane behind him, and releases with a huge swing!'''

    boss_attack_2 = '''
Pococurante threw a book at you!'''

    boss_attack_3 = '''
Pococurante piecres his cane through your heart!'''

    boss_attack_4 = '''
Pococurante conjuress his magic, letter swerve around his cane and a bright ray
of bright light blasts out of it! '''

    boss_attack_5 = '''
Pococurante slams a painting on your head!'''

    boss_attack_6 = '''
Pococurante slams his cane in the ground, ammasing a beautiful explosion of colors and light!'''

    boss_attack_7 = '''
Pococurante tells you how meaningless life is and that nothing beautiful can make you happy. '''

    boss_attack_8 = '''
Pococurante starts spinning around with his cane extended out. It hits you multiple times!'''
    boss_attack_list = [boss_attack_1, boss_attack_2, boss_attack_3, boss_attack_4, boss_attack_5, boss_attack_6, boss_attack_7, boss_attack_8]
    return rand.choice(boss_attack_list)

def pococurante_voice_lines():

    voice_line_chance = rand.randint(1, 3)

    line_1 = '''
"Put these foolish ambitions to rest."''' 
    line_2 = '''
"You will never inspire anyone!"''' 
    line_3 = '''
"You will amount to nothing!"''' 
    line_4 = '''
"Optimism won't lead to happiness!"''' 
    line_5 = '''
"Give up."''' 
    line_6 = '''
"Have you even read a book?!"''' 
    voice_line_list = [line_1, line_2, line_3, line_4, line_5, line_6]
    
    if voice_line_chance >= 1:
        return rand.choice(voice_line_list)

def create_enemy(enemy_name):
    # Below are the base stats of enemies that can be encountered and fought in the game

    if enemy_name == "bandit":
        # Bandit stats
        bandit = Enemy()
        bandit.name = "bandit"
        bandit.max_hp = rand.randint(80, 120)
        bandit.spd = rand.randint(5, 15)
        bandit.str = rand.randint(5, 15)
        bandit.exp_dropped = rand.randint(100, 150)
        bandit.gold_dropped = rand.randint(40, 70)
        
        bandit.spawndialogue_1 = '''
        Oi, yeou, gimme your money before I gut ya ye filthy scum! London sure is a lovely 
        '''
        bandit.spawndialogue_2 = '''
        I'm terribly sorry but you, one's old bean, aaare ah jolly frightful luverly chap and 
        deaaarly hope to defeat you, one's old bean, in this combat and be rid of your prescense.
        '''
        bandit.spawndialogue_3 = '''
        Thee th're! cometh h're betimes and giveth me thy wage 
        bef're i carveth thee with this cankered fusty bodkin!
        '''
    elif enemy_name == "cannibal":
        # Cannibal stats
        cannibal = Enemy()
        cannibal.name = "cannibal"
        cannibal.max_hp = rand.randint(50, 90)
        cannibal.spd = rand.randint(10, 20)
        cannibal.str = rand.randint(10, 20)
        cannibal.exp_dropped = rand.randint(120, 190)
        cannibal.gold_dropped = rand.randint(10, 30)

        cannibal.spawndialogue_1 = '''

        '''
    elif enemy_name == "långöron":
        # Långöron    
        långöron = Enemy()
        långöron.name = "långöron"
        långöron.max_hp = rand.randint(90, 130)
        långöron.spd = rand.randint(15, 25)
        långöron.str = rand.randint(15, 30)
        långöron.exp_dropped = rand.randint(150, 220)
        långöron.gold_dropped = rand.randint(20, 40)
        return långöron
    elif enemy_name == "goblin":
        # Goblin
        goblin = Enemy()
        goblin.name = "goblin"
        goblin.max_hp = rand.randint(40, 80)
        goblin.spd = rand.randint(27, 40)
        goblin.str = rand.randint(6, 10)
        goblin.exp_dropped = rand.randint(100, 140)
        goblin.gold_dropped = rand.randint(40, 70)
        goblin
        return goblin
    elif enemy_name == "bulgar":
        # Bulgar
        bulgar = Enemy()
        bulgar.name = "bulgar"
        bulgar.max_hp = rand.randint(120, 160)
        bulgar.spd = rand.randint(10, 14)
        bulgar.str = rand.randint(25, 32)
        bulgar.exp_dropped = rand.randint(120, 300)
        bulgar.gold_dropped = rand.randint(45, 75)
        return bulgar
    elif enemy_name == "rat":   
        # Råtta
        rat = Enemy()
        rat.name = "rat"
        rat.max_hp = rand.randint(1, 50)
        rat.spd = rand.randint(20, 30)
        rat.str = rand.randint(20, 25)
        rat.exp_dropped = rand.randint(40, 100)
        rat.gold_dropped = rand.randint(10, 20)
        return rat
    elif enemy_name == "traveler":
        # traveler
        traveler = Enemy()
        traveler.name = "traveler"
        traveler.max_hp = rand.randint(160, 220)
        traveler.spd = rand.randint(5, 10)
        traveler.str = rand.randint(35, 45)
        traveler.exp_dropped = rand.randint(150, 350)
        traveler.gold_dropped = rand.randint(85, 150)
        return traveler
    elif enemy_name == "chaos entity":
        chaos_entity = Enemy()
        chaos_entity.name = "Chaos entity"
        chaos_entity.max_hp = rand.randint(5, 200)
        chaos_entity.spd = rand.randint(1, 50)
        chaos_entity.str = rand.randint(6, 50)
        chaos_entity.exp_dropped = rand.randint(1, 350)
        chaos_entity.gold_dropped = rand.randint(1, 150)
        return chaos_entity
    elif enemy_name == "chef":
        #Chef
        chef = Enemy()
        chef.name = "Pizza chef"
        chef.max_hp = rand.randint(80, 160)
        chef.spd = rand.randint(5, 10)
        chef.str = rand.randint(25, 35)
        chef.exp_dropped = rand.randint (60, 120)
        chef.gold_dropped =rand.randint(30, 45)
        return chef

def fight_begin_description(chosen_enemy_name):

    enemy_name = chosen_enemy_name

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

