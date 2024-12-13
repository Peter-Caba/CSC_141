import sys

import pygame

from ex1 import Settings
from ex1 import Jaws

class AlienInvasion:

    def __init__(self):

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.Jaws = Jaws(self)

        self.bg_color = self.setting.bg_color
    
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.Jaws.blitme()
        #self.ship.blitme()

        pygame.display.flip()

if __name__ == '_main_':
    ai = AlienInvasion()  
    ai.run_game()
