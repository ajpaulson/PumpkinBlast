#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

def gameover(screen, background, crosshair):
    timer = pygame.time.Clock()

    pygame.time.delay(1000)

    font2 = pygame.font.SysFont('Comic Sans', 0)

    # another game loop to make this all work
    while True:
        # test event
        for event in pygame.event.get():
            if event.type == KEYDOWN or event.type == QUIT:
                exit()

        # crosshair position
        crosshair_x, crosshair_y = pygame.mouse.get_pos()
        crosshair_x -= 5
        crosshair_y -= 5

        screen.blit(background, (0,0))

        # endgame message
        screen.blit(pygame.image.load("gameover.png"), (10, 30))



        # frame-rate
        pygame.display.update()
        timer.tick(30)
