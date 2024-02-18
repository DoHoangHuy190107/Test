import pygame, sys
from textInput import draw_text
from Button import Button
from textInput import draw_text as draw_text
pygame.init()

screen = pygame.display.set_mode((800, 400))
font = pygame.font.SysFont(None, 30)



def Script2():

    timer = pygame.time.Clock()
    snip = font.render('', True, 'white')
    line = 25
    counter = 0
    speed = 1
    index = 0
    messages = ['Monsters saw your power, they were scared',
                'They ran away',
                'You followed them you see the dungeon nearby',
                'With your curiosity, you went straight inside.',
                'Then you saw a big fire monster'
                ]
    message = messages[index]
    done = False

    while True:
        timer.tick(30)
        if counter < speed * len(message):
            counter += 1
        else: done = True

        if index == len(messages) - 1:
            return
        draw_text('Press any key to continue', font, 520, 360, (252, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if done and index < len(messages) - 1:
                    index += 1
                    message = messages[index]
                    done = False 

        snip = font.render(message[0: counter // speed], True, 'white')
        screen.blit(snip, (10, index * line))
        pygame.display.flip()


if __name__ == '__main__':
    Script2()
