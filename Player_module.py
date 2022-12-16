class Player():
    
    name = ""
    hp = 0
    spd = 0
    str = 0
    exp = 0
    gold = 0
    level = 0
    level_limit = 500

attack_move_name_1 = "Dropkick"
attack_move_name_2 = "Words"
attack_move_name_3 = "Armor breaker"
attack_move_name_4 = "Head cleaver"
attack_move_name_5 = "Roundhouse kick"
attack_move_name_6 = "Gun"
attack_move_name_7 = "Cum"
attack_move_name_8 = "Cannibalism"

attack_move_name_list = [attack_move_name_1, attack_move_name_2, attack_move_name_3, attack_move_name_4, attack_move_name_5, attack_move_name_6, attack_move_name_7, attack_move_name_8]


def attack_move_description(chosen_attack, player_name, player_weapon, enemy_name):
    
    #DROPKICK
    attack_description_1 = f''' 
    You droppkicked {enemy_name}!
    '''
    #WORDS
    attack_description_2 = f''' 
    "Candide balls fit in your mouth?" Uttered {player_name}, {enemy_name} is in distraught!
    '''
    #ARMOR BREAKER
    attack_description_3 = f''' 
    You took a fast grip around your {player_weapon} and crushed the enemy's armor!
    '''
    #HEAD CLEAVER
    attack_description_4 = f''' 
    Using your {player_weapon}, with a swift strike you split {enemy_name} in two!
    '''
    #ROUNDHOUSE KICK
    attack_description_5 = f''' 
    You charged up and roundhouse kicked the {enemy_name}!
    '''
    #GUN
    attack_description_6 = f''' 
    {player_name} pulled out a gun and shot {enemy_name}!
    '''
    #CUM
    attack_description_7 = f''' 
    {player_name} came all over the enemy!
    '''
    #DROPKICK
    attack_description_8 = f''' 
    "Woah is that fucking blackface dude?" said {player_name}.
    {player_name} ate {enemy_name} alive!
    '''


    if chosen_attack == attack_move_name_1:
        returned_description = attack_description_1
    elif chosen_attack == attack_move_name_2:
        returned_description = attack_description_2
    elif chosen_attack == attack_move_name_3:
        returned_description = attack_description_3
    elif chosen_attack == attack_move_name_4:
        returned_description = attack_description_4
    elif chosen_attack == attack_move_name_5:
        returned_description = attack_description_5
    elif chosen_attack == attack_move_name_6:
        returned_description = attack_description_6
    elif chosen_attack == attack_move_name_7:
        returned_description = attack_description_7
    elif chosen_attack == attack_move_name_8:
        returned_description = attack_description_8
    
    return returned_description




