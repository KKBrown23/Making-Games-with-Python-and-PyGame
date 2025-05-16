import pygame, sys
from pygame.locals import *
import random

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
COL_NUMBER = 6
ROW_NUMBER = 4

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

pygame.init()
DISPLAYSURF = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption('Memory Game')




def generate_board_data(nr_of_rows, nr_of_columns):
    assert nr_of_rows * nr_of_columns % 2 == 0, 'Number of boxes needs to be even'
    number_unique_shapes = int((nr_of_rows * nr_of_columns)/2)
    ran_shape_list = []
    # find a way to generate unique random shapes
    counter = 0
    while counter <  number_unique_shapes:
        ran_index = random.randint(0, len(COLOUR_LIST)-1)
        random_colour = COLOUR_LIST[ran_index]
        ran_index = random.randint(0, len(SHAPE_LIST)-1)
        random_shape = SHAPE_LIST[ran_index]
        new_shape = {
            'row': None,
            'column': None,
            'shape':  random_shape, 
            'colour':  random_colour,
        }
        # check if the shape is generated before
        is_unique = check_unique_shape_colour(new_shape, ran_shape_list)
        if not is_unique:
            counter -= 1
        ran_shape_list.append(new_shape)
        ran_shape_list.append(new_shape)
        counter += 1
    random.shuffle(ran_shape_list)
    for row in range(0,nr_of_rows):
        for column in range(0,nr_of_columns):
            ran_shape_list[(row + 1) * column]['row'] = row
            ran_shape_list[(row + 1) * column]['column'] = column
            print(ran_shape_list[(row + 1) * column])
def check_unique_shape_colour(new_shape, ran_shape_list):
    for x in range(0, len(ran_shape_list)):
        ran_shape = ran_shape_list[x]
        if new_shape['shape'] == ran_shape['shape'] and new_shape['colour'] == ran_shape['colour']:
            return False
    return True    

def box_creation():
    box_w = CANVAS_WIDTH / COL_NUMBER
    box_h = CANVAS_HEIGHT / ROW_NUMBER
    for row_index in range(0, ROW_NUMBER):
        for col_index in range(0, COL_NUMBER):
            x1 = col_index * box_w
            y1 = row_index * box_h
            x2 = col_index * box_w + box_w
            y2 = row_index * box_h + box_h
            pygame.draw.rect(DISPLAYSURF, 
                             (255, 255, 255 ),
            ((x1,y1), (x2,y2)) , width=3)

box_creation()

generate_board_data(6,4)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

