import pygame
from pygame.math import Vector2
from world.Plateform import Plateform


class World:
    def __init__(self):
        self.background = pygame.image.load("world/assets/background.png").convert()
        self.position = Vector2()

        self.plateforms = []
        for i in range(0, 10):
            self.plateforms.append(Plateform((47 * i) + (47 * 2), 360))
        self.plateforms.append(Plateform(47*6, 360-90))

    def display(self, window):
        window.blit(self.background, self.position)
        for plateform in self.plateforms:
            plateform.display(window)

    def scroll(self, player):
        if player.position.x >= (self.get_right_scroll_limit() - player.speed):
            self.position.x -= player.speed * 0
        elif player.position.x < (self.get_left_scroll_limit() + player.speed):
            self.position.x += player.speed * 0

    def get_right_scroll_limit(self):
        return 280

    def get_left_scroll_limit(self):
        return 50
