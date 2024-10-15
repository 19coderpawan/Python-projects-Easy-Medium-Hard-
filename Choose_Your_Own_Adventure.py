player = input("Hi there! What is your good name? ").capitalize()
print(f"Welcome, {player}! Are you ready to embark on your new journey?")
choice = input("Player (yes/no): ").lower()

if choice == "yes":
    print("Great! Let's go then!")
    answer = input('''You have left your hometown, Pallet Town, to start your journey to become a Pokémon Master. 
However, first, you need to register yourself as an official Pokémon Trainer in Johto Town, which is quite far. 
Your first destination is Johto Town. Can you reach the town in time? Beware, the path might not be easy but can be quite rewarding. 
So, do you still want to continue (yes/no)? ''').lower()

    if answer == "yes":
        answer = input('''While traveling, you pass multiple towns and cities. Now, you come across a dense jungle. 
Do you want to enter or take another route? (back/enter): ''').lower()

        if answer == "enter":
            answer = input('''As you journey through the jungle, you encounter an injured Pokémon named Pikachu. 
He is hurt; will you help him or leave him behind? (help/leave): ''')

            if answer == "help":
                print(
                    "You carefully tend to Pikachu's wounds. Grateful for your kindness, he decides to join you on your journey!")
                # Continue the adventure...
                answer = input('''With Pikachu by your side, you continue your journey. Suddenly, you hear rustling in the bushes. 
Do you want to investigate or keep moving? (investigate/move): ''').lower()

                if answer == "investigate":
                    print(
                        "You find a hidden treasure chest filled with rare berries! This will surely help you on your journey.")
                else:
                    print("You decide it's best to keep moving and avoid any potential danger.")

            elif answer == "leave":
                print(
                    "A Pokémon has suffered because of your decision! You are not fit to be a Pokémon Trainer; you lose.")
                quit()

        elif answer == "back":
            answer = input('''You decide to return to Lote City and take another route. However, upon entering the city, 
you come across a stranger who needs your help. Some bad guys are searching for him; they might need something from him. 
Would you help him hide or mind your own business? (help/leave): ''').lower()

            if answer == "help":
                print("You help the stranger hide in a nearby alley. The bad guys pass by without noticing!")
                # Continue the adventure...
                answer = input('''The stranger thanks you profusely and offers you a rare Pokémon egg as a reward.
Do you accept it? (yes/no): ''').lower()

                if answer == "yes":
                    print("You've received a rare Pokémon egg! It will hatch into something special.")
                else:
                    print("You politely decline the offer but gain valuable experience from this encounter.")

            elif answer == "leave":
                print("You chose to ignore the stranger's plight. Sometimes, heroes are made by their choices.")
            else:
                print("Invalid choice; you've lost the game!")

        else:
            print("Invalid choice; you've lost the game!")
            quit()

    else:
        print("You're still too young! Go play with your toys.")
        quit()

else:
    print("It's okay; maybe you're not an adventure lover!")
    quit()
