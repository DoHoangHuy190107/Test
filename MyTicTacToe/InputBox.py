import pygame_textinput
import pygame
import pygame.locals as pl

pygame.init()

size = 3
square = 200
white = (255, 255, 255)
grey = (80, 80, 90)
black = (0, 0, 0)
green = (30, 210, 15)
red = (250, 2, 2)

screen = pygame.display.set_mode((600, 600))

class InputBox():

    def __init__(self, x, y, a, b, colAc, colIn):

        self.font = pygame.font.Font(None, 32)

        self.inputBox = pygame.Rect(x, y, a, b)

        self.colourInactive = colAc
        self.colourActive = colIn
        self.colour = self.colourInactive

        self.text = ''

        self.active = False
        self.isBlue = True

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.inputBox.collidepoint(event.pos)
            self.colour = self.colourActive if self.active else self.colourInactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif chr(event.key).isdigit():
                    self.text += event.unicode

    def draw(self, screen):
        txtSurface = self.font.render(self.text, True, self.colour)
        width = max(200, txtSurface.get_width()+10)
        self.inputBox.w = width
        screen.blit(txtSurface, (self.inputBox.x+5, self.inputBox.y+5))
        pygame.draw.rect(screen, self.colour, self.inputBox, 2)

        if self.isBlue:
            self.color = (0, 128, 255)
        else:
            self.color = (255, 100, 0)
