import pygame


class Switchskins(pygame.sprite.Sprite):  # рисовка спрайтов, и счётчик монет
    def __init__(self, screen):
        super().__init__()
        self.game_skins = [
            "game_img/sprite_1.png", "game_img/sprite_2.png", "game_img/sprite_3.png", "game_img/sprite_4.png"
        ]
        self.image_skins = [
             "menu_img/sprite_1.png", "menu_img/sprite_2.png", "menu_img/sprite_3.png", "menu_img/sprite_4.png"
        ]
        self.image_button = ["menu_img/Selected.png", "menu_img/Choose.png", "menu_img/Buy.png"]
        self.screen = screen
        self.all_sprite = pygame.sprite.Group()
        self.len_text = 1
        self.x, self.y = 1270, 50
        self.font_name = pygame.font.match_font('arial')
        self.left()
        self.right()
        self.money()
        self.back()

    def skins_per(self, im):
        self.image_ = im
        self.sprite_skins_per = pygame.sprite.Sprite(self.all_sprite)
        self.sprite_skins_per.image = pygame.image.load(self.image_)
        self.sprite_skins_per.rect = self.sprite_skins_per.image.get_rect()
        self.sprite_skins_per.rect.x = 650
        self.sprite_skins_per.rect.y = 400
        self.all_sprite.draw(self.screen)

    def back(self):
        self.sprite_back = pygame.sprite.Sprite(self.all_sprite)
        self.sprite_back.image = pygame.image.load("menu_img/Back.png")
        self.sprite_back.rect = self.sprite_back.image.get_rect()
        self.sprite_back.rect.x = 30
        self.sprite_back.rect.y = 40

    def right(self):
        self.sprite_right = pygame.sprite.Sprite(self.all_sprite)
        self.sprite_right.image = pygame.image.load("menu_img/Arrow_right.png")
        self.sprite_right.rect = self.sprite_right.image.get_rect()
        self.sprite_right.rect.x = 1300
        self.sprite_right.rect.y = 400

    def left(self):
        self.sprite_left = pygame.sprite.Sprite(self.all_sprite)
        self.sprite_left.image = pygame.image.load("menu_img/Arrow_left.png")
        self.sprite_left.rect = self.sprite_left.image.get_rect()
        self.sprite_left.rect.x = -3
        self.sprite_left.rect.y = 400

    def money(self):
        self.sprite_money = pygame.sprite.Sprite(self.all_sprite)
        self.sprite_money.image = pygame.image.load("menu_img/m.png")
        self.sprite_money.rect = self.sprite_money.image.get_rect()
        self.sprite_money.rect.x = 1300
        self.sprite_money.rect.y = 40

    def draw_text(self, surf, text, size):
        if self.len_text != len(text):
            self.x -= 14
            self.len_text += 1
        if self.len_text > len(text):
            self.len_text = len(text)
        self.font = pygame.font.Font(self.font_name, size)
        self.text_surface = self.font.render(text, True, pygame.color.Color("#ffffff"))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (self.x, self.y)
        surf.blit(self.text_surface, self.text_rect)

    def purchase_button(self, image_but):
        self.sprite_skins_pe = pygame.sprite.Sprite(self.all_sprite)
        self.sprite_skins_pe.image = pygame.image.load(image_but)
        self.sprite_skins_pe.rect = self.sprite_skins_pe.image.get_rect()
        if image_but == "menu_img/Choose.png":
            self.sprite_skins_pe.rect.x = 580
            self.sprite_skins_pe.rect.y = 680
        else:
            self.sprite_skins_pe.rect.x = 620
            self.sprite_skins_pe.rect.y = 700
        self.all_sprite.draw(self.screen)

    def purchase_price(self, index_skin):
        self.index_skin = index_skin
        self.sprite_purchase_price = pygame.sprite.Sprite(self.all_sprite)
        self.sprite_purchase_price.image = pygame.image.load("menu_img/m.png")
        self.sprite_purchase_price.rect = self.sprite_purchase_price.image.get_rect()
        self.sprite_purchase_price.rect.x = 950
        self.sprite_purchase_price.rect.y = 700
        self.all_sprite.draw(self.screen)

    def draw_text_skins(self, surf, text, size):
        self.font = pygame.font.Font(self.font_name, size)
        self.text_surface = self.font.render(text, True, pygame.color.Color("#ffffff"))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (930, 720)
        surf.blit(self.text_surface, self.text_rect)
