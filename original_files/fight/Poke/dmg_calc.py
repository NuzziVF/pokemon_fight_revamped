def dmg_calc(command, Players_mon, enemy_mon, multiplier) -> int:
  if command == Players_mon.move1[6]:
    damage = Players_mon.move1[0] * multiplier
    if Players_mon.move1[3] > 0:
      Players_mon.health += (Players_mon.max_health / 2)
      if Players_mon.health >= Players_mon.max_health:
        Players_mon.health = Players_mon.max_health
    return res_calc(damage, enemy_mon)

  if command == Players_mon.move2[6]:
    damage = Players_mon.move2[0] * multiplier
    if Players_mon.move2[3] > 0:
      Players_mon.health += (Players_mon.max_health / 2)
      if Players_mon.health >= Players_mon.max_health:
        Players_mon.health = Players_mon.max_health
    return res_calc(damage, enemy_mon)

  if command == Players_mon.move3[6]:
    damage = Players_mon.move3[0] * multiplier
    if Players_mon.move3[3] > 0:
      Players_mon.health += (Players_mon.max_health / 2)
      if Players_mon.health >= Players_mon.max_health:
        Players_mon.health = Players_mon.max_health
    return res_calc(damage, enemy_mon)

  if command == Players_mon.move4[6]:
    damage = Players_mon.move4[0] * multiplier
    if Players_mon.move4[3] > 0:
      Players_mon.health += (Players_mon.max_health / 2)
      if Players_mon.health >= Players_mon.max_health:
        Players_mon.health = Players_mon.max_health
    return res_calc(damage, enemy_mon)

  


def res_calc(damage, enemy_mon):
  res = damage / (100 / enemy_mon.resistance)
  return res

  
def dmg_calc_enemy(Players_mon, enemy_mon, multiplier, enemy) -> int:
  
  print(f"\n\nWild {enemy_mon.name} used {enemy}")

  
  if enemy == enemy_mon.move1[6]:
    damage = enemy_mon.move1[0] * multiplier
    if enemy_mon.move1[3] > 0:
      enemy_mon.health += (enemy_mon.max_health / 2)
      if enemy_mon.health >= enemy_mon.max_health:
        enemy_mon.health = enemy_mon.max_health
    return damage

  if enemy == enemy_mon.move2[6]:
    damage = enemy_mon.move2[0] * multiplier
    if enemy_mon.move2[3] > 0:
      enemy_mon.health += (enemy_mon.max_health / 2)
      if enemy_mon.health >= enemy_mon.max_health:
        enemy_mon.health = enemy_mon.max_health
    return damage

  if enemy == enemy_mon.move3[6]:
    damage = enemy_mon.move3[0] * multiplier
    if enemy_mon.move3[3] > 0:
      enemy_mon.health += (enemy_mon.max_health / 2)
      if enemy_mon.health >= enemy_mon.max_health:
        enemy_mon.health = enemy_mon.max_health
    return damage

  if enemy == enemy_mon.move4[6]:
    damage = enemy_mon.move4[0] * multiplier
    if enemy_mon.move4[3] > 0:
      enemy_mon.health += (enemy_mon.max_health / 2)
      if enemy_mon.health >= enemy_mon.max_health:
        enemy_mon.health = enemy_mon.max_health
    return damage

  


def res_calc_enemy(enemy_attack, Players_mon) -> int:
  return enemy_attack / (100 / Players_mon.resistance)