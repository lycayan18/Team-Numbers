import pygame
import sys


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


def button(button_choose__, skins):
    image_but = 0
    if button_choose__[skins] == 2:
        image_but = 2
    if button_choose__[skins] == 1:
        image_but = 1
    if button_choose__[skins] == 0:
        image_but = 0
    return image_but
