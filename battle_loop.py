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
        self.current_health = self.max_health
        self.status = None
        self.stat_stages = {
            "attack": 0,
            "defense": 0,
            "special_attack": 0,
            "special_defense": 0,
            "speed": 0,
        }
        self.ivs = {
            "hp": 0,
            "attack": 0,
            "defense": 0,
            "special_attack": 0,
            "special_defense": 0,
            "speed": 0,
        }
        self.evs = {
            "hp": 0,
            "attack": 0,
            "defense": 0,
            "special_attack": 0,
            "special_defense": 0,
            "speed": 0,
        }

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


# Power: the strength of the move, measured in damage dealt to the opponent's HP.
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
    "HP": 78,
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
    "HP": 80,
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
    "HP": 79,
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
