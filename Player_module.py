import Item_module as I
import pygame

class Player():
    
    name = ""
    hp = 0
    max_hp = 0
    spd = 0
    str = 0
    exp = 0
    gold = 0
    level = 0
    level_limit = 500
    inventory = []
    debuffs = []
    equipped_weapon = I.fists
    equipped_armor = I.empty_armor
    equipped_accessory = I.empty_accessory
    curse_of_eldorado = 0 #COE FUNGERAR SÅ ATT DEN ÄR 0 TILLS MAN KOMMER TILL ELDORADO, OM MAN LÄMNAR BLIR COE 3, OCH FÖR VARJE RUNDA GÅR DEN NER MED 1 DÄR MAN FÖRLORAR 1/3 AV SINA PENGAR 
    
class Attack():
    name = ""
    description = ""
    sound_effect = ''

dropkick = Attack()
dropkick.name = "Dropkick"
dropkick.sound_effect = 'sounds/dropkick.mp3'

words = Attack()
words.name = "Words"
words.sound_effect = 'sounds/dietz nuts.mp3'

armor_breaker = Attack()
armor_breaker.name = "Armor breaker"
armor_breaker.sound_effect = 'sounds/armorbreaker.mp3'

cleaver = Attack()
cleaver.name = "Head cleaver"
cleaver.sound_effect = 'sounds/sword-bloody.mp3'

roundhouse_kick = Attack()
roundhouse_kick.name = "Roundhouse kick"
roundhouse_kick.sound_effect = 'sounds/dropkick.mp3'

gun = Attack()
gun.name = "Gun"
gun.sound_effect = 'sounds/gunshot full.mp3'

cum = Attack()
cum.name = "Cum"
cum.sound_effect = 'sounds/ummuhh.mp3'

cannibalism = Attack()
cannibalism.name = "Cannibalism"
cannibalism.sound_effect = 'sounds/cannibalism.mp3'

nothing = Attack()
nothing.name = "Do nothing"
nothing.sound_effect = ''



ATTACK_MOVE_LIST = [dropkick, words, armor_breaker, cleaver, roundhouse_kick, gun, cum, cannibalism, nothing]


def attack_move_description(chosen_attack, player_name, player_weapon, enemy_name): 
    #DROPKICK
    dropkick.description = f'''
You droppkicked {enemy_name}!'''
    #WORDS
    words.description = f''' 
"Candide balls fit in your mouth?" Uttered {player_name}, {enemy_name} is in distraught!'''
    #ARMOR BREAKER
    armor_breaker.description = f''' 
You took a firm grip around your {player_weapon} and crushed through the enemy's armor!'''
    #HEAD CLEAVER
    cleaver.description = f''' 
Using your {player_weapon}, with a swift strike you split {enemy_name} in two!'''
    #ROUNDHOUSE KICK
    roundhouse_kick.description = f''' 
You charged up and roundhouse kicked {enemy_name}!'''
    #GUN
    gun.description = f''' 
{player_name} pulled out a gun and shot {enemy_name}!'''
    #CUM
    cum.description = f''' 
{player_name} came all over the enemy!'''
    #CANNIBALISM
    cannibalism.description = f''' 
"Woah is that fucking blackface dude?" said {player_name}.
{player_name} ate {enemy_name} alive!'''
    #DO NOTHING
    nothing.description = f'''
{player_name} just kinda stood there.'''

    for attack in ATTACK_MOVE_LIST:
        if attack.name == chosen_attack.name:
            # try:
            #     pygame.mixer.music.load(attack.sound_effect)
            #     pygame.mixer.music.play(0, 1, 0)
            # except:
            #     pass
            
            return attack.description
    




