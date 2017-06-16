import pygame

class World:
    def __init__(self, window):
        self.background = pygame.image.load("world/assets/background.png").convert()
        self.position = [0, 0]

    def display(self, window):
        window.blit(self.background, (self.position[0], self.position[1]))

    def scroll(self, player):
        print(player.position)
        playerSpeed = 13

        if player.position[0] >= (280-playerSpeed): # 13 = Speed
            self.position[0] -= playerSpeed
        elif player.position[0] < 50 + playerSpeed:
            self.position[0] += playerSpeed
