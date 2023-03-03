def enemy_health_bar(enemy_mon):
  healthdashes = 20
  dashconvert = int(enemy_mon.max_health/healthdashes)
  currentdashes = int(enemy_mon.health/dashconvert) 
  remaininghealth = healthdashes - currentdashes
  if enemy_mon.health <= 50:
    healthdisplay = '🟥' * currentdashes  
  if enemy_mon.health < 150 and not enemy_mon.health <= 50:
    healthdisplay = '🟧' * currentdashes
  if enemy_mon.health >= 150:
    healthdisplay = '🟩' * currentdashes  
  remainingdisplay = '⬛' * remaininghealth 
  print(enemy_mon.name)
  print("|" + healthdisplay + remainingdisplay + "|")
  

  
def player_health_bar(Players_mon):
  healthdashes = 20
  dashconvert = int(Players_mon.max_health/healthdashes)
  currentdashes = int(Players_mon.health/dashconvert) 
  remaininghealth = healthdashes - currentdashes
  if Players_mon.health <= 50:
    healthdisplay = '🟥' * currentdashes  
  if Players_mon.health < 150 and not Players_mon.health <= 50:
    healthdisplay = '🟧' * currentdashes
  if Players_mon.health >= 150:
    healthdisplay = '🟩' * currentdashes  
  remainingdisplay = '⬛' * remaininghealth 
  print(f"{Players_mon.name}")
  print("|" + healthdisplay + remainingdisplay + "|")
  print(f"{round(Players_mon.health)} / {Players_mon.max_health}")

def PlayerHP(Players_mon, enemy_mon):
  enemy_health_bar(enemy_mon)
  player_health_bar(Players_mon)

def player_hp_calc(enemy_attack, Players_mon) -> None:
  Players_mon.health -= enemy_attack
  if Players_mon.health <= 0:
    Players_mon.is_fainted = True
    # print(Players_mon.is_fainted)

def enemy_hp_calc(damage, enemy_mon) -> None:
  enemy_mon.health -= damage
  if enemy_mon.health <= 0:
    enemy_mon.is_fainted = True
    # print(enemy_mon.is_fainted)


def blacked_out(Players_mon):
  return Players_mon.is_fainted

def win(enemy_mon):
  return enemy_mon.is_fainted