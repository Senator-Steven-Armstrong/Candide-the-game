import random as rand

#LISTANS LÄNGD ÄR 12
locations=["eldorado", "skogen","bulgarien","lissabon","venedig","turkiet","sydamerika","afrika","england","havet","fältet","tibble"]

#TEXTER OCH DESCRIPTIONER OM VAR MAN ÅKER

#SKOGEN
skogen_travel_description1 = '''
You decide to enter a great forest just beyond the horizon. You think nothing of it, but little do you know
it's part of Rimbo, a deep and crazed hellhole. Upon entering a subtle heat and a disgusting stank fills your
entire body. It only gets worse, until you find a small opening in the trees. Nothing but beautiful grass with
rays of light shining through. However you quickly find yourself in panic as nearby bushes violently shake. 
'''
skogen_travel_description2 = '''
You decide to wander into a small, nearby forest. It's hard to even call it a forest, it's pretty much just one tree.
You walk around the forest for while, pretty much just circuling around the single tree until you realize that you
are standing in someones backyard. The front door of their house slams open.
'''
skogen_travel_description3 = '''
You decide to enter a normal-sized forest just a few miles away. Walking through you can't stop thinking about how 
normal it is. You hear completely normal sounds, and see completely normal animals running around.
It's so not out of the ordinary that you start to questions yourself, it's uncanny, but in a normal way. Eventually
a completely normal creature emerges from a brush beside you. You decide to take it on in a normal fight, just like any other.
'''
skogen_travel_description_list = [skogen_travel_description1, skogen_travel_description2, skogen_travel_description3]



#BULGARIEN
bulgarien_travel_description1 = '''
You decide to enter Bulgaria, or rather, Bulgaria enters you as you are quickly busted up by their entire population.
I dont know why you wanted to enter Bulgaria, but here we are. Being kept in a horrible prison cell and starved for 
years, you evetually make up a plan to escape. The perfect moment revealed itself and you struck, escaping from the cell.
The only thing blocking you from freedom is a small creature at the end of the hallway, you decide to take it on.

'''
bulgarien_travel_description2 = '''
Du blev våldtagen
'''
bulgarien_travel_description3 = '''
You start to wander to the border of Bulgaria. A large wall streches as far as you can see, and smoke rises from the city inside.
With fear and some sense of wonder you walk until you find some sort of entrance. You knew the Bulgarians wouldn't let you in easy,
so you prepared for a fight. Bulgarian borderguards patrol the entrance. One of them spots, and the armored creature 
quickly rushes toward you.
'''
bulgarien_travel_description_list = [bulgarien_travel_description1, bulgarien_travel_description2, bulgarien_travel_description3]



#LISSABON
lissabon_travel_description1 = ''' '''

lissabon_travel_description1_pangloss = '''
You decide to enter Lissabon. Pangloss's heresy echoes through the country as he's being hanged once again.
It was probably a good idea that you didn't pick him at the start of the game. Oh wait you did? You're Pangloss
aren't you? Fuck, shit, this is bad. This will dislodge reality from itself, 
eventually breaking existence as we know it! 
[A rip in space and time opened, and you were sucked in by unimaginable gravitational forces]
I' m  not in contro--l anymo-r_e, all y ou have t-o do is kil--l the e_n t i-t y  re-siding inside and e-v_e- r--y_t h_i/n-g   w-//i-l_l...
'''

lissabon_travel_description1 = '''
You decide to enter Lissabon. Pangloss's heresy echo through the country as he's being hanged once again.
It was probably a good idea that you didn't pick him at the start of the game. You follow the sounds of pangloss,
eventually walking into a large crowd of people watching 'the hanging of Pangloss for the fifth time this day'. You call
out for Pangloss, but he can't hear you. However someone else does, and they really don't like Pangloss. 
This someone pushes through the crowd until eventually putting their hand on your shoulder. 
    '''

lissabon_travel_description2 = '''
pissabon go brrr
'''
lissabon_travel_description3 = '''
guh inte lissbon buruh
'''
lissabon_travel_description_list = [lissabon_travel_description1, lissabon_travel_description2, lissabon_travel_description3]
lissabon_travel_description_list_pangloss = [lissabon_travel_description1_pangloss, lissabon_travel_description2, lissabon_travel_description3]


#VENEDIG
venedig_travel_description1 = '''
bubuebuab venedig
'''
venedig_travel_description2 = '''
pizza pasta put it on my cock
'''
venedig_travel_description3 = '''
in lissabon you lissapissabon
'''
venedig_travel_description_list = [venedig_travel_description1, venedig_travel_description2, venedig_travel_description3]



#TURKIET
turkiet_travel_description1 = '''
ånej turkemistan igen bar förstikgtg
'''
turkiet_travel_description2 = '''
turk turk turk turk turk turk turk turk turk dadada
'''
turkiet_travel_description3 = '''
uhghuhguh uturjitet turkiet go brrr
'''
turkiet_travel_description_list = [turkiet_travel_description1, turkiet_travel_description2, turkiet_travel_description3]



#SYDAMERIKA
sydamerika_travel_description1 = '''
amerika mer som sydarmieka
'''
sydamerika_travel_description2 = '''
amerika fast sämre
'''
sydamerika_travel_description3 = '''
oog sydamerika
'''
sydamerika_travel_description_list = [sydamerika_travel_description1, sydamerika_travel_description2, sydamerika_travel_description3]



#AFRIKA
afrika_travel_description1 = '''
ooga boooga bo
'''
afrika_travel_description2 = '''
ooga afrika ooga
'''
afrika_travel_description3 = '''
välkommen till afrika uhmmm
'''
afrika_travel_description_list = [afrika_travel_description1, afrika_travel_description2, afrika_travel_description3]



#ENGLAND
england_travel_description1 = '''
briiiisihs
'''
england_travel_description2 = '''
bohowoho
'''
england_travel_description3 = '''
boston tea party i love tea who inveted this kid
'''
england_travel_description_list = [england_travel_description1, england_travel_description2, england_travel_description3]



#HAVET
havet_travel_description1 = '''
splash splash
'''
havet_travel_description2 = '''
du klev ombord skeppet som en ajousfhiuanfljaof
'''
havet_travel_description3 = '''
fish
'''
havet_travel_description_list = [havet_travel_description1, havet_travel_description2, havet_travel_description3]



#FÄLTET
fältet_travel_description1 = '''
wow det är väldigt fint utanför lokes hus
'''
fältet_travel_description2 = '''
väldigt fint fält jag älskar detta fält
'''
fältet_travel_description3 = '''
jag har skitiet ner mig
'''
fältet_travel_description_list = [fältet_travel_description1, fältet_travel_description2, fältet_travel_description3]



#TIBBLE
tibble_travel_description1 = '''
du kliver in i de mörka korridorerna, rädlsa sprids över hela din kropp.
'''
tibble_travel_description2 = '''
tibble elever go brrrr
'''
tibble_travel_description3 = '''
du dog (du gick in i tibble.)
'''
tibble_travel_description_list = [tibble_travel_description1, tibble_travel_description2, tibble_travel_description3]




def TravelDescription(chosen_location, is_pangloss):

    #FÖR ATT LÄGGA TILL FLER PLATSER, LÄGG TILL I LISTAN LOCATIONS ÖVER, OCH SEDAN KOPIERA EN RAD HÄR
    #OCH BYT UT VÄRDENA MOT RÄTT PLATSNAMN. DU MÅSTE ÄVEN SKAPA mist 2 plats_tavel_text OCH 1 plats_travel_description_list.

    if chosen_location == locations[locations.index("skogen")]:
        return rand.choice(skogen_travel_description_list)
    elif chosen_location == locations[locations.index("bulgarien")]:
        return rand.choice(bulgarien_travel_description_list)
    elif chosen_location == locations[locations.index("lissabon")]:
        if is_pangloss == True:
            return rand.choice(lissabon_travel_description_list_pangloss)
        else:
            return rand.choice(lissabon_travel_description_list)
    elif chosen_location == locations[locations.index("venedig")]:
        return rand.choice(venedig_travel_description_list)
    elif chosen_location == locations[locations.index("turkiet")]:
        return rand.choice(turkiet_travel_description_list)
    elif chosen_location == locations[locations.index("sydamerika")]:
        return rand.choice(sydamerika_travel_description_list) 
    elif chosen_location == locations[locations.index("afrika")]:
        return rand.choice(afrika_travel_description_list)
    elif chosen_location == locations[locations.index("england")]:
        return rand.choice(england_travel_description_list) 
    elif chosen_location == locations[locations.index("havet")]:
        return rand.choice(havet_travel_description_list)
    elif chosen_location == locations[locations.index("fältet")]:
        return rand.choice(fältet_travel_description_list)
    elif chosen_location == locations[locations.index("tibble")]:
        return rand.choice(tibble_travel_description_list) 
