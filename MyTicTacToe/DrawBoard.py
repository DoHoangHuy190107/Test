import pygame
from DrawText import draw_text as draw_text
pygame.init()

X = 600
Y = 600
height = 600
width = 600
size = 3
square = 200
white = (255, 255, 255)
grey = (80, 80, 90)
black = (0, 0, 0)
green = (30, 210, 15)
red = (250, 2, 2)

screen = pygame.display.set_mode((X, Y))
font = pygame.font.SysFont(None, 32)
board = [['' for _ in range(size)] for _ in range(size)]

def draw_o(row, col):
    row += 1
    col += 1
    pygame.draw.circle(screen, white, ((2 * col - 1) * square / 2, (2 * row - 1) * square / 2), 100)
    pygame.draw.circle(screen, black, ((2 * col - 1) * square / 2, (2 * row - 1) * square / 2), 95)

def draw_x(row, col):
    pygame.draw.line(screen, white, ((col) * square, (row) * square), ((col + 1) * square, (row + 1) * square), 5)
    pygame.draw.line(screen, white, ((col) * square, (row + 1) * square), ((col + 1) * square, (row) * square), 5)

def draw_board(board):
    pygame.draw.rect(screen, white, pygame.Rect(0, 600, width, height)) 
    #pygame.draw.rect(screen, white, pygame.Rect(250, 650, 50, 25)) 
    pygame.draw.rect(screen, white, pygame.Rect(250, 650, 50, 25)) 
    draw_text("Next", font, 250, 600, red)
    for i in range(1, size):
        pygame.draw.line(screen, white, (0, i * square), (width, i * square), 5)
        pygame.draw.line(screen, white, (i * square, 0), (i * square, height), 5)
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'x':
                draw_x(i, j)
            elif board[i][j] == 'o':
                draw_o(i, j)
