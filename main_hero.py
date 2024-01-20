import pygame
from pygame.transform import scale
import main_hero
import Walls
import pygame
from pygame.transform import scale
import main_hero
import PIL

pygame.init()
class mainhero(pygame.sprite.Sprite):

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)


        self.rect = pygame.Rect(100, 200, 50, 50)

        #stay
        self.image1 = []
        self.image1.append(scale(pygame.image.load("hero_Sprite/hero_02.jpg"), (115, 110)))
        self.image1.append(scale(pygame.image.load("hero_Sprite/hero_03.jpg"), (115, 110)))

        #GOING RIGHT
        self.image2 = []
        self.image2.append(scale(pygame.image.load("hero_Sprite/hero_03.jpg"), (115, 110)))
        self.image2.append(scale(pygame.image.load("hero_Sprite/hero_04.jpg"), (115, 110)))
        self.image2.append(scale(pygame.image.load("hero_Sprite/hero_05.jpg"), (115, 110)))
        self.image2.append(scale(pygame.image.load("hero_Sprite/hero_06.jpg"), (115, 110)))
        self.image2.append(scale(pygame.image.load("hero_Sprite/hero_07.jpg"), (115, 110)))

        #KICK
        self.image3 = []
        self.image3.append(scale(pygame.image.load("hero_Sprite/hero_08.jpg"), (115, 110)))
        self.image3.append(scale(pygame.image.load("hero_Sprite/hero_06.jpg"), (115, 110)))

        #GOING LEFT
        self.image4 = []
        self.image4.append(scale(pygame.image.load("hero_Sprite/hero_07.jpg"), (115, 110)))
        self.image4.append(scale(pygame.image.load("hero_Sprite/hero_06.jpg"), (115, 110)))
        self.image4.append(scale(pygame.image.load("hero_Sprite/hero_05.jpg"), (115, 110)))
        self.image4.append(scale(pygame.image.load("hero_Sprite/hero_04.jpg"), (115, 110)))
        self.image4.append(scale(pygame.image.load("hero_Sprite/hero_03.jpg"), (115, 110)))

        #SIT
        self.image5 = []
        self.image5.append(scale(pygame.image.load("hero_Sprite/hero_26.jpg"), (115, 110)))
        self.image5.append(scale(pygame.image.load("hero_Sprite/hero_31.jpg"), (115, 110)))

        #JUMP
        self.image6 = []
        self.image6.append(scale(pygame.image.load("hero_Sprite/hero_19.jpg"), (115, 110)))
        self.image6.append(scale(pygame.image.load("hero_Sprite/hero_15.jpg"), (115, 110)))


        self.image7 = []
        self.image7.append(scale(pygame.image.load("hero_Sprite/hero_25.jpg"), (115, 110)))
        self.image7.append(scale(pygame.image.load("hero_Sprite/hero_26.jpg"), (115, 110)))


        self.image8 = []
        self.image8.append(scale(pygame.image.load("hero_Sprite/hero_01.jpg"), (115, 110)))
        self.image8.append(scale(pygame.image.load("hero_Sprite/hero_02.jpg"), (115, 110)))



        self.xvel = 0

        self.frame_left = 0
        self.frame_Jump = 0
        self.frame_right = 0
        self.frame_sit = 0


    def update(self, left, right, Jump, sit, screen, animation_st):
        if not (Jump or sit):
            self.yvel = 0

        if ((Jump and sit) and (not right and not left)) or (Jump and sit and left and right):
            self.yvel = 0
            a = int(animation_st)
            screen.blit(self.image1[a], (self.rect.x, self.rect.y))
            return()

        if not (left or right):
            self.xvel = 0

        if (left and right) and (not Jump and not sit):
            self.xvel = 0
            a = int(animation_st)
            screen.blit(self.image1[a], (self.rect.x, self.rect.y))


        if left and not right:
            self.frame_left += 0.1
            if (self.frame_left >= 2):
                self.frame_left = 0
            l = int(self.frame_left)
            screen.blit(self.image4[l], (self.rect.x, self.rect.y))
            self.xvel = -4


        if right and not left:
            self.xvel = 4
            self.frame_right += 0.2
            if (self.frame_right >= 2):
                self.frame_right = 0
            w = int(self.frame_right)
            screen.blit(self.image2[w], (self.rect.x, self.rect.y))

        if not (left or right):
            self.xvel = 0

        if (Jump and not sit and not left and not right) or (Jump and left and right):

            self.frame_Jump += 0.1
            if (self.frame_Jump >= 2):
                self.frame_Jump = 0
            q = int(self.frame_Jump)
            screen.blit(self.image6[q], (self.rect.x, self.rect.y))

        if Jump and not sit:
            self.yvel = -4

        if (sit and not Jump and not left and not right) or (sit and left and right):

            self.frame_Sit += 0.1
            if (self.frame_Sit >= 2):
                self.frame_Sit = 0
            e = int(self.frame_Sit)
            screen.blit(self.image5[e], (self.rect.x, self.rect.y))

        if (sit and not Jump):
            self.yvel += 4

        if not (Jump or sit):
            self.yvel = 0

        if (Jump and sit):
            self.yvel = 0

        self.rect.x += self.xvel
        self.rect.y += self.yvel

        if (not (sit or Jump or left or right)):
                    a = int(animation_st)
                    screen.blit(self.image1[a], (self.rect.x, self.rect.y))

    def pushback(self):
        self.rect.x -= self.xvel
        self.rect.y -= self.yvel

