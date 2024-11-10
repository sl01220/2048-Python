import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(" ")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.speed = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

        # Ensure the player stays within the screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600

# Define the obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 750)
        self.rect.y = random.randint(-600, -50)
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.y += self.speed
        # Reset the obstacle to the top if it goes off the bottom
        if self.rect.top > 65:
            self.rect.x = random.randint(0, 750)
            self.rect.y = random.randint(-600, -50)
            self.speed = random.randint(0.01, 0.01)


# Create sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Create player and add to sprite groups
player = Player()
all_sprites.add(player)

# Create obstacles and add to sprite groups
for _ in range(10):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update all sprites
    all_sprites.update()

    # Check for collisions
    if pygame.sprite.spritecollideany(player, obstacles):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()
