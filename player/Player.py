import pygame
from pygame.locals import *
from pygame.math import Vector2


class Player:
    jumpHeight = 70

    def __init__(self):
        self.image = pygame.image.load("player/assets/perso.png").convert_alpha()
        self.position = self.image.get_rect()
        self.position.x = 150
        self.position.y = 100

        self.speed = 13
        self.gravity = 9
        self.movement = Vector2()
        self.jump = 0
        self.is_jumping = False

    def display(self, window):
        window.blit(self.image, self.position)

    def move(self, world):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d]:
            self.movement.x = self.speed
        if pressed[pygame.K_q]:
            self.movement.x = -self.speed
        if pressed[K_SPACE] and not self.is_jumping:
            self.jump = Player.jumpHeight
            self.is_jumping = True

        if self.is_jumping:
            self.jump -= self.gravity

        self.movement.y = self.gravity
        if self.jump > 0:
            self.movement.y -= self.jump

        for plateform in world.plateforms:
            if self.position.x + self.position.width > plateform.position.x and \
                            self.position.x < plateform.position.x + plateform.size.x:
                if self.position.y + self.position.height + self.movement.y > plateform.position.y and \
                                        self.position.y + self.movement.y < plateform.position.y + plateform.size.y:
                    self.movement.y = 0
                    self.jump = 0
                    self.is_jumping = False

            if self.position.y + self.position.height > plateform.position.y and \
                            self.position.y < plateform.position.y + plateform.size.y:
                if self.position.x + self.position.width + self.movement.x > plateform.position.x and \
                                        self.position.x + self.movement.x < plateform.position.x + plateform.size.x:
                    self.movement.x = 0

    def applyMove(self):
        self.position.x = self.position.x + self.movement.x
        self.position.y = self.position.y + self.movement.y

        self.movement = Vector2()
