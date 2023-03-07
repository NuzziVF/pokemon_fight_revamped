import random as r
import os
from typing import List


class Pokemon:
    def __init__(
        self,
        name: str,
        type1: str,
        base_stats: dict,
        abilities: list,
        moves: list,
        weaknesses: list,
        resistances: list,
        immunities: list,
        type2: str = None,
    ):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.base_stats = base_stats
        self.abilities = abilities
        self.moves = moves
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.immunities = immunities
        self.level = 50
        self.experience = 0
        self.status = None
        self.stat_stages = {
            "attack": 0,
            "defense": 0,
            "special_attack": 0,
            "special_defense": 0,
            "speed": 0,
        }
        self.ivs = {
            "hp": 31,
            "attack": 31,
            "defense": 31,
            "special_attack": 31,
            "special_defense": 31,
            "speed": 31,
        }
        self.evs = {
            "hp": 0,
            "attack": 0,
            "defense": 0,
            "special_attack": 0,
            "special_defense": 0,
            "speed": 0,
        }
        self.is_dead = False
        self.current_health = self.max_health

    @property
    def max_health(self):
        return int(
            (
                (
                    (2 * self.base_stats["hp"] + self.ivs["hp"] + self.evs["hp"] / 4)
                    * self.level
                )
                / 100
            )
            + self.level
            + 10
        )

    @property
    def attack(self):
        return int(
            (
                (
                    (
                        2 * self.base_stats["attack"]
                        + self.ivs["attack"]
                        + self.evs["attack"] / 4
                    )
                    * self.level
                )
                / 100
            )
            + 5
        )

    @property
    def defense(self):
        return int(
            (
                (
                    (
                        2 * self.base_stats["defense"]
                        + self.ivs["defense"]
                        + self.evs["defense"] / 4
                    )
                    * self.level
                )
                / 100
            )
            + 5
        )

    @property
    def special_attack(self):
        return int(
            (
                (
                    (
                        2 * self.base_stats["special_attack"]
                        + self.ivs["special_attack"]
                        + self.evs["special_attack"] / 4
                    )
                    * self.level
                )
                / 100
            )
            + 5
        )

    @property
    def special_defense(self):
        return int(
            (
                (
                    (
                        2 * self.base_stats["special_defense"]
                        + self.ivs["special_defense"]
                        + self.evs["special_defense"] / 4
                    )
                    * self.level
                )
                / 100
            )
            + 5
        )

    @property
    def speed(self):
        return int(
            (
                (
                    (
                        2 * self.base_stats["speed"]
                        + self.ivs["speed"]
                        + self.evs["speed"] / 4
                    )
                    * self.level
                )
                / 100
            )
            + 5
        )

    def health_change(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0

    def heal(self, heal_amount):
        print("healing")
        self.current_health += heal_amount
        self.current_health = min(self.current_health, self.max_health)

    def death_check(self):
        if self.current_health <= 0:
            self.is_dead = True
        else:
            self.is_dead = False

    def load_health(self, players_pokemon_bool=False):
        if players_pokemon_bool:
            try:
                with open(f"battle_files/player_{self.name}_health.txt", "r") as f:
                    health = int(f.read())
                    self.current_health = health
                    return health
            except FileNotFoundError:
                self.current_health = self.max_health
                return self.base_stats["hp"]
        else:
            try:
                with open(f"battle_files/enemy_{self.name}_health.txt", "r") as f:
                    health = int(f.read())
                    self.current_health = health
                    return health
            except FileNotFoundError:
                self.current_health = self.max_health
                return self.base_stats["hp"]

    def save_health(self, players_pokemon_bool=False):
        name_lower = self.name
        file_path = (
            f"battle_files/player_{name_lower}_health.txt"
            if players_pokemon_bool
            else f"battle_files/enemy_{name_lower}_health.txt"
        )
        if not os.path.exists(file_path):
            with open(file_path, "x") as f:  # Use "x" mode instead of "w"
                pass  # Create a blank file
        with open(file_path, "w") as f:  # Use "w" mode to write current_health
            f.write(str(self.current_health))


def damage_calc(user: Pokemon, pokemon_move: List, target: Pokemon):
    # Get move data
    power = pokemon_move[0]
    accuracy = pokemon_move[1]
    move_type = pokemon_move[2]
    heal_factor = pokemon_move[3]
    category = pokemon_move[5]

    # Get user and target stats
    attack_stat = user.base_stats["Attack"]
    defense_stat = target.base_stats["Defense"]
    special_attack_stat = user.base_stats["Special Attack"]
    special_defense_stat = target.base_stats["Special Defense"]

    # Determine which attack stat to use based on move category
    if category == "Physical":
        attack = attack_stat
        defense = defense_stat
    else:
        attack = special_attack_stat
        defense = special_defense_stat

    # Calculate damage
    modifier = 1
    # Looking to see if STAB is applicable
    if move_type in user.type1:
        modifier *= 1.5
    if user.type2 is not None and move_type in user.type2:
        modifier *= 1.5
    # Looking to see if it's super effective
    if move_type in target.weaknesses:
        modifier *= 2
    if move_type in target.resistances:
        modifier *= 0.5
    if move_type in target.immunities:
        modifier *= 0

    if r.random() > accuracy:
        return 0

    damage = (((2 * user.level + 10) / 250) * (attack / defense) * power + 2) * modifier
    damage = int(damage)
    # target.current_health -= damage

    if heal_factor:
        print("accidental healing")
        user.current_health += int(((heal_factor / 100) / 2) * damage)
        user.current_health = min(user.current_health, user.max_health)

    return damage


def fake_damage_calc(user: Pokemon, pokemon_move: List, target: Pokemon):
    # Get move data
    power = pokemon_move[0]
    accuracy = pokemon_move[1]
    move_type = pokemon_move[2]
    category = pokemon_move[5]

    # Get user and target stats
    attack_stat = user.base_stats["Attack"]
    defense_stat = target.base_stats["Defense"]
    special_attack_stat = user.base_stats["Special Attack"]
    special_defense_stat = target.base_stats["Special Defense"]

    # Determine which attack stat to use based on move category
    if category == "Physical":
        attack = attack_stat
        defense = defense_stat
    else:
        attack = special_attack_stat
        defense = special_defense_stat

    # Calculate damage
    modifier = 1
    # Looking to see if STAB is applicable
    if move_type in user.type1:
        modifier *= 1.5
    if user.type2 is not None and move_type in user.type2:
        modifier *= 1.5
    # Looking to see if it's super effective
    if move_type in target.weaknesses:
        modifier *= 2
    if move_type in target.resistances:
        modifier *= 0.5
    if move_type in target.immunities:
        modifier *= 0

    if r.random() > accuracy:
        return 0

    damage = (((2 * user.level + 10) / 250) * (attack / defense) * power + 2) * modifier
    damage = int(damage)
    # target.current_health -= damage

    return damage


def enemy_move(enemy_pokemon: Pokemon, players_pokemon: Pokemon):
    if int(enemy_pokemon.current_health) < int(enemy_pokemon.max_health) / 2:
        for each in enemy_pokemon.moves:
            if each[3] > 0 and each[5] == "Status":
                return each

    # elif int(enemy_pokemon.current_health) > int(enemy_pokemon.max_health) / 2:
    else:
        current_move = enemy_pokemon.moves[0]
        for each in enemy_pokemon.moves:
            if fake_damage_calc(
                enemy_pokemon, each, players_pokemon
            ) > fake_damage_calc(enemy_pokemon, current_move, players_pokemon):
                current_move = each
        return current_move


def heal_calc(user: Pokemon, pokemon_move: List):
    heal_factor = pokemon_move[3]
    heal_amount = user.max_health * (heal_factor / 100)
    return heal_amount


def health_check(enemy_pokemon: Pokemon, players_pokemon: Pokemon):
    print(
        "Enemy Pokemon: "
        + str(enemy_pokemon.current_health)
        + "/"
        + str(enemy_pokemon.max_health)
    )
    print(
        "Player Pokemon: "
        + str(players_pokemon.current_health)
        + "/"
        + str(players_pokemon.max_health)
    )
