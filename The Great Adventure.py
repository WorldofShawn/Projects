import random

min = 0
max = 9
first_num = random.randint(min,max)
second_num = random.randint(min,max)
third_num = random.randint(min,max)
cyclops_alive = True
shadow_beast_alive = True
golden_dragon_alive = True
excalibur_acquired = False
torch_acquired = False
first_gate = False
second_gate = False
attempts_left = 3
move = ""
action = ""
still_alive = True
guess = ""
password = str(first_num)+str(second_num)+str(third_num)

print ("You regain consciousness and find yourself in an empty room. You name this room as Central Room #1. You see two paths.")

while first_gate == False and still_alive == True:
    move = input("Do you take the north or west path? ")
    while move.lower()== "north" or move.lower()== "west" and still_alive == True:
        if move.lower()=="north":
            action = input ("There is a giant cyclops blocking the way. Do you fight or flee? ")
            while action.lower() != "fight" and action.lower() != "flee":
                action = input ("Do you fight or flee?! ")
            if action.lower() == "fight" and excalibur_acquired == False:
                print ("You attempted to fight the cyclops. The cyclops laughs and sits on you and you were crushed in the process.")
                still_alive = False
            elif action.lower() == "fight" and excalibur_acquired == True:
                print ("You raise Excalibur and cut down the cyclops. A mysterious number appears on the nearby wall"
                        "\nYou take note of the first number: " +str(first_num) + "\n"
                        "With the defeat of the cyclops, a hidden passageway appears. You have moved to Central Room #2.\n")
                cyclops_alive = False
                first_gate = True
            elif action.lower() == "flee":
                print ("You are now back in Central Room #1.\n")

        else:
            if excalibur_acquired == True:
                print ("There is nothing for you here. You make your way back to Central Room #1.\n")
            else:
                print ("You have found the legendary sword, Excalibur! You make your way back to Central Room #1.\n")
                excalibur_acquired = True
        move = ""
if still_alive == True and first_gate == True:
    print ("You arrive to Central Room #2, you find a north and east path.")
while second_gate == False and still_alive == True:
    move = input("Do you take the north or east path? ")
    while move.lower() == "north" or move.lower() == "east" and still_alive == True:
        if move.lower() == "north":
            if golden_dragon_alive == False and shadow_beast_alive == False:
                second_gate = True
                print ("With the defeat of the Shadow Beast and Golden Dragon, the door in the north path opens.\n"
                       "You proceed to the Final Central Room.")
            else:
                print ("Door is tightly locked and won't budge. Perhaps the defeat of the bosses of this floor will open the door.\n"
                       "You make your way back to Central Room #2.\n")
                move = ""
        else:
            print ("The path divides into three paths: left, right and forward.")
            while move.lower() != "left" and move.lower() != "right" and move.lower() != "forward":
                move = input ("Do you go left, right or forward? ")
            if move.lower() == "left":
                if shadow_beast_alive == False:
                    print ("The Shadow Beast has been slain. There is nothing else for you to do here.\n"
                           "You make your way back to Central Room #2.\n")
                else:
                    action = input("The Shadow Beast lurks in the shadows. Do you fight or flee? ")
                    while action.lower()!="fight" and action.lower()!="flee":
                        action = input("Do you fight or flee? ")
                    if action.lower() == "fight":
                        if torch_acquired == True:
                            print ("You raise the torch and the Shadow Beast burns away with a terrifying scream!\n"
                                   "You see the second mysterious number appear on the nearby wall and make note of it.\n"
                                   "You take note of the second secret number:" + str(second_num) +"\n"
                                   "You make your way back to Central Room #2.\n")
                            shadow_beast_alive = False
                        else:
                            print ("You swing Excalibur and slices only dark mist. You are unable to wound the Shadow Beast!\n"
                                   "The Shadow Beast impales you with its massive claws.")
                            still_alive = False
                    else:
                        print ("You flee and make your way back to Central Room #2.\n")
            if move.lower() == "right":
                if torch_acquired == False:
                    print ("You have found the magic torch!\n"
                       "You make your way back to Central Room #2.\n")
                    torch_acquired = True
                else:
                    print ("There is nothing for you here. You make your way back to Central Room #1.\n")
            if move.lower() == "forward":
                if golden_dragon_alive == False:
                    print("There is nothing for you here. You make your way back to Central Room #1.\n")
                else:
                    print("The Golden Dragon sleeps. You can slightly make out a number written on the wall behind the dragon")
                    action = input ("What will you do? Will you fight, flee or sneak? ")
                    while action.lower() != "fight" and action.lower() != "flee" and action.lower() != "sneak":
                        action = input("Fight, flee or sneak? ")
                    if action.lower()=="fight":
                        print("The Golden Dragon seems annoyed that you would even attempt to hit him with such a puny sword.\n"
                              "The Golden Dragon unleashes his fiery breath and turns you to ashes!")
                        still_alive = False
                    elif action.lower()=="flee":
                        print ("You flee and make your way back to Central Room #2.\n")
                    else:
                        print ("Thankfully, you used your brains and snuck past the dragon.\n"
                               "You obtain the third secret number: " + str(third_num) + "\n"
                               "The Golden Dragon wakes up. It smiles in approval and vanishes in a flash of light.\n"
                                "You make your way back to Central Room #2.\n")
                        golden_dragon_alive = False
        move = ""
if still_alive == True or second_gate == True:
    print ("You finally see the exit to get out of this nightmarish prison.\n"
           "A booming voice warns, \"Three Tries...\"\n"
           "The security system to unlock the door is asking for a password consisting of three numbers.")
    while attempts_left>0 and guess != password:
        guess = input("Guess the three digit password: ")
        attempts_left -= 1
        print (str(attempts_left)+ " tries left\n")

if guess == password:
    print ("You escaped from the maze and lived happily ever after! Congratulations!")
elif still_alive == False:
    print ("You have died. Game Over.")
elif attempts_left == 0:
    print ("You have no more chances. The dungeon starts to violently shake and the ceiling collapses.\n"
           "You have died. Game Over")

