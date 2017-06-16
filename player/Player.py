import pygame
from pygame.locals import *


class Player:
    def __init__(self, window):
        self.player = pygame.image.load("player/assets/perso.png").convert_alpha()
        self.position = [100, 35]
        window.blit(self.player, (self.position[0], self.position[1]))

        self.speed = 13
        self.gravity = 5
        self.movement = [0, 0]
        self.jump = 0
        self.isJumping = False

    def display(self, window):
        window.blit(self.player, self.position)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d]:
            self.movement[0] = self.speed
        if pressed[pygame.K_q]:
            self.movement[0] = -self.speed
        if pressed[K_SPACE] and not self.isJumping:
            self.jump = 60
            self.isJumping = True

        if self.isJumping:
            self.jump -= self.gravity

        if self.position[1] + self.movement[1] <= 480 - 100:  # 100 = height
            self.movement[1] = self.gravity

        if self.position[1] + self.movement[1] - self.jump >= 375 - 100:  # 100 = height
            self.movement[1] = 0
            self.jump = 0
            self.isJumping = False

        if (self.position[0] + self.movement[0] > 280) or (self.position[0] + self.movement[0] < 50):
            self.movement[0] = 0

        self.position[0] = self.position[0] + self.movement[0]
        self.position[1] = self.position[1] + self.movement[1] - self.jump

        self.movement = [0, 0]
