import pygame
import glob
playerName = [input('ENTER THE PLAYER 1 NAME:').upper(),input('ENTER THE PLAYER 2 NAME:').upper()]
pygame.init()
win = pygame.display.set_mode((855,480))
intro = pygame.image.load('intro.png')
pygame.display.set_caption("First Game")
attack_1=[pygame.image.load(img) for img in glob.glob("Attack\\*.png")]
idle = [pygame.image.load('I R.png'),pygame.image.load('I R E.png'),pygame.image.load('I L.png'),pygame.image.load('I L E .png')]
walkRight1 = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft1 = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
walkLeft2 = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]
walkRight2 = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]
winner = pygame.image.load('winner.png')
bg = [pygame.image.load('bg 1.jpg'),pygame.image.load('bg 2.jpg'),pygame.image.load('bg 3.jpg'),pygame.image.load('bg 4.jpg'),pygame.image.load('bg 5.jpg')]
Round=[pygame.image.load('round 1.png'),pygame.image.load('round 2.png'),pygame.image.load('round 3.png'),pygame.image.load('round 4.png'),pygame.image.load('round 5.png')]
song=["music.mp3"]
    ## ****** MUSIC **********************
music=pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
    #************************************
clock=pygame.time.Clock()
class player(pygame.sprite.Sprite):
    def __init__(self, x,y,width,height,powerUpVel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel  = 5 + powerUpVel
        self.isJump = False
        self.jumpCount = 8
        self.right = False
        self.left = False
        self.walkCount = 0
        self.bulletVel = 15
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.standing = True
        self.visible = True
        self.isAttack = False
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
    def attack(self):
        pygame.display.update()
        for i in range(0,10):
            win.blit(attack_1[i],(self.x,self.y))
            j=0
            while(j<=10):
                pygame.time.delay(5)
                j+=1
            pygame.display.update()
        self.isAttack = False

    def Jump(self):
        if(self.jumpCount >= -8):
            self.y -= (self.jumpCount*abs(self.jumpCount))*0.5
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 8
    def Left(self):
        if  self.x > self.vel:
            self.x-=self.vel
            self.left=True
            self.right=False
            self.standing=False
    def Right(self):
        if self.x< 855 - self.width-self.vel:
            self.x += self.vel
            self.left= False
            self.right = True
            self.standing = False
    def draw(self,win,count):
        if self.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if ((self.standing == False) and (self.isAttack == False)):
                if self.left:
                    if count == 1:
                        win.blit(walkLeft1[self.walkCount//3],(self.x,self.y))
                    if count == 2:
                        win.blit(walkLeft2[self.walkCount//3],(self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    if count == 1:
                        win.blit(walkRight1[self.walkCount//3],(self.x,self.y))
                    if count == 2:
                        win.blit(walkRight2[self.walkCount//3],(self.x,self.y))
                    self.walkCount += 1
            elif(self.isAttack == False):
                if self.right:
                    if count == 1:
                        win.blit(idle[0],(self.x,self.y))
                    if count == 2:
                        win.blit(idle[1],(self.x,self.y))
                else:
                    if count == 1:
                        win.blit(idle[2],(self.x,self.y))
                    if count == 2:
                        win.blit(idle[3],(self.x,self.y))
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            if count == 1:
                win.blit(name.render(playerName[0] , 1, (255,0,0)), (self.hitbox[0],self.hitbox[1]-50))
            if count == 2:
                win.blit(name.render(playerName[1] , 1, (255,0,0)), (self.hitbox[0],self.hitbox[1]-50))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
class projectile():
    def __init__(self,x,y,radius,colour,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing
        self.vel = 20*facing
    def draw(self,win):
        win.blit(pygame.image.load('WEAPON.png'),(self.x,self.y))
global gameRun
gameRun = True
def won():
    gameWin[winCount] += 1
    i=0
    if winCount >= 0:
        if winCount == 0:
            text = font.render('---'+ playerName[1] +' WINS!!---', 1, (255,0,0))
        else:
            text = font.render('---' + playerName[0] +' WINS!!---', 1, (255,0,0))
        win.blit(text, (340, 220))
        pygame.display.update()
        while(i <= 210):
            pygame.time.delay(10)
            i += 1
        pygame.display.update()
        if gameWin[0] == 3 or gameWin[1] == 3:
            win.blit(winner,(0,0))
            if gameWin[1] >= 3:
                win.blit(pygame.image.load('standing.png'),(400,240))
                winName = font.render(playerName[0], 1, (255,0,0))
            if gameWin[0] >= 3:
                win.blit(pygame.image.load('R9E.png'),(400,240))
                winName = font.render(playerName[1], 1, (255,0,0))
            win.blit(text, (350, 220))
            pygame.display.update()
            delay()
            return False
        else:
            win.blit(Round[ gameWin[0] + gameWin[1]],(175,100))
            pygame.display.update()
            delay()
    return True

def delay():
    i = 0
    while(i < 300):
        pygame.time.delay(10)
        i += 1
    pygame.display.update()
#--------------------------RE-DRAW------------------------------------------
def reDraw():
    i=(gameWin[0] + gameWin[1])%5
##    win.blit(intro,(0,0))
    win.blit(bg[i],(0,0))# background
    p[0].draw(win,1)
    p[1].draw(win,2)
    text = font.render('ROUNDS WON:- ' + str(gameWin), 1, (255,0,0))
    win.blit(text, (300, 10+i))
    for bullet in bullets:
        bullet.draw(win)
    for bullet in bullets1:
        bullet.draw(win)
    pygame.display.update()
    return -1
#--------------------------------------------------------------------
def init(status,loss):
    ##________________________________initialisations________________________________
    global p
    if status == -1:
        p = [player(700,340,64,64,0),player(50,340,64,64,0)]
    if status == 1:
        p = [player(700,340,90,90,0),player(50,340,90,90,3*loss)]
    if status == 0:
        p = [player(700,340,90,90,3*loss,),player(50,340,90,90,0)]

    global bullets
    bullets = []
    global bullets1
    bullets1 = []
    global facing
    facing = [-1,0]
    global shootLoop
    shootLoop = 0
 # -----------------------------------------------------------------------------------
global gameWin
gameWin = [0,0]
First = True
##global gameRun
##gameRun = True
global font
font = pygame.font.SysFont('comicsans', 30, True)
global name
name = pygame.font.SysFont('comicsans', 20, True)
global winNAme
winName = pygame.font.SysFont('kalinga', 40, True)
global winCount
winCount = -1
global loss
loss = [0,0]
init(-1,0)
#-------------------------------------MAIN LOOP------------------

while(gameRun):
    clock.tick(27)
    if First:
        win.blit(intro,(0,0))
        introName = [winName.render(playerName[0] , 1, (255,0,0)),winName.render(playerName[1] , 1, (255,0,0))]
        win.blit(pygame.image.load('I R.png'),(150,200))
        win.blit(pygame.image.load('I R E.png'),(700,200))
        win.blit(introName[0], (200, 150))
        win.blit(introName[1], (700, 150))
        pygame.display.update()
        First = False
        delay()
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            gameRun=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_BACKSPACE]:
        init(-1,0)
#    ********************* SHOOTING START *******************
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0

    for bullet in bullets:
        if p[1].visible and p[0].visible:
            if bullet.y - bullet.radius < p[1].hitbox[1] + p[1].hitbox[3] and bullet.y + bullet.radius > p[1].hitbox[1]:
                if bullet.x + bullet.radius > p[1].hitbox[0] and bullet.x - bullet.radius < p[1].hitbox[0] + p[1].hitbox[2]:
                    p[1].hit()
                    bullets.pop(bullets.index(bullet))
            if bullet.x < 855 and bullet.x > 0 :
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
    for bullet in bullets1:
        if p[0].visible and p[1].visible:
            if bullet.y - bullet.radius < p[0].hitbox[1] + p[0].hitbox[3] and bullet.y + bullet.radius > p[0].hitbox[1]:
                if bullet.x + bullet.radius > p[0].hitbox[0] and bullet.x - bullet.radius < p[0].hitbox[0] + p[0].hitbox[2]:
                    p[0].hit()
                    bullets1.pop(bullets1.index(bullet))
            if bullet.x<855 and bullet.x>0:
                bullet.x+=bullet.vel
            else:
                bullets1.pop(bullets1.index(bullet))
    if p[1].visible and p[0].visible:
        if keys[pygame.K_END] and shootLoop == 0:
            if(len(bullets)<1):
                bullets.append(projectile(round(p[0].x + p[0].width//2),round(p[0].y+p[0].height//2),6,(255,255,0),facing[0]))
                shootLoop=1
    if p[0].visible and p[1].visible:
        if keys[pygame.K_SPACE] and shootLoop == 0:
            if(len(bullets1)<1):
                bullets1.append(projectile(round(p[1].x+p[1].width//2),round(p[1].y+p[1].height//2),6,(0,0,255),facing[1]))
                shootLoop=1
    #   ********************* SHOOTING END *********************************
    elif not p[1].visible:          #    if player 1 won AND player 2 is dead(not visible)
        winCount = 1
        gameRun = won()
        loss[1]+=1
        init(1,loss[1])
    elif not p[0].visible:          #    if player 2 won AND player 1 is dead(not visible)
        winCount = 0
        gameRun = won()
        loss[0] = 1
        init(0,loss[0])
    if p[0].left:#right side player
        facing[0]= -1
    else:
        facing[0] = 1
    if p[1].left:#left side player
        facing[1]= -1
    else:
        facing[1] = 1
    ###################### ************ MOVEMENT ************* ##########################################
    if keys[pygame.K_LEFT]:
        p[0].Left()
    elif keys[pygame.K_RIGHT]:
        p[0].Right()
    else:
        p[0].standing=True
        p[0].walkcount=0
    if keys[pygame.K_a]:
        p[1].Left()
    elif keys[pygame.K_d]:
        p[1].Right()
    else:
        p[1].standing=True
        p[1].walkcount=0
    if not(p[0].isJump):
        if keys[pygame.K_UP]:
            p[0].isJump = True
            p[0].walkCount = 0
        if keys[pygame.K_RSHIFT]:
            p[0].isAttack = True
            p[0].walkCount = 0
            p[0].attack()
    else:
        p[0].Jump()
    if not(p[1].isJump):
        if keys[pygame.K_w]:
            p[1].isJump = True
            p[1].walkCount = 0
        if keys[pygame.K_LSHIFT]:
            p[1].isAttack = True
            p[1].walkCount = 0
            p[1].attack()
    else:
        p[1].Jump()

    if gameRun:
        winCount = reDraw()
pygame.quit()
