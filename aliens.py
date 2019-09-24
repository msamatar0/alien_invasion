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

  ship = Ship(screen, config)
  bullets = Group()


  while True:
    check_events(config, screen, ship, bullets)
    ship.update()
    bullets.update()
    update_screen(config, screen, ship, bullets)

run_game()
