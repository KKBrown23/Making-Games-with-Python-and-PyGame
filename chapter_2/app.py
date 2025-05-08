import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300)) # sets the height and width of the window
pygame.display.set_caption('Hello World!') # sets the title
fontObj = pygame.font.Font('freesansbold.ttf', 32) # Use pygame.font.Font() to create a new font object
textSurfaceObj = fontObj.render('Hello world!', True, (0,255,0),(0,0,255)) # Type the text into a surface object
textRectObj = textSurfaceObj.get_rect()         # Create a background for the text
textRectObj.center = (200, 150)                 

while True:                                 # infinite loop->run forever
    event_list = pygame.event.get() 
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)       # Copy the text surface to the main surface

    for event in event_list:        
        if event.type == QUIT:              # if we have a quit event
            pygame.quit()                   #stop the loop
            sys.exit()
    pygame.display.update()                 #update UI