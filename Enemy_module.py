import random as rand

class Enemy():
    
    hp = 0
    spd = 0
    str = 0

# Bandit stats
bandit = Enemy()
bandit.hp = rand.randint(80, 120)
bandit.spd = rand.randint(5, 15)
bandit.str = rand.randint(5, 15)

def Enemy_levelup():
    hp = hp*1.125
    spd = spd*1.125
    str = str*1.125