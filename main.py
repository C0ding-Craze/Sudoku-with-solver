import pygame
import sys
import time

pygame.init()
clock = pygame.time.Clock()

cell_size = 100
cell_number = 9

screen_width = cell_size * cell_number
screen_height = cell_size * cell_number

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sudoku ")

font = pygame.font.SysFont(None, 80)
message_font = pygame.font.SysFont(None, 250)
instr_font = pygame.font.SysFont("Impact", 70)

grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

selected_cell = None  # (row, col) or None
game_won = False

instruction_start_time = time.time()

def draw_board():

    screen.fill((245, 245, 220))
    # Draw cell borders
    for row in range(cell_number):
        for col in range(cell_number):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (150, 150, 150), rect, 2)

    # Draw thick lines for 3x3 cells
    for i in range(1, cell_number):
        if i % 3 == 0:
            # Vertical
            pygame.draw.line(screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, screen_height), 6)
            # Horizontal
            pygame.draw.line(screen, (0, 0, 0), (0, i * cell_size), (screen_width, i * cell_size), 6)

    # Draw screen border
    pygame.draw.rect(screen,(144, 162, 80), (0, 0, screen_width, screen_height), 8)
    draw_numbers()

def draw_numbers():
    for row in range(cell_number):
        for col in range(cell_number):
            number = grid[row][col] 
            if number != 0:
                text = font.render(str(number), True, (100, 0, 0))
                text_rect = text.get_rect(center=(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2))
                screen.blit(text, text_rect)

def handle_mouse_click(pos):
    global selected_cell
    row = pos[1] // cell_size
    col = pos[0] // cell_size
    selected_cell = (row, col)
    
def draw_selected_cell(cell=None):
    # Draws a rectangle around the selected cell or a given cell (for solver)
    if cell is None:
        cell = selected_cell
    if cell:
        row, col = cell
        rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (0, 117, 255), rect, 5)  

def handle_key_press(event):
    global selected_cell  

    if selected_cell and event.unicode in "123456789":
        row, col = selected_cell
        grid[row][col] = int(event.unicode)        

def check_win():
    # Check rows
    for row in grid:
        if sorted(row) != list(range(1, 10)):
            return False
    # Check columns
    for col in range(9):
        col_vals = [grid[row][col] for row in range(9)]
        if sorted(col_vals) != list(range(1, 10)):
            return False
    # Check 3x3 boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            block = []
            for r in range(3):
                for c in range(3):
                    block.append(grid[box_row + r][box_col + c])
            if sorted(block) != list(range(1, 10)):
                return False
    return True

def show_win():
    message = message_font.render("You Won!", True, (139,69,19))
    message_rect = message.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(message, message_rect)

def find_empty():
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def is_valid(num, pos):
    row, col = pos
    # Check row
    for c in range(9):
        if grid[row][c] == num and c != col:
            return False
    # Check column
    for r in range(9):
        if grid[r][col] == num and r != row:
            return False
    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for r in range(box_y * 3, box_y * 3 + 3):
        for c in range(box_x * 3, box_x * 3 + 3):
            if grid[r][c] == num and (r, c) != pos:
                return False
    return True

def solver(realtime=True):
    empty = find_empty()
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(num, (row, col)):
            grid[row][col] = num
            if realtime:
                draw_board()
                draw_selected_cell((row, col))
                pygame.display.update()
                # --- Handle events here ---
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.time.delay(50) # Add delay to visualize solving

            if solver(realtime):
                return True
            grid[row][col] = 0
            if realtime:
                draw_board()
                draw_selected_cell((row, col))
                pygame.display.update()
                # --- Handle events here ---
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.time.delay(50) # Add delay to visualize backtracking
    return False

def reset_game():
    global grid, selected_cell
    grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
    selected_cell = None
     

def show_instructions():
    screen.fill((245, 245, 220))
    instr_text = instr_font.render("Press R to reset, Enter to solve", True, (44, 62, 80))
    instr_rect = instr_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(instr_text,instr_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_won:  # Only allow interaction if game not won
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:
                handle_key_press(event)

                if event.key == pygame.K_r:
                    reset_game()

                if event.key == pygame.K_RETURN and not game_won:  # Use Enter key to solve
                    solver(realtime=True)
                    game_won = True

    draw_board()
    draw_selected_cell()
    if check_win():
        game_won = True
        show_win()
        
    if time.time() - instruction_start_time < 2:
        show_instructions()

    clock.tick(60)
    pygame.display.update()