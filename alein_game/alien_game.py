import sys
import pygame
from settings import Settings
from ship import Ship
class AlienIn:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()   # pygame.init() function initializes the background settings that Pygame needs to work properly 1
       
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption("alien Invasion")

        self.ship = Ship(self)
        """set bg color"""

        self.bg_color = (230,230,230)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            """Start the main loop for the game."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
           
           # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
           
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    ai=AlienIn()
    ai.run_game()
