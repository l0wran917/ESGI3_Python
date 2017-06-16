import pygame
from pygame.locals import *
from world.World import World
from player.Player import Player


def main():
    pygame.init()

    window = pygame.display.set_mode((640, 480))
    world = World(window)
    player = Player(window)

    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == QUIT:
                isRunning = False

        player.move()

        world.display()
        player.display(window)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == '__main__':
    main()
