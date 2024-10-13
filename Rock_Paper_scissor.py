import cv2
from tkinter import *
import random
from PIL import Image, ImageTk

# Main Window Setup

root = Tk()
root.title("RPS")
root.geometry('800x680')  #width and height

# Canvas creation
canvas = Canvas(root, width=800, height=680)
canvas.grid(row=0, column=0)

# Labels
label1 = Label(root, text="PLAYER", font=('Algerian', 25))
lable2 = Label(root, text="COMPUTER", font=('Algerian', 25))
lable3 = Label(root, text="VS", font=('Algerian', 25))

# place labels on specified coordination.
label1.place(x=80, y=20)
lable2.place(x=540, y=20)
lable3.place(x=350, y=220)


# Image load
def loadimg(file):
    img = cv2.imread(file)
    img = cv2.resize(img, (200, 200))
    return img


# load image based on choices
default_player_img = loadimg("rock.png")
default_computer_img = cv2.flip(default_player_img, 1)

rock_player = loadimg("rock.png")
rock_computer = cv2.flip(rock_player, 1)

paper_player = loadimg("paper3.jpg")
paper_computer = cv2.flip(paper_player, 1)

scissor_player = loadimg("scissor.png")
scissor_computer = cv2.flip(scissor_player, 1)

# load selection image
selection_img = loadimg("selection.png")
selection_img = cv2.resize(selection_img, (200, 200))


# Image Conversion
def cv_to_tk(img):
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return ImageTk.PhotoImage(Image.fromarray(rgb_img))


# Store PhotoImage objects to prevent garbage collection
player_image = cv_to_tk(default_player_img)
computer_image = cv_to_tk(default_computer_img)
selection_image = cv_to_tk(selection_img)

# Create images on canvas
canvas.create_image(0, 100, anchor=NW, image=player_image)
canvas.create_image(500, 100, anchor=NW, image=computer_image)
canvas.create_image(0, 400, anchor=NW, image=selection_image)
canvas.create_image(500, 400, anchor=NW, image=selection_image)


# gamelogic-:

def play(player):
    global player_img, computer_img
    li1 = [1, 2, 3]
    computer = random.choice(li1)
    canvas.delete("result")
    if player == 1:
        player_img=cv_to_tk(rock_player)
        canvas.create_image(0, 100, anchor=NW, image=player_img)
    elif player == 2:
        player_img=cv_to_tk(paper_player)
        canvas.create_image(0, 100, anchor=NW, image=player_img)
    else:
        player_img=cv_to_tk(scissor_player)
        canvas.create_image(0, 100, anchor=NW, image=player_img)

    if computer == 1:
        computer_img=cv_to_tk(rock_player)
        canvas.create_image(500, 100, anchor=NW, image=computer_img)
    elif computer == 2:
        computer_img=cv_to_tk(paper_computer)
        canvas.create_image(500, 100, anchor=NW, image=computer_img)
    else:
        computer_img=cv_to_tk(scissor_computer)
        canvas.create_image(500, 100, anchor=NW, image=computer_img)

    if player == computer:
        result = "Draw"
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 1):
        result = "Won"
    else:
        result = "Lost"

    canvas.create_text(390, 600, text="Result-: " + result, fill="Black", font=("Algerian", 25), tag='result')


# Clear function
def clear():
    canvas.delete('result')
    canvas.create_image(0, 100, anchor=NW, image=cv_to_tk(player_image))
    canvas.create_image(500, 100, anchor=NW, image=cv_to_tk(computer_image))


# Buttons for user Interaction

rock_b = Button(root, text="Rock", command=lambda: play(1))
rock_b.place(x=20, y=610)

paper_b=Button(root,text="Paper",command=lambda :play(2))
paper_b.place(x=75,y=610)

scissor_b=Button(root,text="Scissor",command=lambda :play(3))
scissor_b.place(x=140,y=610)

clear_b=Button(root,text="Clear",command=lambda :clear())
clear_b.place(x=360,y=40)

root.mainloop()
