import pygame
import random
import sys

# Initialize pygame
pygame.init()
print('Welcome to 2048 use Arrow Keys to move')

# Constants
SIZE = 4
WIDTH, HEIGHT = 400, 500  # Increased height to make room for the score and restart button
TILE_SIZE = WIDTH // SIZE
FONT = pygame.font.Font(None, 40)
BACKGROUND_COLOR = (10, 10, 10)
HEADER_COLOR = (40, 40 ,40)
TILE_COLORS = {
    0: (10, 10, 10),
    2: (50, 50, 50),
    4: (60, 60, 60),
    8: (70, 70, 70),
    16: (80, 80, 80),
    32: (90, 90, 90),
    64: (100, 100, 100),
    128: (110, 110, 110),
    256: (120, 120, 120),
    512: (130, 130, 130),
    1024: (140, 140, 140),
    2048: (150, 150, 150),
}

# Initialize the game board and score
board = [[0] * SIZE for _ in range(SIZE)]
score = 0
high_score = 0

def add_new_tile():
    empty_tiles = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        board[r][c] = 2 if random.random() < 0.9 else 4

def draw_rounded_rect(surface, color, rect, corner_radius):
    """
    Draw a rectangle with rounded corners.
    """
    # Ensure corner_radius doesn't exceed half the rectangle's width/height
    corner_radius = min(corner_radius, rect[2] // 2, rect[3] // 2)

    # Inner rectangle
    inner_rect = (
        rect[0] + corner_radius, rect[1] + corner_radius, rect[2] - 2 * corner_radius, rect[3] - 2 * corner_radius)
    pygame.draw.rect(surface, color, inner_rect)

    # Draw four corner circles
    pygame.draw.circle(surface, color, (rect[0] + corner_radius, rect[1] + corner_radius), corner_radius)  # Top-left
    pygame.draw.circle(surface, color, (rect[0] + rect[2] - corner_radius, rect[1] + corner_radius),
                       corner_radius)  # Top-right
    pygame.draw.circle(surface, color, (rect[0] + corner_radius, rect[1] + rect[3] - corner_radius),
                       corner_radius)  # Bottom-left
    pygame.draw.circle(surface, color, (rect[0] + rect[2] - corner_radius, rect[1] + rect[3] - corner_radius),
                       corner_radius)  # Bottom-right

    # Draw side rectangles
    pygame.draw.rect(surface, color,
                     (rect[0] + corner_radius, rect[1], rect[2] - 2 * corner_radius, corner_radius))  # Top
    pygame.draw.rect(surface, color, (
        rect[0] + corner_radius, rect[1] + rect[3] - corner_radius, rect[2] - 2 * corner_radius, corner_radius))  # Bottom
    pygame.draw.rect(surface, color,
                     (rect[0], rect[1] + corner_radius, corner_radius, rect[3] - 2 * corner_radius))  # Left
    pygame.draw.rect(surface, color, (
        rect[0] + rect[2] - corner_radius, rect[1] + corner_radius, corner_radius, rect[3] - 2 * corner_radius))  # Right

def draw_board(screen):
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen,HEADER_COLOR,(0,0,WIDTH,100))
    corner_radius = TILE_SIZE // 5  # Adjust the corner radius as needed
    for r in range(SIZE):
        for c in range(SIZE):
            value = board[r][c]
            color = TILE_COLORS.get(value, (60, 58, 50))
            rect = (c * TILE_SIZE, r * TILE_SIZE + 100, TILE_SIZE, TILE_SIZE)  # Adjust y-position for tiles
            draw_rounded_rect(screen, color, rect, corner_radius)
            if value != 0:
                text = FONT.render(str(value), True, (210, 210, 210))
                text_rect = text.get_rect(center=(c * TILE_SIZE + TILE_SIZE // 2, r * TILE_SIZE + TILE_SIZE // 2 + 100))
                screen.blit(text, text_rect)

    # Draw current score and high score
    score_text = FONT.render(f"Score: {score}", True, (255, 255, 255))
    high_score_text = FONT.render(f"High Score: {high_score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (WIDTH - 230, 10))

    # Draw restart button
    # Corrected placement for "Restart" button
    restart_rect = pygame.Rect(WIDTH // 2 - 115, 50, 109, 35)
    pygame.draw.rect(screen, (30, 30, 30), restart_rect)
    restart_text = FONT.render("Restart", True, (255, 255, 255))
    screen.blit(restart_text, (WIDTH // 2 - 107, 55))

    # Corrected placement for "Quit" button
    quit_rect = pygame.Rect(WIDTH // 2 + 25, 50, 109, 35)
    pygame.draw.rect(screen, (30, 30, 30), quit_rect)
    quit_text = FONT.render("Quit", True, (255, 255, 255))
    screen.blit(quit_text, (WIDTH // 2 + 45, 55))


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
    global score
    for r in range(SIZE):
        for c in range(SIZE - 1):
            if board[r][c] == board[r][c + 1] and board[r][c] != 0:
                board[r][c] *= 2
                board[r][c + 1] = 0
                score += board[r][c]  # Update score when tiles are merged
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

def is_game_over():
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return False
    for r in range(SIZE):
        for c in range(SIZE - 1):
            if board[r][c] == board[r][c + 1]:
                return False
    for c in range(SIZE):
        for r in range(SIZE - 1):
            if board[r][c] == board[r + 1][c]:
                return False
    return True

def restart_game():
    global board, score, high_score
    if score > high_score:
        high_score = score
    board = [[0] * SIZE for _ in range(SIZE)]
    score = 0
    add_new_tile()
    add_new_tile()


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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            restart_rect = pygame.Rect(WIDTH // 2 - 105, 50, 100, 30)
            quit_rect = pygame.Rect(WIDTH // 2 + 5, 50, 100, 30)
            if restart_rect.collidepoint(mouse_x, mouse_y):
                restart_game()
            elif quit_rect.collidepoint(mouse_x, mouse_y):
                pygame.quit()
                sys.exit()

    draw_board(screen)
    pygame.display.update()

    if is_game_over():
        if score > high_score:
            high_score = score
        print("Game Over! \nYou suck!")

        pygame.quit()
        sys.exit()
