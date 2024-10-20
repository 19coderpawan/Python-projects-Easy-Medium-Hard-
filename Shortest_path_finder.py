# This program is going to find the shortest path by itself in the maze.
# In this we are going to use window-curses module which is used for TUI (text based user interface)
# in terminal application. In this we are using Breadth First Search (BFS) for locating the shortest path.

'''Imp Note-: Sometimes your IDE built in terminal does not support curses module , in that case
               trying using your Windows or linux terminal like CMD for windows.In this simply get in
               the project directory and run your_file_name.py'''

import curses
from curses import wrapper
import queue
import time


# in maze #->hurdles , O->start , 1->Exit
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

def print_maze(maze,stdscr,path=[]):
    blue=curses.color_pair(1)
    green=curses.color_pair(2)

    #now loop though the 2d maze for that we are going to use the for loop-:
    for i , row in enumerate(maze):
        for j , value in enumerate(row):
            stdscr.addstr(i,j*2,value,green)


# function to find the starting position.
def find_start(maze,start):
    for i , row in enumerate(maze):
        for j , value in enumerate(row):
            return i , j
    return None

# function to find the path.
def find_path(maze):
    #initlize the start and the end of the maze.
    End="X"
    Start="O"
    start_pos=find_start(maze,Start) #find the start position in the maze.the start_pos hold the tuple of postion.

    q=queue.Queue()#initlize queue data structure.
    #queue holds the tuple of start position and the list which hold the path to reach the end_pos
    q.put((start_pos,[start_pos]))
    visited=set() #A set (visited) keeps track of visited positions to avoid cycles.


# stdscr is called standard screen which represent the window screen of the terminal all the inputs ,images or graphics manges in this screen only.
def main(stdscr):
    '''We can also add colors using curses for that firslty initilize color .'''
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_YELLOW)#(id,foreground color,background color)
    # blue_yellow=curses.color_pair(1)# to apply the color use color.pair(id)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)

    stdscr.clear()#to clear the screen first.
    # stdscr.addstr(0,0,"pawank ushwaha",blue_yellow)#will add the string at the corridate(row,column) here it is (top left corner)
    print_maze(maze,stdscr)
    stdscr.refresh()# Refresh to show changes
    stdscr.getch()# Wait for user input

'''The wrapper(main) function initializes curses and ensures that it cleans up properly when exiting, 
even if an error occurs. it also execute your main funciton.'''

wrapper(main)
