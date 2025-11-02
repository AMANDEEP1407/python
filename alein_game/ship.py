import pygame

class Ship:
    """ a class to amange the ships"""
    def __init__(self,ai_game):
        """insilize the ship and set its starting position"""
        self.screen= ai_game.screen
        self.screen_rect= ai_game.screen.get_rect()

        #load the ship and  get its rect

        self.image= pygame.image.load("F:\documents\DurrrSpaceShip.png")
        self.rect=self.image.get_rect()

        #start each new ship in bottom

        self.rect.midbottom=self.screen_rect.midbottom

    def blitme(self):
        """draw the ship at its curent location"""

        self.screen.blit(self.image,self.rect)



