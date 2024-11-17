import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 700
TILE_SIZE = WIDTH // 5
FPS = 30
BACKGROUND_COLOR = (255, 255, 255)
TILE_COLOR = (50, 150, 50)
FONT_COLOR = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Tight Squeeze - Klotski Puzzle")

# Set font
FONT = pygame.font.Font(None, 40)

# Initial board setup
board = [
    [1, 1, 2, 2, 0],
    [1, 1, 3, 4, 0],
    [5, 6, 3, 4, 0],
    [7, 8, 0, 9, 9],
    [0, 0, 10, 10, 11]
]

# Define tiles
tiles = {
    0: (0, 0, 0),   # Empty space
    1: (200, 0, 0), # Cao Cao (2x2)
    2: (0, 200, 0),
    3: (0, 0, 200),
    4: (200, 200, 0),
    5: (200, 0, 200),
    6: (0, 200, 200),
    7: (100, 100, 100),
    8: (150, 150, 150),
    9: (100, 50, 150),
    10: (50, 150, 200),
    11: (150, 50, 100)
}

# Draw a tile
def draw_tile(tile, x, y):
    pygame.draw.rect(screen, tile, (x, y, TILE_SIZE, TILE_SIZE))
    text = FONT.render(str(tile), True, FONT_COLOR)
    screen.blit(text, (x + TILE_SIZE // 2 - text.get_width() // 2, y + TILE_SIZE // 2 - text.get_height() // 2))

# Draw the board
def draw_board():
    screen.fill(BACKGROUND_COLOR)
    for r in range(len(board)):
        for c in range(len(board[r])):
            tile = board[r][c]
            if tile != 0:
                draw_tile(tiles[tile], c * TILE_SIZE, r * TILE_SIZE)

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Handle key events to move tiles
            pass

    draw_board()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
