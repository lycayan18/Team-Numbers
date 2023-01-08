import pygame
import sys
import random


def events(screen, sprites_list, game_start, player_task):
    """"обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if len(sprites_list) > 0:
            for i in sprites_list:
                i.update(event)
        if game_start:
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_LEFT]:
                    player_task.mleft = True
                    player_task.mright = False
                elif pressed[pygame.K_RIGHT]:
                    player_task.mright = True
                    player_task.mleft = False
            else:
                player_task.mleft = False
                player_task.mright = False


def update_screen(screen, background_menu, buttons_menu, start_game, game, players, levels):
    """обновление экрана"""
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
                    transition_figure(screen)
                else:
                    levels[0].score_reset()
                    players[1].failed()
                    players[1].output()
    else:
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


def loading(screen, background):
    manual = ["game_img/manual_1.jpg"]
    image = pygame.image.load(random.choice(manual))
    image = pygame.transform.scale(image, (pygame.display.Info().current_w, pygame.display.Info().current_h))
    h = pygame.display.Info().current_h
    w = pygame.display.Info().current_w
    percentages = 0
    screen.blit(image, (0, 0))
    while round(percentages) < 1500:
        pygame.draw.rect(screen, (255, 255, 255), (10, h - 20, w - 10, 20), 2)
        pygame.draw.rect(screen, (255, 255, 255), (10, h - 21, int(percentages), 19))
        percentages += 50 / 60
        pygame.display.flip()


def transition_figure(screen):
    h = pygame.display.Info().current_h
    w = pygame.display.Info().current_w
    radius = 0
    while round(radius) < 1500:
        pygame.draw.circle(screen, pygame.Color("#000000"), (w // 2, h // 2), radius)
        radius += 900 / 60
        pygame.display.flip()
