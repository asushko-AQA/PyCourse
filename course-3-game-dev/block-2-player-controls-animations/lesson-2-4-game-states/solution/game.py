# game.py — Lesson 2.4: start screen → playing → game over
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stage Director")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 64)
font_small = pygame.font.Font(None, 32)

START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"

state = START

x = 295.0
y = 215.0
box_w = 50
box_h = 50
speed = 250
score = 0.0
play_time = 0.0
TIME_LIMIT = 15.0

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                state = PLAYING
                score = 0.0
                play_time = 0.0
                x, y = 295.0, 215.0
            elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                state = START

    screen.fill((12, 14, 28))

    if state == START:
        title = font_big.render("Key Captain", True, (255, 220, 80))
        hint = font_small.render("Press SPACE to start", True, (200, 200, 220))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))

    elif state == PLAYING:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x = x - speed * dt
        if keys[pygame.K_RIGHT]:
            x = x + speed * dt
        if keys[pygame.K_UP]:
            y = y - speed * dt
        if keys[pygame.K_DOWN]:
            y = y + speed * dt

        x = max(0, min(x, WIDTH - box_w))
        y = max(0, min(y, HEIGHT - box_h))

        play_time = play_time + dt
        score = play_time * 10

        if play_time >= TIME_LIMIT:
            state = GAME_OVER

        pygame.draw.rect(screen, (255, 200, 50), (int(x), int(y), box_w, box_h))
        score_surf = font_small.render(f"Score: {int(score)}", True, (255, 255, 255))
        screen.blit(score_surf, (16, 12))
        time_left = max(0, TIME_LIMIT - play_time)
        timer_surf = font_small.render(f"Time: {time_left:.1f}", True, (180, 220, 255))
        screen.blit(timer_surf, (16, 48))

    elif state == GAME_OVER:
        over = font_big.render("Game Over", True, (255, 100, 100))
        final = font_small.render(f"Final score: {int(score)}", True, (255, 255, 255))
        hint = font_small.render("Press SPACE for title", True, (200, 200, 220))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        screen.blit(final, final.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    pygame.display.flip()

pygame.quit()
