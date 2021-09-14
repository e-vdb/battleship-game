#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:43:52 2021

@author: renaud
https://stackoverflow.com/questions/29211794/how-to-bind-a-click-event-to-a-canvas-in-tkinter
"""

import tkinter as tk
import random
import time


haut = 10  # table heigth
larg = 10  # table width
cote = 40  # cell width


cell2 = [[0 for row in range(haut)] for col in range(larg)]
messages=["FIRE","MISSED","HIT","HIT AND SUNK","ALL SHIPS ARE SUNK + "]
name_ships=["Carrier","Battleship","Cruiser","Destroyer","Submarine"]
symbol=["C","B","Cr","D","S"]
lg_ships=[5,4,3,2,1]
nb_ships=[1,1,3,3,2]

ships=[[name,lg,nb,symb] for name,lg,nb,symb in zip(name_ships,lg_ships,nb_ships,symbol)]

def time_convert(sec):
  mins =sec // 60
  sec = sec % 60
  lbl2.configure(text="Game complete in = "+str(mins)+":"+str(sec))
  
  
def click_grid(event):
    global case
    case=canvas2.find_closest(event.x, event.y)[0]
    if case not in playedList:
        playedList.append(case)
        root.after(1000,fire)


def initGrid():
    grid=[['E' for i in range(10)] for j in range(10)]
    return grid

def initGridAttempts():
    grid=[['_' for i in range(10)] for j in range(10)]
    return grid    

def placeShipH(row,col,lg,grid,symbol):
    shipInPlace=True
    if col+lg>10:
            shipInPlace=False
    else:
        for count in range(lg):
            if grid[row][col+count]!="E":
                shipInPlace=False
    if shipInPlace:
        for count in range(lg):
            grid[row][col+count]=symbol
    return shipInPlace

def placeShipV(row,col,lg,grid,symbol):
    shipInPlace=True
    if row+lg>10:
            shipInPlace=False
    else:
        for count in range(lg):
            if grid[row+count][col]!="E":
                shipInPlace=False
    if shipInPlace:
        for count in range(lg):
            grid[row+count][col]=symbol
    return shipInPlace

def randomShipLocation(lg,grid,symbol):
    indiceL=random.randint(0,9)
    indiceC=random.randint(0,9)
    shipInPlace=True
    posHorV=random.randint(0,1)
    if posHorV==0:
        shipInPlace=placeShipH(indiceL,indiceC,lg,grid,symbol)
    else:
        shipInPlace=placeShipV(indiceL,indiceC,lg,grid,symbol)
    return shipInPlace
   

def randomGridShips():
    global ships,grid,gridAttempts
    grid=initGrid() 
    gridAttempts=initGridAttempts()
    dic_ships={}
    for ship in ships:  
        for nb in range(ship[2]):
            shipInPlace=False
            while not shipInPlace:
                shipInPlace=randomShipLocation(ship[1],grid,ship[3]+str(nb))
            dic_ships[ship[3]+str(nb)]=ship[1]
    return dic_ships

def reset_lbl():
    global lbl
    lbl.configure(text=messages[0])

def winner():
    global end_time
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    lbl.configure(text=messages[4])

def fire():
    global dic_ships,remaining_ships,lbl,frame,grid
    y=(case-1)//10
    x=(case-1)%10
    cible=grid[x][y]
    if cible=='E':
        lbl.configure(text=messages[1])
        coul='blue'
    else:
        dic_ships[cible]-=1
        if dic_ships[cible]>0:
            lbl.configure(text=messages[2])
        else:
            lbl.configure(text=messages[3])
            remaining_ships-=1  
            lbl2.configure(text='Remaining ships = '+str(remaining_ships))
        coul="black"
    canvas2.itemconfig(cell2[x][y], fill=coul)
    if remaining_ships==0:
        root.after(1000,winner)  
    else:
        root.after(1000,reset_lbl)

def game():
    global dic_ships,playedList,start_time,remaining_ships,lbl2
    for y in range(haut):
        for x in range(larg):
            canvas2.itemconfig(cell2[x][y], fill='white')
    reset_lbl()
    remaining_ships=sum(nb_ships)
    lbl2.configure(text='Remaining ships = '+str(remaining_ships))
    playedList=[0]
    dic_ships=randomGridShips()
    start_time = time.time()
############################################################################
# Help menu
############################################################################     
def printRules():
    ruleWindow=tk.Toplevel()
    ruleWindow.title("How to play")
    with open('rules_eng.txt') as f:
        gameRules=f.read()
    lab_Rule=tk.Label(ruleWindow,text=gameRules,fg="black", anchor="e", justify=tk.LEFT)
    lab_Rule.pack(side=tk.TOP)
    ruleWindow.mainloop()


def about():
    aboutWindow=tk.Toplevel()
    aboutWindow.title("About") 
    with open('about.txt') as f:
        about=f.read()
    lbl_about=tk.Label(aboutWindow,text=about,fg="black", anchor="e", justify=tk.LEFT)
    lbl_about.pack(side=tk.TOP)
    aboutWindow.mainloop()  
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


frame=tk.Frame(root)
frame.pack(side=tk.TOP)
lbl=tk.Label(frame,text=messages[0],font='Arial 18')
lbl.pack(side=tk.TOP)
frame2=tk.Frame(root)
frame2.pack()
canvas2 = tk.Canvas(frame2, width=cote*larg, height=cote*haut, highlightthickness=0)
canvas2.pack()
for y in range(haut):
    for x in range(larg):
        cell2[x][y] = canvas2.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), outline="gray", fill="white")

canvas2.bind("<Button-1>", click_grid)
lbl2=tk.Label(frame,text='',font='Arial 18')
lbl2.pack(side=tk.BOTTOM)

game()

root.mainloop()
