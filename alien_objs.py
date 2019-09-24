import sys, time, pygame
from pygame import *

class Settings():
  def __init__(self):
    self.screen_width = 900
    self.screen_height = 600
    self.bg_color = (230, 230, 230)

class Ship():
  def __init__(self, screen):
    self.screen = screen
    self.image = pygame.image.load('ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom
    self.right = False
    self.left = False

  def update(self):
    if self.right:
      self.rect.centerx += 1
    elif self.left:
      self.rect.centerx -= 1

    if self.rect.x < 0:
      self.rect.x = 0
    elif self.rect.x > 900 - self.image.get_size()[0]:
      self.rect.x = 900 - self.image.get_size()[0]

  def blitme(self):
    self.screen.blit(self.image, self.rect)

def check_events(ship):
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          ship.right = True
        if event.key == pygame.K_LEFT:
          ship.left = True
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
          ship.right = False
        if event.key == pygame.K_LEFT:
          ship.left = False

def update_screen(config, screen, ship):
  screen.fill(config.bg_color)
  ship.blitme()
  pygame.display.flip()