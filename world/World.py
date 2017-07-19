import pygame
from pygame.math import Vector2
from world.Plateform import Plateform
from world.Enemy import Enemy


class World:
    def __init__(self):
        self.background = pygame.image.load("world/assets/background.png").convert()
        self.position = Vector2()

        self.plateforms = []
        for i in range(0, 50):
            self.plateforms.append(Plateform((32 * i), 360))
        self.plateforms.append(Plateform(32 * 12, 230))

        self.enemy = Enemy(660, 300)

    def display(self, window):
        window.blit(self.background, self.position)
        for plateform in self.plateforms:
            plateform.display(window)
        self.enemy.display(window)

    def scroll(self, player):
        scroll_area = 0
        if player.position.x + player.movement.x > self.get_right_scroll_limit():
            player.movement.x = 0
            scroll_area = 1
        if player.position.x + player.movement.x < self.get_left_scroll_limit():
            player.movement.x = 0
            scroll_area = -1

        if self.position.x + (player.speed * -scroll_area) > 0:
            return False

        self.position.x += player.speed * -scroll_area
        for plateform in self.plateforms:
            plateform.position.x += player.speed * -scroll_area
        self.enemy.position.x += player.speed * -scroll_area

    def checkEnemies(self, player):
        enemy = self.enemy
        if enemy.dead :
            return False

        if player.position.x + player.position.width + player.movement.x > enemy.position.x and player.position.x + \
                player.movement.x < enemy.position.x + enemy.size.x:  # Test X
            if player.position.y + player.position.height + player.movement.y > enemy.position.y and \
                                    player.position.y + player.movement.y < enemy.position.y + enemy.size.y:  # Test Y
                if enemy.position.y - (player.position.y + player.position.height) >= 0:  # Player come from upside
                    enemy.kill()
                    player.jump(40)
                else:
                    player.kill()

    def get_right_scroll_limit(self):
        return 280

    def get_left_scroll_limit(self):
        return 50
