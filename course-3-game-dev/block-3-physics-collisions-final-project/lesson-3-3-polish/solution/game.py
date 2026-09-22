# game.py — Lesson 3.3: Polish — sound, high score, difficulty ramp
import pygame
import os
import random

pygame.init()
pygame.mixer.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Polish Pro")

clock = pygame.time.Clock()
running = True

HERE = os.path.dirname(os.path.abspath(__file__))
star_img = pygame.image.load(os.path.join(HERE, "star.png")).convert_alpha()

# Optional sounds — skip quietly if mixer/file missing
catch_sound = None
miss_sound = None
try:
    catch_path = os.path.join(HERE, "catch.wav")
    miss_path = os.path.join(HERE, "miss.wav")
    if os.path.isfile(catch_path):
        catch_sound = pygame.mixer.Sound(catch_path)
    if os.path.isfile(miss_path):
        miss_sound = pygame.mixer.Sound(miss_path)
except pygame.error:
    catch_sound = None
    miss_sound = None


def play_safe(sound):
    if sound is not None:
        sound.play()


font_big = pygame.font.Font(None, 64)
font_small = pygame.font.Font(None, 32)

START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"
state = START

paddle_w, paddle_h = 100, 18
paddle = pygame.Rect(0, 0, paddle_w, paddle_h)
paddle.midbottom = (WIDTH // 2, HEIGHT - 24)
paddle_speed = 360

star = star_img.get_rect()
BASE_FALL = 160
fall_speed = BASE_FALL

score = 0
high_score = 0  # in-memory best for this session
misses = 0
MAX_MISSES = 3


def reset_star():
    star.size = star_img.get_size()
    star.midtop = (random.randint(20, WIDTH - 20), -40)


def start_round():
    global score, misses, fall_speed, state
    score = 0
    misses = 0
    fall_speed = BASE_FALL
    paddle.midbottom = (WIDTH // 2, HEIGHT - 24)
    reset_star()
    state = PLAYING


reset_star()

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                start_round()
            elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                state = START

    screen.fill((8, 10, 24))

    if state == START:
        title = font_big.render("Polish Pro", True, (255, 220, 80))
        hint = font_small.render("Press SPACE to start", True, (200, 200, 220))
        best = font_small.render(f"High score: {high_score}", True, (160, 220, 180))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
        screen.blit(best, best.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    elif state == PLAYING:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.x -= int(paddle_speed * dt)
        if keys[pygame.K_RIGHT]:
            paddle.x += int(paddle_speed * dt)
        paddle.clamp_ip(screen.get_rect())

        # Difficulty ramp: fall a bit faster as score rises
        fall_speed = BASE_FALL + score * 12
        star.y += int(fall_speed * dt)

        if paddle.colliderect(star):
            score += 1
            play_safe(catch_sound)
            reset_star()
        elif star.top > HEIGHT:
            misses += 1
            play_safe(miss_sound)
            reset_star()
            if misses >= MAX_MISSES:
                if score > high_score:
                    high_score = score
                state = GAME_OVER

        pygame.draw.rect(screen, (90, 210, 255), paddle, border_radius=6)
        screen.blit(star_img, star)
        hud = font_small.render(
            f"Score: {score}  Best: {high_score}  Miss: {misses}/{MAX_MISSES}",
            True,
            (255, 255, 255),
        )
        screen.blit(hud, (16, 12))
        speed_hud = font_small.render(f"Fall: {int(fall_speed)}", True, (180, 190, 220))
        screen.blit(speed_hud, (16, 44))

    elif state == GAME_OVER:
        over = font_big.render("Game Over", True, (255, 100, 100))
        final = font_small.render(f"Score: {score}   High: {high_score}", True, (255, 255, 255))
        hint = font_small.render("Press SPACE for title", True, (200, 200, 220))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        screen.blit(final, final.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    pygame.display.flip()

pygame.quit()
