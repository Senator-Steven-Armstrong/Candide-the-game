import random as rand
import pygame

pygame.mixer.init()

class Location():
    name = ""
    description_list = []
    rarity = 100

class Description():
    music = ''
    description = ""
    possible_enemies = []



#TEXTER OCH DESCRIPTIONER OM VAR MAN ÅKER

#SHOP
shop = Location()
shop.name = "Shop"
shop.rarity = 65

shop1 = Description()
shop1.description = '''
You traveled to the legendary IKEA, known for forging The Legendary Smörkniv, constructing the fort of Fredrik
and their exotic variety of foods such as: Meatballs,
'''
shop1.music = 'sounds/shopmusic.mp3'

shop2 = Description()
shop2.description = '''
After a long and perilous journey, wandering across the hostile ice lands known as Finland, you find yourself in
front of a mysterious building, with a partly destroyed sign reading "K-Market Tikkurila, property of Valma Vä-".
Inside were vast amounts of consumables, mostly whatever edible material the people of these lands can acquire.
This place could store precious items, but you should leave before the owner returns, for she is beyond you.
'''
shop2.music = 'sounds/shopmusic.mp3'

shop3 = Description()
shop3.description = '''
While your local advisor claimed that this place was not far, this journey has felt like an eternity. 
Just as you are on the verge of giving in to the horribly negative energy of the region known as Täby, 
you spot a blue and yellow light through the poisonous fog. 
You muster all of your strength and make it through the magic self-opening doors.
Then, you are met with a familiar face. It is the same advisor who sent you on this perilous voyage.
He laughs maniacally, knowing you have spent half a century venturing to this place.
Finally, he speaks: "Welcome, traveler, to Lidl. I am Kasper, The patient one. What do you wish to purchase?"
'''
shop3.music = 'sounds/shopmusic.mp3'

shop.description_list = [shop1, shop2, shop3]



#ELDORADO
eldorado = Location()
eldorado.name = "Eldorado"
eldorado.rarity = 20

eldorado1 = Description()
eldorado1.description = '''
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
eldorado1.music = ''

eldorado2 = Description()
eldorado2.description = '''
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
eldorado2.music = ''

eldorado.description_list = [eldorado1, eldorado2]



#SKOGEN
skogen = Location()
skogen.name = "Forest"

skogen1 = Description()
skogen1.description = '''
You decide to enter a great forest just beyond the horizon. You think nothing of it, but little do you know
it's part of Rimbo, a deep and crazed hellhole. Upon entering a subtle heat and a disgusting stank fills your
entire body. It only gets worse, until you find a small opening in the trees. Nothing but beautiful grass with
rays of light shining through. However you quickly find yourself in panic again as nearby bushes violently shake
and something jumps out at you. 
'''
skogen1.music = 'sounds/ruins.mp3'
skogen1.possible_enemies = ["bandit", "goblin", "rat"]

skogen2 = Description()
skogen2.description = '''
You decide to enter into a small, nearby forest. It's hard to even call it a forest, it's just one tree.
You walk around the forest for while, pretty much just circling around the single tree until you realize that you
are standing in someones backyard. The front door of their house slams open.
'''
skogen2.music = 'sounds/ruins.mp3'
skogen2.possible_enemies = ["bandit", "goblin", "rat"]

skogen3 = Description()
skogen3.description = '''
You decide to enter a normal-sized forest just a few miles away. Walking through you can't stop thinking about how 
normal it is. You hear completely normal sounds, and see completely normal animals running around.
It's so not out of the ordinary that you start to questions yourself, it's uncanny, but in a normal way. Eventually
a completely normal creature emerges from a brush beside you. You decide to take it on in a normal fight, 
just like any other.
'''
skogen3.music = 'sounds/ruins.mp3'
skogen3.possible_enemies = ["bandit", "goblin", "rat"]

skogen.description_list = [skogen1, skogen2, skogen3]



#BULGARIEN
bulgarien = Location()
bulgarien.name = "Bulgaria"

bulgarien1 = Description()
bulgarien1.description = '''
You decide to enter Bulgaria, or rather, Bulgaria enters you as you are quickly busted up by 
their entire population. I dont know why you wanted to enter Bulgaria, but here we are. 
Being kept in a horrible prison cell and starved for years, you evetually make up a plan to escape. 
The perfect moment revealed itself and you struck, escaping from the cell. The only thing blocking you 
from freedom is a small creature at the end of the hallway, you decide to take it on.
'''
bulgarien1.music = 'sounds/ruins.mp3'
bulgarien1.possible_enemies = ["rat", "goblin", "bulgar"]

bulgarien2 = Description()
bulgarien2.description = '''
You decide to walk to Bulgaria. 
'''
bulgarien2.music = 'sounds/ruins.mp3'
bulgarien2.possible_enemies = ["goblin"]

bulgarien3 = Description()
bulgarien3.description = '''
You start to wander to the border of Bulgaria. A large wall streches as far as you can see, 
and smoke rises from the city inside.With fear and some sense of wonder you walk until you find 
some sort of entrance. You knew the Bulgarians wouldn't let you in easy, so you prepared for a fight. 
Bulgarian borderguards patrol the entrance. One of them spots, and the armored guard 
quickly rushes toward you.
'''
bulgarien3.music = 'sounds/ruins.mp3'
bulgarien3.possible_enemies = ["bulgar"]

bulgarien.description_list = [bulgarien1, bulgarien2, bulgarien3]



#LISSABON
lissabon = Location()
lissabon.name = "Lissabon"

lissabon_special = Description()
lissabon_special.description = '''
You decide to enter Lissabon. Pangloss's heresy echoes through the country as he's being hanged once again.
It was probably a good idea that you didn't pick him at the start of the game. Oh wait you did? 
You're Pangloss aren't you? Fuck, shit, this is bad. This will dislodge reality from itself, 
eventually breaking existence as we know it! 
[A rip in space and time opened, and you were sucked in by unimaginable gravitational forces]
I' m  not in contro--l anymo-r_e, all y ou have t-o do is kil--l the e_n t i-t y  re-siding inside and 
e-v_e- r--y_t h_i/n-g   w-//i-l_l...
'''
lissabon_special.music = 'sounds/ruins.mp3'
lissabon_special.possible_enemies = ["chaos entity"]

lissabon1 = Description()
lissabon1.description = '''
You decide to enter Lissabon. Pangloss's heresy echo through the country as he's being hanged once again.
It was probably a good idea that you didn't pick him at the start of the game. 
You follow the sounds of pangloss, eventually walking into a large crowd of people watching 
'the hanging of Pangloss' for the fifth time this day. You callout for Pangloss, but he can't hear you. 
However someone else does, and they really don't like Pangloss. 
This someone pushes through the crowd until eventually putting their hand on your shoulder.
'''
lissabon1.music = 'sounds/ruins.mp3'
lissabon1.possible_enemies = ["goblin", "bandit"]

lissabon2 = Description()
lissabon2.description = '''
pissabon
'''
lissabon2.music = 'sounds/ruins.mp3'
lissabon2.possible_enemies = ["goblin"]


lissabon3 = Description()
lissabon3.description = '''
You enter a large city. Water channels and a large port makes this city seem very intertwined with the ocean.
Buildings much older than whole countries fill the atmosphere with history. 
Tall towers and catholic churches seem to touch the sky. However, there is an uneasy feeling in the city.
The same towers can be seen swaying back and forth during the day. Large holes are found where buildings were the
day before. The ground seems to be slowly becoming something dangerous. You approach one of them, and a creature
slowly emerges toward you.
'''
lissabon3.music = 'sounds/ruins.mp3'
lissabon3.possible_enemies = ["chaos entity"]

lissabon.description_list = [lissabon1, lissabon2, lissabon3, lissabon_special]


#VENEDIG
venedig = Location()
venedig.name = "Venedig"

venedig1 = Description()
venedig1.description = '''
The smell of fresh pizza leads you to Venedig. Following the smell, you walk into a local resturant. 
However you are in distraught as you realize there is no kebabpizza. This eternal pain fuels you,
you stare down the head chef, and with wrath in your veins you jump over the kitchen counter.
The chef grips his rolling pin with might. It's time.
'''
venedig1.music = 'sounds/ruins.mp3'
venedig1.possible_enemies = ["goblin", "chef", "chef"]

venedig2 = Description()
venedig2.description = '''
pizza pasta put it on my cock
'''
venedig2.music = 'sounds/ruins.mp3'
venedig2.possible_enemies = ["goblin"]

venedig3 = Description()
venedig3.description = '''
in lissabon you lissapissabon
'''
venedig3.music = 'sounds/ruins.mp3'
venedig3.possible_enemies = ["goblin"]

venedig.description_list = [venedig1, venedig2, venedig3]



#TURKIET
turkiet = Location()
turkiet.name = "Turkiet"

turkiet1 = Description()
turkiet1.description = '''
ånej turkemistan igen var förstikgtg, Ohhhh noooo!
'''
turkiet1.music = 'sounds/ruins.mp3'
turkiet1.possible_enemies = ''

turkiet2 = Description()
turkiet2.description = '''
turk turk, turk turk, turk turk turk dadada ohhh nooo
'''
turkiet2.music = 'sounds/ruins.mp3'
turkiet2.possible_enemies = ["goblin"]

turkiet3 = Description()
turkiet3.description = '''
uhghuhguh uturjitet turkiet go brrr   Ohhh nooo
'''
turkiet3.music = 'sounds/ruins.mp3'
turkiet3.possible_enemies = ["goblin"]

turkiet.description_list = [turkiet1, turkiet2, turkiet3]



#SYDAMERIKA
sydamerika = Location()
sydamerika.name = "South America"

sydamerika1 = Description()
sydamerika1.description =  '''
amerika mer som sydarmieka
'''
sydamerika1.music = 'sounds/ruins.mp3'
sydamerika1.possible_enemies = ["goblin"]

sydamerika2 = Description()
sydamerika2.description = '''
amerika fast sämre
'''
sydamerika2.music = 'sounds/ruins.mp3'
sydamerika2.possible_enemies = ["goblin"]

sydamerika3 = Description()
sydamerika3.description = '''
You enter the streets of syd america, gunshots and gang calls everywhere. 
You meet their old president donald of the trump. but wait it was just a costume ohh noo!
'''
sydamerika3.music = 'sounds/ruins.mp3'
sydamerika3.possible_enemies = ["goblin"]
sydamerika.description_list = [sydamerika1, sydamerika2, sydamerika3]



#AFRIKA
afrika= Location()
afrika.name = "Africa"

afrika1 = Description()
afrika1.description = '''
You decide to wander through Africa, unlike anything you have seen before, 
it's just an open savannah, and there isn't much civilization here. 
The gazing sun making it hard to focus. The tall grass becomes tallar and taller, waving in the dry air. But wait, 
something is moving in the grass. You walk closer and something jumps out, shocking you. 
'''
afrika1.music = 'sounds/ruins.mp3'
afrika1.possible_enemies = ["goblin"]

afrika2 = Description()
afrika2.description = '''
You walk to the country africa. 
The savannah stretches for what seems like eternity and it has been days.
Water, you need to find water. The sun on the clear sky is burning ulike anything you felt before,
you see a water hole in the distance. While going to the water you get a strange feeling of being watched. 
After you get a sip of the water you understand why you had that feeling as a figure catches your eye
in the reflection of the puddle. It's standing right behind you.
'''
afrika2.music = 'sounds/ruins.mp3'
afrika2.possible_enemies = ["goblin"]

afrika3 = Description()
afrika3.description = '''
You entered Africa, it’s beautiful but hot. So many animals, some dangerous.
You start to get tired from the strong sun and find shelter under a shadowy tree. 
Suddenly rustling comes from up the tree, you look up and ohh noo!  
'''
afrika3.music = 'sounds/ruins.mp3'
afrika3.possible_enemies = ["goblin"]

afrika.description_list = [afrika1, afrika2, afrika3]



#ENGLAND
england = Location()
england.name = "England"

england1 = Description()
england1.description = '''
You enter the England and decide to enter a place called birmingham, 
but what you didn't know was that this was the birminghamiest part of birmingham and that is not good, 
a gang of whiled twats start to close up on you and suddenly from the horde of birmingham folks a threat appears.   
'''
england1.music = 'sounds/ruins.mp3'
england1.possible_enemies = ["goblin"]

england2 = Description()
england2.description = '''
You decide to enter England. As you walk through the streets you stop by a small bar to have a couple of 
pints with the lads. You sit down at one of the bar stools as a couple of gentlemen with dapper suits walk in.
They walk up to you with threatening smirks across their faces, and the bar owner walks down a small hatch
behind the counter. Then you spot it. One of the lads has a bloody rolling pin in his hand. So you utter:
"Is that a fucking rolling pin? What are you gonna do, bake me a cake? Sing me a song?"
He gets aggrevated and begins the fight.
'''
england2.music = 'sounds/ruins.mp3'
england2.possible_enemies = ["goblin"]

england3 = Description()
england3.description = '''
You start wandering through england. It's dark, it's cold, it's rainy. 
At least this day can't get any worse, it is England after all. Oh my god, it's England.
Suddenly a group of true Brexit Geezers walk up from around the corner and shank you up.
What seems to be their leader steps forward among the group. He challenges you to a true bri'ish bar brawl.
'''
england3.music = 'sounds/ruins.mp3'
england3.possible_enemies = ["goblin"]

england.description_list = [england1, england2, england3]



#HAVET
havet = Location()
havet.name = "The ocean"

havet1 = Description()
havet1.description = '''
The smell of fresh air, and no land as far the eye can see. 
The wooden ship that crunches as it rocked back and forth in the big waves of the great sea. 
You see something ahead of the ship floating in the water,,, and booom you hit it. 
You relaxed but suddenly something climbed up the ship ohh noo!
'''
havet1.music = 'sounds/ruins.mp3'
havet1.possible_enemies = ["goblin"]

havet2 = Description()
havet2.description = '''
You entered a ship, an old one, but in quite the condition for its age. 
There are lots of different people on the ship from all around the world. 
But in the crowd you see something that is looking right at you. Ohh NOOO!
'''
havet2.music = 'sounds/ruins.mp3'
havet2.possible_enemies = ["goblin"]

havet3 = Description()
havet3.description = '''
You enter the open water in a small wooden raft by a local fisherman. 
As you traveled for a while something started to feel strange. 
You look around but see nothing but open water, but when you look down in the water looking back at you is a, ohh noo!  
'''
havet3.music = 'sounds/ruins.mp3'
havet3.possible_enemies = ["goblin"]

havet.description_list = [havet1, havet2, havet3]



#FÄLTET
fältet = Location()
fältet.name = "Great field"

fältet1 = Description()
fältet1.description = '''
You see an absolutley massive field in the distance, so you decide to trek across it.
It's beautiful, the grass is slowly waving in the wind, no clouds in sight, and it seems
like it has been a nice red sunset ever since you entered. That's when you realize, the sun literally
hasn't moved for hours, and neither have you. You seem to be shackled in time, and just as you realize it,
whatever is keeping you frozen walks up behind you, ready to kill you.
'''
fältet1.music = 'sounds/ruins.mp3'
fältet1.possible_enemies = ["goblin"]

fältet2 = Description()
fältet2.description = '''
You see a small field just outside of a small town you just exited. The journey has been
long and hard so far, so you sit down for a picnic. It's nice, the grass is soft, the bread
tastes newly baked, and you see some ants running along the ground. You feel warm and wholesome...
And then BOOM an enemy appeard!
'''
fältet2.music = 'sounds/ruins.mp3'
fältet2.possible_enemies = ["goblin"]

fältet3 = Description()
fältet3.description = '''
Grass stretches over the horizon, it's unnaturally tall so you get interested and walk toward it.
Upon reaching the beginning of the field, the grass stretches an antonishing 6 meters in the air.
Your'e a bit nervous, but you enter. You quickly get lost, realizing that this was a bad idea, until
you stumble upon an empty patch without any grass in the shape of a circle.
You can't help but feel this is a boss arena... but nope there's just a normal enemy in the center.
'''
fältet3.music = 'sounds/ruins.mp3'
fältet3.possible_enemies = ["goblin"]

fältet.description_list = [fältet1, fältet2, fältet3]



#TIBBLE
tibble = Location()
tibble.name = "Tibble"

tibble1 = Description()
tibble1.description = '''
The broken walls of Tibble tower high above the horizon. With a looming sense of dread,
you stride through the main entrance. It smells musty, you see shadowy creatures roaming the halls
presumably teknikelever, and you can barely make out the sunlight peeking through the holes in the walls.
You pass through a ray of sunlight, briefly blinding you, and you feel a moldy hand grab your shoulder.
'''
tibble1.music = 'sounds/ruins.mp3'
tibble1.possible_enemies = ["goblin"]

tibble2 = Description()
tibble2.description = '''
You see a small shack a few miles away. Not realizing its Tibble matsal, you bust through one of the
many moldy walls. You briefly die as the horrid stench covers your lungs, but are quickly dragged back to life by an unknown entity. 
It grabs you and you quickly stand up, nachochips crunching below your feet, staring face to face with a hollow husk of a man. 
'''
tibble2.music = 'sounds/ruins.mp3'
tibble2.possible_enemies = ["goblin"]

tibble3 = Description()
tibble3.description = '''
Tibble gymnasium är en fristående gymnasieskola i Stockholms län. 
Tibble gymnasium Campus Täby ligger i Täby kommun i Stockholms län. 
Tibble gymnasium Campus Täby är en gymnasieskola med ca 1600 elever.
'''
tibble3.music = 'sounds/ruins.mp3'
tibble3.possible_enemies = ["goblin"]

tibble.description_list = [tibble1, tibble2, tibble3]


#LISTANS LÄNGD ÄR 12
locations=[shop, eldorado, skogen, bulgarien, lissabon, venedig, turkiet, sydamerika, afrika, england, havet, fältet, tibble]

def choose_description(chosen_location):

    for location in locations:
        if location.name == chosen_location.name:
            chosen_description = rand.choice(location.description_list)
            play_music(chosen_description.music)
            return chosen_description
                 


#----------------------------------------------------------FÄLLOR-----------------------------------------------------------------



def trap_description(player_name, location, trap_type):
    
    #HÄR INITIALISERAS BARA LISTORNA, SKRIV INGET I DE
    gold_trap_description_list = []
    damage_trap_description_list = []
    

    trap_description_1 = f'''On your way to {location}, you tripped on a small rock
and scraped your knee, poor {player_name}.
''' 
# trap1.music = ''

    damage_trap_description_list.append(trap_description_1)

    trap_description_2 = f'''
While crossing a huge field you accidentally stepped
on an active landmine!
'''
# trap2.music = ''
    damage_trap_description_list.append(trap_description_2)
    
    if location == "Lissabon":
        trap_description_3 = f'''
As you enter Lissabon a violent earthquake erupts
and you are flunged into the air!
'''
# trap3.music = ''
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
Baronen has a firm grip around it, never having let go his gaze of you. 

    -[Health severly damaged].

The wind behind him catches up, and the gust almost tips you over, but baronen doesn't budge. He speaks:
"Why would you do this to yourself, to us, to Kunigunda? Why did you have to love her?
You know i can't allow this. And if you can't hinder yourself, I will have to do it for you."

He lets go of the knife, taking a step back and assuming a calm but dominant pose. The night sky lights the room,
and a large, curved blade forms in hs hand. It shimmers like the moon.
You take a firm grip around the knife and with sheer will pull it out. With determination and animosity you
point the blade at Baronen...
'''

kunigunda_description_intro = '''
A wave of amazement and love washes over you as you near the borders of Constantinople. Kunigunda must be near.
You hastily walk towards the source, her love becoming stronger the closer you get. However, as you
close in on the epicenter, you find it's coming from a mansion that's covered in flame. From
the scorching inferno a figure slowly emerges, leaning over the highest balcony. It's her.

She calls your name, her once beautiful voice now burned, raspy, like rusty metal sheets grinding against
each other. Her smooth skin now charred, her eyes dark and empty. Her state reflects her treacherous journey.
The blaze has devoured her.

Even though her looks are not there anymore, it's still her, so you call back.
She acknowledges you and proceeds to step over the broken balcony, slowly descending down from it.
As her feet touches the ground, the earth around around her incinerates, turning from lushous nature
to coal and slag. She gently walks toward you, pulling a ring from out her beating heart. 
She stops right in front of you, her sweltering breath meeting yours. She presents the ring,
holding it out in front of you, and her flames seem to die down a bit. 
Her barren, yet graceful, eyes meet yours. Will you accept? 
'''

kunigunda_description_accept = '''
You slowly take the ring from her grip, and slide it onto your finger. Its smoldering heat
burns your finger, metling the ring stuck with your finger. It hurts, but she seems happier than
shes ever been, so you endure. 

Together again you make the journey to a small nearby farm. Along the journey you 
met up with the friends you made along the way (Off screen). 
Candide, Kunigunda, Pangloss, Cacambo, Jonas-Olof, Martin, Paquette.. everyone gathers at the farm, picking oranges,
contemplating life. Pangloss finally comes to the realization that this is, like, the worst of all possible worlds.
But he's petty asf and doesn't tell anyone. Cacambo gets bored and leaves, setting out to another journey
around the world. Candide ate Kunigundas ass and later died from an STD.
'''

kunigunda_description_refuse = '''
You refuse the ring. Kunigunda looks at you with despair, and the small flame still in her
heart has now extinguished. The ring melts in an instant, and her flames are awakened anew.
The heat pushes you back, but Kunigunda doesn't let you out of her range.

All of your choices has led up to this moment, as well as your mistakes.
It's time to amount.
'''

kunigunda_description_revive = '''
In the heat-filled battle, you managed to win. It hurts you to her Kunigunda like this.
You never meant for this to happen. Her lifeless corpse lies on the ground, still
hot to the touch. But wait... It seems to be becoming hotter and hotter.
Her body lifts from the ground and a black flame envelopes her.
The flames have her completely covered and you can't see anything.
That's when you hear it..
'''

kunigunda_description_death = '''
That was it. She's dead. It's over.
Your entire journey thus far has been for her, the beautiful woman now a burned corpse on the ground,
her flame completely silent.
You rethink your choices, why did you not accept? It was still her deep down inside after all.
Now, you have nothing left. You did what you came here to do. And now you have nowhere to go with anyone.



This is truly the worst of all possible worlds.
'''


tutorial_description = '''
Candide the game is a text based game, meaning it will take inputs from your keyboard only.
To make things happen in the game you are given choices, such as the following:

1. inventory
2. travel

To make any of these choices, simply type the letter or number to the left of the option.
So for example to travel, you would type 2 and then press enter.

The actual game works by traveling, at which point you can enter one of three locaion.
Thereafter an enemy will attack you. In the fight you will be given three choices of attacks.
Choose one to deal some damage and the enemy will deal some back.

You and all enemies have three stats:
HP, meaning health points, is you characters health, if it reaches 0 you die and it's game over.
STR, meaning strength, is your characters damage, the more strength the more damage you deal.
SPD, meaning speed, is your ability to attack first in combat.
You also have gold which you could use at the shop, and exp that you may level up with.

Now go out there and equip items, slay goblins, and reach your true love!
'''

intro_description = '''
It's a beautiful day in germany and especially in the castle Thunder-ten-tronckh where you reside.
But today is special, for today is when you will finally kiss and expose your love to Kunigunda,
the most beautiful maiden in all of candide-land!

You strut down the castle halls until you find her, you recite in your head what you wrote last night,
and then proceed to enter the room. You make eye contact for a while then muster up the courage to tell
her how you feel. Her cheeks turn red but and just as you lean in for the kiss her brother, Baronen,
steps in. He glances at you both and then furiously stomps toward you.

However just as he is about to reach you a sword swings beside him and just barely misses his head.
You all turn around to find that Bulgarer has filled the castle halls. They take a firm grip around you
and Baronen, draggin and then evetually throwing you out of the castle which has now been destroyed and
engulfed in flame.

You and Baronen look on in despair, until you catch a glimpse of Kunigunda. She is tied up on horseback
and is being taken away by the Bulgarer. You exchange an angry look with Baronen as you set out on
your journey to find and take back Kunigunda, so you can deliver her the kiss.

'''

#-------------------------------------------------------EXTRA------------------------------------------------------------

def play_music(music_track):
    try:
        pygame.mixer.music.load(music_track)
        pygame.mixer.music.play()
    except:
        return
    


