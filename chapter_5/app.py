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
WAITING_TIME = 500

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.draw.rect(DISPLAYSURF, BLUE, ((XMARGIN, YMARGIN),(BUTTONSIZE,BUTTONSIZE)))
pygame.draw.rect(DISPLAYSURF, GREEN,
                  ((XMARGIN + BUTTONSIZE + BUTTONGAPSIZE,
                    YMARGIN), 
                    (BUTTONSIZE,BUTTONSIZE)))
pygame.draw.rect(DISPLAYSURF, YELLOW, ((XMARGIN, YMARGIN +
                                              BUTTONSIZE + BUTTONGAPSIZE),
                                              (BUTTONSIZE,BUTTONSIZE)))
pygame.draw.rect(DISPLAYSURF, RED, ((XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, 
                                           YMARGIN + BUTTONSIZE + BUTTONGAPSIZE),(BUTTONSIZE,BUTTONSIZE)))
pygame.init()
clock = pygame.time.Clock()
pygame.display.update()

# Input: the amount of random moves
# Calculations: Make a loop that repeats as many times as the amount
#                   for each repeat:
#                       generate a random number then add to the array  
#                       range should be 1-4
# Output: Array of random moves
array_of_random_moves = []

def random_moves(amount_of_random_moves):
    for x in range(0, amount_of_random_moves):
        random_number = random.randint(1,4)
        array_of_random_moves.append(random_number)
    return array_of_random_moves

def lighting_squares(array_of_random_moves):
    for x in range(0, len(array_of_random_moves)):
        pygame.time.wait(WAITING_TIME)
        random_move = array_of_random_moves[x]
        if random_move == 1:
            pygame.draw.rect(DISPLAYSURF, BRIGHTBLUE, ((XMARGIN, YMARGIN),(BUTTONSIZE,BUTTONSIZE)))
            pygame.display.update()
            pygame.time.wait(WAITING_TIME)
            pygame.draw.rect(DISPLAYSURF, BLUE, ((XMARGIN, YMARGIN),(BUTTONSIZE,BUTTONSIZE)))
            pygame.display.update()

        if random_move == 2:
            pygame.draw.rect(DISPLAYSURF, BRIGHTGREEN,
                  ((XMARGIN + BUTTONSIZE + BUTTONGAPSIZE,
                    YMARGIN), 
                    (BUTTONSIZE,BUTTONSIZE)))
            pygame.display.update()
            pygame.time.wait(WAITING_TIME)
            pygame.draw.rect(DISPLAYSURF, GREEN,
                  ((XMARGIN + BUTTONSIZE + BUTTONGAPSIZE,
                    YMARGIN), 
                    (BUTTONSIZE,BUTTONSIZE)))
            pygame.display.update()
        if random_move == 3:
            pygame.draw.rect(DISPLAYSURF, BRIGHTYELLOW, ((XMARGIN, YMARGIN +
                                              BUTTONSIZE + BUTTONGAPSIZE),
                                              (BUTTONSIZE,BUTTONSIZE)))
            pygame.display.update()
            pygame.time.wait(WAITING_TIME)
            pygame.draw.rect(DISPLAYSURF, YELLOW, ((XMARGIN, YMARGIN +
                                              BUTTONSIZE + BUTTONGAPSIZE),
                                              (BUTTONSIZE,BUTTONSIZE)))

            pygame.display.update()
        if random_move == 4:
            pygame.draw.rect(DISPLAYSURF, BRIGHTRED, ((XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, 
                                           YMARGIN + BUTTONSIZE + BUTTONGAPSIZE),(BUTTONSIZE,BUTTONSIZE)))
            pygame.display.update()
            pygame.time.wait(1000)
            pygame.draw.rect(DISPLAYSURF, RED, ((XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, 
                                           YMARGIN + BUTTONSIZE + BUTTONGAPSIZE),(BUTTONSIZE,BUTTONSIZE)))
            pygame.display.update()
lighting_squares(random_moves(5))
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            if ((mouse_x >= XMARGIN and mouse_x <= XMARGIN + BUTTONSIZE)
                and (mouse_y >= YMARGIN and mouse_y <= YMARGIN + BUTTONSIZE)):
                print('You clicked on the first square')
            if ((mouse_x >= XMARGIN + BUTTONSIZE + BUTTONGAPSIZE
                 and mouse_x <= XMARGIN + BUTTONSIZE * 2 + BUTTONGAPSIZE) 
                 and (mouse_y >= YMARGIN  and mouse_y <= YMARGIN + BUTTONSIZE )):
                                                                     
                print('You clicked on the second square')
            # Do for the remaining two squares
            if ((mouse_x >= XMARGIN and mouse_x <= XMARGIN + BUTTONSIZE) 
                 and (mouse_y >= YMARGIN + BUTTONGAPSIZE + BUTTONSIZE and mouse_y <= YMARGIN + BUTTONSIZE * 2 + BUTTONGAPSIZE)):
                print('You clicked on the third square')
            if ((mouse_x >= XMARGIN + BUTTONGAPSIZE * 2 + BUTTONSIZE and mouse_x <= XMARGIN + BUTTONSIZE * 2 + BUTTONGAPSIZE)
                 and (mouse_y >= YMARGIN + BUTTONSIZE + BUTTONGAPSIZE and mouse_y <= YMARGIN + BUTTONSIZE * 2 + BUTTONGAPSIZE)):
                print('You clicked on the fourth square')
            print(mouse_pos)
    pygame.display.update()
