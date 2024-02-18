import pygame, sys, os, random

pygame.init()

FPS = 20
width, height = 800, 600
X, Y = 50, 100
sizeW, sizeH = 75, 50
y_gravity = 2
white = (252, 252, 252)
black = (0, 0, 0)
red = (252, 0, 0)
yellow = (252, 252, 0)
pink = (245, 66, 215)
attack_cooldown = 1000  # Time ra đòn

screen = pygame.display.set_mode((width, height))

def colliderect(A, B):  # Check 2 h.vuong cắt nhau
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

class GroupMonster(pygame.sprite.Group):   # Nhóm các spear

    def __init__(self, Hp, target):
        super().__init__()
        self.Hp = Hp
        self.target = target


    def update(self):
        numDef = 0
        for mons in self.sprites():
            if mons.HP < 1:         # Quái hết máu
                self.remove(mons)
                numDef += 1
            else:
                if mons.isAtt:   # Nếu trog trạng thái ra đòn
                    continue
                elif mons.dir > 0:   
                    mons.image = pygame.transform.scale(mons.arc_right[mons.indexR], (sizeW, sizeH))
                    mons.indexR = (mons.indexR + 1) % 6
                else:
                    mons.image = pygame.transform.scale(mons.arc_left[mons.indexL], (sizeW, sizeH))
                    mons.indexL = (mons.indexL + 1) % 6
        return numDef

    def move(self, target):                         # Di chuyển theo nvc
        for mons in self.sprites():
            if mons.isAtt:                  # Nếu trog trạng thái ra đòn
                continue
            elif target.X > mons.X:         # NVC bên phải
                mons.X += mons.Vel
                mons.dir = 2
                mons.rectAtt = pygame.Rect(mons.X + mons.rect.width / 2 - 20, mons.Y , mons.rect.width, mons.rect.height)
            else:                   # NVC bên trái
                mons.X -= mons.Vel
                mons.dir = -2
                mons.rectAtt = pygame.Rect(mons.X - mons.rect.width / 2 + 40, mons.Y , mons.rect.width, mons.rect.height)
            mons.rect = pygame.Rect(mons.X, mons.Y, 50, 50)

    def draw(self):
        for mons in self.sprites():
            screen.blit(mons.image, (mons.X, mons.Y))
    
    def rand(self):
        if len(self) < 5:           # Giới hạn quái trên sân
            rd = random.randint(1, 100)
            if rd >= 50 and rd <= 59:
                if len(self) % 2:
                    rd = random.randint(0, 200)         # Quái xuất hiện bên trái
                else:
                    rd = random.randint(600, 800)        # Quái xuất hiện bên phải

                for mons in self.sprites():             # Check có trùng vt vs quái        
                    while mons.X == rd and mons.image.collidepoint((rd, 222)) and self.target.rect.collidepoint((rd, 222)):
                        if len(self) % 2:
                            rd = random.randint(0, 200)
                        else:
                            rd = random.randint(600, 800)
                newMons = Spear(rd, 245, self.Hp, self.target)
                self.add(newMons)
        
    def isAttack(self):                                   
        for mons in self.sprites():
            A = mons.rectAtt
            B = mons.target.rect
            if (colliderect(A, B)) or mons.isAtt > 0:       # Nếu range of attack cắt nvc
                mons.attack()



class Spear(pygame.sprite.Sprite):
    def __init__(self, x, y, Hp, target):
        super().__init__()

        
        # Vị trí
        self.X = x
        self.Y = y

        self.indexL = 0 # Thứ tự khung hình move
        self.indexR = 0     
        self.indexAL = 0 # Thứ tự khung hình tấn công
        self.indexAR = 0    

        # In4 cơ bản
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Images/SkeRun.png')), (sizeW, sizeH))  # Resize the image as needed
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y) 
        self.rectAtt = pygame.Rect(self.X + self.rect.width / 2 - 20, self.Y , self.rect.width, self.rect.height) # range of Attack
        self.dir = 1
        self.isAtt = 0
        self.Vel = 2
        self.HP = Hp
        self.target = target
        self.col = red
        self.timeAtt = 0

        # Các khung hình
        self.arc_right = []
        self.arc_left = []
        self.arc_attR = []
        self.arc_attL = []

        for i in range(4):
            str = 'Images/SkeAttack'
            if i > 0:
                str += chr(i + 48)
            str += '.png'
            self.arc_attR.append(pygame.image.load(os.path.join(str)))

        for i in range(4):
            str = 'Images/SkeAttack'
            if i > 0:
                str += chr(i + 48)
            str += 'Mi.png'
            self.arc_attL.append(pygame.image.load(os.path.join(str)))

        for i in range(6):
            str = 'Images/SkeRun'
            if i > 0:
                str += chr(i + 48)
            str += '.png'
            self.arc_right.append(pygame.image.load(os.path.join(str)))

        for i in range(6):
            str = 'Images/SkeRunMi'
            if i > 0:
                str += chr(i + 48)
            str += '.png'
            self.arc_left.append(pygame.image.load(os.path.join(str)))

        """
        dir: hướng nhìn
        1, 2 : đứng phải, chạy phải
        -1, -2: đứng trái, nhìn trái
        """
    
    def attack(self):
        if not self.isAtt:
            self.isAtt = 1          # Đánh dấu dg ra đòn
            self.col = pink
            self.timeAtt = pygame.time.get_ticks()
            if self.dir > 0:
                self.image = pygame.transform.scale(self.arc_attR[self.isAtt], (sizeW, sizeH))
            else:
                self.image = pygame.transform.scale(self.arc_attL[self.isAtt], (sizeW, sizeH))
        elif self.isAtt == 1:
            cur = pygame.time.get_ticks()
            if cur - self.timeAtt >= attack_cooldown:         # Hết CoolDown
                self.timeAtt = pygame.time.get_ticks()
                self.isAtt = 2
                if self.dir > 0:
                    self.image = pygame.transform.scale(self.arc_attR[self.isAtt], (sizeW, sizeH))
                else:
                    self.image = pygame.transform.scale(self.arc_attL[self.isAtt], (sizeW, sizeH))
                if colliderect(self.rectAtt, self.target.rect):  # Nếu nvc trog tầm đánh
                    self.target.Hp -= 1
        else:
            cur = pygame.time.get_ticks()
            if cur - self.timeAtt >= attack_cooldown:       # Kết thúc attack
                self.isAtt = 0
                

        
    
