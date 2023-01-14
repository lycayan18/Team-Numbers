import pygame
import sys
import random
import time
from controls import button, draw_particle, update_particle,  loading, transition_figure
from sprite_group_shop import Switchskins
from Settings import clicked_sound_effects, sound_click, Music, SoundEffects, game_sound
from game import Game, LevelOne, LevelThree
from players import PlayerTask, PlayerGame, Bot
from mobs import Mob, IceMob


class SpritesWindow:
    def __init__(self, screen, command):
        self.command = command
        self.screen = screen

    def draw_buttons(self):
        global list_buttons, start_game, game, snows, mobs
        if self.command == 'menu':
            """главное меню"""
            list_buttons = [
                ButtonStartGame(self.screen), ButtonShop(self.screen),
                ButtonSettings(self.screen), ButtonExit(self.screen)
            ]
            start_game = False
        elif self.command == 'start_game':
            """игра"""
            pygame.mixer.music.stop()
            transition_figure(screen)
            loading(screen)
            transition_figure(screen)

            list_buttons = []
            game = Game(screen, snow_image)
            start_game = True

            for i in range(9):
                m = Mob()
                snows.add(m)
                mobs.add(m)

            for i in range(3):
                m = IceMob()
                ice.add(m)
                ice_mobs.add(m)
        elif self.command == 'settings':
            """настройки"""
            list_buttons = [BackButton(self.screen), SoundEffects(self.screen), Music(self.screen)]
        elif self.command == 'shop':
            """магазин"""
            list_buttons = [BackShop(self.screen)]


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
            if clicked_sound_effects:
                sound_click.play()
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
            if clicked_sound_effects:
                sound_click.play()
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
            if clicked_sound_effects:
                sound_click.play()
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
            with open("score_button", "w") as s:
                s.write(str(money) + "\n")
                s.write(str(b))
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
            if clicked_sound_effects:
                sound_click.play()
            SpritesWindow(self.screen, 'menu').draw_buttons()


class BackShop(BackButton, Switchskins):

    def __init__(self, screen):
        super(BackButton, self).__init__(screen)
        self.screen = screen
        self.coor_sprite_back = -1
        self.coor_sprite_left = -1
        self.coor_sprite_right = -1
        self.button = -1
        self.button_choose = -1
        self.n = 0
        self.skins_price = [20, 31, 40]
        self.button_choose__ = image_button  # 0 - скин Выбран, 1 - можно выбрать скин, 2 - надо купить скин
        self.skins = 0  # индекс скина
        if self.button_choose__[0] == 0:
            self.image_but = 0
        else:
            self.image_but = 1
        self.all_sprite.draw(self.screen)
        pygame.display.flip()

    def output(self):
        if self.n != -2:
            self.image_ = self.image_skins[self.skins]
            self.image_button_skins = self.image_button[self.image_but]
            if self.n == 1 or self.n == -1:
                Switchskins(self.screen).skins_per(self.image_)
                Switchskins(self.screen).purchase_button(self.image_button_skins)
                self.n = 0
            else:
                if self.button_choose__[self.skins] == 2:
                    self.price = ""
                    if self.skins == 1 or self.skins == -3:
                        self.price = self.skins_price[0]
                    if self.skins == 2 or self.skins == -2:
                        self.price = self.skins_price[1]
                    if self.skins == 3 or self.skins == -1:
                        self.price = self.skins_price[2]
                    self.draw_text_skins(screen, str(self.price), 65)
                    Switchskins(self.screen).purchase_price(self.button_choose__[self.skins])
                Switchskins(self.screen).skins_per(self.image_)
                Switchskins(self.screen).purchase_button(self.image_button_skins)
                self.all_sprite.draw(self.screen)
            self.draw_text(screen, str(money), 65)  # рисовка счёта монет
            pygame.display.flip()

    def update(self, *args, **kwargs) -> None:
        if len(args) == 0:
            return
        event = args[0]
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.coor_sprite_back = 0 < event.pos[0] < 200 and 20 < event.pos[1] < 100
            self.coor_sprite_left = 30 < event.pos[0] < 130 and 400 < event.pos[1] < 570
            self.coor_sprite_right = 1330 < event.pos[0] < 1430 and 400 < event.pos[1] < 570
            self.button = 580 < event.pos[0] < 830 and 700 < event.pos[1] < 790
            self.button_choose = 610 < event.pos[0] < 865 and 700 < event.pos[1] < 790
            if self.coor_sprite_back:
                if clicked_sound_effects:
                    sound_click.play()
                SpritesWindow(self.screen, 'menu').draw_buttons()
                global b, c
                b = self.button_choose__
            if self.coor_sprite_left:
                if clicked_sound_effects:
                    sound_click.play()
                self.n -= 1
                if -4 < self.skins:
                    self.skins -= 1
                    self.image_but = button(self.button_choose__, self.skins)
                else:
                    self.skins = -1
                    self.image_but = button(self.button_choose__, self.skins)
            if self.coor_sprite_right:
                if clicked_sound_effects:
                    sound_click.play()
                self.n += 1
                if self.skins < 3:
                    self.skins += 1
                    self.image_but = button(self.button_choose__, self.skins)
                else:
                    self.skins = 0
                    self.image_but = button(self.button_choose__, self.skins)
            if self.button or self.button_choose:
                if clicked_sound_effects:
                    sound_click.play()
                if self.image_but == 1:
                    self.image_but = 0
                    self.button_choose__[self.skins] = self.image_but
                    global name_skins
                    name_skins = self.image_skins[self.skins]
                    for _ in range(len(self.button_choose__)):
                        if self.button_choose__[_] == 0 and _ != self.skins:
                            self.button_choose__[_] = 1
                if self.image_but == 2:
                    global money
                    if (self.skins == 1 or self.skins == -3) and money - self.skins_price[0] >= 0:
                        money -= self.skins_price[0]
                        self.image_but = 1
                    if (self.skins == 2 or self.skins == -2) and money - self.skins_price[1] >= 0:
                        money -= self.skins_price[1]
                        self.image_but = 1
                    if (self.skins == 3 or self.skins == -1) and money - self.skins_price[2] >= 0:
                        money -= self.skins_price[2]
                        self.image_but = 1
                    self.button_choose__[self.skins] = self.image_but


ice_time = pygame.USEREVENT + 1
pygame.time.set_timer(ice_time, random.randint(3000, 4500))
ice_image_list = []
player_x_y, ice_x_y = (50, 0), (0, 645)


def events(buttons_menu, game_start, player_task, game):
    """"обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if len(buttons_menu) > 0:
            for button in buttons_menu:
                button.update(event)
        if game_start:
            level = game.get_level()
            if event.type == pygame.KEYDOWN:
                if level == 1:
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_LEFT]:
                        player_task.mleft = True
                        player_task.mright = False
                    elif pressed[pygame.K_RIGHT]:
                        player_task.mright = True
                        player_task.mleft = False
                else:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        player_task.mspace = True
            else:
                player_task.mleft = False
                player_task.mright = False


snow_image = pygame.image.load("game_img/snow_run.png")


def update_screen(screen, buttons_menu, start, game, players, levels):
    global money, start_game
    """обновление экрана"""
    if start:
        level = game.get_level()
        game.draw_playing_field()
        game.draw_sublevel()
        game.draw_sprite(level)
        players[1].update()  # PlayerGame
        players[1].output()
        players[2].output()
        players[2].update()  # Bot
        if level == 1:
            score = levels[0].get_score()
            time_level = levels[0].get_time_level()
            positions = players[1].check_score(score)
            players[2].check_time()
            players[2].check_pos_player_game(positions)
            if score < 100 and time_level < 114:
                players[0].move(True)  # PlayerTask
                players[0].output()
                levels[0].draw_snows()
                levels[0].check_mobs_contact()
                levels[0].draw_score()
            levels[0].draw_time_level()
            if time_level > 114:
                if score == 100:
                    if players[2].sub_level != 3:
                        time.sleep(1)
                        levels[0].reset_score()
                        fail = players[2].failed()
                        players[2].output()
                        if fail:
                            time.sleep(1)
                            transition_figure(screen)
                            pygame.mixer.music.play()
                            SpritesWindow(screen, 'menu').draw_buttons()
                            if clicked_sound_effects:
                                sound = pygame.mixer.Sound(f'music_and_sound_effects/{game_sound[8]}')
                                sound.play()
                            money += 20
                            levels[0].time_level = 0
                            levels[0].sound_effect_level = True
                            players[1].reset()
                            players[2].reset()
                            players[0].rect.y = pygame.display.Info().current_h - 75
                            players[0].rect.x = pygame.display.Info().current_w // 2 - 450
                            start_game = False
                    else:
                        game.next_level()
                        players[1].reset()
                        players[2].reset()
                        players[0].rect.y = 650
                        players[0].rect.x = 50
                        time.sleep(1)
                        transition_figure(screen)
                else:
                    levels[0].reset_score()
                    if players[2].sub_level != 3:
                        players[2].failed()
                        players[2].output()
                    fail = players[1].failed()
                    players[1].output()
                    if fail:
                        time.sleep(1)
                        transition_figure(screen)
                        pygame.mixer.music.play()
                        SpritesWindow(screen, 'menu').draw_buttons()
                        if clicked_sound_effects:
                            sound = pygame.mixer.Sound(f'music_and_sound_effects/{game_sound[8]}')
                            sound.play()
                        money += 10
                        levels[0].time_level = 0
                        levels[0].sound_effect_level = True
                        players[1].reset()
                        players[2].reset()
                        players[0].rect.y = pygame.display.Info().current_h - 75
                        players[0].rect.x = pygame.display.Info().current_w // 2 - 450
                        start_game = False

        elif level == 2:
            score = levels[1].get_score()
            time_level = levels[1].get_time_level()
            positions = players[1].check_score(score)
            players[2].check_time()
            players[2].check_pos_player_game(positions)
            if time_level < 114 and score != 100:
                players[0].move(False)  # PlayerTask
                players[0].output()
                levels[1].draw_snows()
                levels[1].check_mobs_contact()
                levels[1].draw_score()
            levels[1].draw_time_level()
            if score == 100:
                if players[2].sub_level != 3:
                    time.sleep(1)
                    levels[1].score_reset()
                    players[2].failed()
                    players[2].output()
                time.sleep(1.5)
                transition_figure(screen)
                pygame.mixer.music.play()
                SpritesWindow(screen, 'menu').draw_buttons()
                if clicked_sound_effects:
                    sound = pygame.mixer.Sound(f'music_and_sound_effects/{game_sound[8]}')
                    sound.play()
                money += 40
                levels[1].time_level = 0
                levels[0].sound_effect_level = True
                players[1].reset()
                players[2].reset()
                players[0].rect.y = pygame.display.Info().current_h - 75
                players[0].rect.x = pygame.display.Info().current_w // 2 - 450
                start_game = False
            elif players[2].sub_level == 3:
                levels[1].score_reset()
                fail = players[1].failed()
                players[1].output()
                if fail:
                    time.sleep(1)
                    transition_figure(screen)
                    pygame.mixer.music.play()
                    SpritesWindow(screen, 'menu').draw_buttons()
                    if clicked_sound_effects:
                        sound = pygame.mixer.Sound(f'music_and_sound_effects/{game_sound[8]}')
                        sound.play()
                    money += 30
                    levels[1].time_level = 0
                    levels[0].sound_effect_level = True
                    players[1].reset()
                    players[2].reset()
                    players[0].rect.y = pygame.display.Info().current_h - 75
                    players[0].rect.x = pygame.display.Info().current_w // 2 - 450
                    start_game = False
            elif time_level >= 114:
                levels[1].score_reset()
                if players[2].sub_level != 3:
                    players[2].failed()
                    players[2].output()
                fail = players[1].failed()
                players[1].output()
                if fail:
                    time.sleep(1)
                    transition_figure(screen)
                    pygame.mixer.music.play()
                    SpritesWindow(screen, 'menu').draw_buttons()
                    if clicked_sound_effects:
                        sound = pygame.mixer.Sound(f'music_and_sound_effects/{game_sound[8]}')
                        sound.play()
                    money += 30
                    levels[1].time_level = 0
                    levels[0].sound_effect_level = True
                    players[1].reset()
                    players[2].reset()
                    players[0].rect.y = pygame.display.Info().current_h - 75
                    players[0].rect.x = pygame.display.Info().current_w // 2 - 450
                    start_game = False
    else:
        screen.blit(pygame.image.load("menu_img/layer_1.jpg"), (0, 0))
        mx, my = (random.randint(0, pygame.display.Info().current_w),
                  random.randint(0, pygame.display.Info().current_h) // 2 - 100)
        draw_particle(mx, my, 15, random.uniform(-10, 10), 2)
        update_particle(screen)
        if len(buttons_menu) > 0:
            for i in buttons_menu:
                i.output()
    pygame.display.flip()


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
list_buttons = []  # список кнопок которые надо отобразить
name_skins = "sprite_1.png"
start_game = False
game = None
snows = pygame.sprite.Group()
mobs = pygame.sprite.Group()

ice = pygame.sprite.Group()
ice_mobs = pygame.sprite.Group()

with open("score_button", "r") as sc:
    sc = sc.read().split("\n")
    im = sc[1].replace("[", "").replace("]", "").replace(",", "").split()
    money = sc[0]
    money = int(money)  # количество монет
    image_button = []
    for i in range(len(im)):
        image_button.append(int(im[i]))
    b = image_button


def run():
    pygame.init()
    pygame.display.set_caption("Эль Капитан")
    clock = pygame.time.Clock()
    SpritesWindow(screen, 'menu').draw_buttons()
    players = [PlayerTask(screen), PlayerGame(screen), Bot(screen)]
    levels = [LevelOne(snows, mobs, screen, players[0]), LevelThree(ice, ice_mobs, screen, players[0])]
    while True:
        events(list_buttons, start_game, players[0], game)
        update_screen(
            screen,
            list_buttons,
            start_game,
            game,
            players,
            levels
        )
        clock.tick(60)


if __name__ == '__main__':
    run()


