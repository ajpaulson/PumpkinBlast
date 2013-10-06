#!/usr/bin/env/ python

# Blast the pumpkins to get candy! You've got 60 seconds!
# (by Alex Paulson - alex.j.paulson@googlemail.com)

import pygame
from pygame.locals import *
from sys import exit
from pumpkin import pumpkin
from endgame import *

pygame.init()

# window setup
screen = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Pumpkin Gallery')

timer = pygame.time.Clock()

font = pygame.font.SysFont("Comic Sans", 30)

# colour definitions
black = (0, 0, 0)
white = (255, 255, 255)
orange = (245, 121, 0)

background = pygame.image.load('background.png').convert()

pygame.mouse.set_visible(0)
# crosshairs
crosshair = pygame.image.load('crosshair.gif').convert_alpha()
crosshair_x, crosshair_y = pygame.mouse.get_pos()
crosshair_x -= 5
crosshair_y -= 5

candy = 0
velocity = 2
pygame.time.set_timer(USEREVENT+1, 1000)
time = 60

# Pumpkins!
bad_0 = pumpkin(screen)
bad_1 = pumpkin(screen)

fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN and event.key == K_f:
            if fullscreen == False:
                screen = pygame.display.set_mode((600, 600), FULLSCREEN, 32)
                fullscreen = True
            elif fullscreen == True:
                screen = pygame.display.set_mode((600, 600), 0, 32)
                fullscreen = False
        if event.type == KEYDOWN and event.key == K_q:
            exit()

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if bad_0.rect.collidepoint(pygame.mouse.get_pos()):
                bad_0.__init__(screen)
                candy += 10
            if bad_1.rect.collidepoint(pygame.mouse.get_pos()):
                bad_1.__init__(screen)
                candy += 10

        if event.type == USEREVENT+1:
            time -= 1

    screen.blit(background, (0,0))

    # update these fellows
    bad_0.update()
    bad_1.update()

    # mustn't forget the crosshair as well
    screen.blit(crosshair, (crosshair_x, crosshair_y))
    crosshair_x, crosshair_y = pygame.mouse.get_pos()
    crosshair_x -= 5
    crosshair_y -= 5

    # How much candy have we won?
    screen.blit(pygame.font.SysFont("Comic Sans", 30).render("Time: " + str(time), True, orange), (10, 40))
    screen.blit(pygame.font.SysFont("Comic Sans", 30).render("Candy: " + str(candy), True, orange), (10, 20))

    if time <= 0:
        gameover(screen, background, crosshair)

    pygame.display.update()

    timer.tick(60)
