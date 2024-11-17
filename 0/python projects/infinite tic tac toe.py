import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 20
TILE_SIZE = WIDTH // GRID_SIZE
GRAY = (20, 20, 20)
L_GRAY = (50,50,50)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE =(255,255,255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite Tic Tac Toe")

# Fonts
FONT = pygame.font.Font(None, 40)

# Game variables
board = {}
current_player = 'X'
history = []
scores = {'X': 0, 'O': 0}  # Initialize scores for both players


def draw_scores():
    # Display the scores on the screen with colors matching the players
    x_score_text = FONT.render(f"{scores['X']}", True, RED)
    o_score_text = FONT.render(f"{scores['O']}", True, BLUE)

    # Calculate positions for the scores
    x_score_rect = x_score_text.get_rect(center=(WIDTH // 2 - 20, 30))
    o_score_rect = o_score_text.get_rect(center=(WIDTH // 2 + 20, 30))

    # Render the scores on the screen
    screen.blit(x_score_text, x_score_rect)
    screen.blit(o_score_text, o_score_rect)

    # Render the colon separator
    colon_text = FONT.render(":", True, BLACK)
    colon_rect = colon_text.get_rect(center=(WIDTH // 2, 30))
    screen.blit(colon_text, colon_rect)
# Buttons
button_font = pygame.font.Font(None, 36)
button_width = 150
button_height = 50
restart_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT - 60, button_width, button_height)
quit_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT - 120, button_width, button_height)

def draw_grid():
    for x in range(0, WIDTH, TILE_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

def draw_board():
    for (x, y), player in board.items():
        center_x = x * TILE_SIZE + TILE_SIZE // 2
        center_y = y * TILE_SIZE + TILE_SIZE // 2
        if player == 'X':
            color = RED
        else:
            color = BLUE
        text = FONT.render(player, True, color)
        text_rect = text.get_rect(center=(center_x, center_y))
        screen.blit(text, text_rect)

def draw_buttons():
    pygame.draw.rect(screen, L_GRAY, restart_button)
    restart_text = button_font.render("Restart", True, GRAY)
    restart_text_rect = restart_text.get_rect(center=restart_button.center)
    screen.blit(restart_text, restart_text_rect)

    pygame.draw.rect(screen, L_GRAY, quit_button)

    quit_text = button_font.render("Quit", True, GRAY)
    quit_text_rect = quit_text.get_rect(center=quit_button.center)
    screen.blit(quit_text, quit_text_rect)

def restart_game():
    global board, history, current_player
    board = {}
    history = []
    current_player = 'X'


def check_win():
    # Check all possible winning lines for five in a row
    for (x, y), player in board.items():
        # Check horizontal line
        if all(board.get((x + i, y)) == player for i in range(5)):
            return player
        # Check vertical line
        if all(board.get((x, y + i)) == player for i in range(5)):
            return player
        # Check diagonal line (top-left to bottom-right)
        if all(board.get((x + i, y + i)) == player for i in range(5)):
            return player
        # Check diagonal line (top-right to bottom-left)
        if all(board.get((x + i, y - i)) == player for i in range(5)):
            return player
    return None

def main():
    global current_player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if restart_button.collidepoint(x, y):
                    restart_game()
                elif quit_button.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()
                else:
                    grid_x = x // TILE_SIZE
                    grid_y = y // TILE_SIZE
                    if (grid_x, grid_y) not in board:
                        # Remove the logic that deletes the oldest move
                        board[(grid_x, grid_y)] = current_player
                        history.append((grid_x, grid_y))
                        winner = check_win()
                        if winner:
                            scores[winner] += 1  # Update the score for the winning player

                            restart_game()
                        else:
                            current_player = 'O' if current_player == 'X' else 'X'

        screen.fill(GRAY)
        draw_grid()
        draw_board()
        draw_buttons()
        draw_scores()
        pygame.display.flip()

if __name__ == "__main__":
    main()