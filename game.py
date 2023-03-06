# import sys
# sys.path.insert(0, '../python_battle_files')

# import type_adv

# type_adv.grass_check()

# example.my_function()


import pygame
from button import Button
import random as r

from battle_loop import *

# general comment
## tag comment for Ctrl + F

## available tags: screen_config clock time rectangle_config rect_placement color_variables images image_load button_config game_loop key_input input


def enemy_pokemon_choice():
    enemy_choice = r.randint(1, 3)
    print(enemy_choice)
    if enemy_choice == 1:
        return "charizard"
    if enemy_choice == 2:
        return "venusaur"
    if enemy_choice == 3:
        return "blastoise"


def load_image_charizard(is_player_mon):
    image = pygame.image.load("images/charizard.png")

    if is_player_mon:
        # TODO: mess around with positions to get this to change according to the player specifically.
        image = pygame.transform.flip(image, True, False)

    # Get the rectangle representing the loaded image
    ## image_load

    charizard_image = image.get_rect()
    return image, charizard_image


def load_image_venusaur(is_player_mon):
    image = pygame.image.load("images/venusaur.png")

    if is_player_mon:
        # TODO: mess around with positions to get this to change according to the player specifically.
        image = pygame.transform.flip(image, True, False)

    # Get the rectangle representing the loaded image
    ## image_load

    venusaur_image = image.get_rect()
    return image, venusaur_image


def load_image_blastoise(is_player_mon):
    image = pygame.image.load("images/blastoise.png")

    if is_player_mon:
        # TODO: mess around with positions to get this to change according to the player specifically.
        image = pygame.transform.flip(image, True, False)

    # Get the rectangle representing the loaded image
    blastoise_rect = image.get_rect()
    return image, blastoise_rect


def game_loop():
    # Initialize Pygame
    ## init
    pygame.init()

    # Set up the screen
    ## screen_config

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My Pygame")

    # Set up the clock
    ## clock time
    clock = pygame.time.Clock()

    # Set up the rectangle
    ## rectangle_config rect_placement

    rect_color = (0, 0, 0)
    rect_width = 750
    rect_height = 175
    rect_position = (
        screen_width / 2 - rect_width / 2,
        (screen_height - rect_height) - 20,
    )
    rect_thickness = 2

    ## color_variables
    red_color = (255, 0, 0)
    green_color = (0, 255, 0)
    black_color = (0, 0, 0)
    white_color = (255, 255, 255)

    # Chooses pokemon for enemy
    player_pokemon_choice = 2
    enemy_pokemon = enemy_pokemon_choice()

    # TODO: fix dupe clause
    dupe_clause = False

    if enemy_pokemon == player_pokemon_choice:
        if enemy_pokemon == 1:
            enemy_duplicate = load_image_charizard(False)
            dupe_clause = True
        if enemy_pokemon == 2:
            enemy_duplicate = load_image_venusaur(False)
            dupe_clause = True
        if enemy_pokemon == 3:
            enemy_duplicate = load_image_blastoise(False)
            dupe_clause = True

    # Load an image from disk
    ## images image_load

    images = {1: load_image_charizard, 2: load_image_venusaur, 3: load_image_blastoise}

    charizard_image = images.get(1)(player_pokemon_choice == 1)
    venusaur_image = images.get(2)(player_pokemon_choice == 2)
    blastoise_image = images.get(3)(player_pokemon_choice == 3)

    # Extract the rect object from the tuple and assign its bottom attribute
    charizard_rect = charizard_image[1]
    charizard_surface = charizard_image[0]

    # Extract the rect object from the tuple and assign its bottom attribute
    venusaur_rect = venusaur_image[1]
    venusaur_surface = venusaur_image[0]

    # Extract the rect object from the tuple and assign its bottom attribute
    blastoise_rect = blastoise_image[1]
    blastoise_surface = blastoise_image[0]

    if dupe_clause:
        enemy_rect = enemy_duplicate[1]
        enemy_surface = enemy_duplicate[0]

    if player_pokemon_choice == 1:
        player_pokemon_image = charizard_rect
        player_pokemon_surface = charizard_surface
    elif player_pokemon_choice == 2:
        player_pokemon_image = venusaur_rect
        player_pokemon_surface = venusaur_surface
    elif player_pokemon_choice == 3:
        player_pokemon_image = blastoise_rect
        player_pokemon_surface = blastoise_surface

    if enemy_pokemon == "charizard":
        enemy_pokemon_image = charizard_rect
        enemy_pokemon_surface = charizard_surface
    elif enemy_pokemon == "venusaur":
        enemy_pokemon_image = venusaur_rect
        enemy_pokemon_surface = venusaur_surface
    elif enemy_pokemon == "blastoise":
        enemy_pokemon_image = blastoise_rect
        enemy_pokemon_surface = blastoise_surface

    if dupe_clause:
        enemy_pokemon_image = enemy_rect
        enemy_pokemon_surface = enemy_surface

    # Set the position of each image using the Rect attributes
    enemy_position_x = 450
    enemy_position_y = 25
    player_position_x = 75
    player_position_y = 200

    enemy_pokemon_image.left = enemy_position_x
    enemy_pokemon_image.top = enemy_position_y

    player_pokemon_image.left = player_position_x
    player_pokemon_image.top = player_position_y

    # Set up the buttons
    ## button_config
    button_width = 200
    button_height = 50
    button_margin = 20
    button1 = Button(
        (screen_width / 4 - button_width / 4) - 100,
        screen_height / 1.205 - button_height - button_margin,
        button_width,
        button_height,
        "Button 1",
        white_color,
        black_color,
    )
    button2 = Button(
        (screen_width / 4 - button_width / 4) - 100,
        screen_height / 1.205 + button_margin,
        button_width,
        button_height,
        "Button 2",
        white_color,
        black_color,
    )
    button3 = Button(
        (screen_width / 2 - button_width / 2),
        screen_height / 1.205 - button_height - button_margin,
        button_width,
        button_height,
        "Button 3",
        white_color,
        black_color,
    )
    button4 = Button(
        (screen_width / 2 - button_width / 2),
        screen_height / 1.205 + button_margin,
        button_width,
        button_height,
        "Button 4",
        white_color,
        black_color,
    )

    buttons = [button1, button2, button3, button4]
    selected_button_index = 0

    # Main game loop
    ## game_loop

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            ## key_input input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Handle up arrow key press
                    selected_button_index = (selected_button_index - 1) % len(buttons)
                elif event.key == pygame.K_DOWN:
                    # Handle down arrow key press
                    selected_button_index = (selected_button_index + 1) % len(buttons)
                elif event.key == pygame.K_LEFT:
                    # Handle left arrow key press
                    pass
                elif event.key == pygame.K_RIGHT:
                    # Handle right arrow key press
                    pass
                elif event.key == pygame.K_RETURN:
                    # Handle enter key press
                    if buttons[selected_button_index] == button1:
                        print("Button 1 pressed!")
                    if buttons[selected_button_index] == button2:
                        print("Button 2 pressed!")
                    if buttons[selected_button_index] == button3:
                        print("Button 3 pressed!")
                    if buttons[selected_button_index] == button4:
                        print("Button 4 pressed!")

        # Update game state
        ## update_loops
        for i, button in enumerate(buttons):
            button.selected = i == selected_button_index

        # Draw on the screen
        screen.fill((255, 255, 255))
        rect = pygame.draw.rect(
            screen,
            rect_color,
            (rect_position, (rect_width, rect_height)),
            rect_thickness,
        )

        player_pokemon_image.bottom = rect.top - 10

        # Draw the image on the screen
        screen.blit(enemy_pokemon_surface, enemy_pokemon_image)
        screen.blit(player_pokemon_surface, player_pokemon_image)
        # screen.blit(image3, image_rect3)

        for button in buttons:
            button.draw(screen)

        # Update the screen
        pygame.display.update()

        # Set the FPS
        clock.tick(60)
