import pygame
from pygame.locals import *

class Player:
    def __init__(self, window):
        self.player = pygame.image.load("player/assets/perso.png").convert_alpha()
        self.posPlayer = self.player.get_rect()
        window.blit(self.player, self.posPlayer)

        self.speed = 13
        self.gravity = 5
        self.movement = [0, 0]
        self.jump = 0
        self.isJumping = False

    def display(self, window):
        window.blit(self.player, self.posPlayer)

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

        if self.posPlayer.y + self.movement[1] <= 480 - self.posPlayer.height:
            self.movement[1] = self.gravity

        if self.posPlayer.y + self.movement[1] - self.jump >= 480 - self.posPlayer.height:
            self.movement[1] = 0
            self.jump = 0
            self.isJumping = False

        self.posPlayer = self.posPlayer.move(self.movement[0], self.movement[1] - self.jump)
        self.movement = [0, 0]
