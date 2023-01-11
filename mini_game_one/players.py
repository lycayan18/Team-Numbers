import pygame
import random


class PlayerTask(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(PlayerTask, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("game_img/sprite_1.png")
        self.rect = self.img.get_rect()
        self.rect.x = pygame.display.Info().current_w // 2 - 450
        self.rect.y = pygame.display.Info().current_h - 75
        self.mright = False
        self.mleft = False

    def output(self):
        """рисование игрока на экране"""
        # self.img = pygame.transform.scale(self.img, (74, 56))
        self.screen.blit(self.img, self.rect)

    def update(self, *args, **kwargs) -> None:
        pass

    def move(self):
        if self.mright:
            if self.rect.x <= 627:
                self.rect.x += 7
        elif self.mleft:
            if self.rect.x > 4:
                self.rect.x -= 7


class PlayerGame(pygame.sprite.Sprite):
    """класс для игрока на поле для игроков"""

    def __init__(self, screen):
        super(PlayerGame, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("game_img/sprite_1.png")
        self.rect = self.img.get_rect()
        self.rect.x = 1160
        self.rect.y = 740
        self.speedy = 3
        self.positions_list = [False, False, False]

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
            self.positions_list[0] = True
        elif score == 70 and self.positions_list[1] is False:
            self.rect.x = 1035
            self.rect.y = 379
            self.positions_list[1] = True
        elif score == 100:
            self.rect.x = 1035
            self.rect.y = 180
            self.positions_list[2] = True
        return self.positions_list

    def failed(self):
        if self.rect.y < pygame.display.Info().current_h + 20:
            self.rect.y += self.speedy
            self.speedy += 1
            return False
        else:
            return True


class Bot(PlayerGame):
    def __init__(self, screen):
        super(Bot, self).__init__(screen)
        self.img = pygame.image.load("game_img/sprite_2.png")
        self.rect.x = 1060
        self.rect.y = 715
        self.sub_level = 0
        self.time_move = random.randint(15000, 350000)

    def check_time(self):
        self.time_move -= 1
        if self.time_move <= 0:
            self.sub_level += 1
            self.time_move = random.randint(15000, 350000)

    def check_pos_player_game(self, positions_list):
        if self.sub_level == 1 and positions_list[0] is False:
            self.rect.x = 1100
            self.rect.y = 536
        elif self.sub_level == 1 and positions_list[0]:
            self.rect.x = 1000
            self.rect.y = 536

        if self.sub_level == 2 and positions_list[1] is False:
            self.rect.x = 1035
            self.rect.y = 354
        elif self.sub_level == 2 and positions_list[1]:
            self.rect.x = 935
            self.rect.y = 354

        if self.sub_level == 3 and positions_list[2] is False:
            self.rect.x = 1035
            self.rect.y = 155
        elif self.sub_level == 3 and positions_list[2]:
            self.rect.x = 935
            self.rect.y = 155

