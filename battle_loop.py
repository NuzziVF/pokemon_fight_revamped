import random as r
import os

# TODO: fix giga drains healing


def enemy_move(enemy_pokemon, players_pokemon):
    no_heals = False
    if enemy_pokemon.current_health < enemy_pokemon.current_health / 2:
        for each in enemy_pokemon.moves:
            if each[3] > 0 and each[5] == "Status":
                return each
            else:
                no_heals = True
    elif (
        no_heals == True
        or enemy_pokemon.current_health > enemy_pokemon.current_health / 2
    ):
        current_move = enemy_pokemon.moves[0]
        for each in enemy_pokemon.moves:
            if damage_calc(enemy_pokemon, each, players_pokemon) > damage_calc(
                enemy_pokemon, current_move, players_pokemon
            ):
                current_move = each
        return current_move


def damage_calc(user, pokemon_move, target):
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
    if move_type in user.type2:
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
        print("test1")
        print((heal_factor / 100) * damage)
        user.current_health += int(((heal_factor / 100) / 2) * damage)
        user.current_health = min(user.current_health, user.max_health)

    return damage


def heal_calc(user, pokemon_move):
    heal_factor = pokemon_move[3]
    heal_amount = user.max_health * (heal_factor / 100)
    return heal_amount


def health_check(enemy_pokemon, players_pokemon):
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


def death_check(pokemon):
    if pokemon.current_health <= 0:
        return True
    else:
        return False


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

    def heal(self, heal_amount):
        self.current_health += heal_amount
        self.current_health = min(self.current_health, self.max_health)

    def load_health(self, players_pokemon_bool=False):
        if players_pokemon_bool:
            try:
                with open(f"/battle_files/player_{self.name}_health.txt", "r") as f:
                    health = f.read()
                    self.current_health = health
                    return health
            except FileNotFoundError:
                self.current_health = self.max_health
                return self.base_stats["hp"]
        else:
            try:
                with open(f"/battle_files/enemy_{self.name}_health.txt", "r") as f:
                    health = f.read()
                    self.current_health = health
                    return health
            except FileNotFoundError:
                self.current_health = self.max_health
                return self.base_stats["hp"]

    def save_health(self, players_pokemon_bool=False):
        if players_pokemon_bool:
            with open(f"/battle_files/player_{self.name}_health.txt", "w") as f:
                f.write(str(self.current_health))
        else:
            with open(f"/battle_files/enemy_{self.name}_health.txt", "w") as f:
                f.write(str(self.current_health))


def battle_loop_main(players_button_input, enemy_pokemon_random, players_pokemon_input):
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
    venusaur_moves = [giga_drain, sludge_bomb, leech_seed, synthesis]
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

    ### battle order
    # press enter, choose move, speed check, battle calc happens, accuracy check happens first, if successful damage calc, first base damage, then elemental check, then crit chance, then health changes, then next pokemon goes, battle calc loops, then turn ends.

    players_pokemon = players_pokemon_input
    enemy_pokemon = enemy_pokemon_random

    if players_pokemon == "charizard":
        players_pokemon = charizard
    elif players_pokemon == "venusaur":
        players_pokemon = venusaur
    elif players_pokemon == "blastoise":
        players_pokemon = blastoise

    if enemy_pokemon == "charizard":
        enemy_pokemon = charizard
    elif enemy_pokemon == "venusaur":
        enemy_pokemon = venusaur
    elif enemy_pokemon == "blastoise":
        enemy_pokemon = blastoise

    players_pokemon.load_health(True)
    enemy_pokemon.load_health()

    if players_pokemon.base_stats["Speed"] > enemy_pokemon.base_stats["Speed"]:
        health_check(enemy_pokemon, players_pokemon)

        if players_button_input == "Button 1":
            player_button = players_pokemon.moves[1]
        if players_button_input == "Button 2":
            player_button = players_pokemon.moves[2]
        if players_button_input == "Button 3":
            player_button = players_pokemon.moves[3]
        if players_button_input == "Button 4":
            player_button = players_pokemon.moves[4]

        players_attack = player_button

        if players_attack[0] > 0:
            print(damage_calc(players_pokemon, players_attack, enemy_pokemon))
            # This updates the health
            enemy_pokemon.health_change(
                damage_calc(players_pokemon, players_attack, enemy_pokemon)
            )
            enemy_pokemon.is_dead = death_check(enemy_pokemon)
        else:
            players_pokemon.heal(heal_calc(players_pokemon, players_attack))

        health_check(enemy_pokemon, players_pokemon)

        enemy_attack = enemy_move(enemy_pokemon, players_pokemon)

        if enemy_attack[0] > 0:
            print(damage_calc(enemy_pokemon, enemy_attack, players_pokemon))
            # This updates the health
            players_pokemon.health_change(
                damage_calc(enemy_pokemon, enemy_attack, players_pokemon)
            )
            players_pokemon.is_dead = death_check(players_pokemon)
        else:
            enemy_pokemon.heal(heal_calc(enemy_pokemon, enemy_attack))

        health_check(enemy_pokemon, players_pokemon)

    else:
        # this chooses the enemy's move
        enemy_attack = enemy_move(enemy_pokemon, players_pokemon)

        health_check(enemy_pokemon, players_pokemon)
        print(enemy_attack[6])

        if enemy_attack[0] > 0:
            print(damage_calc(enemy_pokemon, enemy_attack, players_pokemon))
            # This updates the health
            players_pokemon.health_change(
                damage_calc(enemy_pokemon, enemy_attack, players_pokemon)
            )
            players_pokemon.is_dead = death_check(players_pokemon)
        else:
            enemy_pokemon.heal(heal_calc(enemy_pokemon, enemy_attack))

        health_check(enemy_pokemon, players_pokemon)

        if players_button_input == "Button 1":
            player_button = players_pokemon.moves[1]
        if players_button_input == "Button 2":
            player_button = players_pokemon.moves[2]
        if players_button_input == "Button 3":
            player_button = players_pokemon.moves[3]
        if players_button_input == "Button 4":
            player_button = players_pokemon.moves[4]

        players_attack = player_button

        if players_attack[0] > 0:
            print(damage_calc(players_pokemon, players_attack, enemy_pokemon))
            # This updates the health
            enemy_pokemon.health_change(
                damage_calc(players_pokemon, players_attack, enemy_pokemon)
            )
            enemy_pokemon.is_dead = death_check(enemy_pokemon)
        else:
            players_pokemon.heal(heal_calc(players_pokemon, players_attack))

        health_check(enemy_pokemon, players_pokemon)

    players_pokemon.save_health(True)
    enemy_pokemon.save_health()

    if players_pokemon.is_dead:
        file_path = f"/battle_files/player_{players_pokemon.name}_health.txt"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} deleted successfully")
        else:
            print(f"{file_path} does not exist")

    if enemy_pokemon.is_dead:
        file_path = f"/battle_files/enemy_{enemy_pokemon.name}_health.txt"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} deleted successfully")
        else:
            print(f"{file_path} does not exist")
