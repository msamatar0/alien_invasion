import sys, time, pygame
from pygame import *
from alien_objs import *

config = Settings()


def run_game():
  pygame.init()
  screen = pygame.display.set_mode\
    ((config.screen_width, config.screen_height))
  pygame.display.set_caption("Alien Invasion!")

  ship = Ship(screen)
  

  while True:
    check_events(ship)
    ship.update()
    update_screen(config, screen, ship)

run_game()