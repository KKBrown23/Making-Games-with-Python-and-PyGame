# HMWRK: Make another animation. Download a gif image and split into frames then, write a python program to display an image.
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
img_list = []
for x in range(0,8):
    img = pygame.image.load(f'animation/img_{x+1}.gif')
    img_list.append(img)
current_img_index = 0
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

    DISPLAYSURF.blit(img_list[current_img_index], (catx, caty))
    current_img_index += 1
    if(current_img_index == len(img_list)):
        current_img_index = 0 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
# HMWRK: Make another animation. Download a gif image and split into frames then, write a python program to display an image.
    pygame.display.update()
    fpsClock.tick(FPS)