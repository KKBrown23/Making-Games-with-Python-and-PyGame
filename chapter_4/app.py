import pygame, sys
from pygame.locals import *
import random, time

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 500
COL_NUMBER = 4
ROW_NUMBER = 4
TALE_SIZE = 95
STARTING_X = 160
STARTING_Y = 60
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
clock = pygame.time.Clock()

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

    drawing_x = STARTING_X
    drawing_y = STARTING_Y

    for x in range(0,len(board_data)):   
        drawing_x = STARTING_X 
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

movement = 2
direction = None
tale_to_animate_row = None
tale_to_animate_column = None
def animate(row, column, direction):
    if(not row or not column or not direction):
        return
    global movement
    x_coord = STARTING_X + row * TALE_SIZE
    y_coord = STARTING_Y + column * TALE_SIZE
    if direction == 'DOWN' and movement < TALE_SIZE:
        pygame.draw.rect(DISPLAYSURF, BLUE, ((x_coord, y_coord),(TALE_SIZE, TALE_SIZE)))
        pygame.draw.rect(DISPLAYSURF, GREEN, ((x_coord, y_coord+movement), (TALE_SIZE-5,TALE_SIZE-5)))
        textSurf = BASICFONT.render(str(BOARD_DATA[row][column]), True, WHITE)
        textRectObj = textSurf.get_rect()
        textRectObj.topleft=(x_coord + (TALE_SIZE/ 4)  , y_coord + (TALE_SIZE/4) +movement)
        DISPLAYSURF.blit(textSurf, textRectObj)
        movement += 1
    # Homework if direction is 'UP' substruct the movment from the y_coord
    # add move 'Left'
    # add move 'Right'

def check_movement(row, column, board_data):
    # check up
    if(row - 1 >= 0 and board_data[row-1][column] == 0):
        return 'UP'
    # check down
    if(row + 1 < ROW_NUMBER and board_data[row+1][column] == 0):
        return 'DOWN'
    # check left
    if(column - 1 >= 0 and board_data[row][column-1] == 0):
        return 'LEFT'
    # check right
    if(column + 1 < COL_NUMBER and board_data[row][column+1] == 0):
        return 'RIGHT'
    return None
while True:
    clock.tick(60)
    for event in pygame.event.get():
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        DISPLAYSURF.blit(newGameSurf, newGameRect)
        DISPLAYSURF.blit(resetGameSurf, resetGameRect)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = event.pos
            movement = 1
            col_index = int((pos[0] - STARTING_X) / TALE_SIZE)
            row_index = int((pos[1] - STARTING_Y) / TALE_SIZE)
            print(check_movement(row_index, col_index, BOARD_DATA))
    animate(tale_to_animate_row,tale_to_animate_column,direction)
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