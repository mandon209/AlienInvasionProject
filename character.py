import pygame

class Character:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the Character
        self.image = pygame.image.load('Alien_Invasion/images/tanjiro.bmp')
        self.rect = self.image.get_rect()

        #Start Character in center of screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship and character at its current location."""
        self.screen.blit(self.image, self.rect)