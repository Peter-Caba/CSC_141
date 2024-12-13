import pygame
from settings import Settings


class Jaws:

    def __init__(self, ai_game):
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()

        self.image = pygame.image.load("images/Jaws.pmg")
        self.rect = self.image.get_rect()
        
        self.rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.speed = 5  

    def blitme(self):
        
        self.screen.blit(self.image, self.rect)

    def update(self):
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
