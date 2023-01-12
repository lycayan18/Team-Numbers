import pygame
from mob import Mob
from Settings import game_sound, clicked_sound_effects


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.level = 1
        self.height_screen = pygame.display.Info().current_h
        self.width_screen = pygame.display.Info().current_w

    def get_level(self):
        return self.level

    def next_level(self):
        self.level += 1

    def draw_playing_field(self):

        """поле задания"""
        color_tasks_field = pygame.Color(55, 65, 71)
        pygame.draw.rect(self.screen, color_tasks_field, (0, 0, self.width_screen // 2, self.height_screen))
        color_tasks_field = pygame.Color(0, 0, 0)
        pygame.draw.rect(self.screen, color_tasks_field, (0, 0, self.width_screen // 2, self.height_screen), 2)

        """поле игроков"""
        self.screen.blit(pygame.image.load("game_img/channels4_profile.jpg"), (self.width_screen // 2, 0))

        """граница"""
        color_line = pygame.Color(216, 209, 70)
        pygame.draw.line(self.screen, color_line, (self.width_screen // 2, 239), (self.width_screen, 239))

    def draw_sprite(self, level):
        self.screen.blit(pygame.image.load("game_img/watch.png"), (self.width_screen // 2 + 10, 15))
        color_time = pygame.Color(216, 209, 70)
        pygame.draw.rect(self.screen, color_time, (self.width_screen // 2 + 70, 33, 120, 15), 3, border_radius=15)
        self.screen.blit(pygame.image.load("game_img/numers_players.png"), (self.width_screen // 2 + 10, 120))
        if level == 1:
            self.screen.blit(pygame.image.load("game_img/round_01.png"), (self.width_screen // 2 + 10, 80))
        elif level == 2:
            self.screen.blit(pygame.image.load("game_img/round_02.png"), (self.width_screen // 2 + 10, 80))
        else:
            self.screen.blit(pygame.image.load("game_img/round_03.png"), (self.width_screen // 2 + 10, 80))
        self.draw_sublevel()

    def draw_sublevel(self):
        cord_sublevel = [
            (1200, 600),
            (1140, 420),
        ]
        for i in cord_sublevel:
            self.screen.blit(pygame.image.load("game_img/sublevel.png"), i)
        self.screen.blit(pygame.image.load("game_img/sub_level_end.png"), (1120, 240))


class LevelOne:
    def __init__(self, snows, mobs, screen, player):
        self.snows = snows
        self.screen = screen
        self.score = 0
        self.player = player
        self.mobs = mobs
        self.time_score = 200
        self.time_level = 0

    def draw_snows(self):
        self.snows.update()
        self.snows.draw(self.screen)

    def check_mobs_contact(self):
        if pygame.sprite.spritecollide(self.player, self.mobs, True):
            # if clicked_sound_effects:
            #     sound = pygame.mixer.Sound(f"music_and_sound_effects/{game_sound[0]}")
            #     sound.play()
            if self.score > 0:
                self.score -= 5
                self.time_score = 200
                for i in range(2):
                    m = Mob()
                    self.snows.add(m)
                    self.mobs.add(m)
        else:
            self.time_score -= 1
            if self.time_score == 0:
                self.score += 5
                # if clicked_sound_effects:
                #     sound = pygame.mixer.Sound(f"music_and_sound_effects/{game_sound[2]}")
                #     sound.play()
                self.time_score = 200

    def draw_score(self):
        font = pygame.font.SysFont('bold', 50)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(text, (pygame.display.Info().current_w // 2 - 200, 20))

    def get_score(self):
        return self.score

    def score_reset(self):
        self.score = 0

    def draw_time_level(self):
        self.time_level += 1
        if round(self.time_level) < 116:
            color_time = pygame.Color(216, 209, 70)
            pygame.draw.rect(self.screen, color_time,
                             (pygame.display.Info().current_w // 2 + 73, 33, self.time_level, 15),
                             border_radius=15)

    def get_time_level(self):
        return self.time_level


