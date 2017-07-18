import pygame
from pygame.locals import *
from pygame.math import Vector2


class Player:
    jumpHeight = 60

    def __init__(self):
        self.image = pygame.image.load("player/assets/perso.png").convert_alpha()
        self.position = self.image.get_rect()
        self.position.x = 100
        self.position.y = 0

        self.speed = 13
        self.gravity = 5
        self.movement = Vector2()
        self.jump = 0
        self.isJumping = False

    def display(self, window):
        window.blit(self.image, self.position)

    def move(self, world):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d]:
            self.movement.x = self.speed
        if pressed[pygame.K_q]:
            self.movement.x = -self.speed
        if pressed[K_SPACE] and not self.isJumping:
            self.jump = Player.jumpHeight
            self.isJumping = True

        if self.isJumping:
            self.jump -= self.gravity

        self.movement.y = self.gravity

        for plateform in world.plateforms:
            if self.position.y + self.movement.y - self.jump + self.position.height > plateform.position.y:
                if self.position.x + self.position.width > plateform.position.x and self.position.x < plateform.position.x + plateform.size.x:
                    self.movement.y = 0
                    self.jump = 0
                    self.isJumping = False

        if (self.position.x + self.movement.x > world.get_right_scroll_limit()) or (
                        self.position.x + self.movement.x < world.getLeftScrollLimit()):
            self.movement.x = self.movement.x

        self.position.x = self.position.x + self.movement.x
        self.position.y = self.position.y + self.movement.y - self.jump

        self.movement = Vector2()
