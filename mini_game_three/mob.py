import pygame


class IceMob(pygame.sprite.Sprite):
    def __init__(self):
        super(IceMob, self).__init__()
        self.image = pygame.image.load("game_img/ice.png")
        self.rect = self.image.get_rect()
        self.rect.x = 620
        self.rect.y = 645
        self.speedx = 20

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.x < -60:
            self.rect.x = 620
            self.speedx = 20
