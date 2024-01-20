import pygame
from pygame.transform import scale


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(300, 800, 300, -70)
        self.get_image = pygame.image.load("pngwing.com.png")
        self.image = scale(self.get_image, (300, 100))

        self.rect1 = pygame.Rect(400, 800, 400, -70)
        self.get_image = pygame.image.load("pngwing.com.png")
        self.image = scale(self.get_image, (300, 100))

    def debug(self, screen): # Отображение хитбоксов
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

