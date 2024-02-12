import pygame, sys
from textInput import draw_text
pygame.init()

screen = pygame.display.set_mode((800, 400))
font = pygame.font.SysFont(None, 30)

#Create images of button
play_button = pygame.image.load("PlayButton.png").convert_alpha()
guide_button = pygame.image.load("GuideButton.png").convert_alpha()
quit_button = pygame.image.load("New Piskel (10).png").convert_alpha()
#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		screen.blit(self.image, (self.rect.x, self.rect.y))

		return action



def GUIDE():
      draw_text("This is Guide", font, 200, 200, (50, 20, 100))

def QUIT():
    pygame.quit()
    sys.exit()

	
def main():
    play = Button(340, 200, play_button, 2)
    guide = Button(340, 250, guide_button, 2)
    quit = Button(340, 300, quit_button, 2)
    t = 1
    while True: 
        if play.draw():
            print(t)
            t += 1
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
