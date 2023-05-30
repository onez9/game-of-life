#!/usr/bin/python3
import pygame
import os
import math

clear=lambda: os.system('clear')





class Barrier(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rectSize=(20, 100)
        self.image=pygame.Surface(self.rectSize)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center=(width-100, height-100)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.rectSize=(50,50)
        self.image = pygame.Surface(self.rectSize)

        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        
        self.rect.center = (width / 2, height - 100)
        self.isJump=False

        self.angle=60
        self.speed=10

        self.jumpCount=10
        #self.speedy = self.speed * math.sin(self.angle * math.pi / 180)
        #self.speedx = self.speed * math.cos(self.angle * math.pi / 180)

    def update(self):
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))

        if keys[pygame.K_SPACE]:
            self.isJump = True
            self.speed=0

        if keys[pygame.K_SPACE] and keys[pygame.K_LEFT] and self.rect.x>=0:
            self.isJump = True
            self.speed = -abs(self.speed)

        if keys[pygame.K_SPACE] and keys[pygame.K_RIGHT] and self.rect.x<=width-50:
            self.isJump = True
            self.speed = abs(self.speed)

        if keys[pygame.K_LEFT] and self.rect.x>=0:
            self.rect.x-=self.speed

        if keys[pygame.K_RIGHT] and self.rect.x<=width-50:
            self.rect.x+=self.speed

        if keys[pygame.K_q]:
            quit()

        if self.isJump is True:
            #tmp=self.speedy
            if self.jumpCount >= -10:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount))//2
                self.jumpCount -= 1
            else: 
                self.jumpCount=10
                self.isJump=False
            self.rect.x+=self.speed

        



if __name__=='__main__':
    clock=pygame.time.Clock()
    GREEN=(0,255,0)
    BLACK=(0,0,0)
    width=700
    height=500
    size=[width,height]
    FPS=60
    pygame.init()
    pygame.mixer.init()
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption("My Game")

    all_sprites = pygame.sprite.Group()
    player = Player()
    barrier = Barrier()
    all_sprites.add(player)
    all_sprites.add(barrier)

    try:
        # Цикл игры
        running = True
        while running:
            # Держим цикл на правильной скорости
            clock.tick(FPS)
            # Ввод процесса (события)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False
            # Обновление
            all_sprites.update()
            # Рендеринг
            screen.fill(BLACK)
            all_sprites.draw(screen)
            # После отрисовки всего, переворачиваем экран
            pygame.display.flip()
                    
        pygame.quit()




    except KeyboardInterrupt:
        clear()
        print('Выход')



   

