import pygame
from random import randint

pygame.init()

sizex = 800
sizey = 600
win = pygame.display.set_mode((sizex, sizey))
pygame.display.set_caption("DVD Logo")

width = 80
height = 60
vel = 2
x = randint(0, sizex - width)
y = randint(0, sizey - height)
direction = 1

rgb = (randint(0,255), randint(0,255), randint(0,255))
pygame.draw.rect(win, rgb, (x, y, width, height))

run = 1
while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0

    if y < 0: # obere Border // nur wenn direction == 3 oder 4
        rgb = (randint(0,255), randint(0,255), randint(0,255))
        if direction == 3:
            direction = 2
        elif direction == 4:
            direction = 1
    elif x > sizex-width: # rechte Border //nur wenn direction == 1 oder 4
        rgb = (randint(0,255), randint(0,255), randint(0,255))
        if direction == 1:
            direction = 2
        elif direction == 4:
            direction = 3
    elif y > sizey-height: # untere Border // nur wenn direction == 1 oder 2
        rgb = (randint(0,255), randint(0,255), randint(0,255))
        if direction == 1:
            direction = 4
        elif direction == 2:
            direction = 3
    elif x < 0: # linke Border // nur wenn direction == 2 oder 3
        rgb = (randint(0,255), randint(0,255), randint(0,255))
        if direction == 2:
            direction = 1
        elif direction == 3:
            direction = 4
        direction = 4


    if direction == 1:
        x += vel
        y += vel
    elif direction == 2:
        x -= vel
        y += vel
    elif direction == 3:
        x -= vel
        y -= vel
    elif direction == 4:
        x += vel
        y -= vel

    win.fill((255, 255, 255))
    pygame.draw.rect(win, rgb, (x, y, width, height))
    pygame.display.update()

pygame.quit()
