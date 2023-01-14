import pygame
import random


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super(Mob, self).__init__()
        self.width = pygame.display.Info().current_w // 2 - 20
        self.height = pygame.display.Info().current_h
        self.image = pygame.image.load("game_img/snow.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.width - self.rect.width - 400)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = 5
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > self.height + 10 or self.rect.left < -25 or self.rect.right > self.width + 20:
            self.rect.x = random.randrange(self.width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = 5


class IceMob(pygame.sprite.Sprite):
    def __init__(self):
        super(IceMob, self).__init__()
        self.image = pygame.image.load("game_img/ice.png")
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 650
        self.speedx = 10

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.x < -60:
            self.rect.x = 620
            self.speedx = 10

