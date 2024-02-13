import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load(r'images\ship.bmp')
        self.rect = self.image.get_rect()
        self.move_right = False
        self.move_left = False

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed
        elif self.move_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed
                    
        self.rect.centerx = self.center
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
