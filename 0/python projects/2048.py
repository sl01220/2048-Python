import pygame
import sys
import random

# Initialize pygame
pygame.init()
print('Welcome to 2048 use Arrow Keys to move')
# Constants
SIZE = 4
WIDTH, HEIGHT = 400, 400
TILE_SIZE = WIDTH // SIZE
FONT = pygame.font.Font(None, 40)
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Initialize the game board
board = [[0] * SIZE for _ in range(SIZE)]

def add_new_tile():
    empty_tiles = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        board[r][c] = 2 if random.random() < 0.9 else 4

def draw_board(screen):
    screen.fill(BACKGROUND_COLOR)
    for r in range(SIZE):
        for c in range(SIZE):
            value = board[r][c]
            color = TILE_COLORS.get(value, (60, 58, 50))
            pygame.draw.rect(screen, color, (c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            if value != 0:
                text = FONT.render(str(value), True, (0, 0, 0))
                text_rect = text.get_rect(center=(c * TILE_SIZE + TILE_SIZE // 2, r * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)

def compress(board):
    new_board = [[0] * SIZE for _ in range(SIZE)]
    for r in range(SIZE):
        pos = 0
        for c in range(SIZE):
            if board[r][c] != 0:
                new_board[r][pos] = board[r][c]
                pos += 1
    return new_board

def merge(board):
    for r in range(SIZE):
        for c in range(SIZE - 1):
            if board[r][c] == board[r][c + 1] and board[r][c] != 0:
                board[r][c] *= 2
                board[r][c + 1] = 0
    return board

def reverse(board):
    new_board = []
    for r in range(SIZE):
        new_board.append(list(reversed(board[r])))
    return new_board

def transpose(board):
    new_board = [[0] * SIZE for _ in range(SIZE)]
    for r in range(SIZE):
        for c in range(SIZE):
            new_board[r][c] = board[c][r]
    return new_board

def move_left():
    global board
    board = compress(board)
    board = merge(board)
    board = compress(board)

def move_right():
    global board
    board = reverse(board)
    move_left()
    board = reverse(board)

def move_up():
    global board
    board = transpose(board)
    move_left()
    board = transpose(board)

def move_down():
    global board
    board = transpose(board)
    move_right()
    board = transpose(board)

# Main game loop
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 game")

add_new_tile()
add_new_tile()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
                add_new_tile()
            elif event.key == pygame.K_RIGHT:
                move_right()
                add_new_tile()
            elif event.key == pygame.K_UP:
                move_up()
                add_new_tile()
            elif event.key == pygame.K_DOWN:
                move_down()
                add_new_tile()


    def is_game_over():
        # Check for any empty tiles
        for r in range(SIZE):
            for c in range(SIZE):
                if board[r][c] == 0:
                    return False

        # Check for possible merges horizontally
        for r in range(SIZE):
            for c in range(SIZE - 1):
                if board[r][c] == board[r][c + 1]:
                    return False

        # Check for possible merges vertically
        for c in range(SIZE):
            for r in range(SIZE - 1):
                if board[r][c] == board[r + 1][c]:
                    return False

        return True


    # Main game loop
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048 game")

    add_new_tile()
    add_new_tile()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left()
                    add_new_tile()
                elif event.key == pygame.K_RIGHT:
                    move_right()
                    add_new_tile()
                elif event.key == pygame.K_UP:
                    move_up()
                    add_new_tile()
                elif event.key == pygame.K_DOWN:
                    move_down()
                    add_new_tile()

        draw_board(screen)
        pygame.display.update()

        # Check for game over
        if is_game_over():
            print("Game Over!")
            pygame.quit()
            sys.exit()
    draw_board(screen)
    pygame.display.update()