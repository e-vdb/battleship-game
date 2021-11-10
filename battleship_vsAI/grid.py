#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Grid class.
"""
import tkinter as tk
from ships_positioning import randomShipLocation


haut = 10  # table heigth
larg = 10  # table width
cote = 40  # cell width

name_ships=["Carrier","Battleship","Cruiser","Destroyer","Submarine"]
symbol=["C","B","Cr","D","S"]
lg_ships=[5,4,3,2,1]
nb_ships=[1,1,3,3,2]
ships=[[name,lg,nb,symb] for name,lg,nb,symb in zip(name_ships,lg_ships,nb_ships,symbol)]
messages=['FIRE',"MISSED","HIT","HIT AND SUNK","ALL SHIPS ARE SUNK + ","Game over"]

class Grid(object):
    def __init__(self, can: tk.Canvas):
        self.grid = [['E' for i in range(10)] for j in range(10)]
        self.game_over = False
        self.remaining_ships = sum(nb_ships)
        self.can = can
        self.cell = [[0 for row in range(haut)] for col in range(larg)]
        self.dic_ships = {}
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
    
    def is_attacked(self, x, y, root, lbl):
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
            root.after(1000,self.end_game, lbl)  
        else:
            root.after(1000,reset_lbl, lbl)
    
    def end_game(self, lbl):
        lbl.configure(text=messages[-1])
        self.game_over = True


def reset_lbl(lbl):
    #global lbl
    lbl.configure(text=messages[0])
    
def winner():
    global lbl,game_over
    game_over=True
    lbl.configure(text=messages[-1])