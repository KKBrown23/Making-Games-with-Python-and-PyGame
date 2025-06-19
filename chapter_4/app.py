import pygame, sys
from pygame.locals import *
import random, time

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 500
COL_NUMBER = 4
ROW_NUMBER = 4
TALE_SIZE = 95

GRAY = (100, 100, 100)
NAVYBLUE = ( 60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 200, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = ( 0, 255, 255)

BOARD_DATA = [   [10,3,14,7],
                 [5,13,1,4],
                 [2,8,6,15], 
                 [11,9,0,12]]
pygame.init()
DISPLAYSURF = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption('Sliding Tales')
BASICFONT = pygame.font.Font('freesansbold.ttf', 20)

def makeText(text, color, bgcolor, top, left):
 # create the Surface and Rect objects for some text.
    BASICFONT = pygame.font.Font('freesansbold.ttf', 24)
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

main_label = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = main_label.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (100, 15)
def draw_board(board_data):
    pygame.draw.rect(DISPLAYSURF, BLUE, ((150, 50), (400, 400)))

    drawing_x = 160
    drawing_y = 60

    for x in range(0,len(board_data)):   
        drawing_x = 160 
        for y in range(0,len(board_data[x])):
            if(board_data[x][y] != 0):
                pygame.draw.rect(DISPLAYSURF, GREEN, ((drawing_x, drawing_y), (TALE_SIZE-5,TALE_SIZE-5)))
                textSurf = BASICFONT.render(str(board_data[x][y]), True, WHITE)
                textRectObj = textSurf.get_rect()
                textRectObj.topleft=(drawing_x + (TALE_SIZE/ 4)  , drawing_y + (TALE_SIZE/4) )
                DISPLAYSURF.blit(textSurf, textRectObj)
            drawing_x += TALE_SIZE
        drawing_y += TALE_SIZE
draw_board(board_data=BOARD_DATA)


resetGameSurf, resetGameRect = makeText('Reset', WHITE, GREEN, 560,300)

newGameSurf, newGameRect = makeText('New Game', WHITE, GREEN, 560,350)




while True:
    for event in pygame.event.get():
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        DISPLAYSURF.blit(newGameSurf, newGameRect)
        DISPLAYSURF.blit(resetGameSurf, resetGameRect)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = event.pos
            # row_index = int(pos[1] / BOX_H)
            # col_index = int(pos[0] / BOX_W)
            # HMRK
            # show the shape
            # show_shape(row_index, col_index)
            # pygame.time.delay(2000)
            # Find the data for the shape in the board data
            # Search by row index and column index
            # Find the x1, y1, x2 and y2 using the formulas 
            # Draw the shape on the screen
            # check_combination
    pygame.display.update()