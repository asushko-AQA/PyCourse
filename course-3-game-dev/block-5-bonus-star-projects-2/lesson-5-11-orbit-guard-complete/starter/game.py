# game.py — Lesson 5.11: Orbit Guard — complete (starter)
import random

import pygame

pygame.init()

WIDTH = 720
HEIGHT = 560
PLAY_TOP = 64
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbit Guard")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 52)
font_small = pygame.font.Font(None, 28)

START = "start"
PLAYING = "playing"
WAVE_CLEAR = "wave_clear"
GAME_OVER = "game_over"
VICTORY = "victory"
state = START

SHIP_Y = HEIGHT - 48
ship_x = WIDTH / 2
lives = 3
score = 0
high_score = 0
wave = 1

player_bolts: list[dict[str, float]] = []
enemy_bolts: list[dict[str, float]] = []
invaders: list[pygame.Rect] = []
shields: list[dict[str, object]] = []

ufo_active = False
ufo_x = -80.0


def reset_wave() -> None:
    """TODO: rebuild invaders, shields, bolts for current wave."""
    pass


def start_play() -> None:
    """TODO: set state PLAYING, reset lives/score/wave, call reset_wave()."""
    pass


def march_formation(dt: float) -> None:
    """TODO: from 5.9 — speed scales with wave and fewer invaders."""
    pass


def update_bolts(dt: float) -> None:
    """TODO: from 5.10 + track high_score."""
    pass


def update_ufo(dt: float) -> None:
    """TODO: spawn bonus UFO; +350 score when shot."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if state == START:
                start_play()
            elif state == PLAYING:
                pass  # TODO: fire_bolt
            elif state in (GAME_OVER, VICTORY, WAVE_CLEAR):
                pass  # TODO: next wave or back to START

    if state == PLAYING:
        pass  # TODO: ship, march, bolts, ufo

    screen.fill((5, 7, 20))
    # TODO: draw ship, invaders, HUD, overlays per state

    pygame.display.flip()

pygame.quit()