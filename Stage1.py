import pygame, sys, os
from Player import Player as Player
from Boss import Boss as Boss
from Boss import GroupMonster as GroupBoss
from Spear import GroupMonster as GroupMonster
from Spear import Spear as Spear
from textInput import draw_text as draw_text

pygame.init()

PlayerHp = 20
BossHp = 100
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
background_image = pygame.image.load("Images2/stage1_forest.png").convert()

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


def Stage1():
    run = True
    numDef = 0
    player = Player(10, 237, PlayerHp)
    monster = Spear(40, 245, MonsHp, player)

    monster_group = GroupMonster(MonsHp, player)
    monster_group.add(monster)
    clock = pygame.time.Clock()

    while(run and numDef < 13):
        clock.tick(FPS)  
        screen.fill(black)

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

        monster_group.rand()
        
        numDef += monster_group.update()
        monster_group.move(player)
        monster_group.isAttack()
        monster_group.draw()

        pygame.display.flip()
    return True

# if __name__ == "__main__":
# 	Stage1()
