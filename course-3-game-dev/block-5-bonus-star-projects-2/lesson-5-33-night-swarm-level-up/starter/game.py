# game.py — Lesson 5.33: Night Swarm — level up (starter)
import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Night Swarm — Bright Choice")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

UPGRADE_POOL = {
    "damage": {"label": "Bright Pulse"},
    "fire_rate": {"label": "Quick Glow"},
    "speed": {"label": "Swift Steps"},
    "extra_orb": {"label": "Twin Lantern"},
    "orbit": {"label": "Halo Guard"},
}

state = "PLAY"
player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
xp = 0
level = 1
xp_need = 10
level_choices: list[str] = []
running = True


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: when state == LEVEL_UP, keys 1/2/3 apply upgrade from UPGRADE_POOL dict

    if state == "PLAY":
        # TODO: reuse lesson 5.32 combat loop; collect gems into xp
        # TODO: when xp >= xp_need, level += 1, pick 3 random keys, state = LEVEL_UP
        pass

    screen.fill((12, 14, 28))
    pygame.draw.circle(screen, (255, 210, 80), (int(player_pos.x), int(player_pos.y)), 14)
    hint = font.render("TODO: XP bar + level-up choice screen (3 upgrades)", True, (190, 200, 240))
    screen.blit(hint, (12, 12))

    pygame.display.flip()

pygame.quit()