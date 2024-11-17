def is_valid_position(r, c, R, C):
    return 0 <= r < R and 0 <= c < C

def detect_bombs(grid, R, C):
    # Directions for the 8 surrounding cells
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),        (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    detected_bombs = 0
    undetected_bombs = 0
    bomb_positions = set()
    malfunctioning_detectors = set()

    # Identify bomb positions
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                bomb_positions.add((r, c))

    # Identify malfunctioning detectors
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 5:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid_position(nr, nc, R, C) and grid[nr][nc] == 5:
                        malfunctioning_detectors.add((r, c))
                        malfunctioning_detectors.add((nr, nc))

    # Detect bombs with functioning detectors
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 5 and (r, c) not in malfunctioning_detectors:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid_position(nr, nc, R, C) and grid[nr][nc] == 1:
                        if (nr, nc) in bomb_positions:
                            detected_bombs += 1
                            bomb_positions.remove((nr, nc))

    undetected_bombs = len(bomb_positions)

    return detected_bombs, undetected_bombs

# Input reading
R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

# Detect bombs
detected, undetected = detect_bombs(grid, R, C)

# Output the results
print(detected, undetected)