import pygame

class Plateform:
    def __init__(self):
        self.background = pygame.image.load("world/assets/plateform_ground.jpg").convert()
        self.position = [100, 360, 120, 360]

    def display(self, window):
        window.blit(self.background, (self.position[0], self.position[1]))
        window.blit(self.background, (self.position[2], self.position[3]))

    def scroll(self, player):
        print(player.position)
        playerSpeed = 13

        if player.position[0] >= (280-playerSpeed): # 13 = Speed
            self.position[0] -= playerSpeed
        elif player.position[0] < 50 + playerSpeed:
            self.position[0] += playerSpeed
