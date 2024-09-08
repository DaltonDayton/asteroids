import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Shot.containers = (shots, updatable, drawable)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
