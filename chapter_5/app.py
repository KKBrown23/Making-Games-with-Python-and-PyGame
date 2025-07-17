import random, sys, time, pygame
from pygame.locals import *


# Homework
# show a pop-up message when the user gets the move wrong and the game restarts
# make another function that will take the move of the user and light the square that the user clicked
# and then turn it off again after half a second
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
array_of_random_moves = []
current_counter = 0
level = 3
level_label = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = level_label.render(f'Level: {level}', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (100, 15)
clock = pygame.time.Clock()
pygame.display.update()


def get_random_moves():
    global level
    random_moves = []
    for x in range(0, level):
        random_number = random.randint(1,4)
        random_moves.append(random_number)
    return random_moves
def update_level_label(level):
    global textSurfaceObj
    textSurfaceObj = level_label.render(f'Level: {level}', True, GREEN, BLUE)
    

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
array_of_random_moves = get_random_moves()
lighting_squares(array_of_random_moves)
def detect_move(mouse_pos):
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    if ((mouse_x >= XMARGIN and mouse_x <= XMARGIN + BUTTONSIZE)
        and (mouse_y >= YMARGIN and mouse_y <= YMARGIN + BUTTONSIZE)):
        return 1
    if ((mouse_x >= XMARGIN + BUTTONSIZE + BUTTONGAPSIZE
            and mouse_x <= XMARGIN + BUTTONSIZE * 2 + BUTTONGAPSIZE) 
            and (mouse_y >= YMARGIN  and mouse_y <= YMARGIN + BUTTONSIZE )):
                                                                
        return 2
        # Do for the remaining two squares
    if ((mouse_x >= XMARGIN and mouse_x <= XMARGIN + BUTTONSIZE) 
            and (mouse_y >= YMARGIN + BUTTONGAPSIZE + BUTTONSIZE and mouse_y <= YMARGIN + BUTTONSIZE * 2 + BUTTONGAPSIZE)):
        return 3
    if ((mouse_x >= XMARGIN + BUTTONGAPSIZE * 2 + BUTTONSIZE and mouse_x <= XMARGIN + BUTTONSIZE * 2 + BUTTONGAPSIZE)
            and (mouse_y >= YMARGIN + BUTTONSIZE + BUTTONGAPSIZE and mouse_y <= YMARGIN + BUTTONSIZE * 2 + BUTTONGAPSIZE)):
        return 4

def restart():
    global level, current_counter, array_of_random_moves
    level = 3
    current_counter = 0 
    array_of_random_moves = get_random_moves()
    lighting_squares(array_of_random_moves)

def check_move(user_move):
    global current_counter
    
    if(array_of_random_moves[current_counter] == user_move):
        current_counter += 1
    else:
        # TODO pop up a windows showing that the game is restarting
        restart()
    if(current_counter == len(array_of_random_moves)):
        print("You won")
        go_next_level()  
def go_next_level():
    global level, current_counter, array_of_random_moves
    current_counter = 0 
    level += 1
    array_of_random_moves = get_random_moves()
    update_level_label(level)
    lighting_squares(array_of_random_moves)
while True:
    clock.tick(FPS)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            user_move = detect_move(mouse_pos)
            # TODO: light clicked squar up
            check_move(user_move)
    pygame.display.update()
