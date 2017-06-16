import pygame

class World:
    def __init__(self, window):
        background = pygame.image.load("world/assets/background.jpg").convert()
        window.blit(background, (0, 0))

    def display(self):
        self