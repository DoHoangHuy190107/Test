import pygame, sys
pygame.init()

width, height = 800, 400
VelPlayer = 5
X, Y = 50, 100

white = (252, 252, 252)
black = (0, 0, 0)

screen = pygame.display.set_mode((width, height))

class Player(pygame.sprite.Sprite):
    def __init__(self, col, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 30, 50)
        self.X = x
        self.Y = y
        self.col = col
    def draw(self):
        pygame.draw.rect(screen, self.col, (self.X, self.Y, 30, 50))
        pygame.display.update()
    def handle_event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_DOWN]:
                self.X -= VelPlayer * 7 / 10
                self.Y += VelPlayer * 7 / 10
            elif keys[pygame.K_UP]:
                self.X -= VelPlayer * 7/ 10
                self.Y -= VelPlayer * 7 / 10
            else:
                self.X -= VelPlayer
        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_DOWN]:
                self.X += VelPlayer * 7 / 10
                self.Y += VelPlayer * 7 / 10
            elif keys[pygame.K_UP]:
                self.X += VelPlayer * 7 / 10
                self.Y -= VelPlayer * 7 / 10
            else :
                self.X += VelPlayer
        elif keys[pygame.K_DOWN]:
            self.Y += VelPlayer
        elif keys[pygame.K_UP]:
            self.Y -= VelPlayer

def main():
    run = True
    player = Player(white, 300, 300)
    clock = pygame.time.Clock()

    while(run):
        clock.tick(40)  
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        player.handle_event()
        player.draw()

if __name__ == "__main__":
    main()
