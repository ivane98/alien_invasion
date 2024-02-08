import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load(r'images\ship.bmp')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.rect.midbottom = self.screen_rect.midbottom
        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        

        self.rect.x = self.x
        

    def blitme(self):
        self.screen.blit(self.image, self.rect)

