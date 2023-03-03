import random

def crit_chance(command, Players_mon) -> bool:
  if command == Players_mon.move1[6]:
    crit = random.randint(0, 100)
    return crit <= Players_mon.crit_chance
  if command == Players_mon.move2[6]:
    crit = random.randint(0, 100)
    return crit <= Players_mon.crit_chance
  if command == Players_mon.move3[6]:
    crit = random.randint(0, 100)
    return crit <= Players_mon.crit_chance
  if command == Players_mon.move4[6]:
    crit = random.randint(0, 100)
    return crit <= Players_mon.crit_chance
    
def crit_chance_enemy(enemy, enemy_mon) -> bool:
  if enemy == enemy_mon.move1[6]: #issue here
    crit = random.randint(0, 100)
    return crit <= enemy_mon.crit_chance
  if enemy == enemy_mon.move2[6]:
    crit = random.randint(0, 100)
    return crit <= enemy_mon.crit_chance
  if enemy == enemy_mon.move3[6]:
    crit = random.randint(0, 100)
    return crit <= enemy_mon.crit_chance
  if enemy == enemy_mon.move4[6]:
    crit = random.randint(0, 100)
    return crit <= enemy_mon.crit_chance