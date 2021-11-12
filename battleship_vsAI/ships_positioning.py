#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module devoted to ships positioning.
"""
import random


def placeShipH(row: int, col: int, lg: int, grid: list, symbol: str) -> bool:
    """
    Place the ship horizontally if possible.

    Parameters
    ----------
    row : int
        Row number.
    col : int
        Column number.
    lg : int
        Number of cells occupied by the ship that is tried to be placed.
    grid : list
        Battleship grid.
    symbol : str
        Character that represents the ship.

    Returns
    -------
    bool
        True if the ship is placed, False otherwise.

    """
    shipInPlace = True
    if col+lg>10:
            shipInPlace = False
    else:
        for count in range(lg):
            if grid[row][col+count]!="E":
                shipInPlace = False
    if shipInPlace:
        for count in range(lg):
            grid[row][col+count] = symbol
    return shipInPlace


def placeShipV(row: int, col: int, lg: int , grid: list, symbol: str) -> bool:
    """
    Place the ship vertically if possible.

    Parameters
    ----------
    row : int
        Row number.
    col : int
        Column number.
    lg : int
        Number of cells occupied by the ship that is tried to be placed.
    grid : list
        Battleship grid.
    symbol : str
        Character that represents the ship.

    Returns
    -------
    bool
        True if the ship is placed, False otherwise.

    """
    shipInPlace = True
    if row+lg>10:
            shipInPlace = False
    else:
        for count in range(lg):
            if grid[row+count][col]!="E":
                shipInPlace = False
    if shipInPlace:
        for count in range(lg):
            grid[row+count][col] = symbol
    return shipInPlace


def randomShipLocation(lg: int, grid: list, symbol: str) -> bool:
    """
    Try to place randomly a ship.
    
    Choose randomly a cell.
    Choose randomly to place the ship horizontally or vertically.
    Try to place the ship using placeShipH (horizontally) or placeShipV (vertically).

    Parameters
    ----------
    lg : int
        Number of cells occupied by the ship that must be placed.
    grid : list
        Battleship grid.
    symbol : str
        Character that represents the ship.

    Returns
    -------
    bool
        True if the ship is placed, False otherwise.

    """
    indiceL = random.randint(0,9)
    indiceC = random.randint(0,9)
    shipInPlace = True
    # Choose randomly to place the ship horizontally or vertically.
    posHorV = random.randint(0,1)
    if posHorV==0:
        shipInPlace = placeShipH(indiceL,indiceC,lg,grid,symbol)
    else:
        shipInPlace = placeShipV(indiceL,indiceC,lg,grid,symbol)
    return shipInPlace