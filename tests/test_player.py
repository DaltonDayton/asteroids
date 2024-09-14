# tests/test_player.py

import pygame
import pytest

from asteroids.constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from asteroids.player import Player


@pytest.fixture
def player():
    pygame.init()
    return Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


def test_player_initialization(player):
    assert player.position.x == SCREEN_WIDTH / 2
    assert player.position.y == SCREEN_HEIGHT / 2
    assert player.radius == PLAYER_RADIUS
    assert player.rotation == 0
    assert player.timer == 0


def test_player_triangle(player):
    triangle = player.triangle()
    assert len(triangle) == 3
    for point in triangle:
        assert isinstance(point, pygame.Vector2)


def test_player_rotation(player):
    initial_rotation = player.rotation
    player.rotate(1)  # Rotate for 1 second
    assert player.rotation == initial_rotation + PLAYER_TURN_SPEED * 1


def test_player_movement_forward(player):
    initial_position = player.position.copy()
    player.rotation = 0
    player.move(1)  # Move forward for 1 second
    assert player.position.y == initial_position.y + PLAYER_SPEED * 1
    assert player.position.x == initial_position.x


def test_player_movement_backward(player):
    initial_position = player.position.copy()
    player.rotation = 0
    player.move(-1)  # Move backward for 1 second
    assert player.position.y == initial_position.y - PLAYER_SPEED * 1
    assert player.position.x == initial_position.x


def test_player_shoot_cooldown(player):
    player.timer = 0
    player.shoot()
    assert player.timer == PLAYER_SHOOT_COOLDOWN

    # Attempt to shoot again before cooldown expires
    player.shoot()
    # Timer should not reset because cooldown hasn't expired
    assert player.timer == PLAYER_SHOOT_COOLDOWN


def test_player_update_cooldown(player):
    player.timer = PLAYER_SHOOT_COOLDOWN
    player.update(0.1)
    assert player.timer == PLAYER_SHOOT_COOLDOWN - 0.1
