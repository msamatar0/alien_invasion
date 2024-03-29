import sys, time, pygame
from pygame import *
from pygame.sprite import Group
from alien_objs import *

config = Settings()

def run_game():
  pygame.init()
  screen = pygame.display.set_mode\
    ((config.screen_width, config.screen_height))
  pygame.display.set_caption("Alien Invasion!")

  stats = GameStats(config)
  ship = Ship(screen, config)
  bullets = Group()
  aliens = Group()

  create_fleet(config, screen, ship, aliens)

  while True:
    check_events(config, screen, ship, bullets)
    ship.update()
    update_bullets\
      (config, screen, ship, aliens, bullets)
    update_aliens(config, ship, aliens)
    update_screen\
      (config, screen, ship, aliens, bullets)

run_game()
