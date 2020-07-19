import random
min= 1
max= 6
roll_again ="y"

while roll_again == "y":
    print ("The dice is rolling...")
    print (random.randint(min,max))
    roll_again= input ("Roll Again? ")
    while roll_again != "n" and roll_again != "y":
        print ("Invalid input. Choose \"y\" or \"n\"")
        roll_again = input("Roll Again? ")
print("Finished! Thanks for playing!")