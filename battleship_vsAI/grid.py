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
    """
    A class for the battleship grid.
    
    Methods
    -----------
    reset
        Reset the grid.
    randomGridShips
        Generate randomly a grid with ships.
    show_ships
        Set to black the cells occupied by ships.
    is_attacked
        Update the canvas after a shot.
    end_game
        Update the label to indicate 'Game over'.
    """
    
    def __init__(self, can: tk.Canvas):
        """
        Constructor.
        """
        self.grid = [['E' for i in range(10)] for j in range(10)]
        self.game_over = False
        self.remaining_ships = sum(nb_ships)
        self.can = can
        self.cell = [[0 for row in range(haut)] for col in range(larg)]
        self.dic_ships = {}
        for y in range(haut):
            for x in range(larg):
                self.cell[x][y] = self.can.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), 
                                                            outline="gray", fill="white")
    
    def reset(self) -> None:
        """
        Reset the grid.

        Returns
        -------
        None.

        """
        self.grid = [['E' for i in range(10)] for j in range(10)]
        for y in range(haut):
            for x in range(larg):
                self.can.itemconfig(self.cell[x][y], fill="white")
        
    def randomGridShips(self) -> dict:
        """
        Generate randomly a grid with ships.

        Returns
        -------
        dict
            Dictionary with keys = ships name and values = ships length.

        """
        for ship in ships:  
            for nb in range(ship[2]):
                shipInPlace = False
                while not shipInPlace:
                    shipInPlace = randomShipLocation(ship[1],self.grid,ship[3]+str(nb))
                self.dic_ships[ship[3]+str(nb)] = ship[1]
        return self.dic_ships
    
    def show_ships(self) -> None:
        """
        Set to black the cells occupied by ships.

        Returns
        -------
        None.

        """
        for i in range(10):
            for j in range(10):
                if self.grid[i][j]!='E':
                    self.can.itemconfig(self.cell[i][j], fill="black")
    
    def is_attacked(self, x, y, root, lbl) -> None:
        """
        Update the canvas after a shot.
        
        Update the color of the cell according to the state.
        Update the label that indicates the result of the shot.

        Parameters
        ----------
        x : int
            Row index of the cell.
        y : int
            Column index of the cell.
        root : tk.Tk
            .
        lbl : tk.Label
            Message that indicates the result of the shot.

        Returns
        -------
        None.

        """
        cible = self.grid[x][y]
        if cible=='E':
            lbl.configure(text=messages[1])
            coul = 'blue'
        else:
            self.dic_ships[cible] -= 1
            if self.dic_ships[cible]>0:
                lbl.configure(text=messages[2])
            else:
                lbl.configure(text=messages[3])
                self.remaining_ships -= 1 
            coul="red"
        self.can.itemconfig(self.cell[x][y], fill=coul)
        if self.remaining_ships==0:
            root.after(1000,self.end_game, lbl)  
        else:
            root.after(1000,reset_lbl, lbl)
    
    def end_game(self, lbl):
        """
        Update the label to indicate 'Game over'.

        Parameters
        ----------
        lbl : tk.Label
            Message that indicates the instructions

        Returns
        -------
        None.

        """
        lbl.configure(text=messages[-1])
        self.game_over = True


def reset_lbl(lbl):
    lbl.configure(text=messages[0])
