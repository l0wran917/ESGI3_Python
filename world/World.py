import pygame
from pygame.math import Vector2
from world.Plateform import Plateform


class World:
    def __init__(self):
        self.background = pygame.image.load("world/assets/background.png").convert()
        self.position = Vector2()

        self.plateforms = []
        for i in range(0, 15):
            self.plateforms.append(Plateform((47 * i), 360))
        self.plateforms.append(Plateform(47*12, 360-90))

    def display(self, window):
        window.blit(self.background, self.position)
        for plateform in self.plateforms:
            plateform.display(window)

    def scroll(self, player):
        self.position.x += player.speed * -player.scrollArea
        for plateform in self.plateforms:
            plateform.position.x += player.speed * -player.scrollArea

    def get_right_scroll_limit(self):
        return 280

    def get_left_scroll_limit(self):
        return 50
