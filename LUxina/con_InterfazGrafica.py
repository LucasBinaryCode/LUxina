import pygame
import sys
def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pintar Cuadrados')
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    square_size = 50
    grid = [[WHITE for _ in range(width // square_size)] for _ in range(height // square_size)]
    button_rect = pygame.Rect(width - 100, 10, 90, 30)
    def draw_grid():
        for y in range(0, height, square_size):
            for x in range(0, width, square_size):
                rect = pygame.Rect(x, y, square_size, square_size)
                pygame.draw.rect(screen, grid[y // square_size][x // square_size], rect, 0)
                pygame.draw.rect(screen, BLACK, rect, 1)
    def grid_to_matrix():
        matrix = []
        for row in grid:
            matrix_row = [1 if color == BLACK else 0 for color in row]
            matrix.append(matrix_row)
        return matrix
    def clean_matrix(matrix):
        first_one_index = min(next((i for i, x in enumerate(row) if x == 1), len(row))
                            for row in matrix if any(row))
        cleaned_matrix = []
        for row in matrix:
            if any(row):
                last_one_index = max(loc for loc, val in enumerate(row) if val == 1)
                cleaned_row = row[first_one_index:last_one_index + 1]
                cleaned_matrix.append(cleaned_row)
            else:
                continue
        return cleaned_matrix
    def draw_button():
        pygame.draw.rect(screen, BLACK, button_rect)
        font = pygame.font.SysFont(None, 24)
        text = font.render('Crear Matriz', True, WHITE)
        screen.blit(text, (button_rect.x + 5, button_rect.y + 5))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x = mouse_x // square_size
                grid_y = mouse_y // square_size
                if button_rect.collidepoint(event.pos):
                    matrix = grid_to_matrix()
                    cleaned_matrix = clean_matrix(matrix)
                    pygame.quit()
                    return cleaned_matrix   
                else:
                    if event.button == 1:
                        grid[grid_y][grid_x] = BLACK
                    elif event.button == 3:
                        grid[grid_y][grid_x] = WHITE
        screen.fill(WHITE)
        draw_grid()
        draw_button()
        pygame.display.flip()
    pygame.quit()
    sys.exit()