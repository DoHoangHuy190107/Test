import pygame
from InputBox import InputBox as InputBox
from DrawText import draw_text as draw_text
from DrawWinEnter import drawEnter as drawEnter
from DrawBoard import draw_board as draw_board
pygame.init()

height = 700
width = 600
size = 3
square = 200
white = (255, 255, 255)
grey = (80, 80, 90)
black = (0, 0, 0)
green = (30, 210, 15)
red = (250, 2, 2)
blue = (3, 227, 252)
Blue = (3, 7, 252)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("XO")
font = pygame.font.SysFont(None, 32)
running = True
board = [['' for _ in range(size)] for _ in range(size)]
                
nextButton = pygame.Rect(250, 600, 50, 25)

turn = 0
curScreen = 0
InputRow = InputBox(200, 250, 100, 50, blue, Blue)
InputCol = InputBox(200, 450, 100, 50, blue, Blue)
clock = pygame.time.Clock()

while running:
    screen.fill(black)
    
    if curScreen == 0: 
        drawEnter()
    else: 
        draw_board(board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if nextButton.collidepoint(pygame.mouse.get_pos()) and curScreen == 1:
                curScreen = 0
            elif InputCol.text != '' and InputRow.text != '' and nextButton.collidepoint(pygame.mouse.get_pos()):
                row = int(InputRow.text)
                col = int(InputCol.text)
                if 0 < row < 4 and 0 < col < 4:
                    curScreen = 1
                    turn += 1
                    if turn % 2:
                        board[row - 1][col - 1] = 'o'
                    else : 
                        board[row - 1][col - 1] = 'x'

        if curScreen == 0: 
            InputRow.handle_event(event)
            InputCol.handle_event(event)
    if curScreen == 0: 
        InputRow.draw(screen)
        InputCol.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()




