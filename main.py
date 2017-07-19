import pygame
from pygame.locals import *
from world.World import World
from player.Player import Player


def main():
    pygame.init()

    window = pygame.display.set_mode((800, 445))
    world = World()
    player = Player()

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                is_running = False

        player.move(world)

        world.checkEnemies(player)

        world.scroll(player)

        player.applyMove()

        world.display(window)
        player.display(window)

        pygame.display.flip()
        pygame.time.Clock().tick(60)


if __name__ == '__main__':
    main()
