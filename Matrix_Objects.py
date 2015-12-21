# -*- coding: utf-8 -*-

'''
Created on Dec, 2015
@author: Timur
'''

import pygame
import pygame.font
from pygame import *
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
RANDOM_COLOR = (200, 200, 200)

z = 50 #zoom factor
pygame.init() #initialization of pygame
basicFont = pygame.font.SysFont(None, z/2) #initialozation of pygame font
FPS = 30 #frames per second (pygame thing)
fpsClock = pygame.time.Clock() #clock init. (pygame thing)
shapes_list = []

class Cell:
    isSingleton = False #is this thing singleton and doesn't have ajacent filled spots?
    isObject = False #is it part of the object?
    isFilled = False #does it exist? (we eventually delete everything)
    whichColor = (200,200,200) #which color the cell have?
    whichID = 0

gridX = 15 #size of matrix in X
gridY = 10 #size of matrix in Y

DISPLAY = (gridX*z+z, gridY*z+z) # display (pygame thing)

grid = [[Cell() for i in range(0,gridY)] for j in range(0,gridX)] #creating the matrix

def draw_grid(screen, grid):
    """This function draws cell grid. Singletons painted dark grey, objects - colored.
    """
    for i in range(0,gridX):
        for j in range(0,gridY):

            if (grid[i][j].isFilled == True) and (grid[i][j].isObject == False):
                pygame.draw.rect(screen, WHITE, (z + i * z, z + j * z, z, z))
            if (grid[i][j].isFilled == False) and (grid[i][j].isSingleton == True):
                pygame.draw.rect(screen, GRAY, (z + i * z, z + j * z, z, z))
            if (grid[i][j].isFilled == False) and (grid[i][j].isSingleton == False):
                pygame.draw.rect(screen, BLACK, (z + i * z, z + j * z, z, z))
            if (grid[i][j].isObject == True): #(grid[i][j].isFilled == False) and
                pygame.draw.rect(screen, grid[i][j].whichColor, (z + i * z, z + j * z, z, z))

def render_text(screen, grid):
    """This function renders text on grid.
    """
    for i in range(0,gridX):
        for j in range(0,gridY):
            if (grid[i][j].isObject == True):
                text = basicFont.render(str(grid[i][j].whichID), True, WHITE, GRAY)
                textRect = text.get_rect()
                textRect.centerx = z+i*z+z/2
                textRect.centery = z+j*z+z/2
                screen.blit(text, textRect)


def random_cell():
    """Populating grid with random data.
    """

    someNumber = 0

    for i in range(0, gridX):
        for j in range(0, gridY):
            someNumber = random.randint(0,100)
            if (someNumber > 70): #the less this number is the more cell there will be on grid
                grid[i][j].isFilled = True

def delete_singletons():
    """Hunting down the cells that are singletons and that we don't need
    """

    for i in range(1,gridX-1):
        for j in range(1,gridY-1):
            if (grid[i][j].isFilled == True) and (grid[i-1][j].isFilled == False) and (grid[i][j-1].isFilled == False) and (grid[i+1][j].isFilled == False) and (grid[i][j+1].isFilled == False):
                #print('Singleton Found! Location:', i, j)
                #print(grid[i][j].isFilled)
                grid[i][j].isSingleton = True
                grid[i][j].isFilled = False
                #print(grid[i][j].isSingleton)
                #print(grid[i][j].isFilled)
    for i in range(1,gridX-1):
        if (grid[i][0].isFilled == True) and (grid[i-1][0].isFilled == False) and (grid[i+1][0].isFilled == False) and (grid[i][1].isFilled == False):
            #print('Top Border Singleton Found!')
            grid[i][0].isSingleton = True
            grid[i][0].isFilled = False
        if (grid[i][gridY-1].isFilled == True) and (grid[i-1][gridY-1].isFilled == False) and (grid[i+1][gridY-1].isFilled == False) and (grid[i][gridY-2].isFilled == False):
            #print('Bottom Border Singleton Found!')
            grid[i][gridY-1].isSingleton = True
            grid[i][gridY-1].isFilled = False

    for j in range(1,gridY-1):
        if (grid[0][j].isFilled == True) and (grid[0][j-1].isFilled == False) and (grid[0][j+1].isFilled == False) and (grid[1][j].isFilled == False):
            #print('Left Border Singleton Found!')
            grid[0][j].isSingleton = True
            grid[0][j].isFilled = False
        if (grid[gridX-1][j].isFilled == True) and (grid[gridX-1][j-1].isFilled == False) and (grid[gridX-1][j+1].isFilled == False) and (grid[gridX-2][j].isFilled == False):
            #print('Right Border Singleton Found!')
            grid[gridX-1][j].isSingleton = True
            grid[gridX-1][j].isFilled = False

    if (grid[0][0].isFilled == True) and (grid[0][1].isFilled == False) and (grid[1][0].isFilled == False):
        #print('Top left corner Singleton Found!')
        grid[0][0].isSingleton = True
        grid[0][0].isFilled = False

    if (grid[gridX-1][0].isFilled == True) and (grid[gridX-1][1].isFilled == False) and (grid[gridX-2][0].isFilled == False):
        print('Top right corner Singleton Found!')
        grid[gridX-1][0].isSingleton = True
        grid[gridX-1][0].isFilled = False

    if (grid[0][gridY-1].isFilled == True) and (grid[0][gridY-2].isFilled == False) and (grid[1][gridY-1].isFilled == False):
        #print('Bottom left corner Singleton Found!')
        grid[0][gridY-1].isSingleton = True
        grid[0][gridY-1].isFilled = False

    if (grid[gridX-1][gridY-1].isFilled == True) and (grid[gridX-2][gridY-1].isFilled == False) and (grid[gridX-1][gridY-2].isFilled == False):
        #print('Bottom right corner Singleton Found!')
        grid[gridX-1][gridY-1].isSingleton = True
        grid[gridX-1][gridY-1].isFilled = False


def cut_object(x,y,objectID,direction):
    """Using recursion to flood fill object we just found
    """

    global shapes_list

    grid[x][y].isObject = True #ok this is part of object what we do next?
    grid[x][y].whichColor = RANDOM_COLOR #this will be the color of cell
    grid[x][y].whichID = objectID

    shapes_list[objectID-1] = shapes_list[objectID-1] + direction

    #CHECK IF CELL IS IN CORNER
    if (x==0) and (y==0): #if cell in left top corner
        if (grid[x+1][y].isObject == False) and (grid[x+1][y].isFilled):#...on the right
            cut_object(x+1,y,objectID,'R')
        if (grid[x][y+1].isObject == False) and (grid[x][y+1].isFilled): #on the bottom
            cut_object(x,y+1,objectID,'D')
    elif (x==gridX-1) and (y==gridY-1): #if cell in right bottom corner
        if (grid[x-1][y].isObject == False) and (grid[x-1][y].isFilled):#checking cell on the left
            cut_object(x-1,y,objectID,'L') #recursion yay!
        if (grid[x][y-1].isObject == False) and (grid[x][y-1].isFilled):#...on the top
            cut_object(x,y-1,objectID,'U')
    elif (x==0) and (y==gridY-1): #if cell in bottom corner
        if (grid[x+1][y].isObject == False) and (grid[x+1][y].isFilled):#...on the right
            cut_object(x+1,y,objectID,'R')
        if (grid[x][y-1].isObject == False) and (grid[x][y-1].isFilled):#...on the top
            cut_object(x,y-1,objectID,'U')
    elif (x==gridX-1) and (y==0): #if cell in right top corner
        print('in corner!')
        if (grid[x-1][y].isObject == False) and (grid[x-1][y].isFilled):#checking cell on the left
            cut_object(x-1,y,objectID,'L') #recursion yay!
        if (grid[x][y+1].isObject == False) and (grid[x][y+1].isFilled): #on the bottom
            cut_object(x,y+1,objectID,'D')
    #CHECK IF CELL IS ON BORDER
    elif (x==0): #left border
        if (grid[x+1][y].isObject == False) and (grid[x+1][y].isFilled):#...on the right
            cut_object(x+1,y,objectID,'R')
        if (grid[x][y-1].isObject == False) and (grid[x][y-1].isFilled):#...on the top
            cut_object(x,y-1,objectID,'U')
        if (grid[x][y+1].isObject == False) and (grid[x][y+1].isFilled): #on the bottom
            cut_object(x,y+1,objectID,'D')
    elif (x==gridX-1): #right border
        if (grid[x-1][y].isObject == False) and (grid[x-1][y].isFilled):#checking cell on the left
            cut_object(x-1,y,objectID,'L') #recursion yay!
        if (grid[x][y-1].isObject == False) and (grid[x][y-1].isFilled):#...on the top
            cut_object(x,y-1,objectID,'U')
        if (grid[x][y+1].isObject == False) and (grid[x][y+1].isFilled): #on the bottom
            cut_object(x,y+1,objectID,'D')
    elif (y==0): #top border
        if (grid[x-1][y].isObject == False) and (grid[x-1][y].isFilled):#checking cell on the left
            cut_object(x-1,y,objectID,'L') #recursion yay!
        if (grid[x+1][y].isObject == False) and (grid[x+1][y].isFilled):#...on the right
            cut_object(x+1,y,objectID,'R')
        if (grid[x][y+1].isObject == False) and (grid[x][y+1].isFilled): #on the bottom
            cut_object(x,y+1,objectID,'D')
    elif (y==gridY-1): #bottom
        if (grid[x-1][y].isObject == False) and (grid[x-1][y].isFilled):#checking cell on the left
            cut_object(x-1,y,objectID,'L') #recursion yay!
        if (grid[x+1][y].isObject == False) and (grid[x+1][y].isFilled):#...on the right
            cut_object(x+1,y,objectID,'R')
        if (grid[x][y-1].isObject == False) and (grid[x][y-1].isFilled):#...on the top
            cut_object(x,y-1,objectID,'U')
    #if nothing above triggered then it's not border case
    else:
        #print(x,y, '---', gridX, gridY)
        if (grid[x-1][y].isObject == False) and (grid[x-1][y].isFilled):#checking cell on the left
            cut_object(x-1,y,objectID,'L') #recursion yay!
        if (grid[x+1][y].isObject == False) and (grid[x+1][y].isFilled):#...on the right
            cut_object(x+1,y,objectID,'R')
        if (grid[x][y-1].isObject == False) and (grid[x][y-1].isFilled):#...on the top
            cut_object(x,y-1,objectID,'U')
        if (grid[x][y+1].isObject == False) and (grid[x][y+1].isFilled): #on the bottom
            cut_object(x,y+1,objectID,'D')



def find_shapes():
    """Finding object. Because we cut all singletons, all we need is existing cell that is not yet part of object
    """

    objectsNumber = 0

    global RANDOM_COLOR
    global shapes_list

    for x in range(0,gridX):#Here we start moving on the axis X verifying each cell
        for y in range(0,gridY):#And here we start moving on the axis Y verifying each cell
            if ((grid[x][y].isFilled == True) and (grid[x][y].isObject == False)):
                #because we took away all singletons the first non-empty grid cell is what we need
                objectsNumber+=1 #here we increase variable of how many shapes - it also serves as ID of shape
                shapes_list.append('') #this is the list containing all the "forms"
                RANDOM_COLOR = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
                cut_object(x,y,objectsNumber,'x') #calling flood_fill
    print('RESULT: %s' % objectsNumber)

    for i in range(1,objectsNumber+1):
        print('Form number ', i, ' has the form of ', shapes_list[i-1])



def main():
    """Main.
    """
    print('Press Space to quit')

    screen = pygame.display.set_mode((gridX*z+z*2, gridY*z+z*2))
    pygame.display.set_caption(("Matrix_Objects"))

    bg = Surface((gridX*z+z*2,gridY*z+z*2)) # Creating view field

    random_cell()
    delete_singletons()
    find_shapes()

    while True: # Main iteration cycle
       # fpsClock.tick(20)
        for e in pygame.event.get(): # Events
            if e.type == KEYDOWN and e.key == K_SPACE:
                turn = True
                raise SystemExit("QUIT")


        screen.blit(bg, (0,0))      # Redrawing screen each iteration
        fpsClock.tick(30)
        draw_grid(screen,grid)
        render_text(screen,grid)
        time.delay(100)
        pygame.display.update()     # Updating screen


if __name__ == '__main__':
    main()
