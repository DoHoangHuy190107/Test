import pygame
from DrawText import draw_text as draw_text
from InputBox import InputBox as InputBox
pygame.init()

X = 600
Y = 600
size = 3
square = 200
white = (255, 255, 255)
grey = (80, 80, 90)
black = (0, 0, 0)
green = (30, 210, 15)
red = (250, 2, 2)
blue = (3, 227, 252)
Blue = (3, 7, 252)

screen = pygame.display.set_mode((X, Y))
font = pygame.font.SysFont(None, 32)

def drawEnter():
    screen.fill(grey)
    draw_text("Enter Row", font, 250, 200, black)
    draw_text("Enter Col", font, 250, 400, black)
    pygame.draw.rect(screen, white, pygame.Rect(250, 600, 50, 25)) 
    draw_text("Next", font, 250, 600, red)


"""
InputRow = InputBox(200, 250, 100, 50, blue, Blue)
InputCol = InputBox(200, 450, 100, 50, blue, Blue)
clock = pygame.time.Clock()
while True:
    drawEnter()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else: 
            pass
        InputRow.handle_event(event)
        InputCol.handle_event(event)

    InputRow.draw(screen)
    InputCol.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
"""