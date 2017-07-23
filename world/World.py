import pygame
from pygame.math import Vector2
from world.Plateform import Plateform
from world.Enemy import Enemy


class World:
    def __init__(self):
        self.background = pygame.image.load("world/assets/background.png").convert()
        self.background = pygame.transform.scale(self.background, (800, 445))
        self.position = Vector2()

        self.plateform = Plateform(1, 1)
        self.plateforms = self.plateform.create()

        self.enemies = []

        for i in range(0, 2):
            self.enemies.append(Enemy(660 + i * 70, 300))

    def display(self, window):
        position = self.position
        if position.x < -800:
            position.x = position.x + 800

        window.blit(self.background, position)
        window.blit(self.background, (position.x + 800, position.y))
        for plateform in self.plateforms:
            plateform.display(window)
        for enemy in self.enemies:
            enemy.display(window)

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
        for enemy in self.enemies:
            enemy.position.x += player.speed * -scroll_area

    def checkEnemies(self, player, window, hud):
        for enemy in self.enemies:
            if enemy.dead:
                continue

            if player.position.x + player.position.width + player.movement.x > enemy.position.x and player.position.x + \
                    player.movement.x < enemy.position.x + enemy.size.x:  # Test X
                if player.position.y + player.position.height + player.movement.y > enemy.position.y and \
                                        player.position.y + player.movement.y < enemy.position.y + enemy.size.y:  # Test Y
                    if enemy.position.y - (player.position.y + player.position.height) >= 0:  # Player come from upside
                        enemy.kill()
                        hud.updateScore(window, player)
                        player.jump(40)
                    else:
                        player.kill()

    def move(self):
        for enemy in self.enemies:
            enemy.position.x += 1

    def applyMove(self):
        test = 1

    def get_right_scroll_limit(self):
        return 280

    def get_left_scroll_limit(self):
        return 50
