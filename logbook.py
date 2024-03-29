from time import sleep
import sys,time

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


# Function to use the logbook menu
def logbook_menu():
    while True:
        print_slow('''
Welcome to the logbook! Surely you have met others on this long journey of yours, 
whether they are friends or foes. Here, you can read logbook entrys giving information about them. 
Fair travels!
''', TEST)

        sleep(0.6)

        print('''
These are the entrys you have:
1. Bandits
2. Cannibals
3. The Långöron
4. The Travelers
5. Goblins
6. Kunigunda
7. Baronen
8. Pococurante
9. The Shopkeeper
''')

        logbook_input = input("Select one of the options. Write 0 to go back: ")
        if logbook_input == "1":
            while True:
        
                print_slow(bandit_lore, TEST)
                sleep(3)
                input("Would you like to go back? Y/N")
                if logbook_input== "Y" or logbook_input== "y":
                    break
                elif logbook_input== "N" or logbook_input== "n":
                    input("Write Y when you are ready to leave.")
                    if logbook_input== "Y" or logbook_input== "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

                input("Write Y when you are ready to leave.")
        elif logbook_input == "2":
            while True:
            
                print_slow(cannibal_lore, TEST)
                sleep(3)
                input("Would you like to go back? Y/N")
                if logbook_input== "Y" or logbook_input== "y":
                    break
                elif logbook_input== "N" or logbook_input== "n":
                    input("Write Y when you are ready to leave.")
                    if logbook_input== "Y" or logbook_input== "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

                input("Write Y when you are ready to leave.")
        elif logbook_input == "3":
            while True:
            
                print_slow(långöron_lore, TEST)
                sleep(3)
                input("Would you like to go back? Y/N")
                if logbook_input== "Y" or logbook_input== "y":
                    break
                elif logbook_input== "N" or logbook_input== "n":
                    input("Write Y when you are ready to leave.")
                    if logbook_input== "Y" or logbook_input== "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

                input("Write Y when you are ready to leave.")
        elif logbook_input == "4":
            while True:
            
                print_slow(traveler_lore, TEST)
                sleep(3)
                input("Would you like to go back? Y/N")
                if logbook_input== "Y" or logbook_input== "y":
                    break
                elif logbook_input== "N" or logbook_input== "n":
                    input("Write Y when you are ready to leave.")
                    if logbook_input== "Y" or logbook_input== "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

                input("Write Y when you are ready to leave.")
        elif logbook_input == "5":
            while True:

                print_slow(goblin_lore, TEST)
                sleep(3)
                input("Would you like to go back? Y/N")
                if logbook_input== "Y" or logbook_input== "y":
                    break
                elif logbook_input== "N" or logbook_input== "n":
                    input("Write Y when you are ready to leave.")
                    if logbook_input== "Y" or logbook_input== "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

                input("Write Y when you are ready to leave.")

        elif logbook_input == "6":
            while True:
            
                print_slow(kunigunda_lore, TEST)
                sleep(3)
                input("Would you like to go back? Y/N")
                if logbook_input== "Y" or logbook_input== "y":
                    break
                elif logbook_input== "N" or logbook_input== "n":
                    input("Write Y when you are ready to leave.")
                    if logbook_input== "Y" or logbook_input== "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

        elif logbook_input == "7":
            while True:
            
                print_slow(baronen_lore, TEST)
                sleep(3)
                input("Would you like to go back? Y/N")
                if logbook_input== "Y" or logbook_input== "y":
                    break
                elif logbook_input== "N" or logbook_input== "n":
                    input("Write Y when you are ready to leave.")
                    if logbook_input== "Y" or logbook_input== "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

        elif logbook_input == "8":
            while True:
            
                print_slow(pococurante_lore, TEST)
                sleep(3)
                input("Would you like to go back? Y/N")
                if logbook_input== "Y" or logbook_input== "y":
                    break
                elif logbook_input== "N" or logbook_input== "n":
                    input("Write Y when you are ready to leave.")
                    if logbook_input== "Y" or logbook_input== "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

        elif logbook_input == "9":
            while True:
            
                print_slow(shopkeeper_lore, TEST)
                sleep(3)
                input("Would you like to go back? Y/N")
                if logbook_input == "Y" or logbook_input == "y":
                    break
                elif logbook_input == "N" or logbook_input == "n":
                    input("Write Y when you are ready to leave.")
                    if logbook_input == "Y" or logbook_input == "y":
                        break
                    else:
                        print_slow("Try again.", TEST)
                        continue

        elif logbook_input == "0":
            break

        else:
            print_slow("Try again.", TEST)
            continue