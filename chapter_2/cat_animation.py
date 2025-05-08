import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
cat_img_list = []
catImg = pygame.image.load('cat.png')
cat_1 = pygame.image.load('cat-1.png')
cat_2 = pygame.image.load('cat-2.png')
cat_img_list.append(catImg)
cat_img_list.append(cat_1)
cat_img_list.append(cat_2)
current_cat_img_index = 0
catx = 10
caty = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(cat_img_list[current_cat_img_index], (catx, caty))
    current_cat_img_index += 1
    if(current_cat_img_index == len(cat_img_list)):
        current_cat_img_index = 0 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
# HMWRK: Make another animation. Download a gif image and split into frames then, write a python program to display an image.
    pygame.display.update()
    fpsClock.tick(FPS)