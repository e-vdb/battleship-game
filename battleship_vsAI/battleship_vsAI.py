#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:43:52 2021

@author: Emeline

"""

import tkinter as tk
import random
from help_GUI import printRules, about
from ships_positioning import randomShipLocation

haut = 10  # table heigth
larg = 10  # table width
cote = 40  # cell width

messages=['FIRE',"MISSED","HIT","HIT AND SUNK","ALL SHIPS ARE SUNK + ","Game over"]
name_ships=["Carrier","Battleship","Cruiser","Destroyer","Submarine"]
symbol=["C","B","Cr","D","S"]
lg_ships=[5,4,3,2,1]
nb_ships=[1,1,3,3,2]
'''playedList=[0]
AI_playabledList=[i for i in range(1,101)]
random.shuffle(AI_playabledList)'''
ships=[[name,lg,nb,symb] for name,lg,nb,symb in zip(name_ships,lg_ships,nb_ships,symbol)]




class Grid(object):
    def __init__(self,can):
        self.grid = [['E' for i in range(10)] for j in range(10)]
        self.remaining_ships = sum(nb_ships)
        self.can=can
        self.cell=[[0 for row in range(haut)] for col in range(larg)]
        self.dic_ships={}
        for y in range(haut):
            for x in range(larg):
                self.cell[x][y] = self.can.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), outline="gray", fill="white")
    
    def reset(self):
        self.grid = [['E' for i in range(10)] for j in range(10)]
        for y in range(haut):
            for x in range(larg):
                self.can.itemconfig(self.cell[x][y], fill="white")
        
    
    def randomGridShips(self):
        global ships
        
        for ship in ships:  
            for nb in range(ship[2]):
                shipInPlace=False
                while not shipInPlace:
                    shipInPlace=randomShipLocation(ship[1],self.grid,ship[3]+str(nb))
                self.dic_ships[ship[3]+str(nb)]=ship[1]
        return self.dic_ships
    
    def show_ships(self):
        for i in range(10):
            for j in range(10):
                if self.grid[i][j]!='E':
                    self.can.itemconfig(self.cell[i][j], fill="black")
    
    def is_attacked(self,x,y):
        cible=self.grid[x][y]
        if cible=='E':
            lbl.configure(text=messages[1])
            coul='blue'
        else:
            self.dic_ships[cible]-=1
            if self.dic_ships[cible]>0:
                lbl.configure(text=messages[2])
            else:
                lbl.configure(text=messages[3])
                self.remaining_ships-=1 
            coul="red"
        self.can.itemconfig(self.cell[x][y], fill=coul)
        if self.remaining_ships==0:
            root.after(1000,winner)  
        else:
            root.after(1000,reset_lbl)

def attack():
    global gridUser,game_over,user_can_play
    if not game_over:
        case=AI_playabledList.pop()
        y=(case-1)//10
        x=(case-1)%10
        gridUser.is_attacked(x,y)
        user_can_play=True
 
        

 
def click_grid(event):
    global gridAI,canvas2,game_over,user_can_play
    if not game_over and user_can_play:
        case=canvas2.find_closest(event.x, event.y)[0]
        if case not in playedList:
            user_can_play=False
            playedList.append(case)
            y=(case-1)//10
            x=(case-1)%10
            gridAI.is_attacked(x, y)
            root.after(1000,attack)


def reset_lbl():
    global lbl
    lbl.configure(text=messages[0])

def winner():
    global lbl,game_over
    game_over=True
    lbl.configure(text=messages[-1])


def game():
    global gridUser,gridAI,AI_playabledList,playedList,game_over,user_can_play
    game_over=False
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

frame1=tk.Frame(root)
frame1.pack(side=tk.TOP)
lbl_user=tk.Label(frame1,text="Player",font='Arial 18')
lbl_user.pack(side=tk.TOP)
canvas = tk.Canvas(frame1, width=cote*larg, height=cote*haut, highlightthickness=0)
canvas.pack()
frame=tk.Frame(root)
frame.pack(side=tk.TOP)
lbl=tk.Label(frame,text=messages[0],font='Arial 18')
lbl.pack(side=tk.TOP)
lbl_ai=tk.Label(frame,text="Computer",font='Arial 18')
lbl_ai.pack(side=tk.TOP)
frame2=tk.Frame(root)
frame2.pack()
canvas2 = tk.Canvas(frame2, width=cote*larg, height=cote*haut, highlightthickness=0)
canvas2.pack()
canvas2.bind("<Button-1>", click_grid)

gridUser=Grid(canvas)
gridAI=Grid(canvas2)
game()

root.mainloop()
