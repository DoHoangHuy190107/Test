import pygame, sys, os
from Player import Player as Player
from Boss import Boss as Boss
from Boss import GroupMonster as GroupBoss
from Spear import GroupMonster as GroupMonster
from Spear import Spear as Spear
from textInput import draw_text as draw_text

pygame.init()

PlayerHp = 20
BossHp = 80
MonsHp = 10
FPS = 20
width, height = 800, 400
X, Y = 50, 100
sizeW, sizeH = 40, 42
y_gravity = 2
white = (252, 252, 252)
black = (0, 0, 0)
green = (0, 242, 20)

font = pygame.font.SysFont(None, 32)
fontS = pygame.font.SysFont(None, 16)
screen = pygame.display.set_mode((width, height))
background_image = pygame.image.load("Images/stage2_castle.png").convert()

player = Player(10, 290, PlayerHp)

def Died():
    
    Again_Button = pygame.Rect(370, 200, 70, 10)
    while True:
        
        screen.fill((252, 0, 0))
        draw_text("YOU DIED", font, 350, 150, black)
        draw_text("PLAY AGAIN", fontS, 370, 200, black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Again_Button.collidepoint(pygame.mouse.get_pos()):
                    return False
        

        pygame.display.flip()


def phase1():
    run = True
    numDef = 0
    monster = Boss(40, 200, BossHp, player)

    monster_group = GroupBoss(BossHp, player)
    monster_group.add(monster)
    clock = pygame.time.Clock()

    while(run and numDef < 1):
        clock.tick(FPS)  
        screen.blit(background_image, (0, 0))
        draw_text("HP : " + str(player.Hp), font, 0, 0, green)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if player.Hp < 1:
            return Died()

        player.update()
        player.handle_event(monster_group)
        player.draw()

        numDef += monster_group.update()
        monster_group.move(player)
        monster_group.isAttack()
        monster_group.draw()

        pygame.display.flip()
    return True

def phase2():
    run = True
    numDef = 0
    monster = Boss(40, 200, BossHp, player)
    monster1 = Boss(40, 200, BossHp, player)

    monster_group = GroupBoss(BossHp, player)
    monster_group.add(monster)
    monster_group.add(monster1)
    clock = pygame.time.Clock()

    while(run and numDef <= 2):
        clock.tick(FPS)  
        screen.blit(background_image, (0, 0))
        draw_text("HP : " + str(player.Hp), font, 0, 0, green)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if player.Hp < 1:
            return Died()

        player.update()
        player.handle_event(monster_group)
        player.draw()

        numDef += monster_group.update()
        monster_group.move(player)
        monster_group.isAttack()
        monster_group.draw()

        pygame.display.flip()
    return True

def Stage2():
    run = True

    clock = pygame.time.Clock()

    while(run):
        clock.tick(FPS)  
        screen.fill(black)
        screen.blit(background_image, (0, 0))
        if phase1():
            if phase2():
                run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        

        pygame.display.flip()
    return True