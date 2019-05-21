import pygame
pygame.init()

win = pygame.display.set_mode((640, 360))

pygame.display.set_caption("test pohyb")
clock = pygame.time.Clock()

class POSTAVA(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

    def hit(self):
        font1 = pygame.font.SysFont('Calibri',100)
        text = font1.render('git gud' , 1, (255,255,0))
        textRect = text.get_rect()
        textRect.center = (misto.screenWidth//2, misto.screenHeight//2)
        win.blit(text, textRect)
        man.visible = False
        self.vel = 0
        pygame.display.update()



class PLAYGROUND(object):
    def __init__(self, width,height):
        self.screenWidth = width
        self.screenHeight = height

class ENEMY(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel_x = 10
        self.vel_y = 10

    def hit(self):
        zly.visible = False
        self.vel_x = 0
        self.vel_y = 0


#maincycle
man = POSTAVA(300,100,30,30)
misto = PLAYGROUND(640,360)
zly = ENEMY(100, 100, 40, 40)
run = True
while run:
    clock.tick(60)

    win.fill((0, 0, 0))

    if man.y < zly.y + zly.height and man.y + man.height > zly.y:
        if man.x + man.width > zly.x and man.x < zly.x + zly.width:
            man.hit()
            zly.hit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and man.x > man.vel:
        man.x -= man.vel
    if keys[pygame.K_d] and man.x < misto.screenWidth - man.width - man.vel:
        man.x += man.vel
    if keys[pygame.K_w] and man.y > man.vel:
        man.y -= man.vel
    if keys[pygame.K_s] and man.y < misto.screenHeight - man.height - man.vel:
        man.y += man.vel

    zly.x += zly.vel_x
    zly.y += zly.vel_y

    if zly.x <= 0 or zly.x >= misto.screenWidth - zly.width - zly.vel_x:
        zly.vel_x = zly.vel_x * -1
    if zly.y <= 0 or zly.y >= misto.screenHeight - zly.width - zly.vel_y:
        zly.vel_y = zly.vel_y * -1

    pygame.draw.rect(win, (255, 255, 0), (man.x, man.y, man.width, man.height))
    pygame.draw.rect(win, (255, 0, 0), (zly.x, zly.y, zly.width, zly.height))
    pygame.display.update()

pygame.quit()
