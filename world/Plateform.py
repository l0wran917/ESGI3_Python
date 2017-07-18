import pygame
from pygame.math import Vector2


class Plateform:
    def __init__(self, x, y):
        self.background = pygame.image.load("world/assets/plateform_ground.jpg").convert()
        self.position = Vector2()
        self.size = Vector2()

        self.position.x = x
        self.position.y = y
        self.size.x = self.background.get_rect().width
        self.size.y = self.background.get_rect().height

    def display(self, window):
        window.blit(self.background, self.position)

    def scroll(self, player):
        player_speed = 13

        if player.position.x >= (280 - player_speed):  # 13 = Speed
            self.position.x -= player_speed
        elif player.position.x < 50 + player_speed:
            self.position.x += player_speed
