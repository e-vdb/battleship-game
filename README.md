# battleship-game

## Summary

Battleship game for one player.

Code written in python3 with graphics user interface (GUI) using Tkinter.


## Battleship-game

Battleship is a *guessing-game*. 
To learn more about this game, visit https://en.wikipedia.org/wiki/Battleship_(game)

## Game modes

### 1 player (solo mode)
Sink the fleet within minimal time.

### Versus AI
Sink the opposing computer's fleet before the computer destroys your fleet. 

## Repository content
* battleship_1player : Python 3 script for solo mode
* battleship_vsAI : Python 3 script for versus AI mode
* about.txt : plain text document that contains copyright and license information
* rules_eng.txt : plain text document that explains how to play the game


## Tkinter interface mode versus AI

### Interface

Two 10x10 grids

* Player's grid with ships
* Computer's grid

![GUI_vsAI_1](https://user-images.githubusercontent.com/82372483/133804656-fd3cd725-fc82-499e-aad9-f7f459399ced.png)

### Example of game
Colour legend:
* Black : ship
* Blue: water
* Red : hit


![GUI_vsAI](https://user-images.githubusercontent.com/82372483/133804628-12d3bd5d-0626-4702-9e2f-016ba2b5bbfc.png)


## Tkinter interface 1 player (solo mode)

### Interface

Grid 10x10

![GUI](https://user-images.githubusercontent.com/82372483/133255011-8ea2deb0-447d-4592-9728-5ae7cca059d6.png)

### Help

From the GUI you can read How to play? as well as copyright and license information.

### Example of game

![HIT](https://user-images.githubusercontent.com/82372483/133255342-d2e955d2-c1fa-4e08-bc0e-8686fc128bf9.png)

![MISSED](https://user-images.githubusercontent.com/82372483/133255348-8167a46c-b594-4c26-9001-09765296f35f.png)

## TASK LIST
- [x] Implement *naive* AI
- [ ] Implement *intelligent* AI
