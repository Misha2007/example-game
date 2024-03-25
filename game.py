# Simple pygame programm

import pygame
from settings import Settings
from player import Player
import game_functions as gf


def run_game():
    pygame.init()
    gm_settings = Settings()

    # Set up the drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)

    # Set up clock to decent frame rate
    clock = pygame.time.Clock()

    #Instantiate player
    player = Player(screen)

    #Create group to hold bubbles
    bubbles = pygame.sprite.Group()

    # Run until the user asks ti quit
    running = True
    while running:
        gf.check_events(gm_settings, screen, player, bubbles)
        player.update()
        gf.update_bubbles(player, bubbles)
        bubbles.update()
        gf.update_screen(gm_settings, screen, player, bubbles, clock)

run_game()