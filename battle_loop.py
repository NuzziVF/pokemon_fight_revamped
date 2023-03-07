import random as r
import os
from poke_functions.functions_file import *

# TODO: fix giga drains healing


def battle_loop_main(
    players_button_input, enemy_pokemon_random: Pokemon, players_pokemon_input: Pokemon
):
    ### battle order
    # press enter, choose move, speed check, battle calc happens, accuracy check happens first, if successful damage calc, first base damage, then elemental check, then crit chance, then health changes, then next pokemon goes, battle calc loops, then turn ends.

    players_pokemon = players_pokemon_input
    enemy_pokemon = enemy_pokemon_random

    players_pokemon.death_check()
    enemy_pokemon.death_check()

    # players_pokemon.load_health(True)
    # enemy_pokemon.load_health()

    if players_pokemon.base_stats["Speed"] >= enemy_pokemon.base_stats["Speed"]:
        print(f"{players_pokemon.name} Goes first")

        health_check(enemy_pokemon, players_pokemon)

        if players_button_input == players_pokemon.moves[0][6]:
            player_button = players_pokemon.moves[0]
        if players_button_input == players_pokemon.moves[1][6]:
            player_button = players_pokemon.moves[1]
        if players_button_input == players_pokemon.moves[2][6]:
            player_button = players_pokemon.moves[2]
        if players_button_input == players_pokemon.moves[3][6]:
            player_button = players_pokemon.moves[3]

        players_attack = player_button

        print(f"{players_pokemon.name} used {players_attack[6]}")

        if players_pokemon.is_dead == False:
            if players_attack[0] > 0:
                # This updates the health
                enemy_pokemon.health_change(
                    damage_calc(players_pokemon, players_attack, enemy_pokemon)
                )
                print(
                    f"{players_pokemon.name} Did {damage_calc(players_pokemon, players_attack, enemy_pokemon)} to {enemy_pokemon.name}"
                )
                enemy_pokemon.death_check()
            elif players_attack[3] > 0:
                print("healing")
                players_pokemon.heal(heal_calc(players_pokemon, players_attack))
                print(
                    f"{players_pokemon.name} Healed {heal_calc(players_pokemon, players_attack)}"
                )

        enemy_attack = enemy_move(enemy_pokemon, players_pokemon)

        print(f"{enemy_pokemon.name} used {enemy_attack[6]}")

        if enemy_pokemon.is_dead == False:
            if enemy_attack[0] > 0:
                # This updates the health
                players_pokemon.health_change(
                    damage_calc(enemy_pokemon, enemy_attack, players_pokemon)
                )
                print(
                    f"{enemy_pokemon.name} Did {damage_calc(enemy_pokemon, enemy_attack, players_pokemon)} to {players_pokemon.name}"
                )
                players_pokemon.death_check()
            elif enemy_attack[3] > 0:
                print("healing")
                enemy_pokemon.heal(heal_calc(enemy_pokemon, enemy_attack))
                print(
                    f"{enemy_pokemon.name} Healed {heal_calc(enemy_pokemon, enemy_attack)}"
                )

    else:
        print(f"{enemy_pokemon.name} Goes first")

        health_check(enemy_pokemon, players_pokemon)
        # this chooses the enemy's move
        enemy_attack = enemy_move(enemy_pokemon, players_pokemon)

        print(f"{enemy_pokemon.name} used {enemy_attack[6]}")

        if enemy_pokemon.is_dead == False:
            if enemy_attack[0] > 0:
                # This updates the health
                players_pokemon.health_change(
                    damage_calc(enemy_pokemon, enemy_attack, players_pokemon)
                )
                print(
                    f"{enemy_pokemon.name} Did {damage_calc(enemy_pokemon, enemy_attack, players_pokemon)} to {players_pokemon.name}"
                )
                players_pokemon.death_check()
            elif enemy_attack[3] > 0:
                print("healing")
                enemy_pokemon.heal(heal_calc(enemy_pokemon, enemy_attack))
                print(
                    f"{enemy_pokemon.name} Healed {heal_calc(enemy_pokemon, enemy_attack)}"
                )

        if players_button_input == players_pokemon.moves[0][6]:
            player_button = players_pokemon.moves[0]
        if players_button_input == players_pokemon.moves[1][6]:
            player_button = players_pokemon.moves[1]
        if players_button_input == players_pokemon.moves[2][6]:
            player_button = players_pokemon.moves[2]
        if players_button_input == players_pokemon.moves[3][6]:
            player_button = players_pokemon.moves[3]

        players_attack = player_button

        print(f"{players_pokemon.name} used {players_attack[6]}")

        if players_pokemon.is_dead == False:
            if players_attack[0] > 0:
                # This updates the health
                enemy_pokemon.health_change(
                    damage_calc(players_pokemon, players_attack, enemy_pokemon)
                )
                print(
                    f"{players_pokemon.name} Did {damage_calc(players_pokemon, players_attack, enemy_pokemon)} to {enemy_pokemon.name}"
                )
                enemy_pokemon.death_check()
            elif players_attack[3] > 0:
                print("healing")
                players_pokemon.heal(heal_calc(players_pokemon, players_attack))
                print(
                    f"{players_pokemon.name} Healed {heal_calc(players_pokemon, players_attack)}"
                )
