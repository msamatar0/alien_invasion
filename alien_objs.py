import sys, time, pygame
from pygame import *
from pygame.sprite import Sprite

#Game Objects
class Settings():
  def __init__(self):
    self.screen_width = 900
    self.screen_height = 600
    self.bg_color = (230, 230, 230)
    self.speed = .7
    self.bullet_speed = 1
    self.bullet_width = 3
    self.bullet_height = 8
    self.bullet_color = (255, 0, 0)

class Ship():
  def __init__(self, screen, config):
    self.screen = screen
    self.config = config
    self.image = pygame.image.load('ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom
    self.center = float(self.rect.centerx)
    self.right = False
    self.left = False

  def update(self):
    if self.right and self.rect.right < self.screen_rect.right:
      self.center += self.config.speed
    if self.left and self.rect.left > 0:
      self.center -= self.config.speed

    self.rect.centerx = self.center
    
  def blitme(self):
    self.screen.blit(self.image, self.rect)

class Bullet(Sprite):
  def __init__(self, screen, config, ship):
    super().__init__()
    self.screen = screen
    self.rect = pygame.Rect\
      (0, 0, config.bullet_width, config.bullet_height)
    self.rect.centerx = ship.rect.centerx
    self.rect.top = ship.rect.top
    self.y = float(self.rect.y)
    self.color = config.bullet_color
    self.speed = config.bullet_speed

  def update(self):
    self.y -= self.speed
    self.rect.y = self.y

  def draw(self):
    pygame.draw.rect(screen, color, rect)

#Game Functions

def check_events(config, screen, ship, bullets):
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

      elif event.type == pygame.KEYDOWN:
        check_keydown(config, screen, event, ship, bullets)
      elif event.type == pygame.KEYUP:
        check_keyup(config, screen, event, ship, bullets)
  
def check_keydown(config, screen, event, ship, bullets):
  if event.key == pygame.K_RIGHT:
    ship.right = True
  elif event.key == pygame.K_LEFT:
    ship.left = True
  elif event.key == pygame.K_z:
    new_bullet = Bullet(config, screen, ship)
    bullets.add(new_bullet)

def check_keyup(config, screen, event, ship, bullets):
  if event.key == pygame.K_RIGHT:
    ship.right = False
  elif event.key == pygame.K_LEFT:
    ship.left = False

def update_screen(config, screen, ship, bullets):
  screen.fill(config.bg_color)
  ship.blitme()
  for bullet in bullets:
    bullet.draw()
  pygame.display.flip()
