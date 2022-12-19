import pygame
import sys
from controls import events, update_screen
from background_menu_anim import BACKGOUND_MENU


class ButtonsMenu:
    def __init__(self, screen, command):
        self.command = command
        self.screen = screen

    def draw_buttons(self):
        global list_buttons
        if self.command == 'menu':
            """главное меню"""
            list_buttons = [
                ButtonStartGame(self.screen), ButtonShop(self.screen),
                ButtonSettings(self.screen), ButtonExit(self.screen)
            ]
        elif self.command == 'start_game':
            """игра"""
            pass
        elif self.command == 'settings':
            """настройки"""
            list_buttons = [BackButton(self.screen)]
        elif self.command == 'shop':
            """магазин"""
            list_buttons = [BackButton(self.screen)]


class ButtonStartGame(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(ButtonStartGame, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("menu_img/Начать игру_.png")
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
            ButtonsMenu(self.screen, 'start_game').draw_buttons()
        if event.type == pygame.MOUSEMOTION and self.rect.collidepoint(event.pos):
            self.img = pygame.transform.scale(self.img, (388, 76))
        else:
            self.img = pygame.image.load("menu_img/Начать игру_.png")


class ButtonSettings(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(ButtonSettings, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("menu_img/Настройки.png")
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
            ButtonsMenu(self.screen, 'settings').draw_buttons()
        if event.type == pygame.MOUSEMOTION and self.rect.collidepoint(event.pos):
            self.img = pygame.transform.smoothscale(self.img, (355, 85))
        else:
            self.img = pygame.image.load("menu_img/Настройки.png")


class ButtonShop(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(ButtonShop, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("menu_img/Магазин.png")
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
            ButtonsMenu(self.screen, 'shop').draw_buttons()
        if event.type == pygame.MOUSEMOTION and self.rect.collidepoint(event.pos):
            self.img = pygame.transform.smoothscale(self.img, (280, 70))
        else:
            self.img = pygame.image.load("menu_img/Магазин.png")


class ButtonExit(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(ButtonExit, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("menu_img/Выход.png")
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
            self.img = pygame.image.load("menu_img/Выход.png")


class BackButton(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(BackButton, self).__init__()
        self.screen = screen
        self.img = pygame.image.load("menu_img/Назад.png")
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
            ButtonsMenu(self.screen, 'menu').draw_buttons()


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
list_buttons = []  # список кнопок которые надо отобразить


def run():
    pygame.init()
    pygame.display.set_caption("Эль Капитан")
    clock = pygame.time.Clock()
    background_menu_anim_count = 0
    ButtonsMenu(screen, 'menu').draw_buttons()
    while True:
        events(screen, list_buttons)
        update_screen(
            screen,
            pygame.image.load(f'menu_img/background_menu_anim/{BACKGOUND_MENU[background_menu_anim_count]}'),
            list_buttons
        )
        if background_menu_anim_count == 337:
            background_menu_anim_count = 0
        else:
            background_menu_anim_count += 1
        clock.tick(40)


if __name__ == '__main__':
    run()
