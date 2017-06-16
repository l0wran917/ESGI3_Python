import pygame

class World:
    def __init__(self, window):
        self.background = pygame.image.load("world/assets/background.jpg").convert()
        window.blit(self.background, (0, 0))

    def display(self, window):
        window.blit(self.background, (0, 0))
