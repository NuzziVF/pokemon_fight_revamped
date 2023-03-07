# import sys
# sys.path.insert(0, '../python_battle_files')

# import type_adv

# type_adv.grass_check()

# example.my_function()


import pygame
from poke_functions.button import Button
import random as r

from poke_functions.functions_file import Pokemon
from battle_loop import battle_loop_main

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


def load_image_magikarp(is_player_mon):
    image = pygame.image.load("images/magikarp.png")

    if is_player_mon:
        # TODO: mess around with positions to get this to change according to the player specifically.
        image = pygame.transform.flip(image, True, False)

    # Get the rectangle representing the loaded image
    magikarp_rect = image.get_rect()
    return image, magikarp_rect


def game_loop():
    # Initialize Pygame
    ## init
    pygame.init()

    # Set up the screen
    ## screen_config

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pokemon Fight Revamped")

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

    # Setting up pokemon:

    # Power: the strength of the move, measured in damage dealt to the opponent's hp.
    # Accuracy: the likelihood of the move hitting the opponent, measured as a percentage (e.g. 90% accuracy).
    # Type: the elemental type of the move, which determines its effectiveness against other types.
    # Heal Factor : The percent amount that you would heal.
    # Weather : Boolean value that tells if the move evokes a weather status.
    # Category: the classification of the move as either "Physical" or "Special", which determines which of the user's stats (Attack or Special Attack) is used to calculate damage.
    # Name: the name of the move.

    flamethrower = [90, 100, "Fire", 0, False, "Special", "Flamethrower"]
    air_slash = [75, 95, "Flying", 0, False, "Special", "Air Slash"]
    dragon_pulse = [85, 100, "Dragon", 0, False, "Special", "Dragon Pulse"]
    roost = [0, 100, "Flying", 50, False, "Status", "Roost"]
    giga_drain = [75, 100, "Grass", 50, False, "Special", "Giga Drain"]
    sludge_bomb = [90, 100, "Poison", 0, False, "Special", "Sludge Bomb"]
    leech_seed = [0, 90, "Grass", 0, False, "Status", "Leech Seed"]
    synthesis = [0, 100, "Grass", 50, False, "Status", "Synthesis"]
    hydro_pump = [110, 80, "Water", 0, False, "Special", "Hydro Pump"]
    ice_beam = [90, 100, "Ice", 0, False, "Special", "Ice Beam"]
    earthquake = [100, 100, "Ground", 0, False, "Physical", "Earthquake"]
    rapid_spin = [50, 100, "Normal", 0, False, "Physical", "Rapid Spin"]
    splash = [0, 100, "Water", 0, False, "Physical", "Splash"]

    # Define the base stats, abilities, moves, and type strengths/weaknesses for each Pokémon
    charizard_base_stats = {
        "hp": 78,
        "Attack": 84,
        "Defense": 78,
        "Special Attack": 109,
        "Special Defense": 85,
        "Speed": 100,
    }

    charizard_abilities = ["Blaze", "Solar Power"]
    charizard_moves = [flamethrower, air_slash, dragon_pulse, roost]
    charizard_weaknesses = ["Rock", "Electric", "Water"]
    charizard_resistances = ["Fire", "Grass", "Bug", "Steel", "Fairy"]
    charizard_immunities = ["Ground"]

    venusaur_base_stats = {
        "hp": 80,
        "Attack": 82,
        "Defense": 83,
        "Special Attack": 100,
        "Special Defense": 100,
        "Speed": 80,
    }
    venusaur_abilities = ["Overgrow", "Chlorophyll"]
    venusaur_moves = [splash, sludge_bomb, leech_seed, synthesis]
    venusaur_weaknesses = ["Fire", "Flying", "Ice", "Psychic"]
    venusaur_resistances = ["Water", "Electric", "Grass", "Fighting", "Fairy"]
    venusaur_immunities = []

    blastoise_base_stats = {
        "hp": 79,
        "Attack": 83,
        "Defense": 100,
        "Special Attack": 85,
        "Special Defense": 105,
        "Speed": 78,
    }
    blastoise_abilities = ["Torrent", "Rain Dish"]
    blastoise_moves = [hydro_pump, ice_beam, earthquake, rapid_spin]
    blastoise_weaknesses = ["Electric", "Grass"]
    blastoise_resistances = ["Water", "Fire", "Ice", "Steel"]
    blastoise_immunities = []

    magikarp_base_stats = {
        "hp": 300,
        "Attack": 85,
        "Defense": 200,
        "Special Attack": 85,
        "Special Defense": 200,
        "Speed": 80,
    }

    magikarp = Pokemon(
        name="Magikarp",
        type1="Water",
        base_stats=magikarp_base_stats,
        abilities=["Swift Swim", "Rattled"],
        moves=[splash, hydro_pump, flamethrower, synthesis],
        weaknesses=["Electric", "Grass"],
        resistances=["Fire", "Water", "Ice", "Steel"],
        immunities=[],
        type2=None,
    )

    # Create Charizard, Venusaur, and Blastoise Pokémon objects
    charizard = Pokemon(
        name="Charizard",
        type1="Fire",
        type2="Flying",
        base_stats=charizard_base_stats,
        abilities=charizard_abilities,
        moves=charizard_moves,
        weaknesses=charizard_weaknesses,
        resistances=charizard_resistances,
        immunities=charizard_immunities,
    )

    venusaur = Pokemon(
        name="Venusaur",
        type1="Grass",
        type2="Poison",
        base_stats=venusaur_base_stats,
        abilities=venusaur_abilities,
        moves=venusaur_moves,
        weaknesses=venusaur_weaknesses,
        resistances=venusaur_resistances,
        immunities=venusaur_immunities,
    )

    blastoise = Pokemon(
        name="Blastoise",
        type1="Water",
        type2=None,
        base_stats=blastoise_base_stats,
        abilities=blastoise_abilities,
        moves=blastoise_moves,
        weaknesses=blastoise_weaknesses,
        resistances=blastoise_resistances,
        immunities=blastoise_immunities,
    )

    # Chooses pokemon for enemy

    player_pokemon_choice = "magikarp"

    enemy_pokemon = enemy_pokemon_choice()
    enemy_pokemon_input = ""
    if player_pokemon_choice == "charizard":
        player_pokemon_input = charizard
    elif player_pokemon_choice == "venusaur":
        player_pokemon_input = venusaur
    elif player_pokemon_choice == "blastoise":
        player_pokemon_input = blastoise
    elif player_pokemon_choice == "magikarp":
        player_pokemon_input = magikarp

    if player_pokemon_choice != enemy_pokemon:
        if enemy_pokemon == "charizard":
            enemy_pokemon_input = charizard
        elif enemy_pokemon == "venusaur":
            enemy_pokemon_input = venusaur
        elif enemy_pokemon == "blastoise":
            enemy_pokemon_input = blastoise
    else:
        if enemy_pokemon == "charizard":
            enemy_pokemon_input = Pokemon(
                name="Charizard",
                type1="Fire",
                type2="Flying",
                base_stats=charizard_base_stats,
                abilities=charizard_abilities,
                moves=charizard_moves,
                weaknesses=charizard_weaknesses,
                resistances=charizard_resistances,
                immunities=charizard_immunities,
            )
        elif enemy_pokemon == "venusaur":
            enemy_pokemon_input = Pokemon(
                name="Venusaur",
                type1="Grass",
                type2="Poison",
                base_stats=venusaur_base_stats,
                abilities=venusaur_abilities,
                moves=venusaur_moves,
                weaknesses=venusaur_weaknesses,
                resistances=venusaur_resistances,
                immunities=venusaur_immunities,
            )
        else:
            enemy_pokemon_input = Pokemon(
                name="Blastoise",
                type1="Water",
                type2=None,
                base_stats=blastoise_base_stats,
                abilities=blastoise_abilities,
                moves=blastoise_moves,
                weaknesses=blastoise_weaknesses,
                resistances=blastoise_resistances,
                immunities=blastoise_immunities,
            )

    print(str(player_pokemon_choice) + "/" + str(enemy_pokemon))

    # TODO: fix dupe clause
    dupe_clause = False

    if enemy_pokemon == player_pokemon_choice:
        if enemy_pokemon == "charizard":
            enemy_duplicate = load_image_charizard(False)
            dupe_clause = True
        if enemy_pokemon == "venusaur":
            enemy_duplicate = load_image_venusaur(False)
            dupe_clause = True
        if enemy_pokemon == "blastoise":
            enemy_duplicate = load_image_blastoise(False)
            dupe_clause = True

    # Load an image from disk
    ## images image_load

    images = {
        1: load_image_charizard,
        2: load_image_venusaur,
        3: load_image_blastoise,
        4: load_image_magikarp,
    }

    charizard_image = images.get(1)(player_pokemon_choice == "charizard")
    venusaur_image = images.get(2)(player_pokemon_choice == "venusaur")
    blastoise_image = images.get(3)(player_pokemon_choice == "blastoise")
    magikarp_image = images.get(4)(player_pokemon_choice == "magikarp")

    # Extract the rect object from the tuple and assign its bottom attribute
    charizard_rect = charizard_image[1]
    charizard_surface = charizard_image[0]

    # Extract the rect object from the tuple and assign its bottom attribute
    venusaur_rect = venusaur_image[1]
    venusaur_surface = venusaur_image[0]

    # Extract the rect object from the tuple and assign its bottom attribute
    blastoise_rect = blastoise_image[1]
    blastoise_surface = blastoise_image[0]

    # Extract the rect object from the tuple and assign its bottom attribute
    magikarp_rect = magikarp_image[1]
    magikarp_surface = magikarp_image[0]

    if dupe_clause:
        enemy_rect = enemy_duplicate[1]
        enemy_surface = enemy_duplicate[0]

    if player_pokemon_choice == "charizard":
        player_pokemon_image = charizard_rect
        player_pokemon_surface = charizard_surface
    elif player_pokemon_choice == "venusaur":
        player_pokemon_image = venusaur_rect
        player_pokemon_surface = venusaur_surface
    elif player_pokemon_choice == "blastoise":
        player_pokemon_image = blastoise_rect
        player_pokemon_surface = blastoise_surface
    elif player_pokemon_choice == "magikarp":
        player_pokemon_image = magikarp_rect
        player_pokemon_surface = magikarp_surface

    if enemy_pokemon == "charizard":
        enemy_pokemon_image = charizard_rect
        enemy_pokemon_surface = charizard_surface
    elif enemy_pokemon == "venusaur":
        enemy_pokemon_image = venusaur_rect
        enemy_pokemon_surface = venusaur_surface
    elif enemy_pokemon == "blastoise":
        enemy_pokemon_image = blastoise_rect
        enemy_pokemon_surface = blastoise_surface
    elif enemy_pokemon == "magikarp":
        enemy_pokemon_image = magikarp_rect
        enemy_pokemon_surface = magikarp_surface

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

    # Setting up health bar

    # Define the width and height of the health bar
    BAR_WIDTH = 200
    BAR_HEIGHT = 20

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
        player_pokemon_input.moves[0][6],
        white_color,
        black_color,
    )
    button2 = Button(
        (screen_width / 4 - button_width / 4) - 100,
        screen_height / 1.205 + button_margin,
        button_width,
        button_height,
        player_pokemon_input.moves[1][6],
        white_color,
        black_color,
    )
    button3 = Button(
        (screen_width / 2 - button_width / 2),
        screen_height / 1.205 - button_height - button_margin,
        button_width,
        button_height,
        player_pokemon_input.moves[2][6],
        white_color,
        black_color,
    )
    button4 = Button(
        (screen_width / 2 - button_width / 2),
        screen_height / 1.205 + button_margin,
        button_width,
        button_height,
        player_pokemon_input.moves[3][6],
        white_color,
        black_color,
    )

    buttons = [button1, button2, button3, button4]
    selected_button_index = 0

    # Main game loop
    ## game_loop

    result = ""

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif result == "Player":
                pygame.quit()
                quit()
            elif result == "Enemy":
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
                        battle_loop_main(
                            button1.text, enemy_pokemon_input, player_pokemon_input
                        )
                    if buttons[selected_button_index] == button2:
                        result = battle_loop_main(
                            button2.text, enemy_pokemon_input, player_pokemon_input
                        )
                    if buttons[selected_button_index] == button3:
                        result = battle_loop_main(
                            button3.text, enemy_pokemon_input, player_pokemon_input
                        )
                    if buttons[selected_button_index] == button4:
                        result = battle_loop_main(
                            button4.text, enemy_pokemon_input, player_pokemon_input
                        )

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

        # Calculate the width of the health bar
        health_bar_width = int(
            (player_pokemon_input.current_health / player_pokemon_input.max_health)
            * BAR_WIDTH
        )

        # Draw the health bar
        health_bar_rect = pygame.Rect(100, 100, health_bar_width, BAR_HEIGHT)
        pygame.draw.rect(screen, green_color, health_bar_rect)

        # Draw the border of the health bar
        border_rect = pygame.Rect(100, 100, BAR_WIDTH, BAR_HEIGHT)
        pygame.draw.rect(screen, red_color, border_rect, 2)

        # Draw the border of the health bar
        border_rect = pygame.Rect(100, 100, BAR_WIDTH, BAR_HEIGHT)
        pygame.draw.rect(screen, black_color, border_rect, 2)

        # Calculate the width of the health bar
        health_bar_width = int(
            (enemy_pokemon_input.current_health / enemy_pokemon_input.max_health)
            * BAR_WIDTH
        )

        # Draw the health bar
        health_bar_rect = pygame.Rect(460, 300, health_bar_width, BAR_HEIGHT)
        pygame.draw.rect(screen, green_color, health_bar_rect)

        # Draw the border of the health bar
        border_rect = pygame.Rect(460, 300, BAR_WIDTH, BAR_HEIGHT)
        pygame.draw.rect(screen, red_color, border_rect, 2)

        # Draw the border of the health bar
        border_rect = pygame.Rect(460, 300, BAR_WIDTH, BAR_HEIGHT)
        pygame.draw.rect(screen, black_color, border_rect, 2)

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
