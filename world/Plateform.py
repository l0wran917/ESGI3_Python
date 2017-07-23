import pygame
from pygame.math import Vector2
from random import randint

class Plateform:
    def __init__(self, x, y):
        self.background = pygame.image.load("world/assets/plateform_ground.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, (35, 50))

        self.startedPlateform = 10
        self.position = Vector2()
        self.size = Vector2()

        self.position.x = x
        self.position.y = y
        self.size.x = self.background.get_rect().width
        self.size.y = self.background.get_rect().height

        self.plateformMaxSize = 500
        self.plateform = []

    def display(self, window):
        window.blit(self.background, self.position)

    def scroll(self, player):
        player_speed = 13

        if player.position.x >= (280 - player_speed):  # 13 = Speed
            self.position.x -= player_speed
        elif player.position.x < 50 + player_speed:
            self.position.x += player_speed

    def create(self):
        for i in range(0, self.plateformMaxSize):
            if i > 5:
                self.blank(i)
                self.jump(i)
            else:
                self.plateform.append(Plateform(32 * i, 360))
        return self.plateform

    def blank(self, i):
        random = randint(0, 20)
        if random > 17:
            self.plateform.append(Plateform(32 * i, 500))
            randomDobleBlank = i + randint(0, 1)
            self.plateform.append(Plateform((32 * randomDobleBlank), 500))
        else:
            self.plateform.append(Plateform(32 * i, 360))

    def jump(self, i):
        random = randint(0, 20)
        if random > 17:
            self.plateform.append(Plateform(32 * i, 230))
        if random > 19:
            randomDoblePlateform = i + randint(1, 3)
            self.plateform.append(Plateform(32 * randomDoblePlateform, 100))
