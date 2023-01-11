import pygame

pygame.init()
# pygame.mixer.music.load("music_and_sound_effects/music_menu.mp3")
# pygame.mixer.music.play(-1)
sound_click = pygame.mixer.Sound('music_and_sound_effects/SoundClick.ogg')
sound_hover = pygame.mixer.Sound('music_and_sound_effects/Sound1.ogg')
game_sound = ["uuff.mp3", "sound_pop.mp3", "sound_score+.mp3"]
clicked_music = True
clicked_sound_effects = True


class Music(pygame.sprite.Sprite):
    def __init__(self, screen):
        global clicked_music
        super(Music, self).__init__()
        self.screen = screen
        if clicked_music:
            self.img_name = 'music_2.png'
        else:
            self.img_name = 'music.png'
        self.img = pygame.image.load(f"menu_img/{self.img_name}")
        self.rect = self.img.get_rect()
        self.rect.x = 500
        self.rect.y = 450

    def output(self):
        global sound_click, clicked_music
        if clicked_music:
            self.screen.blit(self.img, self.rect)
            pygame.mixer.music.unpause()
        else:
            self.screen.blit(self.img, self.rect)
            pygame.mixer.music.pause()

    def update(self, *args, **kwargs) -> None:
        global sound_click, clicked_music
        if len(args) == 0:
            return
        event = args[0]
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            sound_click.play()
            if clicked_music:
                self.img_name = 'music.png'
                clicked_music = False
            else:
                self.img_name = 'music_2.png'
                clicked_music = True
            self.img = pygame.image.load(f"menu_img/{self.img_name}")


class SoundEffects(pygame.sprite.Sprite):
    def __init__(self, screen):
        global clicked_sound_effects
        super(SoundEffects, self).__init__()
        self.screen = screen
        if clicked_sound_effects:
            self.img_name = 'sound_effect_2.png'
        else:
            self.img_name = 'sound_effect.png'
        self.img = pygame.image.load(f"menu_img/{self.img_name}")
        self.sound_click = pygame.mixer.Sound('music_and_sound_effects/SoundClick.ogg')
        self.sound1 = pygame.mixer.Sound('music_and_sound_effects/Sound1.ogg')
        self.clicked = True
        self.rect = self.img.get_rect()
        self.rect.x = 500
        self.rect.y = 550

    def output(self):
        global sound_click, clicked_sound_effects
        if clicked_sound_effects:
            self.screen.blit(self.img, self.rect)
            sound_click.set_volume(1)
            sound_hover.set_volume(1)
        else:
            self.screen.blit(self.img, self.rect)
            sound_click.set_volume(0)
            sound_hover.set_volume(0)

    def update(self, *args, **kwargs) -> None:
        global sound_click, clicked_sound_effects
        if len(args) == 0:
            return
        event = args[0]
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            sound_click.play()
            if clicked_sound_effects:
                self.img_name = 'sound_effect.png'
                clicked_sound_effects = False
            else:
                self.img_name = 'sound_effect_2.png'
                clicked_sound_effects = True
            self.img = pygame.image.load(f"menu_img/{self.img_name}")





