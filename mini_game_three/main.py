import random

import pygame
import sys
import time
from controls import loading, transition_figure
from background_menu_anim import BACKGOUND_MENU
from game import Game, LevelThree
from player import PlayerTask, PlayerGame
from mob import IceMob
pygame.init()


class SpritesWindow:
    def __init__(self, screen, command):
        self.command = command
        self.screen = screen

    def draw_buttons(self):
        global sprites_list, start_game, game, snows
        if self.command == 'menu':
            """главное меню"""
            sprites_list = [
                ButtonStartGame(self.screen), ButtonShop(self.screen),
                ButtonSettings(self.screen), ButtonExit(self.screen)
            ]
            start_game = False

        elif self.command == 'start_game':
            """игра"""
            transition_figure(screen)
#            loading(screen)
#            transition_figure(screen)

            sprites_list = []
            game = Game(screen, snow_image)

            start_game = True
            for i in range(3):
                m = IceMob()
                ice.add(m)
                ice_mobs.add(m)
        elif self.command == 'settings':
            """настройки"""
            sprites_list = [BackButton(self.screen)]
        elif self.command == 'shop':
            """магазин"""
            sprites_list = [BackButton(self.screen)]


class ButtonStartGame(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(ButtonStartGame, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("menu_img/Start_game.png")
        self.rect = self.img.get_rect()
        self.rect.x = 30
        self.rect.y = 450

    def output(self):
        # рисование кнопки на экране
        self.screen.blit(self.img, self.rect)

    def update(self, *args, **kwargs) -> None:
        if len(args) == 0:
            return
        event = args[0]
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            SpritesWindow(self.screen, 'start_game').draw_buttons()
        if event.type == pygame.MOUSEMOTION and self.rect.collidepoint(event.pos):
            self.img = pygame.transform.scale(self.img, (388, 76))
        else:
            self.img = pygame.image.load("menu_img/Start_game.png")


class ButtonSettings(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(ButtonSettings, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("menu_img/Settings.png")
        self.rect = self.img.get_rect()
        self.rect.x = 30
        self.rect.y = 550

    def output(self):
        # рисование кнопки на экране
        self.screen.blit(self.img, self.rect)

    def update(self, *args, **kwargs) -> None:
        if len(args) == 0:
            return
        event = args[0]
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            SpritesWindow(self.screen, 'settings').draw_buttons()
        if event.type == pygame.MOUSEMOTION and self.rect.collidepoint(event.pos):
            self.img = pygame.transform.smoothscale(self.img, (355, 85))
        else:
            self.img = pygame.image.load("menu_img/Settings.png")


class ButtonShop(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(ButtonShop, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("menu_img/Shop.png")
        self.rect = self.img.get_rect()
        self.rect.x = 30
        self.rect.y = 650

    def output(self):
        # рисование кнопки на экране
        self.screen.blit(self.img, self.rect)

    def update(self, *args, **kwargs) -> None:
        if len(args) == 0:
            return
        event = args[0]
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            SpritesWindow(self.screen, 'shop').draw_buttons()
        if event.type == pygame.MOUSEMOTION and self.rect.collidepoint(event.pos):
            self.img = pygame.transform.smoothscale(self.img, (280, 70))
        else:
            self.img = pygame.image.load("menu_img/Shop.png")


class ButtonExit(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(ButtonExit, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("menu_img/Exit.png")
        self.rect = self.img.get_rect()
        self.rect.x = 30
        self.rect.y = 750

    def output(self):
        # рисование кнопки на экране
        self.screen.blit(self.img, self.rect)

    def update(self, *args, **kwargs) -> None:
        if len(args) == 0:
            return
        event = args[0]
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            sys.exit()
        if event.type == pygame.MOUSEMOTION and self.rect.collidepoint(event.pos):
            self.img = pygame.transform.smoothscale(self.img, (225, 78))
        else:
            self.img = pygame.image.load("menu_img/Exit.png")


class BackButton(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(BackButton, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("menu_img/Back.png")
        self.rect = self.img.get_rect()
        self.rect.x = 30
        self.rect.y = 40

    def output(self):
        # рисование кнопки на экране
        self.screen.blit(self.img, self.rect)

    def update(self, *args, **kwargs) -> None:
        if len(args) == 0:
            return
        event = args[0]
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            SpritesWindow(self.screen, 'menu').draw_buttons()


ice_time = pygame.USEREVENT + 1
pygame.time.set_timer(ice_time, random.randint(3000, 4500))
ice_image_list = []
player_x_y, ice_x_y = (50, 0), (0, 645)


def events(sprites_list, game_start, player_task):
    """"обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if len(sprites_list) > 0:
            for i in sprites_list:
                i.update(event)
        if game_start:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player_task.mspace = True


snow_image = pygame.image.load("game_img/snow_run.png")


def update_screen(screen, background_menu, buttons_menu, start_game, game, players, levels):
    # обновление экрана
    screen.blit(background_menu, (0, 0))
    if len(buttons_menu) > 0:
        for i in buttons_menu:
            i.output()
    if start_game:
        level = game.get_level()
        game.draw_playing_field()
        game.draw_sublevel()
        game.draw_sprite(level)
        players[1].update()  # PlayerGame
        players[1].output()
        if level == 1:
            score = levels[0].get_score()
            players[1].check_score(score)
            time_level = levels[0].get_time_level()
            if score < 100 and time_level < 114:
                players[0].move()  # PlayerTask
                players[0].output()
                levels[0].draw_snows()
                levels[0].check_mobs_contact()
                levels[0].draw_score()
            levels[0].draw_time_level()
            if time_level > 114:
                if score == 100:
                    game.next_level()
                    time.sleep(1)
                    transition_figure(screen)
                else:
                    levels[0].score_reset()
                    fail = players[1].failed()
                    players[1].output()
                    if fail:
                        time.sleep(1)
                        transition_figure(screen)
                        SpritesWindow(screen, 'menu').draw_buttons()
                        players[1] = PlayerGame(screen)
                        levels[0].time_level = 0
    pygame.display.flip()


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
sprites_list = []  # список кнопок которые надо отобразить
start_game = False
game = False
fps = 60
snows = pygame.sprite.Group()
mobs = pygame.sprite.Group()

ice = pygame.sprite.Group()
ice_mobs = pygame.sprite.Group()


def run():
    pygame.init()
    pygame.display.set_caption("Эль Капитан")
    clock = pygame.time.Clock()
    background_menu_anim_count = 0
    SpritesWindow(screen, 'menu').draw_buttons()
    players = [PlayerTask(screen), PlayerGame(screen)]
    levels = [LevelThree(ice, ice_mobs, screen, players[0]), None, None]
    while True:
        events(sprites_list, start_game, players[0])
        update_screen(
            screen,
            pygame.image.load(f'menu_img/background_menu_anim/{BACKGOUND_MENU[background_menu_anim_count]}'),
            sprites_list,
            start_game,
            game,
            players,
            levels,
        )
        if start_game is False:
            if background_menu_anim_count == 337:
                background_menu_anim_count = 0
            else:
                background_menu_anim_count += 1
        clock.tick(fps)


if __name__ == '__main__':
    run()
