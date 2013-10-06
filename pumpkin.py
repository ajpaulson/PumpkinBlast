#!/usr/bin/env python

import pygame
from random import randrange

class pumpkin():
    def __init__(self, surface):
        self.x = randrange(20, 550)
        self.y = randrange(20, 550)

        # determine speed
        self.speed_x = randrange(1, 3)
        self.speed_y = randrange(0, 2)

        # which type of pumpkin?
        self.type = randrange(0, 2)

        # Which type equals which image
        if self.type == 0:
            self.image = pygame.image.load('pumpkin1.png').convert_alpha()
        if self.type == 1:
            self.image = pygame.image.load('pumpkin2.png').convert_alpha()

        # the rect object
        self.rect = pygame.rect.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

        self.surface = surface

    def move (self):
        self.x += self.speed_x
        self.y += self.speed_y

        # ahhh refreshing
        self.rect = pygame.rect.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

        if self.y <= 20 or self.y >= 580:
            self.speed_y = -self.speed_y
        if self.x <= 20 or self.x >= 580 - self.image.get_width():
            self.speed_x = -self.speed_x



    def draw (self):
        self.surface.blit(self.image, (self.x, self.y))

    def update (self):
        self.move()
        self.draw()
