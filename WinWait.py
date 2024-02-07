import pygame
import sys
pygame.init()

height, width = 400, 800
size = 32
X = 100
Y = 50

# COLOUR
black = (0, 0, 0)
white = (252, 252, 252)
grey = (100, 100, 100)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Huy Dep Trai")
font = pygame.font.SysFont(None, size)

def draw_text(screen, text, infont, x, y, col):
    img = infont.render(text, True, col)
    screen.blit(img, (x, y))

run = True
rectPlay = pygame.Rect((width - X) / 2, (height - Y) / 2, X, Y)
BackPlay = pygame.Rect((width - X - 10) / 2, (height - Y - 10) / 2, X + 10, 10 + Y)

rectUser = pygame.Rect(320, 260, 175, 45)
BackUser = pygame.Rect(320 - 5, 260 - 5, 185, 55)

while run:
    screen.fill(white)
    pygame.draw.rect(screen, black, BackPlay)
    pygame.draw.rect(screen, grey, rectPlay)
    
    draw_text(screen, "PLAY", font, 373, 190, black)

    pygame.draw.rect(screen, black, BackUser)
    pygame.draw.rect(screen, grey, rectUser)
    draw_text(screen, "USER MANUAL", font, 323, 270, black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            sys.exit()
    pygame.display.flip()