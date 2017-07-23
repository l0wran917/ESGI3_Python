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

    background_dead = pygame.image.load("world/assets/dead_screen.png").convert_alpha()
    background_dead = pygame.transform.scale(background_dead, (800, 445))
    waiting_input = False

    is_running = True
    while is_running:
        if not player.dead:
            for event in pygame.event.get():
                if event.type == QUIT:
                    is_running = False

            player.move(world)
            world.move()

            world.check_enemies(player, window, hud)
            world.scroll(player)

            player.apply_move()

            world.display(window)
            player.display(window)
            hud.display(window)
        else:
            if not waiting_input:
                window.blit(background_dead, (0, 0))
                pygame.mixer.music.stop()
                pygame.mixer.music.load('monsterkill.mp3')
                pygame.mixer.music.play()
                waiting_input = True
            else:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        is_running = False
                    if event.type == KEYDOWN and event.key == K_r:
                        world.restart()
                        player.restart()
                        hud.restart()
                        pygame.mixer.music.load('bestsongever.mp3')
                        pygame.mixer.music.play(-1)
                        waiting_input = False

        pygame.display.flip()
        pygame.time.Clock().tick(60)


if __name__ == '__main__':
    main()
