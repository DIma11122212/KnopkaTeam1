
import pygame
from pygame.transform import scale
import main_hero
import Walls
from pygame import *
pygame.init()
clock = pygame.time.Clock()


info = pygame.display.Info()
width, height = info.current_w, info.current_h


kekinfo = (width, height)
infoX = kekinfo[0]
infoY = kekinfo[1]

animation_st = 0
ani_dop = 0.016
gameDisplay = pygame.display.set_mode((infoX, infoY))
for i in range(1, 10):
    img = pygame.image.load(f'hero_Sprite/hero_0{i}.jpg').convert_alpha(gameDisplay)

#Create a displace surface object
screen = pygame.display.set_mode(size=kekinfo)
pygame.display.set_caption("Karate_simulation")
mainLoop = True


big_sky = pygame.image.load("zadnii-fon-dlia-2d-igry-1.webp")
sky = scale(big_sky, (infoX, infoY))
block = pygame.image

Karate = main_hero.mainhero(infoX % 2 - 65, infoY % 2 - 40)

walls = pygame.sprite.Group()
walls_cords = [
    (100, 300)
]

for index in walls_cords:
    wall = Walls.Wall(index[0], index[1])
    walls.add(wall)

left = False
right = False
Jump = False
sit = False
while mainLoop:
    screen.blit(sky, (0, 0))
    for wall in walls:
        walls.draw(screen)

    for e in pygame.event.get():

        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            left = True
            print('hi')
            # s.play()

        if e.type == pygame.KEYUP and e.key == pygame.K_a:
            left = False

        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            right = True
            # s.play()
            # run.play(-1)

        if e.type == pygame.KEYUP and e.key == pygame.K_d:
            right = False
            # run.stop()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            Jump = True
            # s.play()

        if e.type == pygame.KEYUP and e.key == pygame.K_w:
            Jump = False

        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            sit = True
            # s.play()

        if e.type == pygame.KEYUP and e.key == pygame.K_s:
            sit = False

        if e.type == pygame.QUIT:
            mainLoop = False

    animation_st += ani_dop
    if (animation_st >= 1):
        ani_dop = 0.2
        if (animation_st >= 2):
            ani_dop = 0.010
            animation_st = 0

    Karate.update(left, right, Jump, sit, screen, animation_st)

    pygame.display.update()

    clock.tick(60)

pygame.quit()