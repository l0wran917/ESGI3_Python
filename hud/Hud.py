import pygame


class Hud:
    def __init__(self):
        pygame.font.init()
        self.score = 0

    def display(self, window):
        myfont = pygame.font.SysFont('Arial', 30)
        textsurface = myfont.render('Score : ' + str(self.score), False, (0, 0, 0))
        window.blit(textsurface, (0, 0))

    def update_score(self, window):
        self.score += 1
        self.display(window)

    def restart(self):
        self.score = 0
