import sys, time, pygame
from pygame import *
from alien_objs import *

config = Settings()


def run_game():
  pygame.init()
  screen = pygame.display.set_mode((config.screen_width, config.screen_height))
  pygame.display.set_caption("Alien Invasion!")

  while True:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    screen.fill(config.bg_color)
    pygame.display.flip()

run_game()