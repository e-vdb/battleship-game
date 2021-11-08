#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module devoted to ships positioning.
"""
import random


def placeShipH(row, col, lg, grid, symbol):
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