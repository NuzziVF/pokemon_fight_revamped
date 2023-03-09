import random as r
from poke_functions.functions_file import *
import pygame

# TODO: fix giga drains healing


def test_func(screen: pygame.Surface):
    # Initialize Pygame
    pygame.init()
    rect_surface = pygame.Surface((200, 150))
    rect_surface.fill((255, 0, 0))

    screen.blit(rect_surface, (100, 100))


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

    print(enemy_attack)

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


def battle_loop_main(
    players_button_input, enemy_pokemon_random: Pokemon, players_pokemon_input: Pokemon
):
    ### battle order
    # press enter, choose move, speed check, battle calc happens, accuracy check happens first, if successful damage calc, first base damage, then elemental check, then crit chance, then health changes, then next pokemon goes, battle calc loops, then turn ends.

    players_pokemon = players_pokemon_input
    enemy_pokemon = enemy_pokemon_random

    if players_pokemon.base_stats["Speed"] >= enemy_pokemon.base_stats["Speed"]:
        player_goes_first(players_button_input, enemy_pokemon, players_pokemon)

    else:
        enemy_goes_first(players_button_input, enemy_pokemon, players_pokemon)
