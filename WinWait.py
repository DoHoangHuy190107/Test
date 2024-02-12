import pygame, sys
from textInput import draw_text
from Button import Button
pygame.init()

screen = pygame.display.set_mode((800, 400))
font = pygame.font.SysFont(None, 30)

#Create images of button
play_button = pygame.image.load("PlayButton.png").convert_alpha()
guide_button = pygame.image.load("GuideButton.png").convert_alpha()
quit_button = pygame.image.load("New Piskel (10).png").convert_alpha()
#button class

def GUIDE():
      draw_text("This is Guide", font, 200, 200, (50, 20, 100))

def QUIT():
    pygame.quit()
    sys.exit()

def PLAY():
     draw_text("Now You can play", font, 400, 200, (50, 20, 100))
	
def main():
    play = Button(340, 200, play_button, 2)
    guide = Button(340, 250, guide_button, 2)
    quit = Button(340, 300, quit_button, 2)
    t = 1
    while True: 
        if play.draw():
            PLAY()
        if guide.draw():
            GUIDE()
        if quit.draw():
            QUIT()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


if __name__ == "__main__":
	main()
