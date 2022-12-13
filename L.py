import random as rand

locations=["skogen","bulgarien","lissabon","venedig","turkiet","sydamerika","afrika","england","havet","fältet","tibble"]


#TEXTER OCH DESCRIPTIONER OM VAR MAN ÅKER

#SKOGEN
skogen_travel_description1 = '''
Du åker till ksog
'''
skogen_travel_description2 = '''
ksokg nu bor du skogen för alltid
'''
skogen_travel_description3 = '''
uhhushudh skogen
'''
skogen_travel_description_list = [skogen_travel_description1, skogen_travel_description2, skogen_travel_description3]



#BULGARIEN
bulgarien_travel_description1 = '''
ububugbug
'''
bulgarien_travel_description2 = '''
du blev våldtagen
'''
bulgarien_travel_description3 = '''
fuck uou bulgarien
'''
bulgarien_travel_description_list = [bulgarien_travel_description1, bulgarien_travel_description2, bulgarien_travel_description3]



#LISSABON
lissabon_travel_description1 = '''
lissaboin mer som pissabon
'''
lissabon_travel_description2 = '''
pissabon go brrr
'''
lissabon_travel_description3 = '''
guh inte lissbon buruh
'''
lissabon_travel_description_list = [lissabon_travel_description1, lissabon_travel_description2, lissabon_travel_description3]



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




def TravelDescription(chosen_location):

    #FÖR ATT LÄGGA TILL FLER PLATSER, LÄGG TILL I LISTAN LOCATIONS ÖVER, OCH SEDAN KOPIERA EN RAD HÄR
    #OCH BYT UT VÄRDENA MOT RÄTT PLATSNAMN. DU MÅSTE ÄVEN SKAPA mist 2 plats_tavel_text OCH 1 plats_travel_description_list.

    if chosen_location == locations[locations.index("skogen")]:
        return rand.choice(skogen_travel_description_list)
    elif chosen_location == locations[locations.index("bulgarien")]:
        return rand.choice(bulgarien_travel_description_list)
    elif chosen_location == locations[locations.index("lissabon")]:
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
