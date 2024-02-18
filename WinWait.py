import pygame, sys
from textInput import draw_text
from Button import Button
from Play import play as play
pygame.init()

screen = pygame.display.set_mode((800, 400))
font = pygame.font.SysFont(None, 30)

#Create images of button
play_button = pygame.image.load("PlayButton.png").convert_alpha()
guide_button = pygame.image.load("GuideButton.png").convert_alpha()
quit_button = pygame.image.load("QuitButton.png").convert_alpha()
# Background
background_image = pygame.image.load("Images2/Knight_of_Jambon.png").convert()
guide_image = pygame.image.load("Images2/WinGuide.png").convert()

def GUIDE():
    Esc_button = pygame.Rect(0, 30, 68, 28)
    while True: 
        screen.blit(guide_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if Esc_button.collidepoint(pos):
                    return 
        pygame.display.flip()


def PLAY():
    play()
	
def WinWait():
    play = Button(300, 350, play_button, 2)
    guide = Button(475, 350, guide_button, 2)
    t = 1
    while True: 
        screen.blit(background_image, (0, 0))
        if play.draw():
            PLAY()
        if guide.draw():
            GUIDE()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


if __name__ == "__main__":
	WinWait()
