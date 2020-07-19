import random

min=1
max=6
secret_num = ""
guess_num = ""
num_match = False
attempts_left= 3

secret_num = str(random.randint(min,max))
print ("Select a number between " + str(min) + " and " + str(max) +": ")
while guess_num != secret_num and attempts_left > 0:
    print ("Attempts left: "+ str(attempts_left))
    guess_num = input("Guess the number! ")
    attempts_left -=1

print ("The secret number was "+ secret_num)
if attempts_left > 0:
    print ("Congratulations! You win!")
else:
    print ("You lose! Better luck next time!")
