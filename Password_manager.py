# This is a password manager application in which you can save your personal password in encrypted format.

master_code=input("Please Enter your Master Code. Remember only if your master code is correct then only your "
                  "passwords will be decrypted. :- ")
while True:
    choice=input("Would you like to see your password list or add new password to the list (display/add) Or press 'q' to Quit-: ").lower()

    if choice=="q":
        break
    if choice=="display":
        pass
    elif choice=="add":
        pass
    else:
        print("Invalid choice?")
        quit()
