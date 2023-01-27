from time import sleep
import sys,time
import Enemy_module as E
import random as rand

TEST = 0.02
PUNCTUATION_PAUSE_TIME = 0.4
COMMA_PAUSE_TIME = 0.15
SEMICOLON_PAUSE_TIME = 0.6
# This is a logbook of lore entries on the different enemies. 
# Here, you can learn about the enemies backstory and appearance, and also some
# common attributes that they may possess, such as increased speed or higher health.
# There will also be categories that you may select such as locations and enemies.

#Foes Category

def print_slow(str, write_speed):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(write_speed)
        if letter == "." or letter == "?" or letter == "!":
            sleep(PUNCTUATION_PAUSE_TIME)
        elif letter == ",":
            sleep(COMMA_PAUSE_TIME)
        elif letter == ";":
            sleep(SEMICOLON_PAUSE_TIME)

bandit_lore = '''
Bandits are one of the most common foes you will meet. They roam the land, looking for 
innocents to steal from and kill. Bandits are quite average in every category of a fight, 
but that does not mean they should be underestimated.
'''

cannibal_lore = '''
Cannibals are the subordinates of the Långöron. They are generally weaker than them,
but there are stronger individuals among them that can rival their superiors in strength.
They are ferocious and when they've got your scent they will not cease their hunt until stopped.
Some cannibals have left their original tribe to start their own in the jungle, so you may encounter them often.
'''

långöron_lore = '''
The Långöron are the leaders of the cannibal tribes are at the physical peak. They often stand over 7 feet tall,
and carry weapons that can deal massive damage, and their training has made them very fast. It is believed they have a certain connection to nature, 
and follow a deity by the name of Eivor. This may be the cause of their physical prowess.
'''

traveler_lore = '''
Travelers are very large humans, towering above the average person. They carry an enormous sword in honor 
of their culture. This sword, combined with superior size, provides a very large advantage in combat. 
While Travelers are very strong, due to their size they fall behind in speed. 
Legends say Travelers also have capabilities of magic. Do not challenge these foes if you are not ready.
'''

goblin_lore = '''
Goblins are lowly creatures, often found in packs looking for people to steal from and kill for sport.
They are very weak except for being extremely fast. Despite being weak alone, their strength is in their numbers.
Do not approach if your speed is low, and do not linger in the heat of battle, for others could be on their way.
'''

baronen_lore = '''
Baronen, short for Baron Thunder-ten-tronckh, is the head of a castle that goes by the same name. 
His strength is immaculate, and the mere thought of challenging him is dangerous. 
His name shall be remembered for long, and it's power will have an effect on the world long after he is gone.
'''

pococurante_lore = '''
Pococurante is one of the most powerful men in Venice. He has an exquisite taste for wine, 
but not nearly such respect for women. He is a very petty man, if any person has an opinion not equal to his,
you shall not be allowed to live further. He is the physical embodiment of danger.
'''

#Friends Category

kunigunda_lore = '''
The sweet Kunigunda is Candide's betrothen. Candide is currently looking for her,
in hope that they might one day be together again.
'''

shopkeeper_lore = '''
Not much is known about the shopkeeper. He always manages to find us on our journey
despite our constant traveling to many different locations. This is especially curious,
since we have never told him where we are going. 

It seems like what happens never surprises him, almost as if he knows what will happen.
We have asked him several times how he manages to obtain these items, but he always
laughs it off saying 'I have my ways'.
'''

shop_encounters = False
#entries_list=[E.bandit_encounters, E.cannibal_encounters, E.långöron_encounters, E.traveler_encounters, E.goblin_encounters, E.kunigunda_encounters, E.baronen_encounters, E.pococurante_encounters, shop_encounters]

# Function to use the logbook menu
def logbook_menu():
    while True:
        print_slow('''
        Welcome to the logbook! Surely you have met others on this long journey of yours, 
        whether they are friends or foes. Once you have met (often killed) these fellows, 
        you will unlock a logbook entry here giving information about them. Good luck!
        ''', TEST)

        sleep(3)

        print_slow('''
        These are the entrys you have unlocked:
        ''', TEST)

        if E.bandit.encounters == True:
            print('''
            1. Bandits
            ''')
        elif E.cannibal.encounters == True:
            print('''
            2. Cannibals
            ''')
        
        if E.långöron_encounters == True:
            print('''
            3. The Långöron
            ''')

        if E.traveler_encounters == True:
            print('''
            4. Travelers
            ''')

        if E.goblin_encounters == True:
            print('''
            5. Goblins
            ''')

        if E.kunigunda_encounters == True:
            print('''
            6. Kunigunda
            ''')

        if E.baronen_encounters == True:
            print('''
            7. Baronen
            ''')
        
        if E.pococurante_encounters == True:
            print('''
            8. Pococurante
            ''')

        if shop_encounters == True:
            print('''
            9. The Shopkeeper
            ''')

        int(input("Select one of the options."))
        if input == "1":
            while True:
        
                print_slow(bandit_lore)
                sleep(3)
                input("Would you like to go back? Y/N")
                if input == "Y" or input == "y":
                    break
                elif input == "N" or input == "n":
                    input("Write Y when you are ready to leave.")
                    if input == "Y" or input == "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

                input("Write Y when you are ready to leave.")
        if input == "2":
            while True:
            
                print_slow(cannibal_lore, TEST)
                sleep(3)
                input("Would you like to go back? Y/N")
                if input == "Y" or input == "y":
                    break
                elif input == "N" or input == "n":
                    input("Write Y when you are ready to leave.")
                    if input == "Y" or input == "y":
                        break
                    else:
                        print_slow("Try again.")
                        continue

                input("Write Y when you are ready to leave.")
        if input == "3":
            while True:
            
                print_slow(långöron_lore)
                sleep(3)
                input("Would you like to go back? Y/N")
                if input == "Y" or input == "y":
                    break
                elif input == "N" or input == "n":
                    input("Write Y when you are ready to leave.")
                    if input == "Y" or input == "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

                input("Write Y when you are ready to leave.")
        if input == "4":
            while True:
            
                print_slow(traveler_lore)
                sleep(3)
                input("Would you like to go back? Y/N")
                if input == "Y" or input == "y":
                    break
                elif input == "N" or input == "n":
                    input("Write Y when you are ready to leave.")
                    if input == "Y" or input == "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

                input("Write Y when you are ready to leave.")
        if input == "5":
            while True:

                print_slow(goblin_lore, TEST)
                sleep(3)
                input("Would you like to go back? Y/N")
                if input == "Y" or input == "y":
                    break
                elif input == "N" or input == "n":
                    input("Write Y when you are ready to leave.")
                    if input == "Y" or input == "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

                input("Write Y when you are ready to leave.")

            if input == "6":
                while True:
                
                    print_slow(kunigunda_lore, TEST)
                    sleep(3)
                    input("Would you like to go back? Y/N")
                    if input == "Y" or input == "y":
                        break
                    elif input == "N" or input == "n":
                        input("Write Y when you are ready to leave.")
                        if input == "Y" or input == "y":
                            break
                        else:
                            print_slow("Try again.", TEST)
                            continue

            if input == "7":
                while True:
                
                    print_slow(baronen_lore, TEST)
                    sleep(3)
                    input("Would you like to go back? Y/N")
                    if input == "Y" or input == "y":
                        break
                    elif input == "N" or input == "n":
                        input("Write Y when you are ready to leave.")
                        if input == "Y" or input == "y":
                            break
                        else:
                            print_slow("Try again.", TEST)
                            continue

            if input == "8":
                while True:
                
                    print_slow(pococurante_lore, TEST)
                    sleep(3)
                    input("Would you like to go back? Y/N")
                    if input == "Y" or input == "y":
                        break
                    elif input == "N" or input == "n":
                        input("Write Y when you are ready to leave.")
                        if input == "Y" or input == "y":
                            break
                        else:
                            print_slow("Try again.", TEST)
                            continue

            if input == "9":
                while True:
                
                    print_slow(shopkeeper_lore, TEST)
                    sleep(3)
                    input("Would you like to go back? Y/N")
                    if input == "Y" or input == "y":
                        break
                    elif input == "N" or input == "n":
                        input("Write Y when you are ready to leave.")
                        if input == "Y" or input == "y":
                            break
                        else:
                            print_slow("Try again.", TEST)
                            continue
