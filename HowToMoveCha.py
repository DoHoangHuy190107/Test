import pygame, sys
pygame.init()

width, height = 800, 400
VelPlayer = 5
X, Y = 50, 100

white = (252, 252, 252)
black = (0, 0, 0)

screen = pygame.display.set_mode((width, height))


def draw(player):
    screen.fill(black)
    pygame.draw.rect(screen, white, player)
    pygame.display.update()

def main():
    run = True
    player = pygame.Rect((width - X) / 2, (height - Y) / 2, X, Y)
    clock = pygame.time.Clock()

    while(run):
        clock.tick(100)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_DOWN]:
                player.x -= VelPlayer / 2
                player.y += VelPlayer / 2
            elif keys[pygame.K_UP]:
                player.x -= VelPlayer / 2
                player.y -= VelPlayer / 2
            else:
                player.x -= VelPlayer
        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_DOWN]:
                player.x += VelPlayer / 2
                player.y += VelPlayer / 2
            elif keys[pygame.K_UP]:
                player.x += VelPlayer / 2
                player.y -= VelPlayer / 2
            else :
                player.x += VelPlayer
        elif keys[pygame.K_DOWN]:
            player.y += VelPlayer
        elif keys[pygame.K_UP]:
            player.y -= VelPlayer
        draw(player)

if __name__ == "__main__":
    main()