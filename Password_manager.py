# This is a password manager application in which you can save your personal password in encrypted format.
# for Encryption we are going to use the crptography module.

from cryptography.fernet import Fernet

key=Fernet.generate_key() #to generate new encryption key.
fer=Fernet(key) #create the instace of the class Fernet using the unique key.

# to encrypt the message use encrypt function and pass the data in bytes format.
# token=fer.encrypt(b'hii my name is pawan')


# to decrypt the encrypted message use decrypt function.
# print(fer.decrypt(token))
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
            # here again we have to firstly convert the encrypted string into byte string then convert it
            #   decrypt it and convert it back to normal string using decode()
            print(f"User-:{user}|password-:{fer.decrypt(password.encode()).decode()}")

def add():
    username=input("enter your User name-: ").lower()
    password=input("enter your password-: ").lower()

    with open("password.txt","a") as f:
        ''' encode() and decode() is used to convert regular string to bytes sting then from
             bytes string to regular string.'''
        encrypted_password = fer.encrypt(password.encode()).decode()
        f.write(f"{username}|{encrypted_password}\n")



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
