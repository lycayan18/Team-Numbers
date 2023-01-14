import pygame
import random

particles = []


def draw_particle(x, y, x_vel, y_vel, radius):
    particles.append([[x, y], [x_vel, y_vel], radius])


def update_particle(screen):
    for i, particle in reversed(list(enumerate(particles))):
        particle[0][0] += 2
        particle[0][1] += 2
        particle[2] -= 0.1

        revers_particle = particles[len(particles) - i - 1]
        pygame.draw.circle(screen, (255, 255, 255), (int(revers_particle[0][0]), int(revers_particle[0][1])),
                           revers_particle[2])

        if particle[2] <= 0:
            particles.pop(i)


def loading(screen):
    manual = ["game_img/manual_1.jpg", "game_img/manual_2.jpg", "game_img/manual_3.jpg"]
    image = pygame.image.load(random.choice(manual))
    image = pygame.transform.scale(image, (pygame.display.Info().current_w, pygame.display.Info().current_h))
    h = pygame.display.Info().current_h
    w = pygame.display.Info().current_w
    percentages = 0
    screen.blit(image, (0, 0))
    while round(percentages) < 1500:
        pygame.draw.rect(screen, (255, 255, 255), (10, h - 20, w - 10, 20), 2)
        pygame.draw.rect(screen, (255, 255, 255), (10, h - 21, int(percentages), 19))
        percentages += 80 / 60
        pygame.display.flip()


def transition_figure(screen):
    h = pygame.display.Info().current_h
    w = pygame.display.Info().current_w
    radius = 0
    while round(radius) < 2500:
        pygame.draw.circle(screen, pygame.Color("#000000"), (w // 2, h // 2), radius)
        radius += 1000 / 60
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
