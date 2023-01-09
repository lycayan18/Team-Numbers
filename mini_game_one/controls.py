import pygame
import random


def loading(screen):
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
    while round(radius) < 2500:
        pygame.draw.circle(screen, pygame.Color("#000000"), (w // 2, h // 2), radius)
        radius += 700 / 60
        pygame.display.flip()
