# game.py — Lesson 1.4: frame-rate independent motion with delta time
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Slider")

clock = pygame.time.Clock()
running = True

x = 50.0  # float position — important for smooth dt math
y = 220.0
box_w = 50
box_h = 50
# Speed in pixels per SECOND (not per frame)
speed = 200

while running:
    # TODO: Cap at 60 FPS and convert milliseconds → seconds
    # dt = clock.tick(60) / 1000
    dt = 0  # replace after you write clock.tick

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: Move using speed * dt so motion stays smooth on any machine
    # x = x + speed * dt

    # Wrap when off the right edge
    if x > WIDTH:
        x = -box_w

    screen.fill((15, 18, 32))
    pygame.draw.rect(screen, (80, 220, 180), (int(x), int(y), box_w, box_h))
    pygame.display.flip()

pygame.quit()
