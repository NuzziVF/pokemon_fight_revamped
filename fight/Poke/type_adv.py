def type_advantage(command, Players_mon, enemy_mon):

  weakness_grass = ["Fire", "Flying", "Poison", "Ice", "Bug"]
  weakness_fire = ["Water", "Ground", "Rock"]
  weakness_water = ["Grass", "Eletric"]
  weakness_rock = ["Water","Steel","Ground","Fighting","Grass"]
  weakness_electric = ["Ground"] 
  weakness_flying = ["Rock","Eletric","Ice"]
  weakness_ground = ["Ice","Water","Grass"]
  weakness_psychic = ["Dark","Ghost","Bug"]
  weakness_dark = ["Fairy","Bug","Fighting"]
  weakness_fairy = ["Steel","Poison"]
  weakness_dragon = ["Fairy","Dragon","Ice"]
  weakness_bug = ["Flying","Rock","Fire"]
  weakness_steel = ["Fire","Ground","Fighting"]
  weakness_normal = ["Fighting"]
  weakness_ice = ["Steel","Fighting","Rock","Fire"]
  weakness_fighting = ["Fairy","Flying","Psychic"]
  weakness_poison = ["Rock","Psychic"]
  weakness_ghost = ["Dark","Ghost"]
#thank you JW, tomorrow Ima tell you how to make the lists and use them in a for loop

  if enemy_mon.type == "Grass":
    for weakness in weakness_grass:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_grass:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_grass:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_grass:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_grass:
          return True
     
  if enemy_mon.type == "Fire":
    for weakness in weakness_fire:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_fire:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_fire:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_fire:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_fire:
          return True

  if enemy_mon.type == "Water":
    for weakness in weakness_water:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_water:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_water:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_water:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_water:
          return True

  if enemy_mon.type == "Rock":
    for weakness in weakness_rock:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_rock:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_rock:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_rock:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_rock:
          return True

  if enemy_mon.type == "Eletric":
    for weakness in weakness_electric:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_electric:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_electric:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_electric:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_electric:
          return True

  if enemy_mon.type == "Flying":
    for weakness in weakness_flying:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_flying:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_flying:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_flying:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_flying:
          return True

  if enemy_mon.type == "Ground":
    for weakness in weakness_ground:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_ground:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_ground:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_ground:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_ground:
          return True

  if enemy_mon.type == "Psychic":
    for weakness in weakness_psychic:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_psychic:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_psychic:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_psychic:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_psychic:
          return True

  if enemy_mon.type == "Dark":
    for weakness in weakness_dark:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_dark:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_dark:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_dark:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_dark:
          return True

  if enemy_mon.type == "Fairy":
    for weakness in weakness_fairy:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_fairy:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_fairy:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_fairy:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_fairy:
          return True

  if enemy_mon.type == "Dragon":
    for weakness in weakness_dragon:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_dragon:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_dragon:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_dragon:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_dragon:
          return True

  if enemy_mon.type == "Bug":
    for weakness in weakness_bug:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_bug:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_bug:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_bug:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_bug:
          return True

  if enemy_mon.type == "Steel":
    for weakness in weakness_steel:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_steel:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_steel:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_steel:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_steel:
          return True

  if enemy_mon.type == "Normal":
    for weakness in weakness_normal:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_normal:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_normal:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_normal:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_normal:
          return True

  if enemy_mon.type == "Ice":
    for weakness in weakness_ice:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_ice:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_ice:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_ice:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_ice:
          return True

  if enemy_mon.type == "Fighting":
    for weakness in weakness_fighting:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_fighting:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_fighting:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_fighting:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_fighting:
          return True

  if enemy_mon.type == "Poison":
    for weakness in weakness_poison:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_poison:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_poison:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_poison:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_poison:
          return True

  if enemy_mon.type == "Ghost":
    for weakness in weakness_ghost:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == weakness_ghost:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == weakness_ghost:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == weakness_ghost:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == weakness_ghost:
          return True


def type_disadvantage(command, Players_mon, enemy_mon):

  strong_grass = ["Water","Eletric","Grass","Ground"]
  strong_fire = ["Fire", "Grass","Ice","bug","Fairy","Steel"]
  strong_water = ["Water", "Fire","Ice","Steel"]
  strong_rock = ["Poison","Normal","Fire","Flaying"]
  strong_electric = ["Eletric","Flying","Steel"] 
  strong_flying = ["Grass","Fighting","Bug"]
  strong_ground = ["Poison","Rock"]
  strong_psychic = ["Fighting","Psychic"]
  strong_dark = ["Ghost","Dark"]
  strong_fairy = ["Fighting","Bug","Dark"]
  strong_dragon = ["Fire","Water","Grass","Eletric"]
  strong_bug = ["Grass","Fighting","Ground"]
  strong_steel = ["Normal","Grass","Ice","Flying","Psychic","Bug","Rock","Dragon","Steel","Fairy"]
  strong_normal = []
  strong_ice = ["Ice"]
  strong_fighting = ["Bug","Rock","Dark"]
  strong_poison = ["Grass","Fighting","Poison","Fairy","Bug"]
  strong_ghost = ["Poison","Bug"]
#normal has no effect on ghost
#eletric has no effect on ground
#ground has no effect on flying
#fighting has no effect on ghost
#poison has no effect on steel
#dragon has no effect on fairy
  if enemy_mon.type == "Grass":
    for element in strong_grass:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_grass:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_grass:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_grass:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_grass:
          return True

  if enemy_mon.type == "Fire":
    for element in strong_fire:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_fire:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_fire:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_fire:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_fire:
          return True

  if enemy_mon.type == "Water":
    for element in strong_water:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_water:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_water:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_water:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_water:
          return True

  if enemy_mon.type == "Rock":
    for element in strong_rock:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_rock:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_rock:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_rock:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_rock:
          return True

  if enemy_mon.type == "Electric":
    for element in strong_electric:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_electric:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_electric:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_electric:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_electric:
          return True

  if enemy_mon.type == "Flying":
    for element in strong_flying:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_flying:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_flying:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_flying:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_flying:
          return True

  if enemy_mon.type == "Ground":
    for element in strong_ground:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_ground:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_ground:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_ground:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_ground:
          return True

  if enemy_mon.type == "Psychic":
    for element in strong_psychic:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_psychic:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_psychic:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_psychic:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_psychic:
          return True

  if enemy_mon.type == "Dark":
    for element in strong_dark:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_dark:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_dark:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_dark:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_dark:
          return True

  if enemy_mon.type == "Fairy":
    for element in strong_fairy:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_fairy:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_fairy:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_fairy:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_fairy:
          return True

  if enemy_mon.type == "Dragon":
    for element in strong_dragon:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_dragon:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_dragon:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_dragon:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_dragon:
          return True

  if enemy_mon.type == "Bug":
    for element in strong_bug:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_bug:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_bug:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_bug:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_bug:
          return True

  if enemy_mon.type == "Steel":
    for element in strong_steel:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_steel:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_steel:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_steel:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_steel:
          return True

  if enemy_mon.type == "Normal":
    for element in strong_normal:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_normal:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_normal:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_normal:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_normal:
          return True

  if enemy_mon.type == "Ice":
    for element in strong_ice:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_ice:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_ice:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_ice:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_ice:
          return True

  if enemy_mon.type == "Fighting":
    for element in strong_fighting:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_fighting:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_fighting:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_fighting:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_fighting:
          return True

  if enemy_mon.type == "Poison":
    for element in strong_poison:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_poison:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_poison:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_poison:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_poison:
          return True

  if enemy_mon.type == "Ghost":
    for element in strong_ghost:
      if command == Players_mon.move1[6]:
        if Players_mon.move1[3] == strong_ghost:
          return True
      if command == Players_mon.move2[6]:
        if Players_mon.move2[3] == strong_ghost:
          return True
      if command == Players_mon.move3[6]:
        if Players_mon.move3[3] == strong_ghost:
          return True
      if command == Players_mon.move4[6]:
        if Players_mon.move4[3] == strong_ghost:
          return True

def type_advantage_enemy(Players_mon, enemy_mon,enemy):

  weakness_grass = ["Fire", "Flying", "Poison", "Ice", "Bug"]
  weakness_fire = ["Water", "Ground","Rock"]
  weakness_water = ["Grass", "Eletric"]
  weakness_rock = ["Water","Steel","Ground","Fighting","Grass"]
  weakness_electric = ["Ground"] 
  weakness_flying = ["Rock","Eletric","Ice"]
  weakness_ground = ["Ice","Water","Grass"]
  weakness_psychic = ["Dark","Ghost","Bug"]
  weakness_dark = ["Fairy","Bug","Fighting"]
  weakness_fairy = ["Steel","Poison"]
  weakness_dragon = ["Fairy","Dragon","Ice"]
  weakness_bug = ["Flying","Rock","Fire"]
  weakness_steel = ["Fire","Ground","Fighting"]
  weakness_normal = ["Fighting"]
  weakness_ice = ["Steel","Fighting","Rock","Fire"]
  weakness_fighting = ["Fairy","Flying","Psychic"]
  weakness_poison = ["Rock","Psychic"]
  weakness_ghost = ["Dark","Ghost"]
#thank you JW, tomorrow Ima tell you how to make the lists and use them in a for loop

  if Players_mon.type == "Grass":
    for weakness in weakness_grass:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_grass:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_grass:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_grass:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_grass:
          return True
     
  if Players_mon.type == "Fire":
    for weakness in weakness_fire:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_fire:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_fire:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_fire:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_fire:
          return True

  if Players_mon.type == "Water":
    for weakness in weakness_water:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_water:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_water:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_water:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_water:
          return True

  if Players_mon.type == "Rock":
    for weakness in weakness_rock:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_rock:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_rock:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_rock:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_rock:
          return True

  if Players_mon.type == "Eletric":
    for weakness in weakness_electric:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_electric:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_electric:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_electric:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_electric:
          return True

  if Players_mon.type == "Flying":
    for weakness in weakness_flying:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_flying:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_flying:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_flying:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_flying:
          return True

  if Players_mon.type == "Ground":
    for weakness in weakness_ground:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_ground:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_ground:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_ground:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_ground:
          return True

  if Players_mon.type == "Psychic":
    for weakness in weakness_psychic:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_psychic:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_psychic:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_psychic:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_psychic:
          return True

  if Players_mon.type == "Dark":
    for weakness in weakness_dark:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_dark:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_dark:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_dark:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_dark:
          return True

  if Players_mon.type == "Fairy":
    for weakness in weakness_fairy:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_fairy:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_fairy:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_fairy:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_fairy:
          return True

  if Players_mon.type == "Dragon":
    for weakness in weakness_dragon:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_dragon:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_dragon:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_dragon:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_dragon:
          return True

  if Players_mon.type == "Bug":
    for weakness in weakness_bug:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_bug:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_bug:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_bug:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_bug:
          return True

  if Players_mon.type == "Steel":
    for weakness in weakness_steel:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_steel:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_steel:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_steel:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_steel:
          return True

  if Players_mon.type == "Normal":
    for weakness in weakness_normal:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_normal:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_normal:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_normal:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_normal:
          return True

  if Players_mon.type == "Ice":
    for weakness in weakness_ice:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_ice:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_ice:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_ice:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_ice:
          return True

  if Players_mon.type == "Fighting":
    for weakness in weakness_fighting:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_fighting:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_fighting:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_fighting:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_fighting:
          return True

  if Players_mon.type == "Poison":
    for weakness in weakness_poison:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_poison:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_poison:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_poison:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_poison:
          return True

  if Players_mon.type == "Ghost":
    for weakness in weakness_ghost:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == weakness_ghost:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == weakness_ghost:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == weakness_ghost:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == weakness_ghost:
          return True


def type_disadvantage_enemy(enemy, Players_mon, enemy_mon):

  strong_grass = ["Water","Eletric","Grass","Ground"]
  strong_fire = ["Fire", "Grass","Ice","bug","Fairy","Steel"]
  strong_water = ["Water", "Fire","Ice","Steel"]
  strong_rock = ["Poison","Normal","Fire","Flaying"]
  strong_electric = ["Eletric","Flying","Steel"] 
  strong_flying = ["Grass","Fighting","Bug"]
  strong_ground = ["Poison","Rock"]
  strong_psychic = ["Fighting","Psychic"]
  strong_dark = ["Ghost","Dark"]
  strong_fairy = ["Fighting","Bug","Dark"]
  strong_dragon = ["Fire","Water","Grass","Eletric"]
  strong_bug = ["Grass","Fighting","Ground"]
  strong_steel = ["Normal","Grass","Ice","Flying","Psychic","Bug","Rock","Dragon","Steel","Fairy"]
  strong_normal = []
  strong_ice = ["Ice"]
  strong_fighting = ["Bug","Rock","Dark"]
  strong_poison = ["Grass","Fighting","Poison","Fairy","Bug"]
  strong_ghost = ["Poison","Bug"]
#normal has no effect on ghost
#eletric has no effect on ground
#ground has no effect on flying
#fighting has no effect on ghost
#poison has no effect on steel
#dragon has no effect on fairy
  if Players_mon.type == "Grass":
    for element in strong_grass:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_grass:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_grass:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_grass:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_grass:
          return True

  if Players_mon.type == "Fire":
    for element in strong_fire:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_fire:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_fire:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_fire:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_fire:
          return True

  if Players_mon.type == "Water":
    for element in strong_water:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_water:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_water:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_water:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_water:
          return True

  if Players_mon.type == "Rock":
    for element in strong_rock:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_rock:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_rock:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_rock:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_rock:
          return True

  if Players_mon.type == "Electric":
    for element in strong_electric:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_electric:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_electric:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_electric:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_electric:
          return True

  if Players_mon.type == "Flying":
    for element in strong_flying:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_flying:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_flying:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_flying:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_flying:
          return True

  if Players_mon.type == "Ground":
    for element in strong_ground:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_ground:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_ground:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_ground:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_ground:
          return True

  if Players_mon.type == "Psychic":
    for element in strong_psychic:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_psychic:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_psychic:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_psychic:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_psychic:
          return True

  if Players_mon.type == "Dark":
    for element in strong_dark:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_dark:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_dark:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_dark:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_dark:
          return True

  if Players_mon.type == "Fairy":
    for element in strong_fairy:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_fairy:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_fairy:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_fairy:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_fairy:
          return True

  if Players_mon.type == "Dragon":
    for element in strong_dragon:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_dragon:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_dragon:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_dragon:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_dragon:
          return True

  if Players_mon.type == "Bug":
    for element in strong_bug:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_bug:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_bug:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_bug:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_bug:
          return True

  if Players_mon.type == "Steel":
    for element in strong_steel:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_steel:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_steel:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_steel:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_steel:
          return True

  if Players_mon.type == "Normal":
    for element in strong_normal:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_normal:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_normal:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_normal:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_normal:
          return True

  if Players_mon.type == "Ice":
    for element in strong_ice:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_ice:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_ice:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_ice:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_ice:
          return True

  if Players_mon.type == "Fighting":
    for element in strong_fighting:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_fighting:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_fighting:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_fighting:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_fighting:
          return True

  if Players_mon.type == "Poison":
    for element in strong_poison:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_poison:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_poison:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_poison:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_poison:
          return True

  if Players_mon.type == "Ghost":
    for element in strong_ghost:
      if enemy == enemy_mon.move1[6]:
        if enemy_mon.move1[3] == strong_ghost:
          return True
      if enemy == enemy_mon.move2[6]:
        if enemy_mon.move2[3] == strong_ghost:
          return True
      if enemy == enemy_mon.move3[6]:
        if enemy_mon.move3[3] == strong_ghost:
          return True
      if enemy == enemy_mon.move4[6]:
        if enemy_mon.move4[3] == strong_ghost:
          return True