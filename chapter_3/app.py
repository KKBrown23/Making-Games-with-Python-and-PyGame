import pygame, sys
from pygame.locals import *
import random, time

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
COL_NUMBER = 6
ROW_NUMBER = 4
BOX_W = CANVAS_WIDTH / COL_NUMBER
BOX_H = CANVAS_HEIGHT / ROW_NUMBER
OPENED_SHAPE = None
GRAY = (100, 100, 100)
NAVYBLUE = ( 60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = ( 0, 255, 255)

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

COLOUR_LIST = [RED, GRAY, NAVYBLUE, WHITE, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN]
SHAPE_LIST = [DONUT, SQUARE, DIAMOND, LINES, OVAL]
BOARD_DATA = []
pygame.init()
DISPLAYSURF = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption('Memory Game')




def generate_board_data(ROW_NUMBER, COL_NUMBER):
    assert ROW_NUMBER * COL_NUMBER % 2 == 0, 'Number of boxes needs to be even'
    number_unique_shapes = int((ROW_NUMBER * COL_NUMBER)/2)
    ran_shape_list = []
    # find a way to generate unique random shapes
    counter = 0
    while counter <  number_unique_shapes:
        ran_index = random.randint(0, len(COLOUR_LIST)-1)
        random_colour = COLOUR_LIST[ran_index]
        ran_index = random.randint(0, len(SHAPE_LIST)-1)
        random_shape = SHAPE_LIST[ran_index]
        new_shape = {
            'shape':  random_shape, 
            'colour':  random_colour,
        }
        # check if the shape is generated before
        is_unique = check_unique_shape_colour(new_shape, ran_shape_list)
        if not is_unique:
            continue

        ran_shape_list.append(new_shape)
        ran_shape_list.append(new_shape)
        counter += 1
    random.shuffle(ran_shape_list)
    global BOARD_DATA
    BOARD_DATA = ran_shape_list

def check_unique_shape_colour(new_shape, ran_shape_list):
    for x in range(0, len(ran_shape_list)):
        ran_shape = ran_shape_list[x]
        if new_shape['shape'] == ran_shape['shape'] and new_shape['colour'] == ran_shape['colour']:
            return False
    return True    

def box_creation():
    for row_index in range(0, ROW_NUMBER):
        for col_index in range(0, COL_NUMBER):
            x1 = col_index * BOX_W
            y1 = row_index * BOX_H
            x2 = col_index * BOX_W + BOX_W
            y2 = row_index * BOX_H + BOX_H
            pygame.draw.rect(DISPLAYSURF, 
                             (255, 255, 255 ),
            ((x1,y1), (x2,y2)) , width=3)
def show_shape(row_index, col_index):
    shape_index = row_index*COL_NUMBER + col_index
    current_shape = BOARD_DATA[shape_index]
    shape_coords = get_coords(row_index, col_index)
    quarter = int(BOX_W * 0.25) # syntactic sugar
    half = int(BOX_H * 0.5) # syntactic sugar
    
    if(current_shape['shape'] == OVAL):
        pygame.draw.ellipse(DISPLAYSURF, current_shape['colour'], 
                            (shape_coords['x1'], shape_coords['y1'] + BOX_H/4 , BOX_W, BOX_H/2),
                              0)
    if(current_shape['shape'] == DONUT):
        pygame.draw.circle(DISPLAYSURF, current_shape['colour'], (shape_coords['x1'] + half, shape_coords['y1'] + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, (0,0,0), (shape_coords['x1'] + half, shape_coords['y1'] + half), quarter - 5)
    if(current_shape['shape'] == SQUARE):
        pygame.draw.rect(DISPLAYSURF, current_shape['colour'], (shape_coords['x1']+BOX_W/4, shape_coords['y1']+BOX_H/4, BOX_W/2, BOX_H/2), 0)
    # draw the other shapes keep in mind that quater = BOX_W/4 half = BOX_W / 2, left => shap_coords['x1], top => shape_coords['y1]
    if(current_shape['shape'] == DIAMOND):
        pygame.draw.polygon(DISPLAYSURF, current_shape['colour'], ((shape_coords['x1'] + BOX_W / 2, shape_coords['y1']), (shape_coords['x1']
        + BOX_W - 1, shape_coords['y1'] + BOX_W / 2), (shape_coords['x1'] + BOX_W / 2, shape_coords['y1'] + BOX_W - 1), (shape_coords['x1'],  shape_coords['y1'] + 
        BOX_W / 2)))
    if(current_shape['shape'] == LINES):
        for i in range(0, int(BOX_W), 4):
            pygame.draw.line(DISPLAYSURF, current_shape['colour'], (shape_coords['x1'] , shape_coords['y1'] + i), (shape_coords['x1'] + 
            i, shape_coords['y1'] ))
            pygame.draw.line(DISPLAYSURF, current_shape['colour'], (shape_coords['x1'] + i, shape_coords['y1'] + BOX_W 
            - 1), (shape_coords['x1']+ BOX_W - 1, shape_coords['y1'] + i))
    if(current_shape['shape'] == OVAL):
        pygame.draw.ellipse(DISPLAYSURF, current_shape['colour'], (shape_coords['x1'], shape_coords['y1'] + BOX_W / 4, 
        BOX_W, BOX_W / 2))
    pygame.display.update()
    check_shape(row_index, col_index)

def check_shape(row_index, col_index):

    global OPENED_SHAPE
    shape_index = row_index*COL_NUMBER + col_index
    current_shape = BOARD_DATA[shape_index]
    shape_coords = get_coords(row_index, col_index)
    
    if OPENED_SHAPE != None:
        pygame.time.wait(1000)

        opened_shape_coords = get_coords(OPENED_SHAPE['row_index'], OPENED_SHAPE['col_index'])
        if current_shape['shape'] == OPENED_SHAPE['shape'] and current_shape['colour'] == OPENED_SHAPE['colour']:
            OPENED_SHAPE = None
        else:
            OPENED_SHAPE = None
            pygame.draw.rect(DISPLAYSURF, 
                             (0, 0, 0 ),
            (shape_coords['x1'],shape_coords['y1'], BOX_W, BOX_H), 0 )
            pygame.draw.rect(DISPLAYSURF, 
                             (255, 255, 255 ),
            (shape_coords['x1'],shape_coords['y1'], BOX_W, BOX_H), width=3)
            pygame.draw.rect(DISPLAYSURF, 
                             (0, 0, 0 ),
            (opened_shape_coords['x1'],opened_shape_coords['y1'], BOX_W, BOX_H) , 0)
            pygame.draw.rect(DISPLAYSURF, 
                             (255, 255, 255 ),
            (opened_shape_coords['x1'],opened_shape_coords['y1'], BOX_W, BOX_H), width=3)
    else:
        OPENED_SHAPE = {
            'shape': current_shape['shape'],
            'colour': current_shape['colour'],
            'row_index': row_index,
            'col_index': col_index
        }
    # check if we have an opened shape 
    #       if yes -> check if they match
    #           if yes-> leave open + cleare the opened-shape variable
    #           if not -> close then + clear the opened-shape
    # if don't have opened-card
    #   initialize opened-card 
def get_coords(row_index, col_index):
    x1 = col_index * BOX_W
    y1 = row_index * BOX_H
    x2 = col_index * BOX_W + BOX_W
    y2 = row_index * BOX_H + BOX_H
    return {'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2}

box_creation()
generate_board_data(ROW_NUMBER, COL_NUMBER)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = event.pos
            row_index = int(pos[1] / BOX_H)
            col_index = int(pos[0] / BOX_W)
            # HMRK
            # show the shape
            show_shape(row_index, col_index)
            # pygame.time.delay(2000)
            # Find the data for the shape in the board data
            # Search by row index and column index
            # Find the x1, y1, x2 and y2 using the formulas 
            # Draw the shape on the screen
            # check_combination
    pygame.display.update()

