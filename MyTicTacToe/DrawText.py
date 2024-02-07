import pygame_textinput
import pygame
import pygame.locals as pl

screen = pygame.display.set_mode((400, 400))

def draw_text(text, infont, x, y, col):
	img = infont.render(text, True, col)
	screen.blit(img, (x, y))


