import pygame, sys, os, random

pygame.init()

FPS = 20
width, height = 800, 600
X, Y = 50, 100
sizeW, sizeH = 75, 100
y_gravity = 2
white = (252, 252, 252)
black = (0, 0, 0)
red = (252, 0, 0)
yellow = (252, 252, 0)
pink = (245, 66, 215)
attack_cooldown = 750  # Time ra đòn

screen = pygame.display.set_mode((width, height))

def colliderect(A, B):      # Check 2 h.vuong cắt nhau
    leftA = A.x
    rightA = leftA + A.width
    topA = A.y
    downA = topA + A.height
    leftB = B.x
    rightB = leftB + B.width
    topB = B.y
    downB = topB + B.height
    if (leftA <= rightB and downA >= topB and rightA >= leftB and topA <= downB):
        return True
    return False

class GroupMonster(pygame.sprite.Group):

    def __init__(self, Hp, target):
        super().__init__()
        self.Hp = Hp
        self.target = target


    def update(self):
        for mons in self.sprites():
            if mons.HP < 1:
                self.remove(mons)
            else:
                if mons.isAtt:          # Nếu trog trạng thái ra đòn
                    continue
                elif mons.dir > 1:
                    mons.image = pygame.transform.scale(mons.boss_right[mons.indexR], (sizeW, sizeH))
                    mons.indexR = (mons.indexR + 1) % 7
                else:
                    mons.image = pygame.transform.scale(mons.boss_left[mons.indexL], (sizeW, sizeH))
                    mons.indexL = (mons.indexL + 1) % 7

    def move(self, target):
        for mons in self.sprites():
            if mons.isAtt:              # Nếu trog trạng thái ra đòn
                continue
            elif target.X > mons.X:   # NVC bên phải
                mons.X += mons.Vel
                mons.dir = 2
                mons.rectAtt = pygame.Rect(mons.X + mons.rect.width - 10, mons.Y , mons.rect.width, mons.rect.height)
            else:                   # NVC bên trái
                mons.X -= mons.Vel
                mons.dir = -2
                mons.rectAtt = pygame.Rect(mons.X - mons.rect.width + 10, mons.Y , mons.rect.width, mons.rect.height)
            mons.rect = pygame.Rect(mons.X, mons.Y, 50, 50)

    def draw(self):
        for mons in self.sprites():
            screen.blit(mons.image, (mons.X, mons.Y))
        
    def isAttack(self):
        for mons in self.sprites():
            A = mons.rectAtt
            B = mons.target.rect
            if (colliderect(A, B)) or mons.isAtt > 0:       # Nếu range of attack cắt nvc
                mons.attack()



class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, Hp, target):
        super().__init__()

        
        # Vị trí
        self.X = x
        self.Y = y

        self.indexL = 0 # Thứ tự khung hình move
        self.indexR = 0     
        self.indexAL = 0 # Thứ tự khung hình  attack
        self.indexAR = 0    

        #Basic In4
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Images/demon_walk_1.png')), (sizeW, sizeH))  # Resize the image as needed
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y) 
        self.rectAtt = pygame.Rect(self.X + self.rect.width - 10, self.Y , self.rect.width, self.rect.height) # range of Attack
        self.dir = 1
        self.isAtt = 0
        self.Vel = 2
        self.HP = Hp
        self.target = target
        self.col = red
        self.timeAtt = 0

        # Khung hình
        self.boss_right = []
        self.boss_left = []
        self.boss_attR = []
        self.boss_attL = []

        for i in range(1, 8):
            str = 'Images/demon_walk_'
            if i > 0:
                str += chr(i + 48)
            str += '.png'
            self.boss_left.append(pygame.image.load(os.path.join(str)))

        for i in range(1, 8):
            str = 'Images/demon_walk_'
            if i > 0:
                str += chr(i + 48)
            str += 'Mi.png'
            self.boss_right.append(pygame.image.load(os.path.join(str)))

        for i in range(1, 11):
            str = 'Images/demon_cleave_'
            if i > 0:
                if i == 10:
                    str += chr(49) + chr(48)
                else:
                    str += chr(i + 48)
            str += '.png'
            self.boss_attL.append(pygame.image.load(os.path.join(str)))

        for i in range(1, 11):
            str = 'Images/demon_cleave_'
            if i > 0:
                if i == 10:
                    str += chr(49) + chr(48)
                else:
                    str += chr(i + 48)
            str += 'Mi.png'
            self.boss_attR.append(pygame.image.load(os.path.join(str)))

        """
        dir: hướng nhìn
        1, 2 : đứng phải, chạy phải
        -1, -2: đứng trái, nhìn trái
        """
    
    def attack(self):
        if self.isAtt < 8:      # 0-7 Hoạt ảnh dg ra đòn
            if not self.isAtt:      
                self.timeAtt = pygame.time.get_ticks()
            if self.dir > 0:
                self.image = pygame.transform.scale(self.boss_attR[self.isAtt], (sizeW, sizeH))
            else:
                self.image = pygame.transform.scale(self.boss_attL[self.isAtt], (sizeW, sizeH))
            self.isAtt += 1             # Đánh dấu dg ra đòn
        else:
            if self.isAtt == 10:    
                self.isAtt = 0
                return 
            if pygame.time.get_ticks() - self.timeAtt >= attack_cooldown:    # Hết CoolDown
                if self.dir > 0:
                    self.image = pygame.transform.scale(self.boss_attR[self.isAtt], (sizeW, sizeH))
                else:
                    self.image = pygame.transform.scale(self.boss_attL[self.isAtt], (sizeW, sizeH))
                if colliderect(self.rectAtt, self.target.rect):     # Nếu nvc trog tầm đánh
                    self.target.Hp -= 1 
                self.isAtt += 1
                

        
    