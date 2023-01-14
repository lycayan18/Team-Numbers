import pygame
import random
from Settings import game_sound, clicked_sound_effects


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
        self.snow_x = -300
        self.ice_rect = 0
        self.mspace = False
        self.coll = False
        self.positions_list = [False, False]

    def output(self):
        """рисование игрока на экране"""
        # self.img = pygame.transform.scale(self.img, (74, 56))
        self.screen.blit(self.img, self.rect)

    def update(self, *args, **kwargs) -> None:
        pass

    def move(self, command):
        if command:
            if self.mright:
                if self.rect.x <= 627:
                    self.rect.x += 7
            elif self.mleft:
                if self.rect.x > 4:
                    self.rect.x -= 7
        else:
            if self.mspace:
                if 510 < self.rect.y <= 650:
                    self.rect.y -= 20
                if self.rect.y == 510 or self.rect.y == 500:
                    self.mspace = False
            else:
                if (self.rect.y > 509 or self.rect.y == 500) and self.rect.y != 650:
                    self.mspace = False
                    self.rect.y += 10


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
        self.positions_sublevel_list = [False, False, False]
        self.current_positions = [False, False, False]
        self.sound_effect_play = True

    def output(self):
        """рисование игрока на экране"""
        # self.img = pygame.transform.scale(self.img, (74, 56))
        self.screen.blit(self.img, self.rect)

    def update(self, *args, **kwargs) -> None:
        pass

    def check_score(self, score):

        if score == 40 and self.positions_sublevel_list[0] is False:
            self.rect.x = 1100
            self.rect.y = 561
            if clicked_sound_effects:
                sound = pygame.mixer.Sound(f'music_and_sound_effects/{game_sound[1]}')
                sound.play()
            self.positions_sublevel_list[0] = True
            self.current_positions = [True, False, False]
        elif score == 70 and self.positions_sublevel_list[1] is False:
            self.rect.x = 1035
            self.rect.y = 379
            if clicked_sound_effects:
                sound = pygame.mixer.Sound(f'music_and_sound_effects/{game_sound[1]}')
                sound.play()
                self.current_positions = [False, True, False]
            self.positions_sublevel_list[1] = True
        elif score == 100:
            self.rect.x = 1035
            self.rect.y = 180
            if clicked_sound_effects and self.sound_effect_play:
                sound = pygame.mixer.Sound(f'music_and_sound_effects/{game_sound[7]}')
                sound.play()
            self.sound_effect_play = False
            self.positions_sublevel_list[2] = True
            self.current_positions = [False, False, True]
        return self.current_positions

    def failed(self):
        if self.rect.y < pygame.display.Info().current_h + 20:
            self.rect.y += self.speedy
            self.speedy += 1
            return False
        else:
            if clicked_sound_effects:
                sound = pygame.mixer.Sound(f'music_and_sound_effects/{game_sound[6]}')
                sound.play()
            return True

    def reset(self):
        self.rect.x = 1160
        self.rect.y = 740
        self.positions_sublevel_list = [False, False, False]
        self.current_positions = [False, False, False]
        self.sound_effect_play = True
        self.speedy = 3


class Bot:
    def __init__(self, screen):
        self.screen = screen
        self.img = pygame.image.load("game_img/sprite_2.png")
        self.rect = self.img.get_rect()
        self.rect.x = 1060
        self.rect.y = 715
        self.speedy = 3
        self.sub_level = 0
        self.time_move = random.randint(1500, 2000)

    def check_time(self):
        self.time_move -= 1
        if self.time_move <= 0 and self.sub_level != 3:
            self.sub_level += 1
            if clicked_sound_effects:
                sound = pygame.mixer.Sound(f'music_and_sound_effects/{game_sound[1]}')
                sound.play()
            self.time_move = random.randint(1500, 2000)

    def check_pos_player_game(self, positions_list):
        if self.sub_level == 1 and positions_list[0] is False:
            self.rect.x = 1100
            self.rect.y = 536
        elif self.sub_level == 1 and positions_list[0]:
            self.rect.x = 1000
            self.rect.y = 536
        elif self.sub_level == 2 and positions_list[1] is False:
            self.rect.x = 1035
            self.rect.y = 354
        elif self.sub_level == 2 and positions_list[1]:
            self.rect.x = 935
            self.rect.y = 354
        elif self.sub_level == 3 and positions_list[2] is False:
            self.rect.x = 1035
            self.rect.y = 155
        elif self.sub_level == 3 and positions_list[2]:
            self.rect.x = 935
            self.rect.y = 155

    def reset(self):
        self.rect.x = 1060
        self.rect.y = 715
        self.sub_level = 0
        self.speedy = 3

    def failed(self):
        if self.rect.y < pygame.display.Info().current_h + 20:
            self.rect.y += self.speedy
            self.speedy += 1
            return False
        else:
            if clicked_sound_effects:
                sound = pygame.mixer.Sound(f'music_and_sound_effects/{game_sound[6]}')
                sound.play()
            return True

    def output(self):
        """рисование  бота на экране"""
        # self.img = pygame.transform.scale(self.img, (74, 56))
        self.screen.blit(self.img, self.rect)

    def update(self, *args, **kwargs) -> None:
        pass

