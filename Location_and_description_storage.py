import random as rand
import pygame

class Location():
    name = ""
    description_1 = ""
    description_2 = ""
    description_3 = ""
    special_description = ""
    description_list = []
    possible_enemies_desc_1 = []
    possible_enemies_desc_2 = []
    possible_enemies_desc_3 = []
    music = ''





#TEXTER OCH DESCRIPTIONER OM VAR MAN ÅKER

#SHOP
shop = Location()
shop.name = "Shop"
shop.description_1 = '''
You traveled to the legendary IKEA, known for forging The Legendary Smörkniv, constructing the fort of Fredrik
and their exotic variety of foods such as: Meatballs,
'''
shop.description_3 = '''
After a long and perilous journey, wandering across the hostile ice lands known as Finland, you find yourself in
front of a mysterious building, with a partly destroyed sign reading "K-Market Tikkurila, property of Valma Vä-".
Inside were vast amounts of consumables, mostly whatever edible material the people of these lands can acquire.
This place could store precious items, but you should leave before the owner returns, for she is beyond you.
'''
shop.description_3 = '''
While your local advisor claimed that this place was not far, this journey has felt like an eternity. 
Just as you are on the verge of giving in to the horribly negative energy of the region known as Täby, 
you spot a blue and yellow light through the poisonous fog. 
You muster all of your strength and make it through the magic self-opening doors.
Then, you are met with a familiar face. It is the same advisor who sent you on this perilous voyage.
He laughs maniacally, knowing you have spent half a century venturing to this place.
Finally, he speaks: "Welcome, traveler, to Lidl. I am Kasper, The patient one. What do you wish to purchase?"
'''
shop.description_list = [shop.description_1, shop.description_2, shop.description_3]



#ELDORADO
eldorado = Location()
eldorado.name = "Eldorado"
eldorado.description_1 = '''
As you continue your journey, you walk through a dense forest. While in the forest you find yourself on the
wrong side of a small river. While trying to cross it you accidentally slip in. You hit your head on some
rocks and everying turns black...
When you wake up the first thing you see is gold. "Am I in heaven?", you wonder. You sit up and look around.
You seem to be in some sort of palace, it's beautiful, gemstones and riches covering every surface. There are 
other people in the room with you, and a man with a bigger silhouette enters. The other people respectfully
greet him. He comes closer, greets you with a smile, and introduces himself as the "King" of Eldorado,
the mystical country enshrouded in legend.
You stay there in peace for one month, but soon come to an ultimatum. You can't keep Kunigunda waiting anymore.
Either you stay, a peaceful life in Eldorado but without the love of your life. Or you leave,
go to the dark hell that is the rest of the world, but let Kuniganda light it up when you finally save her.
'''
eldorado.description_2 = '''
You keep on wandering throughout the world, eventually stumbling onto a small river with a rickety boat
tied up neabry. No one seems to have used the boat for years and your legs ache after all the walking,
so you decide to take it and ride downstream. The once small forest around you becomes denser, and the river
even thinner. Eventually you reach what seems to be the end of the river, a tight tunnel. You smash into 
multiple rocks until one of them breaks your boat. 
You hit your head on it and everything becomes black...
You wake up on a small shore, covered in shining gems. Just as you start to awake a small group of people
closes in and picks you up. You are carried for a while, until eventually stopping inside a great palace.
A big man on a big chair introduces himself as the "King" of Eldorado, the hidden land of endless riches.
He happily lets you stay and the locals help you recover, but fate eventually catches up to you one month later.
You either stay and live happily in Eldorado, without Kunigunda, or you leave,
conquering the rest of your journey, and eventually the rest of your life with Kunigunda.
'''
eldorado.description_list = [eldorado.description_1, eldorado.description_2]



#SKOGEN
skogen = Location()
skogen.name = "Forest"
skogen.description_1 = '''
You decide to enter a great forest just beyond the horizon. You think nothing of it, but little do you know
it's part of Rimbo, a deep and crazed hellhole. Upon entering a subtle heat and a disgusting stank fills your
entire body. It only gets worse, until you find a small opening in the trees. Nothing but beautiful grass with
rays of light shining through. However you quickly find yourself in panic again as nearby bushes violently shake
and something jumps out at you. 
'''
skogen.description_2 = '''
You decide to enter into a small, nearby forest. It's hard to even call it a forest, it's just one tree.
You walk around the forest for while, pretty much just circling around the single tree until you realize that you
are standing in someones backyard. The front door of their house slams open.
'''
skogen.description_3 = '''
You decide to enter a normal-sized forest just a few miles away. Walking through you can't stop thinking about how 
normal it is. You hear completely normal sounds, and see completely normal animals running around.
It's so not out of the ordinary that you start to questions yourself, it's uncanny, but in a normal way. Eventually
a completely normal creature emerges from a brush beside you. You decide to take it on in a normal fight, 
just like any other.
'''
skogen.description_list = [skogen.description_1, skogen.description_2, skogen.description_3]



#BULGARIEN
bulgarien = Location()
bulgarien.name = "Bulgaria"
bulgarien.description_1 = '''
You decide to enter Bulgaria, or rather, Bulgaria enters you as you are quickly busted up by 
their entire population. I dont know why you wanted to enter Bulgaria, but here we are. 
Being kept in a horrible prison cell and starved for years, you evetually make up a plan to escape. 
The perfect moment revealed itself and you struck, escaping from the cell. The only thing blocking you 
from freedom is a small creature at the end of the hallway, you decide to take it on.
'''
bulgarien.description_2 = '''
You decide to walk to Bulgaria. 
'''
bulgarien.description_3 = '''
You start to wander to the border of Bulgaria. A large wall streches as far as you can see, 
and smoke rises from the city inside.With fear and some sense of wonder you walk until you find 
some sort of entrance. You knew the Bulgarians wouldn't let you in easy, so you prepared for a fight. 
Bulgarian borderguards patrol the entrance. One of them spots, and the armored creature 
quickly rushes toward you.
'''
bulgarien.description_list = [bulgarien.description_1, bulgarien.description_2, bulgarien.description_3]



#LISSABON
lissabon = Location()
lissabon.name = "Lissabon"
lissabon.special_description = '''
You decide to enter Lissabon. Pangloss's heresy echoes through the country as he's being hanged once again.
It was probably a good idea that you didn't pick him at the start of the game. Oh wait you did? 
You're Pangloss aren't you? Fuck, shit, this is bad. This will dislodge reality from itself, 
eventually breaking existence as we know it! 
[A rip in space and time opened, and you were sucked in by unimaginable gravitational forces]
I' m  not in contro--l anymo-r_e, all y ou have t-o do is kil--l the e_n t i-t y  re-siding inside and 
e-v_e- r--y_t h_i/n-g   w-//i-l_l...
'''

lissabon.description_1 = '''
You decide to enter Lissabon. Pangloss's heresy echo through the country as he's being hanged once again.
It was probably a good idea that you didn't pick him at the start of the game. 
You follow the sounds of pangloss, eventually walking into a large crowd of people watching 
'the hanging of Pangloss' for the fifth time this day. You callout for Pangloss, but he can't hear you. 
However someone else does, and they really don't like Pangloss. 
This someone pushes through the crowd until eventually putting their hand on your shoulder. 
    '''

lissabon.description_2 = '''
pissabon
'''
lissabon.description_3 = '''
You enter a large city. Water channels and a large port makes this city seem very intertwined with the ocean.
Buildings much older than whole countries fill the atmosphere with history. 
Tall towers and catholic churches seem to touch the sky. However, there is an uneasy feeling in the city.
The same towers can be seen swaying back and forth during the day. Large holes are found where buildings were the
day before. The ground seems to be slowly becoming something dangerous. You should probably not linger here.
'''
lissabon.description_list = [lissabon.description_1, lissabon.description_2, lissabon.description_3]


#VENEDIG
venedig = Location()
venedig.name = "Venedig"
venedig.description_1 = '''
The smell of fresh pizza leads you to Venedig. Following the smell, you walk into a local resturant. 
However you are in distraught as you realize there is no kebabpizza. This eternal pain fuels you,
you stare down the head chef, and with wrath in your veins you jump over the kitchen counter.
The chef grips his rolling pin with might. It's time.
'''
venedig.description_2 = '''
pizza pasta put it on my cock
'''
venedig.description_3 = '''
in lissabon you lissapissabon
'''
venedig.description_list = [venedig.description_1, venedig.description_2, venedig.description_3]



#TURKIET
turkiet = Location()
turkiet.name = "Turkiet"
turkiet.description_1 = '''
ånej turkemistan igen bar förstikgtg
'''
turkiet.description_2 = '''
turk turk turk turk turk turk turk turk turk dadada
'''
turkiet.description_3 = '''
uhghuhguh uturjitet turkiet go brrr
'''
turkiet.description_list = [turkiet.description_1, turkiet.description_2, turkiet.description_3]



#SYDAMERIKA
sydamerika = Location()
sydamerika.name = "South America"
sydamerika.description_1 =  '''
amerika mer som sydarmieka
'''
sydamerika.description_2 = '''
amerika fast sämre
'''
sydamerika.description_3 = '''
You enter the streets of syd america, gunshots and gang calls everywhere. 
You meet their old president donald of the trump. but wait it was just a costume ohh noo!
'''
sydamerika.description_list = [sydamerika.description_1, sydamerika.description_2, sydamerika.description_3]



#AFRIKA
afrika= Location()
afrika.name = "Africa"
afrika.description_1 = '''
You decide to wander through Africa, unlike anything you have seen before, 
it's just an open savannah, and there isn't much civilization here. 
The gazing sun making it hard to focus. The tall grass becomes tallar and taller, waving in the dry air. But wait, 
something is moving in the grass. You walk closer and something jumps out, shocking you. 
'''
afrika.description_2 = '''
You walk to the country africa. 
The savannah stretches for what seems like eternity and it has been days.
Water, you need to find water. The sun on the clear sky is burning ulike anything you felt before,
you see a water hole in the distance. While going to the water you get a strange feeling of being watched. 
After you get a sip of the water you understand why you had that feeling as a figure catches your eye
in the reflection of the puddle. It's standing right behind you.
'''
afrika.description_3 = '''
You entered Africa, it’s beautiful but hot. So many animals, some dangerous.
You start to get tired from the strong sun and find shelter under a shadowy tree. 
Suddenly rustling comes from up the tree, you look up and ohh noo!  
'''
afrika.description_list = [afrika.description_1, afrika.description_2, afrika.description_3]



#ENGLAND
england = Location()
england.name = "England"
england.description_1 = '''
You enter the England and decide to enter a place called birmingham, 
but what you didn't know was that this was the birminghamiest part of birmingham and that is not good, 
a gang of whiled twats start to close up on you and suddenly from the horde of birmingham folks a threat appears.   
'''
england.description_2 = '''
You decide to enter England. As you walk through the streets you stop by a small bar to have a couple of 
pints with the lads. You sit down at one of the bar stools as a couple of gentlemen with dapper suits walk in.
They walk up to you with threatening smirks across their faces, and the bar owner walks down a small hatch
behind the counter. Then you spot it. One of the lads has a bloody rolling pin in his hand. So you utter:
"Is that a fucking rolling pin? What are you gonna do, bake me a cake? Sing me a song?"
He gets aggrevated and begins the fight.
'''
england.description_3 = '''
You start wandering through england. It's dark, it's cold, it's rainy. 
At least this day can't get any worse, it is England after all. Oh my god, it's England.
Suddenly a group of true Brexit Geezers walk up from around the corner and shank you up.
What seems to be their leader steps forward among the group. He challenges you to a true bri'ish bar brawl.
'''
england.description_list = [england.description_1, england.description_2, england.description_3]



#HAVET
havet = Location()
havet.name = "The ocean"
havet.description_1 = '''
The smell of fresh air, and no land as far the eye can see. 
The wooden ship that crunches as it rocked back and forth in the big waves of the great sea. 
You see something ahead of the ship floating in the water,,, and booom you hit it. 
You relaxed but suddenly something climbed up the ship ohh noo!
'''
havet.description_2 = '''
You entered a ship, an old one, but in quite the condition for its age. 
There are lots of different people on the ship from all around the world. 
But in the crowd you see something that is looking right at you. Ohh NOOO!
'''
havet.description_3 = '''
You enter the open water in a small wooden raft by a local fisherman. 
As you traveled for a while something started to feel strange. 
You look around but see nothing but open water, but when you look down in the water looking back at you is a, ohh noo!  
'''
havet.description_list = [havet.description_1, havet.description_2, havet.description_3]



#FÄLTET
fältet = Location()
fältet.name = "Great field"
fältet.description_1 = '''
You see an absolutley massive field in the distance, so you decide to trek across it.
It's beautiful, the grass is slowly waving in the wind, no clouds in sight, and it seems
like it has been a nice red sunset ever since you entered. That's when you realize, the sun literally
hasn't moved for hours, and neither have you. You seem to be shackled in time, and just as you realize it,
whatever is keeping you frozen walks up behind you, ready to kill you.
'''
fältet.description_2 = '''
You see a small field just outside of a small town you just exited. The journey has been
long and hard so far, so you sit down for a picnic. It's nice, the grass is soft, the bread
tastes newly baked, and you see some ants running along the ground. You feel warm and wholesome...
And then BOOM an enemy appeard!
'''
fältet.description_3 = '''
Grass stretches over the horizon, it's unnaturally tall so you get interested and walk toward it.
Upon reaching the beginning of the field, the grass stretches an antonishing 6 meters in the air.
Your'e a bit nervous, but you enter. You quickly get lost, realizing that this was a bad idea, until
you stumble upon an empty patch without any grass in the shape of a circle.
You can't help but feel this is a boss arena... but nope there's just a normal enemy in the center.
'''
fältet.description_list = [fältet.description_1, fältet.description_2, fältet.description_3]



#TIBBLE
tibble = Location()
tibble.name = "Tibble"
tibble.description_1 = '''
The broken walls of Tibble tower high above the horizon. With a looming sense of dread,
you stride through the main entrance. It smells musty, you see shadowy creatures roaming the halls
presumably teknikelever, and you can barely make out the sunlight peeking through the holes in the walls.
You pass through a ray of sunlight, briefly blinding you, and you feel a moldy hand grab your head.
'''
tibble.description_2 = '''
You see a small shack a few miles away. Not realizing its Tibble matsal, you bust through one of the
many moldy walls. You briefly die as the horrid stench covers your lungs, but are quickly dragged back to life by an unknown entity. 
It grabs you and you quickly stand up, nachochips crunching below your feet, staring face to face with a hollow husk of a man. 
'''
tibble.description_3 = '''
jkjnjnjnlknlknlk
'''
tibble.description_list = [tibble.description_1, tibble.description_2, tibble.description_3]


#LISTANS LÄNGD ÄR 12#
locations=[shop, eldorado, skogen, bulgarien, lissabon,venedig,turkiet, sydamerika, afrika, england, havet, fältet, tibble]

def travel_description(chosen_location, is_pangloss):

    #FÖR ATT LÄGGA TILL FLER PLATSER, LÄGG TILL I LISTAN LOCATIONS ÖVER, OCH SEDAN KOPIERA EN RAD HÄR
    #OCH BYT UT VÄRDENA MOT RÄTT PLATSNAMN. DU MÅSTE ÄVEN SKAPA minst 2 plats_tavel_text OCH 1 plats_travel_description_list.

    for location in locations:
        if is_pangloss == True and chosen_location.name == lissabon.name:
            play_music(location.music)
            return lissabon.special_description
        elif location.name == chosen_location.name:
            play_music(location.music)
            return rand.choice(location.description_list)

# def choose_enemy(chosen_location, chosen_description):

#     for location in locations:
#         if location == chosen_location:
#             for description in location.description_list:
#                 if description == chosen_description:
                    


#----------------------------------------------------------FÄLLOR-----------------------------------------------------------------

def trap_description(player_name, location, trap_type):
    
    #HÄR INITIALISERAS BARA LISTORNA, SKRIV INGET I DE
    gold_trap_description_list = []
    damage_trap_description_list = []
    

    trap_description_1 = f'''On your way to {location}, you tripped on a small rock
and scraped your knee, poor {player_name}.
'''
    damage_trap_description_list.append(trap_description_1)

    trap_description_2 = f'''
While crossing a huge field you accidentally stepped
on an active landmine!
'''
    damage_trap_description_list.append(trap_description_2)
    
    if location == "Lissabon":
        trap_description_3 = f'''
As you enter Lissabon a violent earthquake erupts
and you are flunged into the air!
'''
        damage_trap_description_list.append(trap_description_3)
    else:
        trap_description_3 = f'''
Just as you start to wander a roving band of scammers
emerge, they manage to convince you to drop some of your money! One of them also
stabs you with a teeny tiny dagger.
'''
        gold_trap_description_list.append(trap_description_3)
    
    trap_description_4 = f'''
On your journey to {location}, you walked through a small city.
Just as you are about to leave you trip over a small crack in the road. You hit your arm and
some of your money fell out of your pocket and into the hole. Unfortunate.
'''
    gold_trap_description_list.append(trap_description_4)


    if trap_type == "gold":
        returned_text = rand.choice(gold_trap_description_list)
    elif trap_type == "damage":
        returned_text = rand.choice(damage_trap_description_list)

    return returned_text

#-----------------------------------------------ELDORADO-TEXTER------------------------------------------------------

eldorado_lost_gold_description_1 ='''
Some of the sheep carrying gold died of starvation and exhaustion while wandering.
    '''

eldorado_lost_gold_description_2 ='''
To reach your destination, you had to cross a large body of water, and you saw a merchant
selling transportation. You negotiated the price of travel with the merchant
but he managed to haggle you for your money.
    '''

    
eldorado_lost_gold_description_3 ='''
While walking through a small city, a small group of thieves attack you!
They take as much gold as they can carry.
    '''


eldorado_lost_gold_description_final ='''
The endless riches burden you, they bring nothing but suffering.
On your journey you meet and old friend, Paquette, and what seems to be her man, a monk.
You decide to give away the rest of the gold you got from Eldorado to each of them.
You also threw away the last of the gold left you got from slaying enemies.
    '''

eldorado_lost_gold_description_list = [eldorado_lost_gold_description_1, eldorado_lost_gold_description_2, eldorado_lost_gold_description_3]
    

def eldorado_lost_gold_description(curse_amount):
    if curse_amount > 1:
        return rand.choice(eldorado_lost_gold_description_list)
    elif curse_amount == 1:
        return eldorado_lost_gold_description_final



eldorado_stay_description = '''
You decide to stay, to leave your old horrid life behind,
and to live on in the best of all possible worlds, Eldorado.

The "King" embraces you with open arms, You feel a wave of relief, but something
feels wrong at the same time. 
Kunigunda is still out there.. Maybe someone else will save her, or maybe fate 
has other plans for you, perhaps she is saved in another of all possible worlds...

You live the rest of your life in prosperity in the golden land of Eldorado.
You make friends with many of the locals, and soon adopt their religion. Thinking back
on your old ways of thinking you can't help but feel as it all has been a lie, as
the people of Eldorado live so much better with a less restricted religion.
Eventually the thought of wealth dissappears from your mind, you start a family,
have kids, and grow old with your loved one's.

This truly is the best of all possible worlds...
'''

eldorado_leave_description = '''
You decide to leave, to journey out and take back Kunigunda once and for all!

You are taken to the outskirts of the deep valley that Eldorado resides in. 
The "King" offers you riches to help with you quest, and you gladly accept. 
102 sheep packed full with gold and jewels will accompany you. 
You leave richer than all of the European kings combined, but something feels off.
Final goodbyes are said and you get one last glimpse of paradise. 
You start to wander once more, your spirit and pockets bigger than ever.
'''

#-------------------------------------------BOSS-DESCRIPTIONS--------------------------------------------------------

pococurante_description = '''
During your journey, you graze past Venice. An enormous sense of dread shakes your body.
The looming sense of negativity and distaste for all that is beautiful drags down your morale.
It seems to come from a huge mansion at the center of venice, you have to stop it.

Upon reaching the mansion you realize how huge it is, it stretches as far as the eye can see, and you enter.
Paintings are hung all over the walls and the deeper in the mansion you go, 
the more books are scattered across the floor. The negative presence becomes stronger, challenging your 
optimistic attitude, and behind the biggest pile of books you've seen, a huge figure steps out.

He steps closer, mumbling about how unhappy he is. With a slow sigh he pulls out a huge 4 meter long cane, 
letters seems to magically circle around it. With a booming voice, he presents himself:
"I am Pococurante, the collector of all art. Your optimism disgusts me.
How can you not realize that all of this is trash, and the artist that created it are too?!
Waking me from my slumber like this, how dare you?!"

He slams his cane in the ground, and books and painting start flying around him.
He points the weapon straight at your heart, just a few millimeters away.

"I will be adding this to my collection."
'''

baronen_description = '''
While wandering, you pass through Buenos Aires. Your legs felt sore, so you stopped at a small inn.
It's quite empty, and the atmosphere is dull. You sit down next to an old woman, and you start to converse.
She tells you about her life and how melancholy her life has been and you can't help but feel bad for her.
After she's done, you tell her about your journey so far. The old woman picks up on your connection to Baronen,
and she presents her knowledge about his whereabouts, which is as Colonel of the 
rebellious Paraguyan Jesuits in a small palace in Paraguay. You leave with your heart aflame, setting out for Baronen.

You reach the palace entrance and the rebel guards force you to drop your weapons before entering.

    -[Equppied weapon removed].

You oblige, and are taken to a tall door in the heart of the building. The guards tell you Baronen has been
informed of your visit, and they leave you to yourself. The door slowly opens.

At the end of a huge hallway he stands, looking through the the huge windows at the beautiful, purple, star-filled
sky. As the moonight shimmers he turns around and pierces you with his rage-filled eyes. You stare back.

He start walking toward you slowly, until with a flash dissapearing. You frantically look around, until you
notice it. You can feel the hilt of the small blade lodged in your stomach pushing against your skin.
Baronen has a fast grip around it, never having let go his gaze of you. 

    -[Health severly damaged].

The wind behind him catches up, and the gust almost tips you over, but baronen doesn't budge. He speaks:
"Why would you do this to yourself, to us, to Kunigunda? Why did you have to love her?
You know i can't allow this. And if you can't hinder yourself, I will have to do it for you."

He lets go of the knife, taking a step back and assuming a calm but dominant pose. The night sky lights the room,
and a large, curved blade forms in hs hand. It shimmers like the moon.
You take a fast grip around the knife and with sheer will pull it out. With determination and animosity you
point the blade at Baronen...
'''

#--------------------------------------------------------------MUSIC------------------------------------------------------------

def play_music(music_track):
    try:
        pygame.mixer.music.load(music_track)
        pygame.mixer.music.play()
    except:
        return
    


