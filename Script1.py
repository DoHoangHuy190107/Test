import pygame, sys
from textInput import draw_text
from Button import Button
from textInput import draw_text as draw_text
pygame.init()

screen = pygame.display.set_mode((800, 400))
font = pygame.font.SysFont(None, 30)

timer = pygame.time.Clock()
snip = font.render('', True, 'white')


def Script1():

    counter = 0
    speed = 1
    line = 25
    index = 0
    messages = ['You are a knight, you desire power',
                'One day you accidentally meet a mysterious person with a hood',
                'He shows you a ritual to get there to another world that will give you the power',
                'You performed the ritual and you were transported to another world',
                'As soon as you opened your eyes, you saw yourself lying at the edge of the ',
                'forest',
                'You look around and see monsters gradually appearing.', 
                'You quickly run into the forest to hide.',
                'They quickly chase you.',
                'Luckily on the way, you saw someone\'s old armor and sword thrown away,',
                'so you quickly picked them up and went back to fighting the monsters.'
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
        
