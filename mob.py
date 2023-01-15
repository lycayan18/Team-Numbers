import pygame


class IceMob(pygame.sprite.Sprite):
    def __init__(self):
        super(IceMob, self).__init__()
        self.check = False
        self.image = pygame.image.load("game_img/ice.png")
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 645
        self.speedx = 14

    def update_rect(self, check):
        self.check = check
        self.update()

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.x < 70 or self.check:
            print(self.check)
            self.rect.x = 700
            self.speedx = 14

