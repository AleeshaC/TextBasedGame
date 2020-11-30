weapons_available = [
    "axe",
    "knife",
    "sword",
    "bow",
    "slingshot"
]
my_weapons = [
    "empty slot 1",
    "empty slot 2"
]

my_crystals = 0
ground_crystals = 0
crystal_choice = 0

fight_weapon="none"

def error_text():
    print("The game didn't understand your input, please try again.")

def out_of_time():
    tryagain= input("Oh no! You have taken too long to reach the dragon.\nYou hear distant screams, and when you return to the village you find it has burned to the ground.\nYou lose.\nTry again? ")
    if tryagain.lower()=="yes":
        welcome()
    else:
        quit()

def you_win():
    print("Your quest was a success! Now the village is safe again!\nYou win!")

def you_lose():
    tryagain=input("You have failed to defeat the dragon. It defeated you instead!\nYou lose this time, but if you try again you may get a different outcome!\nSECRET CODE UNLOCKED: enter the code 'warrior' after the introduction to skip back the fight!\nTry again? ")
    if tryagain.lower()=="yes":
        welcome()
    else:
        quit()

import random

def fight():
    global fight_weapon
    coin_flip=random.randint(1,2)
    if fight_weapon.lower()=="slingshot":
        print("The pebble bounces off the dragon’s scaly skin harmlessly.\nThe dragon awakens and notices you.\nBefore you have a chance to run, you are incinerated by the dragon’s fiery breath.")
        you_lose()
    elif fight_weapon.lower()=="axe":
        print("You swing your axe into the dragon's neck.\nOh no! Your axe isn't sharp enough!\nThe dragon awakens and swallows you whole.")
        you_lose()
    elif fight_weapon.lower()=="knife":
        print("You try to stab your knife into the dragon's scaly skin.\nOh no! Your knife is too small to hurt the dragon.\nThe dragon awakens and swallows you whole.")
        you_lose()
    elif fight_weapon.lower()=="bow" and coin_flip==1:
        print("You take aim with your bow and let the arrow fly.\nOh no! You missed!\nThe arrow hits a rock beside the dragon’s head with an echoing snap.\nThe dragon is alerted and before you can run, it incinerates you with its fiery breath.")
        you_lose()
    elif fight_weapon.lower()=="bow" and coin_flip==2:
        print("You take aim with your bow and let the arrow fly.\nIt hits the dragon right in the eye!\nAs the dragon bellows in pain, you shoot another arrow into the dragon’s heart.\nThe dragon is defeated.")
        you_win()
    elif fight_weapon.lower()=="sword" and coin_flip==1:
        print("You slash your sword into the dragon’s scaly skin.\nOh no! Your sword is stuck!\nAs you struggle to pull it free, the dragon awakens and swallows you whole.")
        you_lose()
    elif fight_weapon.lower()=="sword" and coin_flip==2:
        print("You jump on top of the dragon and thrust your sword into its head.\nThe dragon is defeated.")
        you_win()
    else:
        error_text()
        fight()

def check_weapon_for_fight():
    global fight_weapon
    global my_weapons
    fight_weapon = input("Inside the cave, you reach the chamber where the dragon is sleeping.\nYou decide to attack first while the element of surprise is on your side.\nWhich weapon do you want to use?\nYou are carrying the {} and the {}. ".format(my_weapons[0], my_weapons[1]))
    if fight_weapon.lower() in my_weapons:
        fight()
    elif fight_weapon.lower() not in my_weapons and fight_weapon.lower() in weapons_available:
        print("You don't have a {} with you.".format(fight_weapon.lower()))
        check_weapon_for_fight()
    else:
        error_text()
        check_weapon_for_fight()

def collect_crystals():
    global my_crystals
    global ground_crystals
    global crystal_choice
    ground_crystals = random.randint(4, 15)
    print ("Among the leaves you notice {} strange crystals. You recognise them as magical crystals which can show you the way.".format (ground_crystals))
    try:
        crystal_choice = int(input("How many crystals would you like to pick up: "))
    except ValueError:
        print("Please type a number here.")
        collect_more_crystals()
    if crystal_choice > ground_crystals:
        impossible_crystal_pickup()
    else:
        my_crystals = my_crystals + crystal_choice
        print ("You have picked up {} crystals. You now have {} crystals.".format(crystal_choice, my_crystals))
        use_crystals()

def impossible_crystal_pickup():
    global my_crystals
    global ground_crystals
    global crystal_choice
    print ("There are only {} crystals.".format(ground_crystals))
    crystal_choice = int(input("How many crystals would you like to pick up: "))
    if crystal_choice <= ground_crystals:
        my_crystals = my_crystals + crystal_choice
        print ("You have picked up {} crystals. You now have {} crystals.".format(crystal_choice, my_crystals))
        use_crystals()
    else:
        impossible_crystal_pickup()

def return_for_crystals():
    global ground_crystals
    global my_crystals
    global crystal_choice
    ground_crystals = ground_crystals - crystal_choice
    if  ground_crystals == 0:
        print ("There are no crystals left! You wander the forest searching for more crystals.")
        out_of_time()
    else:
        collect_more_crystals()

def collect_more_crystals():
    global ground_crystals
    global my_crystals
    global crystal_choice
    print ("There are {} crystals left".format(ground_crystals))
    try:
        crystal_choice = int(input("How many crystals would you like to pick up: "))
    except ValueError:
        print("Please type a number here.")
        collect_more_crystals()
    if crystal_choice > ground_crystals:
        impossible_crystal_pickup()
    if  crystal_choice <= ground_crystals:
        my_crystals = my_crystals + crystal_choice
        print ("You have picked up {} crystals. You now have {} crystals.".format(crystal_choice, my_crystals))
        use_crystals()
    else:
        impossible_crystal_pickup()

def use_crystals():
    global my_crystals
    if my_crystals <= 5:
        print ("You head off again in search of the cave. But you don't have enough crystals to guide you to it. You go back to collect more crystals.")
        return_for_crystals()
    elif my_crystals > 5 and my_crystals <= 10:
        print ("You head off again in search of the cave. With the crystals' power, you are led to the entrance of the cave.")
        check_weapon_for_fight()
    else:
        print ("You head off again in search of the cave. With the crystals' power, you are led to the entrance of the cave.\nHowever, you are exhausted after carrying so many heavy crystals and decide to stop for a quick rest before you enter.")
        out_of_time()

def toolchoose():
    global my_weapons
    global weapons_available
    chosentool=input("What tool should you use?\nYou are carrying the {} and the {}. " .format(my_weapons[0], my_weapons[1]))
    if chosentool.lower()=="knife" and "knife" in my_weapons:
        print("You try to saw at the trunk of the tree with the knife.\nNo matter how hard you try it cannot cut through..")
        out_of_time()
    elif chosentool.lower()=="slingshot" and "slingshot" in my_weapons:
        print ("You shoot pebbles at the tree hoping to knock it down.\nUnfortunately the pebbles don't make a dent.")
        out_of_time()
    elif chosentool.lower()=="sword" and "sword" in my_weapons:
        print("You slash at the tree trunk with your sword.\nIt doesn't seem to be working.")
        out_of_time()
    elif chosentool.lower()=="axe" and "axe" in my_weapons:
        print("You chop at the tree and it falls to the ground.")
        collect_crystals()
    elif chosentool.lower()=="bow" and "bow" in my_weapons:
        print("You shoot arrows at the tree hoping to knock it down.\nNothing happens.")
        out_of_time()
    elif chosentool.lower() not in my_weapons and chosentool.lower() in weapons_available:
        print ("You didn't bring the {} with you. You only have the {} and the {}.)" .format(chosentool.lower(), my_weapons[0], my_weapons[1]))
        toolchoose()
    else:
        error_text()
        toolchoose()

def treecut():
    cut=input("You reach the forest and begin looking for the cave entrance.\nYou see a tree that is glimmering with a strange light.\nWould you like to cut down the tree? ")
    if cut.lower()=="no":
        print("You decide to keep searching for the cave instead.\nYou wander around the forest for so long that you get lost.")
        out_of_time()
        print(you_lose)
    elif cut.lower()=="yes":
        toolchoose()
    else:
        error_text()
        treecut()

def view_weapons_available():
    global weapons_available
    global my_weapons
    print ("First you must choose which weapons to take. You have the following weapons in your house:")
    for weaponlist in weapons_available:
        print (weaponlist)

def choose_weapon():
    view_weapons_available()
    weapon_choice=input("Which weapon would you like to take with you? ")
    if weapon_choice.lower() in weapons_available:
        weapons_available.remove(weapon_choice.lower())
        my_weapons[0]=weapon_choice.lower()
        choose_second_weapon()
    else:
        print ("That's not an available weapon.")
        choose_weapon()

def choose_second_weapon():
    global my_weapons
    print("You have room for one more weapon.")
    second_weapon_choice=input("What else would you like to take? ")
    if second_weapon_choice.lower() in weapons_available:
        weapons_available.remove(second_weapon_choice.lower())
        my_weapons[1]=second_weapon_choice.lower()
        print ("Great! You're armed with one {} and one {}. Ready to go!".format(my_weapons[0], my_weapons[1]))
        treecut()
    elif second_weapon_choice.lower() in my_weapons:
        print ("You've already got one {}. Take something else - you don't know what you might need.".format(second_weapon_choice.lower()))
        choose_second_weapon()
    else:
        print ("That's not an available weapon.")
        choose_second_weapon()

def welcome():
    global my_crystals
    my_crystals=0
    global weapons_available
    weapons_available = [
    "axe",
    "knife",
    "sword",
    "bow",
    "slingshot"
    ]
    global my_weapons
    my_weapons = [
    "empty slot 1",
    "empty slot 2"
]
    global fight_weapon
    fight_weapon="none"
    begin=input("Welcome to the Adventure of the Dragon’s Den.\nYou are a brave warrior.\nYou have heard rumours that a dragon has taken up residence in a cave in the nearby forest.\nIt is your duty to find and slay the dragon.\nAre you ready to begin? ")
    if begin.lower()=="yes":
        choose_weapon()    
    elif begin.lower()=="no":
        print("You need to say 'yes' to begin!")
        welcome()
    elif begin.lower()=="warrior":
        my_weapons[0]="sword"
        my_weapons[1]="bow"
        check_weapon_for_fight()
    else:
        error_text()
        welcome()

welcome()