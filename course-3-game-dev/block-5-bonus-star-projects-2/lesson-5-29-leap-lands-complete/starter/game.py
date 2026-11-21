# game.py — Lesson 5.29: Leap Lands — complete (starter)
import pygame

pygame.init()

VIEW_W, VIEW_H = 640, 480
screen = pygame.display.set_mode((VIEW_W, VIEW_H))
pygame.display.set_caption("Leap Lands — Pro")

clock = pygame.time.Clock()
font_big = pygame.font.Font(None, 46)
font = pygame.font.Font(None, 28)

state = "MENU"
running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: MENU → PLAY on ENTER; 3 LEVELS from strings; WIN when F flag on last level
        # TODO: GAME_OVER when lives == 0; session best JSON in ~/.leap_lands_best.json

    screen.fill((12, 16, 38))
    if state == "MENU":
        title = font_big.render("Leap Lands", True, (90, 250, 210))
        screen.blit(title, (VIEW_W // 2 - title.get_width() // 2, 160))
        hint = font.render("Finish TODOs — see solution/game.py", True, (200, 210, 255))
        screen.blit(hint, (VIEW_W // 2 - hint.get_width() // 2, 230))

    pygame.display.flip()

pygame.quit()