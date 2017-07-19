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
        self.isJumping = False
        self.scrollArea = 0

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
            print('jump')

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
                    self.isJumping = False

            if self.position.y + self.position.height > plateform.position.y and \
                            self.position.y < plateform.position.y + plateform.size.y:
                if self.position.x + self.position.width + self.movement.x > plateform.position.x and \
                                        self.position.x + self.movement.x < plateform.position.x + plateform.size.x:
                    self.movement.x = 0

        self.scrollArea = 0
        if self.position.x + self.movement.x > world.get_right_scroll_limit():
            self.movement.x = 0
            self.scrollArea = 1
        if self.position.x + self.movement.x < world.get_left_scroll_limit():
            self.movement.x = 0
            self.scrollArea = -1

        print(self.movement)

        self.position.x = self.position.x + self.movement.x
        self.position.y = self.position.y + self.movement.y

        self.movement = Vector2()
