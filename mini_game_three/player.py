import pygame


class PlayerTask(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(PlayerTask, self).__init__()
        self.screen = screen
        self.player = pygame.image.load("game_img/sprite_1.png")
        self.rect = self.player.get_rect()
        self.rect.x = 50
        self.rect.y = 650
        self.snow_x = -300
        self.ice_rect = 0
        self.mspace = False
        self.coll = False
        self.positions_list = [False, False]

    def output(self):
        """рисование игрока на экране"""
        # self.img = pygame.transform.scale(self.img, (74, 56))
        self.screen.blit(self.player, self.rect)

    def update(self, *args, **kwargs) -> None:
        pass

    def move(self):
        if self.mspace:
            if 490 < self.rect.y <= 650:
                self.rect.y -= 20
                print(self.rect.y)
            if 490 >= self.rect.y >= 475:
                self.mspace = False
                print(self.mspace)
        else:
            if self.rect.y > 474 and self.rect.y != 650:

                self.mspace = False
                self.rect.y += 5

class PlayerGame(pygame.sprite.Sprite):
    """класс для игрока на поле для игроков"""

    def __init__(self, screen):
        super(PlayerGame, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("game_img/sprite_1.png")
        self.rect = self.img.get_rect()
        self.rect.x = 1160
        self.rect.y = 740

    def output(self):
        """рисование игрока на экране"""
        # self.img = pygame.transform.scale(self.img, (74, 56))
        self.screen.blit(self.img, self.rect)

    def update(self, *args, **kwargs) -> None:
        pass

    def check_score(self, score):
        if score == 40 and self.positions_list[0] is False:
            self.rect.x = 1100
            self.rect.y = 561
            self.positions_list = [True, False]
        elif score == 70 and self.positions_list[1] is False:
            self.rect.x = 1035
            self.rect.y = 379
            self.positions_list = [True, True]
        elif score == 100:
            self.rect.x = 1035
            self.rect.y = 180
