import pygame
from pygame.math import Vector2


class Enemy:
    def __init__(self, x, y):
        self.background = pygame.image.load("world/assets/enemy.png").convert()
        self.position = Vector2()
        self.size = Vector2()

        self.position.x = x
        self.position.y = y
        self.size.x = self.background.get_rect().width
        self.size.y = self.background.get_rect().height

        self.dead = False

    def display(self, window):
        if not self.dead:
            window.blit(self.background, self.position)

    def kill(self):
        self.dead = True