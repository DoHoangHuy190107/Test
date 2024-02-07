import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
LINE_COLOR = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def draw_board():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_xo():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                draw_x(row, col)
            elif board[row][col] == 'O':
                draw_o(row, col)
def draw_x(row, col):
    pygame.draw.line(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE),
                     ((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, ((col + 1) * SQUARE_SIZE, row * SQUARE_SIZE),
                     (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH)

def draw_o(row, col):
    pygame.draw.circle(screen, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                       SQUARE_SIZE // 2 - LINE_WIDTH // 2, LINE_WIDTH)
def check_winner():
    for i in range(BOARD_SIZE):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0], [(i, 0), (i, 1), (i, 2)]  
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i], [(0, i), (1, i), (2, i)]  

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0], [(0, 0), (1, 1), (2, 2)]  
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2], [(0, 2), (1, 1), (2, 0)]  

    return None, []

def is_board_full():
    return all(board[i][j] != ' ' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

current_player = 'X'
game_over = False
winning_cells = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == ' ':
                board[clicked_row][clicked_col] = current_player

                winner, winning_cells = check_winner()
                if winner:
                    game_over = True
                elif is_board_full():
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    screen.fill(BLACK)
    draw_board()
    draw_xo()

    if winning_cells:
        for cell in winning_cells:
            pygame.draw.rect(screen, (255, 0, 0), (cell[1] * SQUARE_SIZE, cell[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)

    if game_over:
        font = pygame.font.Font(None, 74)
        if winner:
            text = font.render(f"Player {winner} wins!", True, RED)
        else:
            text = font.render("Draw", True, RED)

        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()