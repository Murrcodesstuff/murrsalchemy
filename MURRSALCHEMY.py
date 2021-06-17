#Loot tables

masterloot = {
    "home": ["BEAKERE", "RED POTION", "BLUE POTION", "SLAGE", "alchmemytabletrue "]
}
roomloot = masterloot["home"]
drawerloot1 = ["ANTITHIESIS of AIRE", "LEAD", "DEAD BEE"]
Right_hand = None
Left_hand = None

#Other
def silly_proposition():
    print(f"{alchemist_name} objects-eth to your sillie PROPOSITION!")


def whatethisdone():
    whateth_is_done1 = (input("What do you do? >"))
    if "inspect" or "i" in whateth_is_done1:
        if whateth_is_done1 == "inspect BEAKERE":
            beakere()

        elif whateth_is_done1 == "inspect RED POTION" or "i RED POTION": #VALVE PLS FIX LITERALLY UNPLAYBLE
            red_potion()
    
        elif whateth_is_done1 == "inspect BLUE POTION" or "i BLUE POTION":
            blue_potion()

        elif whateth_is_done1 == "d":
             home_room()

        elif whateth_is_done1 == "inspect WINDOW" or "i WINDOW":
            window()

        elif whateth_is_done1 == "inspect SLAGE" or "inspect CHUNK OF SLAGE" or "i SLAGE" or "i CHUNK OF SLAGE":
            slag()

        elif whateth_is_done1 == "inspect ALCHEMY TABLE" or "inspect TABLE" or "i ALCHEMY TABLE" or "i TABLE":
            table()

        elif whateth_is_done1 == "inspect BED":
            bed()

        elif whateth_is_done1 == "inspect yourself" or "inspect myself":
            alchemist()

        elif whateth_is_done1 == "take BED"or"t BED"or"take TABLE"or"t TABLE"or"take ALCHEMY TABLE"or"t ALCHEMY TABLE":
            heavieweaponsguy1()

        else:
            print(f"Inspect what? {alchemist_name} screams-eth, for he has no knowinge of your inner machinitations.")

    elif "combine" or "o" in whateth_is_done1:
        if drawer_open == None:
            print("You have not located-eth your ALCEHEMICAL SUPPLIES.")

        elif whateth_is_done1 == "combine":
            print("placeholder")
        else:
            silly_proposition()

    #elif "take" or "+" in whateth_is_done1:

    #elif "put" or "-" in whateth_is_done1:
    
    else:
        silly_proposition()

    print("-")
    whatethisdone()

def inventory():
    print(f"Right hand: {Right_hand}")
    print(f"Left hand: {Left_hand}")
    
def YN1():
    drawer_open = (input("Y/N? >"))
    if drawer_open == "Y" or "y":
        print(f"{alchemist_name} opens the DRAWER")
        print(f"In the DRAWER is: {drawerloot}")
            
    elif drawer_open == "N" or "n":
        print(f"{alchemist_name} hears-eth the strange VOICE telling them to not open the DRAWER.")
        print("Naturallie, they open it anyways")
        print(f"In the DRAWER is: {drawerloot}")
        
    else:
        YN1()
    
#Objects
def beakere():
    print("The beakere is filled withe 100 ml of wilde HONEIE.")

def red_potion():
    print("This RED POTION is a potion of... something. You made it while drunke")

def blue_potion():
    print("The BLUE POTION is a potion of HEALTH. It costs 25G and keepse you not dead-eth")

def window():
    print("The KINGS MEN haveth trapped you in yours ROOM. This WINDOW is the only Viable Exit.")
    print("Sadlie it is reinforcede with IRONBAR, leavinge you without room enoughe to ESCAPE")

def slag():
    print("The SLAGE is slaggie")

def table():
    print("Yours TABLE is where you spend your days, alchemizing.")
    drawer_open = (input("There is a DRAWER here contining your alchehemical supplies. Do you open it? (Y/N) >"))
    if drawer_open == "Y" or "y":
        print(f"{alchemist_name} opens the DRAWER")
        print(f"In the DRAWER is: {drawerloot}")
            
    elif drawer_open == "N" or "n":
         drawer_open = "Y"
         #NOTE: if the code you wrote about preventing the player from accessing alchemical supplies without opening the drawer, look here, you fishfaced blockhead, and slap yourself.
         print(f"{alchemist_name} hears-eth the strange VOICE telling them to not open the DRAWER.")
         print("Naturallie, they open it anyways")
         print(f"In the DRAWER is: {drawerloot}")
        
    else:
        YN1()

def bed():
    print("This is your BED. It is messie and unkempt-eth.")

def alchemist():
    print("You are nothinge special, a simple ALCHEMIST. You are rather MESSIE-ETH and slightly SLEEPIE")

def heavieweaponsguy():
    print("This OBJECT is too heavie to carrie!")

def t():
    whateth_is_done1 = whateth_is_done1.translate(None, 'take' or '+')
    if Right_hand == None:
        print(f"You take the {whateth_is_done1}.")
        remove(whateth_is_done1)
        Right_hand = whateth_is_done1
    elif Left_hand == None:
        print(f"You take the whateth_is_done1.")
        remove(whateth_is_done1)
        Left_hand = whateth_is_done1
    else:
        if  whateth_is_done1 not in roomloot:
            print(f"There is no {whateth_is_done1} here!")
        else: 
            print("Your SLOTS are filled-eth!")
def p():
    whateth_is_done1 = whateth_is_done1.translate(None, 'put' or '-')
    if Right_hand == whateth_is_done1:
        print(f"You drop the {whateth_is_done1}")
        room.append(whateth_is_done1)
        Right_hand = None
    elif Left_hand == whateth_is_done1:
        print(f"You drop the {whateth_is_done1}")
        room.append(whateth_is_done1)
        Left_hand = None
    else:
        print("You don't have-eth such a thinge.")
        
#Rooms
def home_room():
    print("This is YOUR ROOM. There is a small WINDOW on the WEST WALL.  There is no DOOR. In the SOUTH CORNER, there is yours ALCHEMY TABLE.")
    print ("On your TABLE there is-eth a large BEAKERE. Two POTIONS sit-eth on the TABLE, one RED and the othere BLUE. In the NORTH CORNER, there is a CHUNK OF SLAGE, a remindere of yours failed expiriments.")

def street_1():
    print("This is the TOWNE STREETS. This stretch contains-eth your HOUSE, alongeside countless others, (arounde 6-eth of them)")
    print("to the LEFT is the MARKET. to the RIGHT is the KEEP, where the vile and pitifule KING resides")

#Code
print("WELCOME TO MURR'S ALCHEMY.")
print("-")
print("Controls:")
print("To look at an item, type ""(i)nspect"" then the name of the object you wish to interact with.")
print("Most objects that are CAPITALIZED can be inspected. (Make sure to write it as is written in game, although sometimes it can be shortened)")
print("If you can't interact with a capilized object, it is likely still somewhat important and should be remembered")
print("To describe the room you are in, type d (when you have a ""What do you do?"" prompt)")
print("To remove items from a container or room, type: take(or +) ITEM. To put them back, type: put(or -) ITEM . To conume an item you are holding, type: (c)onsume ITEM.")
print("To combine items, find a room with a table and write c(o)mbine ITEM, then when prompted, the ITEM you wish to combine it with")
print("Have fun!")
print("-")
alchemist_name = (input("What is thy name? > ")) #maybe include option to remove fancy pants talk?
print("-")
print (f"Yours name is {alchemist_name}, an ALCHEMIST. Yours Lifelong Goale is to alchemhize the PHILOSIPHERS STONE.")                                                                                                                             
print ("However, due to greate misfourtunes, the KING hates-eth your exploitation of MAGICKS UNTOLD")
print("-")
print ("You waketh up in yours ROOM. There is a small WINDOW on the WEST WALL. There is no DOOR. In the SOUTH CORNER, there is yours ALCHEMY TABLE")
print ("On your TABLE there is-eth a large BEAKERE. Two POTIONS sit-eth on the TABLE, one RED and the othere BLUE. In the NORTH CORNER, there is a CHUNK OF SLAGE, a remindere of yours failed expiriments.")
print("-")
whatethisdone()
