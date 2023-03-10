import random as r
from poke_functions.functions_file import *
import pygame

# TODO: fix giga drains healing

## color_variables
red_color = (255, 0, 0)
green_color = (0, 255, 0)
black_color = (0, 0, 0)
white_color = (255, 255, 255)


def update_health_bar(
    player_pokemon_input: Pokemon, enemy_pokemon_input: Pokemon, screen: pygame.Surface
):
    pygame.init()
    # Define the width and height of the health bar
    BAR_WIDTH = 200
    BAR_HEIGHT = 20
    # Calculate the width of the health bar
    health_bar_width = int(
        (player_pokemon_input.current_health / player_pokemon_input.max_health)
        * BAR_WIDTH
    )

    # Draw the health bar
    health_bar_rect = pygame.Rect(125, 100, health_bar_width, BAR_HEIGHT)
    pygame.draw.rect(screen, green_color, health_bar_rect)

    # Draw the border of the health bar
    border_rect = pygame.Rect(125, 100, BAR_WIDTH, BAR_HEIGHT)
    pygame.draw.rect(screen, red_color, border_rect, 2)

    # Draw the border of the health bar
    border_rect = pygame.Rect(125, 100, BAR_WIDTH, BAR_HEIGHT)
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

    # Update the screen
    pygame.display.update()


def player_text(screen: pygame.Surface, text_surface: pygame.Surface, move_used: Move):
    # Initialize Pygame
    pygame.init()
    # rect_surface = pygame.Surface((200, 150))
    # rect_surface.fill((255, 0, 0))
    font = pygame.font.Font(None, 28)
    # Set the text position
    text_x = 100
    text_y = 75

    text_surface = font.render("Move used: " + move_used.name, True, (0, 0, 0))

    # Blit the text surface onto the game display
    screen.blit(text_surface, (text_x, text_y))

    # Update the screen
    pygame.display.update()

    # Pause for half a second
    pygame.time.wait(300)


def enemy_text(screen: pygame.Surface, text_surface: pygame.Surface, move_used: Move):
    # Initialize Pygame
    pygame.init()
    # rect_surface = pygame.Surface((200, 150))
    # rect_surface.fill((255, 0, 0))
    font = pygame.font.Font(None, 28)
    # Set the text position
    text_x = 450
    text_y = 325

    text_surface = font.render("Move used: " + move_used.name, True, (0, 0, 0))

    # Blit the text surface onto the game display
    screen.blit(text_surface, (text_x, text_y))

    # Update the screen
    pygame.display.update()

    # Pause for half a second
    pygame.time.wait(1000)


def player_goes_first(
    players_button_input, enemy_pokemon: Pokemon, players_pokemon: Pokemon
):
    print(f"{players_pokemon.name} Goes first")

    if players_button_input == players_pokemon.moves[0].name:
        player_button = players_pokemon.moves[0]
    if players_button_input == players_pokemon.moves[1].name:
        player_button = players_pokemon.moves[1]
    if players_button_input == players_pokemon.moves[2].name:
        player_button = players_pokemon.moves[2]
    if players_button_input == players_pokemon.moves[3].name:
        player_button = players_pokemon.moves[3]

    players_attack = player_button

    enemy_attack = enemy_move(enemy_pokemon, players_pokemon)

    print(f"{players_pokemon.name} used {players_attack.name}")

    if players_pokemon.is_dead == False and enemy_pokemon.is_dead == False:
        if players_attack.power > 0:
            # This updates the health
            battle_damage = damage_calc(players_pokemon, players_attack, enemy_pokemon)
            enemy_pokemon.health_change(battle_damage)
            print(f"{players_pokemon.name} Did {battle_damage} to {enemy_pokemon.name}")
            enemy_pokemon.death_check()
        elif players_attack.heal_factor > 0:
            heal_amount = heal_calc(players_pokemon, players_attack)
            players_pokemon.heal(heal_amount)
            print(f"{players_pokemon.name} Healed {heal_amount}")

    if players_pokemon.is_dead == False and enemy_pokemon.is_dead == False:
        print(f"{enemy_pokemon.name} used {enemy_attack.name}")
        if enemy_attack.power > 0:
            # This updates the health
            battle_damage = damage_calc(enemy_pokemon, enemy_attack, players_pokemon)
            players_pokemon.health_change(battle_damage)
            print(f"{enemy_pokemon.name} Did {battle_damage} to {players_pokemon.name}")
            players_pokemon.death_check()
        elif enemy_attack.heal_factor > 0:
            heal_amount = heal_calc(enemy_pokemon, enemy_attack)
            enemy_pokemon.heal(heal_amount)
            print(f"{enemy_pokemon.name} Healed {heal_amount}")

    health_check(enemy_pokemon, players_pokemon)
    return "player", players_pokemon, players_attack, enemy_pokemon, enemy_attack


def enemy_goes_first(
    players_button_input: str, enemy_pokemon: Pokemon, players_pokemon: Pokemon
):
    print(f"{enemy_pokemon.name} Goes first")
    print(players_button_input)
    # this chooses the enemy's move
    enemy_attack = enemy_move(enemy_pokemon, players_pokemon)

    if players_pokemon.is_dead == False and enemy_pokemon.is_dead == False:
        print(f"{enemy_pokemon.name} used {enemy_attack.name}")
        if enemy_attack.power > 0:
            # This updates the health
            battle_damage = damage_calc(enemy_pokemon, enemy_attack, players_pokemon)
            players_pokemon.health_change(battle_damage)
            print(f"{enemy_pokemon.name} Did {battle_damage} to {players_pokemon.name}")
            players_pokemon.death_check()
        elif enemy_attack.heal_factor > 0:
            heal_amount = heal_calc(enemy_pokemon, enemy_attack)
            enemy_pokemon.heal(heal_amount)
            print(f"{enemy_pokemon.name} Healed {heal_amount}")

    if players_button_input == players_pokemon.moves[0].name:
        player_button = players_pokemon.moves[0]
    if players_button_input == players_pokemon.moves[1].name:
        player_button = players_pokemon.moves[1]
    if players_button_input == players_pokemon.moves[2].name:
        player_button = players_pokemon.moves[2]
    if players_button_input == players_pokemon.moves[3].name:
        player_button = players_pokemon.moves[3]

    players_attack = player_button

    print(f"{players_pokemon.name} used {players_attack.name}")

    if players_pokemon.is_dead == False and enemy_pokemon.is_dead == False:
        if players_attack.power > 0:
            # This updates the health
            battle_damage = damage_calc(players_pokemon, players_attack, enemy_pokemon)
            enemy_pokemon.health_change(battle_damage)
            print(f"{players_pokemon.name} Did {battle_damage} to {enemy_pokemon.name}")
            enemy_pokemon.death_check()
        elif players_attack.heal_factor > 0:
            heal_amount = heal_calc(players_pokemon, players_attack)
            players_pokemon.heal(heal_amount)
            print(f"{players_pokemon.name} Healed {heal_amount}")
    health_check(enemy_pokemon, players_pokemon)
    return "enemy", players_pokemon, players_attack, enemy_pokemon, enemy_attack


def battle_loop_main(
    players_button_input,
    enemy_pokemon_random: Pokemon,
    players_pokemon_input: Pokemon,
    screen: pygame.Surface,
):
    ### battle order
    # press enter, choose move, speed check, battle calc happens, accuracy check happens first, if successful damage calc, first base damage, then elemental check, then crit chance, then health changes, then next pokemon goes, battle calc loops, then turn ends.

    players_pokemon = players_pokemon_input
    enemy_pokemon = enemy_pokemon_random

    if players_pokemon.base_stats["Speed"] >= enemy_pokemon.base_stats["Speed"]:
        turn_details = player_goes_first(
            players_button_input, enemy_pokemon, players_pokemon
        )
        turn_detail = Turn(
            turn_details[0],
            turn_details[1],
            turn_details[2],
            turn_details[3],
            turn_details[4],
        )
        return turn_detail
    else:
        turn_details = enemy_goes_first(
            players_button_input, enemy_pokemon, players_pokemon
        )
        turn_detail = Turn(
            turn_details[0],
            turn_details[1],
            turn_details[2],
            turn_details[3],
            turn_details[4],
        )
        return turn_detail
