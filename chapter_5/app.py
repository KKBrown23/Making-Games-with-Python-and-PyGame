import random, sys, time, pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 1000
WINDOWHEIGHT = 800
FLASHSPEED = 500 
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4
WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0)
BRIGHTRED = (255, 0, 0) 
RED = (155, 0, 0)
BRIGHTGREEN = ( 0, 255, 0)
GREEN = ( 0, 155, 0)
BRIGHTBLUE = ( 0, 0, 255)
BLUE = ( 0, 0, 155)
BRIGHTYELLOW = (255, 255, 0)
YELLOW = (155, 155, 0)
DARKGRAY = ( 40, 40, 40)
bgColor = BLACK
XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, 
BUTTONSIZE, BUTTONSIZE)
REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, 
BUTTONSIZE, BUTTONSIZE)
GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + 
BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)


DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.draw.rect(DISPLAYSURF, BLUE, ((XMARGIN, YMARGIN),(BUTTONSIZE,BUTTONSIZE)))
pygame.draw.rect(DISPLAYSURF, BRIGHTGREEN,
                  ((XMARGIN + BUTTONSIZE + BUTTONGAPSIZE,
                    YMARGIN), 
                    (BUTTONSIZE,BUTTONSIZE)))
pygame.draw.rect(DISPLAYSURF, BRIGHTYELLOW, ((XMARGIN, YMARGIN +
                                              BUTTONSIZE + BUTTONGAPSIZE),
                                              (BUTTONSIZE,BUTTONSIZE)))
pygame.draw.rect(DISPLAYSURF, BRIGHTRED, ((XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, 
                                           YMARGIN + BUTTONSIZE + BUTTONGAPSIZE),(BUTTONSIZE,BUTTONSIZE)))
pygame.init()
clock = pygame.time.Clock()
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()

    pygame.display.update()
