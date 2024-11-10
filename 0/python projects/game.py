import pygame
background_colour = (0, 0, 0)
screen = pygame.display.set_mode((300, 300))

# Set the caption of the screen
pygame.display.set_caption('Pygame')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

# game loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
from pygame.locals import *

import pygame
import sys

GRAVITY = 1.2

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 25, 25)
        self.yvel = 0

    def tick(self):
        self.yvel += GRAVITY

        self.rect.y += int(self.yvel)

        if self.rect.y >= 475:
            self.rect.y = 475
            self.yvel = 0

    def set(self, y):
        if y:
            self.yvel = y

class Block:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.player = Player(0, 0)
        self.block = Block(225, 400, 50, 50)

    def main(self):
        up = down = left = right = False
        while True:
            self.screen.fill((230, 230, 230))
            pygame.draw.rect(self.screen, (40, 40, 40), self.block.rect)
            pygame.draw.rect(self.screen, (100, 200, 100), self.player.rect)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == KEYDOWN:
                    if event.key == K_w:
                        self.player.set(-20)
                    elif event.key == K_d:
                        right = True
                    elif event.key == K_a:
                        left = True
                    elif event.key == K_s:
                        down = True
                elif event.type == KEYUP:
                    if event.key == K_d:
                        right = False
                    elif event.key == K_a:
                        left = False
                    elif event.key == K_s:
                        down = False

            if right:
                self.player.rect.x += 5
                while self.player.rect.colliderect(self.block.rect):
                    self.player.rect.x -= 1
            if left:
                self.player.rect.x -= 5
                while self.player.rect.colliderect(self.block.rect):
                    self.player.rect.x += 1
            if down:
                self.player.rect.y += 5
                while self.player.rect.colliderect(self.block.rect):
                    self.player.rect.y -= 1
            self.player.tick()
            if self.player.yvel > 0:
                while self.player.rect.colliderect(self.block.rect):
                    self.player.rect.y -= 1
                    self.player.yvel = 0
            elif self.player.yvel < 0:
                while self.player.rect.colliderect(self.block.rect):
                    self.player.rect.y += 1
                    self.player.yvel = 0

game = Game()
game.main()
