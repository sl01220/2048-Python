import pygame
import sys
import time
import math

# Game constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAYER_SIZE = 50
BLOCK_SIZE = 20
PLAYER_COLOR = (255, 255, 255)
BLOCK_COLOR = (255, 0, 0)
BG_COLOR = (0, 0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PLAYER_SIZE, PLAYER_SIZE])
        self.image.fill(PLAYER_COLOR)
        pygame.draw.rect(self.image, BG_COLOR, pygame.Rect(10, 10, PLAYER_SIZE - 20, PLAYER_SIZE - 20))
        self.rect = self.image.get_rect()
        pygame.draw.line(self.image, PLAYER_COLOR, (10, 10), (PLAYER_SIZE - 10, PLAYER_SIZE - 10), 10)
        pygame.draw.line(self.image, PLAYER_COLOR, (10, PLAYER_SIZE - 10), (PLAYER_SIZE - 10, 10), 10)
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[pygame.K_d] and self.rect.x < WINDOW_WIDTH - PLAYER_SIZE:
            self.rect.x += 5
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[pygame.K_s] and self.rect.y < WINDOW_HEIGHT - PLAYER_SIZE:
            self.rect.y += 5



class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE], pygame.SRCALPHA)  # Use SRCALPHA to allow transparent background
        pygame.draw.circle(self.image, BLOCK_COLOR, (BLOCK_SIZE // 2, BLOCK_SIZE // 2), BLOCK_SIZE // 2)
        self.rect = self.image.get_rect(center=(x, y))


    def update(self):
        t = (time.time() - self.start_time) / 30  # Normalize to 30 seconds
        angle = 2 * math.pi * t  # Convert to radians
        radius = PLAYER_SIZE // 2 + BLOCK_SIZE // 2  # Distance from player center
        self.rect.center = (self.player_rect.centerx + radius * math.cos(angle),
                            self.player_rect.centery + radius * math.sin(angle))


def game():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    blocks = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 is the left mouse button
                    block = Block(player.rect.x + PLAYER_SIZE / 2 - BLOCK_SIZE / 2,
                                  player.rect.y + PLAYER_SIZE / 2 - BLOCK_SIZE / 2)
                    all_sprites.add(block)
                    blocks.add(block)

        all_sprites.update()

        screen.fill(BG_COLOR)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

game()
