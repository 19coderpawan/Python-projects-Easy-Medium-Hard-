# This program is going to find the shortest path by itself in the maze.
# In this we are going to use window-curses module which is used for TUI (text based user interface)
# in terminal application.

'''Imp Note-: Sometimes your IDE built in terminal does not support curses module , in that case
               trying using your Windows or linux terminal like CMD for windows.In this simply get in
               the project directory and run your_file_name.py'''

import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


# stdscr is called standard screen which represent the window screen of the terminal all the inputs ,images or graphics manges in this screen only.
def main(stdscr):
    stdscr.clear()#to clear the screen first.
    stdscr.addstr(0,0,"pawank ushwaha")#will add the string at the corridate here it is (top left corner)
    stdscr.refresh()# Refresh to show changes
    stdscr.getch()# Wait for user input

'''The wrapper(main) function initializes curses and ensures that it cleans up properly when exiting, 
even if an error occurs. it also execute your main funciton.'''

wrapper(main)
