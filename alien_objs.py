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
    self.lives = 3
    self.bullet_limit = 4
    self.bullet_speed = 3
    self.bullet_width = 3
    self.bullet_height = 8
    self.bullet_color = (255, 0, 0)
    self.alien_speed = 1
    self.drop_speed = 10
    self.fleet_dir = 1

class GameStats():
  def __init__(self, config):
    self.config = config
    self.reset_stats()

  def reset_stats(self):
    self.ships_left = self.config.ship_limit

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
  def __init__(self, config, screen, ship):
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
    pygame.draw.rect(self.screen, self.color, self.rect)


class Alien(Sprite):
  def __init__(self, config, screen):
    super().__init__()
    self.screen = screen
    self.config = config
    self.image = pygame.image.load('alien.bmp')
    self.rect = self.image.get_rect()
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height
    self.x = float(self.rect.x)
    self.speed = config.speed

  def blitme(self):
    self.screen.blit(self.image, self.rect)

  def update(self):
    self.x += (self.config.alien_speed * self.config.fleet_dir)
    self.rect.x = self.x

  def check_edges(self):
    screen_rect = self.screen.get_rect()
    if self.rect.right >= screen_rect.right:
      return True
    elif self.rect.left <= 0:
      return True

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
  if event.key == pygame.K_q:
    sys.exit()
  elif event.key == pygame.K_RIGHT:
    ship.right = True
  elif event.key == pygame.K_LEFT:
    ship.left = True
  elif event.key == pygame.K_z:
    fire(config, screen, ship, bullets)


def check_keyup(config, screen, event, ship, bullets):
  if event.key == pygame.K_RIGHT:
    ship.right = False
  elif event.key == pygame.K_LEFT:
    ship.left = False


def update_screen(config, screen, ship, aliens, bullets):
  screen.fill(config.bg_color)
  ship.blitme()
  aliens.draw(screen)
  for bullet in bullets:
    bullet.draw()
  pygame.display.flip()


def update_bullets(config, screen, ship, aliens, bullets):
  bullets.update()
  

  for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
      bullets.remove(bullet)

  check_bullet_alien_collisions(config, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(config, screen, ship, aliens, bullets):
  collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

  if len(aliens) == 0:
    bullets.empty()
    create_fleet(config, screen, ship, aliens)


def fire(config, screen, ship, bullets):
  if len(bullets) < config.bullet_limit:
    new_bullet = Bullet(config, screen, ship)
    bullets.add(new_bullet)


def get_number_aliens_x(config, alien_width):
  available_space_x = config.screen_width - 2 * alien_width
  number_aliens_x = int(available_space_x / (2 * alien_width))
  return number_aliens_x


def create_alien(config, screen, aliens, alien_number, row_number):
  alien = Alien(config, screen)
  alien_width = alien.rect.width
  alien.x = alien_width + 2 * alien_width * alien_number  
  alien.rect.x = alien.x
  alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
  aliens.add(alien)


def get_number_rows(config, ship_height, alien_height):
  available_space_y = (config.screen_height -\
    (3 * alien_height) - ship_height)
  number_rows = int(available_space_y / (2 * alien_height))
  return number_rows


def create_fleet(config, screen, ship, aliens):
  alien = Alien(config, screen)
  number_aliens_x = get_number_aliens_x(config, alien.rect.width)
  number_rows = get_number_rows\
    (config, ship.rect.height, alien.rect.height)

  for row_number in range(number_rows):
    for alien_number in range(number_aliens_x):
      create_alien(config, screen, aliens, alien_number, row_number)


def check_fleet_edges(config, aliens):
  for alien in aliens.sprites():
    if alien.check_edges():
      change_dir(config, aliens)
      break


def change_dir(config, aliens):
  for alien in aliens.sprites():
    alien.rect.y += config.drop_speed

  config.fleet_dir *= -1


def update_aliens(config, ship, aliens):
  check_fleet_edges(config, aliens)
  aliens.update()

  if pygame.sprite.spritecollideany(ship, aliens):

