import pygame
import sys


def events(screen, buttons_menu):
    """"обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if len(buttons_menu) > 0:
            for i in buttons_menu:
                i.update(event)


def update_screen(screen, background_menu, buttons_menu):
    """обновление экрана"""
    screen.blit(background_menu, (0, 0))
    if len(buttons_menu) > 0:
        for i in buttons_menu:
            i.output()
    pygame.display.flip()


def button(button_choose__, skins):
    image_but = 0
    if button_choose__[skins] == 2:
        image_but = 2
    if button_choose__[skins] == 1:
        image_but = 1
    if button_choose__[skins] == 0:
        image_but = 0
    return image_but
