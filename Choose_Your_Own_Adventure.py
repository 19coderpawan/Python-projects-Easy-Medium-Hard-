# In this game you have given two options at every stage your choice will decide your destiny.

player=input("hi! Mate what your Good name-: ").capitalize()
print(f"Welcome {player} are you ready to imbark on your new journey.")
choice=input("player(yes/no)-: ").lower()

if choice=="yes":
    print("Great let's go then!")
    answer=input('''You left your home town (Plaet Town) to start your journey to become a Pokemon Master
    However for that firstly you need to register yourself as a official pokemon trainer 
    in joto town which is quite far. Your first desitnation is JOTO Town can you reach the 
    town in time .Beware the path might not be the easy one but can be the most rewarding.
    So do you still want to continue (yes/no)-:''').lower()
    if answer=="yes":
        answer=input('''while traveling you pass multiple towns and cities but , now you came accross 
    an jungle a very dense jungle do you want to enter or go back take another route.(back/enter)-:''').lower()
        if answer=="enter":
            answer=input('''while continuing your journey through jungle you encounter an injured pokemon
            named (Pikachu) he is injured will you help him or leave (help/leave)-: ''')
            if answer=="help":
                pass
            elif answer=="leave":
                print("A pokemon die beacuse of you ! you are not fit to be a pokemon trainer you loose.")
                quit()
        elif answer=="back":
            answer=input('''You decide to move back to lote city to take another route however, upon entering
    the city you came across a stranger you need's your help, some bad guys are searching for him
    maybe they need something from him would you help him in hiding or mind your own business(help/leave)-: ''').lower()
            if answer=="help":
                pass
            elif answer=="leave":
                pass
            else:
                print("invalid choice you loose the game!")
        else:
            print("invalid choice you loose the game!")
            quit()
    else:
        print("You are still a kid ! Go play with your toys.")
        quit()

else:
    print("It's ok may be you are not an adventure lover!")
    quit()