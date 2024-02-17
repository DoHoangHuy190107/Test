import pygame, sys, os

pygame.init()

FPS = 20
width, height = 800, 600
X, Y = 50, 100
sizeW, sizeH = 40, 42
y_gravity = 2
white = (252, 252, 252)
black = (0, 0, 0)

screen = pygame.display.set_mode((width, height))
knight_stand_right = pygame.image.load(os.path.join('Images/__Idle.png'))
knight_stand_left = pygame.image.load(os.path.join('Images/__IdleMi.png'))



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, Hp):
        super().__init__()
        self.image = pygame.transform.scale(knight_stand_right, (sizeW, sizeH))  # Resize the image as needed
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y) 
        self.dir = 1
        self.Hp = Hp
        
        """
        dir: hướng nhìn
        1, 2 : đứng phải, chạy phải
        -1, -2: đứng trái, nhìn trái
        """
        self.indexL = 0 # Thứ tự khung hình
        self.indexR = 0
        self.indexAR = 0
        self.indexAL = 0

        # Vị trí
        self.X = x
        self.Y = y
        # In4 jump
        self.jumping = False
        self.VelJump = 10
        self.Vel = 10
        self.jump_height = self.VelJump
        self.dirJump = 0

        # Vùng đánh
        self.isAtt = 0
        self.rectAtt = pygame.Rect(self.X + self.rect.width, self.Y , self.rect.width * 2, self.rect.height)

        self.knight_run_right = [] # Khung hình chạy phải
        self.knight_run_left = [] # Khung hình chạy trái
        self.knight_jump = [] # Khung hình nhảy
        self.knight_attack_right = [] # Khung hình đánh phải
        self.knight_attack_left = [] # Khung hình đánh trái

        for i in range(9):
            str = 'Images/_Run'
            if i > 0:
                str += chr(i + 48)
            str += '.png'
            self.knight_run_right.append(pygame.image.load(os.path.join(str)))
    
        for i in range(9):
            str = 'Images/_RunMi'
            if i > 0:
                str += chr(i + 48)
            str += '.png'
            self.knight_run_left.append(pygame.image.load(os.path.join(str)))

        self.knight_jump.append(pygame.image.load(os.path.join('Images/_Jump.png')))
        self.knight_jump.append(pygame.image.load(os.path.join('Images/_JumpMi.png')))

        for i in range(4):
            str = 'Images/_Attack'
            if i > 0:
                str += chr(i + 48)
            str += '.png'
            self.knight_attack_right.append(pygame.image.load(os.path.join(str)))

        for i in range(4):
            str = 'Images/_AttackMi'
            if i > 0:
                str += chr(i + 48)
            str += '.png'
            self.knight_attack_left.append(pygame.image.load(os.path.join(str)))

    def draw(self):
        screen.blit(self.image, (self.X, self.Y))
        if self.isAtt:
            self.X += 30
            self.isAtt = 0
        
        pygame.draw.rect(screen, (252, 0, 0), self.rectAtt)

    def attack(self, target):
        for mons in target:
            A = self.rectAtt
            B = mons.rect
            leftA = A.x
            rightA = leftA + A.width
            topA = A.y
            downA = topA + A.height
            leftB = B.x
            rightB = leftB + B.width
            topB = B.y
            downB = topB + B.height
            if leftA <= rightB and downA >= topB and rightA >= leftB and topA <= downB:
                mons.HP -= 2

    def update(self):
        if self.dir > 0:
            self.rectAtt = pygame.Rect(self.X + self.rect.width - 10, self.Y , self.rect.width, self.rect.height)
        else:
            self.rectAtt = pygame.Rect(self.X - self.rect.width + 10, self.Y , self.rect.width, self.rect.height)

    def handle_event(self, target):
        keys = pygame.key.get_pressed()
        event = pygame.event.get()

        if keys[pygame.K_j]:
            if self.dir > 0:
                self.indexAR = (self.indexAR + 1) % 4
                self.image = self.knight_attack_right[self.indexAR]
                self.attack(target)
            else:
                self.indexAL = (self.indexAL + 1) % 4
                self.image = self.knight_attack_left[self.indexAL]
                self.X -= 30
                self.isAtt = 1
                self.attack( target)
        elif keys[pygame.K_a] and self.X > self.Vel: # Trái
            self.dir = -2
            self.X -= self.Vel
            self.dirJump = 1
            self.indexR = 0
            self.indexL = (self.indexL + 1) % 8
            self.image = self.knight_run_left[self.indexL]
        elif keys[pygame.K_d] and self.X < width - self.Vel - sizeW: # Phải
            self.dir = 2
            self.X += self.Vel
            self.dirJump = 0
            self.indexL = 0
            self.indexR = (self.indexR + 1) % 8
            self.image = self.knight_run_right[self.indexR]
        elif keys[pygame.K_SPACE]:
            self.jumping = True
        else:
            self.indexR = 0
            self.indexL = 0
            if self.dir > 0:
                self.image = pygame.transform.scale(knight_stand_right, (sizeW, sizeH))
            else:
                self.image = pygame.transform.scale(knight_stand_left, (sizeW, sizeH))

        if not self.jumping:
            if keys[pygame.K_SPACE]:
                self.jumping = True
        else :
            self.Y -= self.VelJump
            self.VelJump -= y_gravity
            if self.VelJump < -self.jump_height:
                self.jumping = False
                self.VelJump =  self.jump_height
            self.image = self.knight_jump[self.dirJump]