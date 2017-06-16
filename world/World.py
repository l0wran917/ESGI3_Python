import pygame
from pygame.math import Vector2


class World:
    def __init__(self,):
        self.background = pygame.image.load("world/assets/background.png").convert()
        self.position = Vector2()

    def display(self, window):
        window.blit(self.background, (self.position[0], self.position[1]))

    def scroll(self, player):

        if player.position[0] >= (self.getRightScrollLimit() - player.speed):
            self.position[0] -= player.speed
        elif player.position[0] < (self.getLeftScrollLimit() + player.speed):
            self.position[0] += player.speed

    def getRightScrollLimit(self):
        return 280

    def getLeftScrollLimit(self):
        return 50
