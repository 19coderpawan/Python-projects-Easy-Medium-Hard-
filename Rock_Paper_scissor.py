# This is basic rock paper scissor game which we had played a lot when we were kid's lets code it.
import random
print("Welcome to RPS game choose R-rock, P-paper , S-scissor let see if you can beat the bot.")
li1=["r","p","s"]

comp_choice=random.choice(li1)

print("Bot-: Would you like to start the game !")
concent=input("User(yes/no)-: ")

if concent.lower()=="yes":
    while True:
        user_choice=input("User-:Choose (R/P/S)-: ").lower()
        print(f"Bot-:{comp_choice}")

        if user_choice==comp_choice:
            print("Draw")
            rematch=input("Would you like to play again-:")
            if rematch.lower()=="yes":
                continue
            else:
                break

        elif user_choice=="r" and comp_choice=="s":
            print("User-:Won")
            rematch=input("Would you like to play again-:")
            if rematch.lower()=="yes":
                continue
            else:
                break

        elif user_choice=="r" and comp_choice=="p":
            print("Bot-:Won")
            rematch=input("Would you like to play again-:")
            if rematch.lower()=="yes":
                continue
            else:
                break

        elif user_choice=="s" and comp_choice=="r":
            print("Bot-:Won")
            rematch=input("Would you like to play again-:")
            if rematch.lower()=="yes":
                continue
            else:
                break

        elif user_choice=="s" and comp_choice=="p":
            print("User-:Won")
            rematch=input("Would you like to play again-:")
            if rematch.lower()=="yes":
                continue
            else:
                break

        elif user_choice=="p" and comp_choice=="s":
            print("Bot-:Won")
            rematch=input("Would you like to play again-:")
            if rematch.lower()=="yes":
                continue
            else:
                break

        else:
            print("User-:Won")
            rematch=input("Would you like to play again-:")
            if rematch.lower()=="yes":
                continue
            else:
                break

print("Hope you enjoyed! See you again.")


