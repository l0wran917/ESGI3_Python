import pygame
from pygame.math import Vector2
from random import randint


class Enemy:
    def __init__(self, x=0, y=0, type='ground'):
        if type == 'ground':
            self.background = pygame.image.load("world/assets/enemy.png").convert_alpha()
        elif type == 'fly':
            self.background = pygame.image.load("world/assets/kirby.png").convert_alpha()
        self.type = type
        self.background = pygame.transform.scale(self.background, (40, 47))
        self.background = pygame.transform.flip(self.background, 90, 0)
        self.position = Vector2()
        self.size = Vector2()

        self.position.x = x
        self.position.y = y
        self.size.x = self.background.get_rect().width
        self.size.y = self.background.get_rect().height

        self.enemies = []
        self.countmove = 0
        self.direction = 'right'

        self.sound = pygame.mixer.Sound("no.wav")
        self.sound.set_volume(0.5)

        self.dead = False

    def move(self):
        if self.direction == 'right':
            if self.countmove < 200:
                if self.type == 'ground':
                    self.position.x += 1
                else:
                    self.position.y += 1
            else:
                self.countmove = 0
                self.direction = 'roll'
        else:
            if self.countmove < 200:
                if self.type == 'ground':
                    self.position.x -= 1
                else:
                    self.position.y -= 1
            else:
                self.countmove = 0
                self.direction = 'right'
        self.countmove += 1

    def display(self, window):
        if not self.dead:
            window.blit(self.background, self.position)

    def kill(self):
        self.sound.play()
        self.dead = True

    def create(self, quantity=10):
        for i in range(0, quantity):
            position = randint(10, 50)
            rand = randint(0, 2)
            if rand < 2:
                self.enemies.append(Enemy(600 + (i * position * 10), 300))
            else:
                self.enemies.append(Enemy(660 + (i * position * 10), 200, 'fly'))
        return self.enemies
