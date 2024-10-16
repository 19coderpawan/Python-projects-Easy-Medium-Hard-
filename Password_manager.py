# This is a password manager application in which you can save your personal password in encrypted format.

master_code=input("Please Enter your Master Code. Remember only if your master code is correct then only your "
                  "passwords will be decrypted. :- ")

def display():
    with open("password.txt","r") as f:
        for lines in f.readlines():
            data=lines.rstrip()
#             rstrip() remove the trailing char from the string.
#             A trailing character refers to any character that appears at the end of a string.
#             In programming and data processing, trailing characters can often include spaces,
#             punctuation marks, or any other specified characters that follow the last meaningful
#             character in the string.
            user,password=data.split("|")
#             so it split the string wherever it finds the | operator in the string.
            print(f"User-:{user}|password-:{password}")

def add():
    username=input("enter your User name-: ").lower()
    password=input("enter your password-: ").lower()

    # file=open("password.txt","a")
    # file.write(f"{username}|{password}")
    # file.close()

    with open("password.txt","a") as f:
        f.write(username+"|"+password+"\n")



    print("Your data is saved")

while True:
    choice=input("Would you like to see your password list or add new password to the list (display/add) Or press 'q' to Quit-: ").lower()

    if choice=="q":
        quit()
    if choice=="display":
        display()
    elif choice=="add":
        add()
    else:
        print("Invalid choice?")
        quit()
