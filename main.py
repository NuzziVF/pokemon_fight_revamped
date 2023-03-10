import pygame
from game import *


# Initialize Pygame
pygame.init()

selection = menu()
if selection == "start_game":
    # Call game loop
    selector = pokemon_selector().lower()
    game_loop(selector)
