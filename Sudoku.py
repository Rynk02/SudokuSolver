'''
Creates and solves a sudoku puzzle
Created on Sep 6, 2020

@author: randy
'''
import turtle
import tkinter as tk
import random
import sys
import os
#grid
grid = []
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])


#turtle
t = turtle.Turtle()
t.speed(0)
t._tracer(0, 0)
t.color("#000000")
t.hideturtle()
topLeftX = -150
topLeftY = 150

wn = turtle.Screen()

canvas = turtle.getcanvas()
parent = canvas.master

button1 = tk.Button(parent, text='Solve', command = lambda: solve(grid))
id1 = canvas.create_window((-100,-200), window=button1)

button2 = tk.Button(parent, text='Restart', command = lambda:restart_program())
id2 = canvas.create_window((-50,-200), window=button2)

#restart
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
#makes a random grid
numbers = [1,2,3,4,5,6,7,8,9]
def makeGrid(grid):
    for i in range(0,81):
        #print("next number")
        row = i // 9
        column = i % 9
        if (grid[row][column] == 0):
            random.shuffle(numbers)
            for i in numbers:
                grid[row][column] = i;
                if (check(grid, row, column)):
                    if row == 8 and column == 8:
                        return 
                    
                    makeGrid(grid)
                    
                    if grid[8][8] != 0:
                        return
                        
                    if (i == numbers[-1]):
                        grid[row][column] = 0
                        return
                else:
                    if(i == numbers[-1]):
                        #for z in range (9):
                            # print (grid[z])
                        #print ("-------------------")
                        grid[row][column] = 0

                        #print ("backtrack")
                        return 
#clears a random number of cells (needs improvement, can sometimes create unsolvable puzzles)
def clearBoard(grid):
    for i in range(50):
        row = random.randint(1, 8)
        column = random.randint(1, 8)
        if (grid[row][column] != 0):
            grid[row][column] = 0     
                    
def printGrid(grid):
    for i in range(9):
        print(grid[i])
    print("----------------------")
    
            
def text(message,x,y,size):
    FONT = ("Arial", size, "normal")
    t.penup()
    t.goto(x,y)
    t.write(message, align="center", font = FONT)


#draws the grid (needs improvement)
def drawGrid(grid):
    intDist = 35
    for row in range(0,10):
        if (row % 3) == 0:
            t.pensize(3)
        else:
            t.pensize(1)
        t.penup()
        t.goto(topLeftX, topLeftY - row * intDist)
        t.pendown()
        t.goto(topLeftX + 9 * intDist,topLeftY - row * intDist)
    for column in range (0,10):
        if (column % 3) == 0:
            t.pensize(3)
        else:
            t.pensize(1)
        t.penup()
        t.goto(topLeftX + column * intDist, topLeftY)
        t.pendown()
        t.goto(topLeftX + column * intDist, topLeftY - 9 * intDist)

    for row in range(9):
        for column in range(9):
            if grid[row][column] != 0:
                text(grid[row][column], topLeftX + column * intDist + 9, topLeftY - row * intDist - intDist + 8, 18)
                
def solve(grid):
    for i in range(0,81):
        row = i // 9
        column = i % 9 
        if(grid[row][column] == 0):
            for i in range (1, 10):
                #print ("row " + str(row) + ' column ' + str(column))
                grid[row][column] = i;
                if (check(grid, row, column)):
                    t.clear()
                    drawGrid(grid)
                    t.getscreen().update()
                    if row == 8 and column == 8:
                        return 
                    
                    solve(grid)
                    
                    if grid[8][8] != 0:
                        return
                        
                    if (i == 9):
                        grid[row][column] = 0
                        return
                else:
                    if(i == 9):
                        #for z in range (9):
                            # print (grid[z])
                        #print ("-------------------")
                        grid[row][column] = 0

                        #print ("backtrack")
                        return
        
#if the number is okay check returns true
def check(grid, row, column):
    
    #checks the row returns false if the number is repeated
    for i in range (9):
        if (column == i):
            continue
        if (grid[row][column] == grid[row][i]):
            return False
        
    #checks the column false if the number is repeated
    for i in range (9):
        if (row == i):
            continue
        if (grid[row][column] == grid[i][column]):
            return False
        
    #check every subcube (needs improvement)
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            for r in range(i, i+3):
                for c in range(j, j+3):
                    if (grid[r][c] != 0):
                        temp.append(grid[r][c])
            if len(temp) != len(set(temp)):
                return False;
                
            
    return True
#main
makeGrid(grid)
clearBoard(grid)
drawGrid(grid)
t.getscreen()._root.mainloop()

