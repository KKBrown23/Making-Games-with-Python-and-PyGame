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
animation_running = False
BOARD_DATA = [   [1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12], 
                 [13,14,0,15]]
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
newGameSurf, newGameRect = makeText('New Game', WHITE, GREEN, 560,350)

movement = 2
direction = None
tale_to_animate_row = None
tale_to_animate_column = None
def animate(row, column, direction):
    global movement, tale_to_animate_row, tale_to_animate_column, animation_running
    if row is None or column is None or direction is None:
        return
    if row is not None and column is not None and direction is not None:
        animation_running = True 
    # animation ends -> reseting
    if movement > TALE_SIZE:
        if direction == 'DOWN':
            BOARD_DATA[row+1][column] = BOARD_DATA[row][column]
            BOARD_DATA[row][column] = 0
        if direction == 'UP':
            BOARD_DATA[row-1][column] = BOARD_DATA[row][column]
            BOARD_DATA[row][column] = 0
        if direction == 'LEFT':
            BOARD_DATA[row][column-1] = BOARD_DATA[row][column]
            BOARD_DATA[row][column] = 0
        if direction == 'RIGHT':
            BOARD_DATA[row][column+1] = BOARD_DATA[row][column]
            BOARD_DATA[row][column] = 0
        print(check_data(BOARD_DATA))
        tale_to_animate_column = None
        tale_to_animate_row = None
        direction = None
        animation_running = False
    x_coord = STARTING_X + column * TALE_SIZE
    y_coord = STARTING_Y + row * TALE_SIZE
    if direction == 'DOWN' and movement < TALE_SIZE:
        pygame.draw.rect(DISPLAYSURF, BLUE, ((x_coord, y_coord),(TALE_SIZE, TALE_SIZE)))
        pygame.draw.rect(DISPLAYSURF, GREEN, ((x_coord, y_coord+movement), (TALE_SIZE-5,TALE_SIZE-5)))
        textSurf = BASICFONT.render(str(BOARD_DATA[row][column]), True, WHITE)
        textRectObj = textSurf.get_rect()
        textRectObj.topleft=(x_coord + (TALE_SIZE/ 4)  , y_coord + (TALE_SIZE/4) +movement)
        DISPLAYSURF.blit(textSurf, textRectObj)
        movement += 5
    if direction == 'UP' and movement < TALE_SIZE:

        pygame.draw.rect(DISPLAYSURF, BLUE, ((x_coord, y_coord),(TALE_SIZE, TALE_SIZE)))
        pygame.draw.rect(DISPLAYSURF, GREEN, ((x_coord, y_coord-movement), (TALE_SIZE-5,TALE_SIZE-5)))
        textSurf = BASICFONT.render(str(BOARD_DATA[row][column]), True, WHITE)
        textRectObj = textSurf.get_rect()
        textRectObj.topleft=(x_coord + (TALE_SIZE/ 4)  , y_coord + (TALE_SIZE/4) - movement)
        DISPLAYSURF.blit(textSurf, textRectObj)
        movement += 5
    if direction == 'RIGHT' and movement < TALE_SIZE:

        pygame.draw.rect(DISPLAYSURF, BLUE, ((x_coord, y_coord),(TALE_SIZE, TALE_SIZE)))
        pygame.draw.rect(DISPLAYSURF, GREEN, ((x_coord+movement, y_coord), (TALE_SIZE-5,TALE_SIZE-5)))
        textSurf = BASICFONT.render(str(BOARD_DATA[row][column]), True, WHITE)
        textRectObj = textSurf.get_rect()
        textRectObj.topleft=(x_coord + (TALE_SIZE/ 4) + movement , y_coord + (TALE_SIZE/4))
        DISPLAYSURF.blit(textSurf, textRectObj)
        movement += 5
    if direction == 'LEFT' and movement < TALE_SIZE:

        pygame.draw.rect(DISPLAYSURF, BLUE, ((x_coord, y_coord),(TALE_SIZE, TALE_SIZE)))
        pygame.draw.rect(DISPLAYSURF, GREEN, ((x_coord-movement, y_coord), (TALE_SIZE-5,TALE_SIZE-5)))
        textSurf = BASICFONT.render(str(BOARD_DATA[row][column]), True, WHITE)
        textRectObj = textSurf.get_rect()
        textRectObj.topleft=(x_coord + (TALE_SIZE/ 4) - movement , y_coord + (TALE_SIZE/4))
        DISPLAYSURF.blit(textSurf, textRectObj)
        movement += 5

def check_data(board_data):
    correct_number = 1
    for row in range(0, len(board_data)):
        for col in range(0, len(board_data[row])):
            if(row == ROW_NUMBER - 1 and col == COL_NUMBER - 1):
                return True
            current_element = board_data[row][col]
            if(current_element != correct_number):
                return False
            correct_number += 1
    return True

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

board_data_list = [
    [
        [5, 1, 3, 4],
        [2, 0, 7, 8],
        [6, 10, 11, 12],
        [9, 13, 14, 15]
    ], 
    [
        [1, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 7, 12],
        [13, 14, 11, 15]
    ],
    [
        [1, 0, 3, 4],
        [2, 5, 7, 8],
        [6, 10, 11, 12],
        [9, 13, 14, 15]
    ],
    [
        [5, 1, 3, 4],
        [2, 7, 8, 0],
        [6, 10, 11, 12],
        [9, 13, 14, 15]
    ],
    [
        [5, 1, 2, 3],
        [9, 6, 7, 4],
        [13, 10, 11, 8],
        [0, 14, 15, 12]
    ]
]

def reset():
    global BOARD_DATA
    # generate new board data
    random_index = random.randint(0, len(board_data_list))
    random_board_data = board_data_list[random_index]
    BOARD_DATA = random_board_data
    # redraw the board using the draw board function
    draw_board(BOARD_DATA)
while True:
    clock.tick(60)
    for event in pygame.event.get():
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        DISPLAYSURF.blit(newGameSurf, newGameRect)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if animation_running == True:
                continue
            pos = event.pos
            if((pos[0] > 560 and pos[0] <760) and (pos[1] > 350 and pos[1] < 375)  ):
                reset()
                continue
            
            movement = 1
            col_index = int((pos[0] - STARTING_X) / TALE_SIZE)
            row_index = int((pos[1] - STARTING_Y) / TALE_SIZE)
            direction = check_movement(row_index, col_index, BOARD_DATA)
            if(direction != None):
                tale_to_animate_row = row_index
                tale_to_animate_column = col_index
                
    animate(tale_to_animate_row,tale_to_animate_column,direction)
          
    pygame.display.update()