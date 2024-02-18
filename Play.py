import pygame, sys, os
from Player import Player as Player
from Boss import Boss as Boss
from Boss import GroupMonster as GroupBoss
from Spear import GroupMonster as GroupMonster
from Spear import Spear as Spear
from Stage1 import Stage1 as Stage1
from Stage2 import Stage2 as Stage2
from Script1 import Script1 as Script1
from Script2 import Script2 as Script2

pygame.init()

screen = pygame.display.set_mode((800, 400))
font = pygame.font.SysFont(None, 30)

PlayerHp = 20
BossHp = 100
MonsHp = 10
FPS = 20
width, height = 800, 600
X, Y = 50, 100
sizeW, sizeH = 40, 42
y_gravity = 2
white = (252, 252, 252)
black = (0, 0, 0)

background_image = pygame.image.load("Images/stage1_forest.png").convert()

def play():
    run = True

    while(run):
        screen.fill(black)
        Script1()
        if Stage1():
            screen.fill(black)
            Script2()
            if Stage2():
                run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()