import pygame
from pygame.math import Vector2
from world.Plateform import Plateform


class World:
    def __init__(self):
        self.background = pygame.image.load("world/assets/background.png").convert()
        self.position = Vector2()

        self.plateforms = []
        for i in range(0, 50):
            self.plateforms.append(Plateform((32 * i), 360))
        self.plateforms.append(Plateform(32 * 12, 230))

    def display(self, window):
        window.blit(self.background, self.position)
        for plateform in self.plateforms:
            plateform.display(window)

    def scroll(self, player):
        scroll_area = 0
        if player.position.x + player.movement.x > self.get_right_scroll_limit():
            player.movement.x = 0
            scroll_area = 1
        if player.position.x + player.movement.x < self.get_left_scroll_limit():
            player.movement.x = 0
            scroll_area = -1

        if self.position.x + (player.speed * -scroll_area) > 0:
            return False

        self.position.x += player.speed * -scroll_area
        for plateform in self.plateforms:
            plateform.position.x += player.speed * -scroll_area

    def get_right_scroll_limit(self):
        return 280

    def get_left_scroll_limit(self):
        return 50
