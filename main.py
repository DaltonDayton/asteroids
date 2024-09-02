import pygame

from constants import *
from player import Player


def main():
    print("Starting asteroids!")

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    updatable.add(player)
    drawable.add(player)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
