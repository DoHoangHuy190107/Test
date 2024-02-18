import pygame, sys
from textInput import draw_text
from Button import Button
from textInput import draw_text as draw_text
pygame.init()

screen = pygame.display.set_mode((800, 400))
font = pygame.font.SysFont(None, 30)



def Script3():

    timer = pygame.time.Clock()
    snip = font.render('', True, 'white')
    line = 25
    counter = 0
    speed = 1
    index = 0
    messages = ['After killed 3 monsters, Mysterious Person appeared',
                'He said: Congratulations on achieving the power you desire',
                'Now you can enjoy this world,',
                 'that power is yours'
                ]
    message = messages[index]
    done = False

    while True:
        timer.tick(30)
        if counter < speed * len(message):
            counter += 1
        else: done = True

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
                elif index == len(messages) - 1:
                    return

        snip = font.render(message[0: counter // speed], True, 'white')
        screen.blit(snip, (10, index * line))
        pygame.display.flip()
