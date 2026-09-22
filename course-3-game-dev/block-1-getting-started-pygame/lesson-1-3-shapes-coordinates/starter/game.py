# game.py — Lesson 1.3: draw a rectangle and move it with x/y
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Box Voyager")

clock = pygame.time.Clock()
running = True

# Player box — top-left corner and size
x = 100
y = 200
box_w = 50
box_h = 50
speed = 3  # pixels per frame (Lesson 1.4 will make this smoother!)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: Move the box to the right a little each frame
    # x = x + speed
    # Bonus later: wrap or bounce when it leaves the window

    screen.fill((20, 24, 40))

    # TODO: Draw a filled rectangle at (x, y)
    # pygame.draw.rect(screen, (255, 200, 50), (x, y, box_w, box_h))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
