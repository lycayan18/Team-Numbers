import pygame

pygame.init()
pygame.mixer.music.load("music_and_sound_effects/music_menu.mp3")
pygame.mixer.music.play(-1)
sound_click = pygame.mixer.Sound('music_and_sound_effects/SoundClick.ogg')
sound_hover = pygame.mixer.Sound('music_and_sound_effects/Sound1.ogg')
clicked_music = True
clicked_sound_effects = True
run = True
game_sound = ["sound_application_ points.mp3",
              "sound_transition_new_sublevel.mp3",
              "sound_score+.mp3",
              "sound_impact.mp3",
              "sound_alarm.mp3",
              "sound _boxing _gong.mp3",
              "game_over.mp3",
              "sound_victory.mp3",
              "coins.mp3"]


class Settings:
    def __init__(self, screen):
        self.screen = screen
        if clicked_music:
            self.img_name1 = 'music_2.png'

        else:
            self.img_name1 = 'music.png'

        if clicked_sound_effects:
            self.img_name2 = 'sound_effect_2.png'

        else:
            self.img_name2 = 'sound_effect.png'

        self.img1 = pygame.image.load(f"menu_img/{self.img_name1}")
        self.rect1 = self.img1.get_rect()
        self.rect1.x = 500
        self.rect1.y = 450
        self.img2 = pygame.image.load(f"menu_img/{self.img_name2}")
        self.rect2 = self.img2.get_rect()
        self.rect2.x = 500
        self.rect2.y = 550
        self.m = Music(screen)
        self.s = SoundEffect(screen)

    def update(self, *args, **kwargs) -> None:
        global run
        if len(args) == 0:
            return
        event = args[0]
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect1.collidepoint(event.pos):
            sound_click.play()
            self.m.run()

        if event.type == pygame.MOUSEBUTTONDOWN and self.rect2.collidepoint(event.pos):
            sound_click.play()
            self.s.run()

    def output(self):
        global clicked_music, clicked_sound_effects
        if clicked_music:
            self.img_name1 = 'music_2.png'
            self.screen.blit(self.img1, self.rect1)
        else:
            self.img_name1 = 'music.png'
            self.screen.blit(self.img1, self.rect1)
        if clicked_sound_effects:
            self.img_name2 = 'sound_effect_2.png'
            self.screen.blit(self.img2, self.rect2)
        else:
            self.img_name2 = 'sound_effect.png'
            self.screen.blit(self.img2, self.rect2)
        self.img1 = pygame.image.load(f"menu_img/{self.img_name1}")
        self.img2 = pygame.image.load(f"menu_img/{self.img_name2}")
        pygame.display.flip()


class Music:
    def __init__(self, screen):
        global clicked_music
        self.screen = screen
        if clicked_music:
            self.img_name = 'music_2.png'
        else:
            self.img_name = 'music.png'
        self.img = pygame.image.load(f"menu_img/{self.img_name}")
        self.rect1 = self.img.get_rect()
        self.rect1.x = 500
        self.rect1.y = 450

    @staticmethod
    def run():
        global sound_click, clicked_music, run
        if clicked_music:
            pygame.mixer.music.pause()
            clicked_music = False
        else:
            pygame.mixer.music.unpause()
            clicked_music = True


class SoundEffect:
    def __init__(self, screen):
        global clicked_music
        self.screen = screen
        if clicked_sound_effects:
            self.img_name = 'sound_effect_2.png'
        else:
            self.img_name = 'sound_effect.png'
        self.img = pygame.image.load(f"menu_img/{self.img_name}")
        self.rect = self.img.get_rect()
        self.rect.x = 500
        self.rect.y = 550

    @staticmethod
    def run():
        global sound_click, clicked_sound_effects, run
        if clicked_sound_effects:
            sound_click.set_volume(0)
            sound_hover.set_volume(0)
            clicked_sound_effects = False
        else:
            sound_click.set_volume(1)
            sound_hover.set_volume(1)
            clicked_sound_effects = True

#
# if __name__ == '__main__':
#     screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#     s = Settings(screen)
#     while run:
#         screen.fill((0, 0, 0))
#         s.output()

