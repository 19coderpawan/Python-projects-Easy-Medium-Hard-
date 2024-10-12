# In this game the user need to guess the correct  number which is generated randomly.
# the user need to guess the number in a minimum turns.

import random
# this will generate an random number from 0 t0 10
random_number=random.randint(0,10)

print("Welcome to Random_num_guesser game you need to guess the number between 0 to 10 including these.")
consent=input("Are you ready (yes/no)-: ")
attempt=0
if consent.lower()=="yes":
    while True:
        choice=int(input("What's your guess-:  "))
        if(choice==random_number):
            attempt+=1
            print(f"you guess the correct number in {attempt} attempt")
            break
        elif choice>random_number:
            attempt+=1
            print("guess the smaller number")
        else:
            attempt+=1
            print("guess the larger number")
if attempt<=2:
    print("you are among the 1% who guess the number in 2 or less than 2  attempt")
elif attempt<=6:
    print("you can do better than this ")
else:
    print("keep trying you have quite far behind! try again.")
print("Thankyou for playing comeback anytime to have more fun.")


