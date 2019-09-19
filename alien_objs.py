import sys, time, pygame
from pygame import *

class Settings():
  def __init__(self):
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230, 230, 230)

class Ship():
  def __init__(self, screen):
    """Initialize the ship and set its starting position."""
    self.screen = screen
    # Load the ship image and get its rect.
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    # Start each new ship at the bottom center of the screen.
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom
  def blitme(self):
    """Draw the ship at its current location."""
    self.screen.blit(self.image, self.rect)