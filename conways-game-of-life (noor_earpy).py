# -----------------------------------------------------------------------------
# NAME: Noor Earpy
# TITLE: Implementation of Conway's "Game of Life," version 3.
#        Using a list of rectangles, whose color is updated as their status
#        changes (from live to dead, or dead to live).
# -----------------------------------------------------------------------------

import tkinter as tk
import time
import random

WIN_W = 520
WIN_H = 520
CELL_W = 20
GRIDSIZE = int(WIN_W/CELL_W) - 2
PLAY = True
FPS = .25
BORDER = 'orange'
ON = 'blue'
OFF = 'black'


class Tile:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.status = 0
        x1 = CELL_W * col
        y1 = CELL_W * row
        x2 = CELL_W + (CELL_W*col)
        y2 = CELL_W + (CELL_W*row)
        self.shape = canvas.create_rectangle(x1, y1, x2, y2,
                                        width=0, fill=BORDER)      

class Cell(Tile):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.status = random.randrange(2)
        self.neighbors = 0
        self.set_color()
       
       
    def count_neighbors(self):
        nscore = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                nscore += cgrid[self.row+x][self.col+y].status
        self.neighbors = nscore - self.status
                   
    def set_status(self):
        if self.status == 1:
            if self.neighbors not in [2, 3]:
                self.status = 0
                self.set_color()          
            else:
                if self.neighbors == 3:
                    self.status = 1
                    self.set_color()
   
               
    def set_color(self):
        canvas.itemconfig(self.shape, fill=ON) if self.status == 1\
                                else canvas.itemconfig(self.shape, fill=OFF)
             
# -----------------------------------------------------------------------------
# Gracefully respond to closing of the game window
# -----------------------------------------------------------------------------

def on_closing():
    global PLAY
    PLAY= False
    print('Game Ended')

# -----------------------------------------------------------------------------
# Defining main
# -----------------------------------------------------------------------------

def main():
   
    global cgrid
    global canvas
   
# -----------------------------------------------------------------------------
# Create the game window
# -----------------------------------------------------------------------------  

    window = tk.Tk()
    window.title('Game of Life v3 - Noor Earpy')
    canvas = tk.Canvas(window, width=WIN_W, height=WIN_H)
    canvas.pack()
   
# -------------------------------------------------------------------------
# Create Grid of Tile/Cell Objects (cgrid)
# -------------------------------------------------------------------------    
    cgrid = list()
    for row in range(GRIDSIZE+2):
         cgrid.append([])
         for col in range(GRIDSIZE+2):
             cgrid[row].append(Tile(row, col))  
    while PLAY:
       
        # ---------------------------------------------------------------------
        # Show window and pause (FPS)
        # ---------------------------------------------------------------------
        cgrid =  list()
        for row in range(GRIDSIZE+2):
            cgrid.append([])
            for col in range(GRIDSIZE+2):
                if row in [0, GRIDSIZE+1] or col in [0, GRIDSIZE+1]:
                    cgrid[row].append(Tile(row,col))
                else:
                    cgrid[row].append(Cell(row,col))
       
       
       

        window.update()
        time.sleep(FPS)
       
        # ---------------------------------------------------------------------
        # Count the number of live neighbors
        # ---------------------------------------------------------------------
           
        for row in cgrid:
            msg= ''
            for item in row:
                if type(item) is Tile:
                    canvas.itemconfig(item.shape, fill=BORDER)
                else:
                    item.count_neighbors()
     
        # ---------------------------------------------------------------------
        # Set the status of cells
        # ---------------------------------------------------------------------
       
        if item.status == 1:
            if item.neighbors not in [2,3]:
                item.status= 0
                item.set_color()
            else:
                if item.neighbors == 3:
                    item.status=1
                    item.set_color()
       
        # ---------------------------------------------------------------------
        # Detect the closing of the game window
        # ---------------------------------------------------------------------
       
        window.protocol('WM_DELETE_WINDOW', on_closing)
       
    window.destroy()    
             
# -----------------------------------------------------------------------------
# Call to main()
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    main()