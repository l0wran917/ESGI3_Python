import pygame
from pygame.locals import *
from world.World import World
from player.Player import Player
from hud.Hud import Hud


def main():
    pygame.init()

    window = pygame.display.set_mode((800, 445))
    world = World()
    player = Player()

    hud = Hud()

    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.music.load('bestsongever.mp3')
    pygame.mixer.music.play(-1)

    backgroundDead = pygame.image.load("world/assets/dead_screen.png").convert_alpha()
    backgroundDead = pygame.transform.scale(backgroundDead, (800, 445))
    waiting_input = False

    is_running = True
    while is_running:
        if not player.dead:
            for event in pygame.event.get():
                if event.type == QUIT:
                    is_running = False

            player.move(world)
            world.move()

            world.checkEnemies(player, window, hud)
            world.scroll(player)

            player.applyMove()
            world.applyMove()

            world.display(window)
            player.display(window)
            hud.display(window, player)
        else:
            if not waiting_input:
                window.blit(backgroundDead, (0, 0))
                waiting_input = True
            else:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        is_running = False
                    if event.type == KEYDOWN and event.key == K_r:
                        world.restart()
                        player.restart()
                        waiting_input = False

        pygame.display.flip()
        pygame.time.Clock().tick(60)


if __name__ == '__main__':
    main()
