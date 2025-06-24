import pygame, sys
from pygame.locals import *
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('Test')
DISPLAYSURF.fill(WHITE)


# pygame.draw.rect(DISPLAYSURF, RED, ((45, 50), (150, 150)))
# pygame.draw.rect(DISPLAYSURF, RED, ((50, 50), (150, 150)))
# pygame.draw.rect(DISPLAYSURF, RED, ((55, 50), (150, 150)))
x_position = 45
speed_x = 1
y_position = 50
speed_y = 1
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)
    pygame.draw.rect(DISPLAYSURF, RED, ((x_position, y_position), (150, 150)))
    
    x_position += speed_x
    # if x_position == 200:
    #     speed_x = -1
    # if x_position == 0:
    #     speed_x = 1
    # Homework: 
    #       make the square go up and down
    y_position += speed_y
    # if y_position == 250:
    #     speed_y = -1
    # if y_position == 0:
    #     speed_y = 1
    # make  the square do a circular animation, when it hit x =200 it goes down, 
    # when it hits y=250 it goes left, when it hits x = 0 it goes up, when it hit y = 0 it goes right
    
    if x_position == 200:
        speed_x = -1
    if y_position == 250:
        speed_y = -1
    if x_position == 0:
       speed_x = 1
    if y_position == 0:
        speed_y = 1
    pygame.display.update()