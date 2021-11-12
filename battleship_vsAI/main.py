#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:43:52 2021

@author: Emeline

"""

import tkinter as tk
import random
from help_GUI import printRules, about
from grid import Grid


haut = 10  # table heigth
larg = 10  # table width
cote = 40  # cell width

messages=['FIRE',"MISSED","HIT","HIT AND SUNK","ALL SHIPS ARE SUNK + ","Game over"]

def attack(root):
    global gridUser, gridAI,user_can_play
    if not gridUser.game_over and not gridAI.game_over:
        case=AI_playabledList.pop()
        y=(case-1)//10
        x=(case-1)%10
        gridUser.is_attacked(x, y, root, lbl)
        user_can_play=True
 
        
def click_grid(event):
    global gridAI, gridUser, canvas2, user_can_play
    if not gridUser.game_over and not gridAI.game_over and user_can_play:
        case=canvas2.find_closest(event.x, event.y)[0]
        if case not in playedList:
            user_can_play=False
            playedList.append(case)
            y=(case-1)//10
            x=(case-1)%10
            gridAI.is_attacked(x, y, root, lbl)
            root.after(1000,attack, root)


def game():
    global gridUser,gridAI,AI_playabledList,playedList,user_can_play
    
    user_can_play=True
    playedList=[0]
    AI_playabledList=[i for i in range(1,101)]
    random.shuffle(AI_playabledList)
    gridUser.reset()
    gridUser.randomGridShips()
    gridUser.show_ships()
    gridAI.reset()
    gridAI.randomGridShips()


############################################################################
#GUI
############################################################################ 
root = tk.Tk()
root.title('Battleship')
#Menu
top = tk.Menu(root)
root.config(menu=top)
gameMenu = tk.Menu(top, tearoff=False)
helpMenu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=gameMenu)
gameMenu.add_command(label='New game', command=game)
gameMenu.add_command(label='Exit', command=root.destroy)
helpMenu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='How to play?',command=printRules)
helpMenu.add_command(label='About',command=about)

frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP)
lbl_user = tk.Label(frame1,text="Player",font='Arial 18')
lbl_user.pack(side=tk.TOP)
canvas = tk.Canvas(frame1, width=cote*larg, height=cote*haut, highlightthickness=0)
canvas.pack()
frame=tk.Frame(root)
frame.pack(side=tk.TOP)
lbl = tk.Label(frame,text=messages[0],font='Arial 18')
lbl.pack(side=tk.TOP)
lbl_ai = tk.Label(frame,text="Computer",font='Arial 18')
lbl_ai.pack(side=tk.TOP)
frame2 = tk.Frame(root)
frame2.pack()
canvas2 = tk.Canvas(frame2, width=cote*larg, height=cote*haut, highlightthickness=0)
canvas2.pack()
canvas2.bind("<Button-1>", click_grid)

gridUser = Grid(canvas)
gridAI = Grid(canvas2)
game()

root.mainloop()
