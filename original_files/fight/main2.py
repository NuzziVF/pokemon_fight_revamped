from .Poke import *
from getkey import getkey, keys
import os, sys, time
import random
from dataclasses import dataclass
@dataclass
class Pokemon:
  name: str
  max_health: int
  health: int
  is_fainted: bool
  crit_chance: int
  type: str
  duel_type: str
  move1: list
  move2: list
  move3: list
  move4: list
  resistance: int

def random_attack(enemy_mon):
  attack = random.randint(1,4)
  if attack == 1:
    return enemy_mon.move1[6]
  if attack == 2:
    return enemy_mon.move2[6]
  if attack == 3:
    return enemy_mon.move3[6]
  if attack == 4:
    return enemy_mon.move4[6]
def Continue():
  ...

def play_fight(Players_mon):
  attack = "1"
  # flamethrower = FlameThrower()
  # dragon_breath = DragonBreath()
  # roost = Roost()
  # sunny_day = Sunnyday()
  # skull_bash = SkullBash()
  # rain_dance = RainDance()
  # hydro_pump = HydroPump()
  # ice_beam = IceBeam()
  # solar_beam = SolarBeam()
  # synthesis = Synthesis()
  # light_screen = LightScreen()

  # moves = [flamethrower, dragon_breath, roost, sunny_day, rain_dance, skull_bash, hydro_pump, ice_beam, solar_beam, synthesis, light_screen]

  
  # charizard = Charizard(moves)
  # blastoise = Blastoice()
  # venusaur = Venusaur()

  multiplier = 1
  
  
# Power: the strength of the move, measured in damage dealt to the opponent's hp.
# Accuracy: the likelihood of the move hitting the opponent, measured as a percentage (e.g. 90% accuracy).
# Type: the elemental type of the move, which determines its effectiveness against other types.
# Heal Factor : The percent amount that you would heal.
# Weather : Boolean value that tells if the move evokes a weather status.
# Category: the classification of the move as either "Physical" or "Special", which determines which of the user's stats (Attack or Special Attack) is used to calculate damage.
# Name: the name of the move.
  
  flamethrower = [90, 100, "Fire", 0, False, "Special", "FlameThrower"]
  dragon_breath = [60, 100, "Dragon", 0, False, "Special", "Dragon Breath"]
  roost = [0, 100, "Flying", 50, False, "Status", "Roost"]
  sunny_day = [0, 100, "Fire", 0, True, "Status", "Sunny Day"]
  skull_bash = [130, 100, "Normal", 0, False, "Phyical", "Skull Bash"]
  rain_dance = [0, 100, "Water", 0, True, "Status", "Rain Dance"]
  hydro_pump = [110, 80, "Water", 0, False, "Special", "Hydro Pump"]
  ice_beam = [90, 100, "Ice", 0, False, "Special", "Ice Beam"]
  solar_beam = [120, 100, "Grass", 0, False, "Special", "Solar Beam"]
  synthesis = [0, 100, "Grass", 50, False, "Status", "Synthesis"]
  light_screen = [0, 100, "Psychic", 0, False, "Status", "Light Screen"]



  charizard = Pokemon("Charizard", 297, 297, False, 6.25, "Fire", "Flying", flamethrower, dragon_breath, roost, sunny_day, 38)
  
  
  blastoise = Pokemon("Blastoise", 299, 299, False, 6.25, "Water", None, skull_bash, rain_dance, hydro_pump, ice_beam, 35)
  
  venusaur = Pokemon("Venusaur", 301, 301, False, 6.25, "Grass", "Poison", solar_beam, sunny_day, synthesis, light_screen, 45)


  choice = [charizard, blastoise, venusaur]  



  
# @dataclass
# class Move:
#   dmg: int
#   hit: int
#   type: str
#   heal: int
#   weather: bool
#   catagory: str
  command = ""
  enemy_mon = random_encounter(choice)

   
  typingPrint(
    f"Player encounters a wild {enemy_mon.name}\n"
  )
  typingPrint(
    f"Player Sends out {Players_mon.name}"
  )
  print("""
        """)
  enemy_health_bar(enemy_mon)
  if enemy_mon == charizard:
      charpic()
  if enemy_mon == venusaur:
      venpic()
  if enemy_mon == blastoise:
      blastpic()
  
  print("")
  player_health_bar(Players_mon)


########################################
  location = "fight"
  def map():
    for y in range(mapS[1]):
      line = ""
      numbery = y + 1
      for x in range(mapS[0]):
          numberx = x + 1
          for place in objects:
              if objects [place] [:2] == [numberx, numbery]:
                  line += objects [place] [2]
                  break
          else:
              line += "  "        
      print(line)
  
  def attackslist():
    for y in range(mapA[1]):
      line = ""
      numbery = y + 1
      for x in range(mapA[0]):
          numberx = x + 1
          for place in objects2:
              if objects2 [place] [:2] == [numberx, numbery]:
                  line += objects2 [place] [2]
                  break
          else:
              line += "  "        
      print(line) 
  
  mapS = [10,5]
  mapA = [2, 4]
  
  objects = {}
  objects2 = {}
  
  def mapSize(x, y):
      global mapS
      mapS = [x, y]
  def cls():
      os.system('cls' if os.name=='nt' else 'clear')
    
  def uiclear():
    cls()
    
    enemy_health_bar(enemy_mon)
    if enemy_mon == charizard:
      charpic()
    if enemy_mon == venusaur:
      venpic()
    if enemy_mon == blastoise:
      blastpic()
      
    print("")
    player_health_bar(Players_mon)
    # PlayerHP(Players_mon, enemy_mon)
      # PlayerHP(Players_mon, enemy_mon)
    map()
  
  def addObject(name, x, y, symbol):
      objects[name] = [x, y, symbol]
    
  def addObject2(name, x, y, symbol):
      objects2[name] = [x, y, symbol]
  
  addObject("Fight", 2, 2, "Fight ")
  
  addObject("Bag", 4, 2, "Bag")
  
  addObject("Switch", 2, 4, "Switch")
  
  addObject("Run", 4, 4, "Run")
  
  addObject("pointer", 1, 2, " >")
  
  addObject2("Attack1",2, 1, Players_mon.move1[6])
  addObject2("Attack2",2, 2, Players_mon.move2[6])
  addObject2("Attack3",2, 3, Players_mon.move3[6])
  addObject2("Attack4",2, 4, Players_mon.move4[6])
  addObject2("pointer",1, 1, " >")
  
  map()
  
  while True:
      key = getkey()
      if location == "fight":
        if key == 's':
          objects["pointer"] = [1, 4, " >"]
          location = "switch"
          uiclear()
        elif key == 'd':
          objects["pointer"] = [3, 2, " >"]
          location = "bag"
          uiclear() 
          
      elif location == "bag":
        if key == 's':
          objects["pointer"] = [3, 4, " >"]
          location = "run"
          uiclear()
        elif key == "a":
          addObject("pointer", 1, 2, " >")
          location = "fight"
          uiclear()
          
        
      elif location == "switch":
        if key == "w":
          addObject("pointer", 1, 2, " >")
          location = "fight"
          uiclear()
        elif key == "d":
          objects["pointer"] = [3, 4, " >"]
          location = "run"
          uiclear()
        
      elif location == "run":
        if key == "w":
          objects["pointer"] = [3, 2, " >"]
          location = "bag"
          uiclear() 
        elif key == "a":
          objects["pointer"] = [1, 4, " >"]
          location = "switch"
          uiclear()
      if location == "fight":
        
          if key == keys.ENTER:
            cls()
            attackslist()
            while True:
              attackget = getkey()
              
              if attack == "1":
                
                if attackget == "s":
                  objects2["pointer"] = [1, 2, " >"]
                  attack = "2"
                  cls() 
                  attackslist()
                  continue
                  
                elif attackget == keys.ENTER:
                  command = Players_mon.move1[6]
                  enemy = random_attack(enemy_mon)
                  print(
                    enemy
                  )
                  print(enemy_mon.move1[6])
                  if command == Players_mon.move1[6]:
                      if hit_calc(command, Players_mon) == True:
                        if crit_chance(command, Players_mon) == True:
                          multiplier += 1
                        if type_advantage(command, Players_mon, enemy_mon) == True:
                          multiplier += 1
                        if type_disadvantage(command, Players_mon, enemy_mon) == True:
                          multiplier -= 1
                          if multiplier == 0:
                            multiplier += 0.5
                        damage = dmg_calc(command, Players_mon, enemy_mon, multiplier)
                        damage = res_calc(damage, Players_mon)
                        enemy_hp_calc(damage, enemy_mon)
                        multiplier = 1
                        enemy = random_attack(enemy_mon)
                        print(f"\n\nWild {enemy_mon.name} used {enemy}")
                        # if crit_chance_enemy(enemy_mon, enemy) == True:
                        #   multiplier += 1
                        # if type_advantage_enemy(Players_mon, enemy_mon, enemy) == True:
                        #   multiplier += 1
                        # if type_disadvantage_enemy(Players_mon, enemy_mon, enemy) == True:
                        #   multiplier -= 1
                        #   if multiplier == 0:
                        #     multiplier += 0.5
                        enemy_attack = dmg_calc_enemy(Players_mon, enemy_mon, multiplier, enemy)
                        enemy_attack = res_calc_enemy(enemy_attack, Players_mon)
                        player_hp_calc(enemy_attack, Players_mon)
                        multiplier = 1
                        if blacked_out(Players_mon) == True:
                          print(  
                            f"""
{Players_mon.name} fainted
You  Blacked out and never woke up
                            """
                          )
                          while win(enemy_mon) == True or blacked_out(Players_mon) == True: 
                            print("Game Over")
                            ui = input("> ") 
                          break
                        if win(enemy_mon) == True:
                          print(
                            f"""
The wild {enemy_mon.name} has fainted
You feel nothing
                            """
                          )
                          while win(enemy_mon) == True or blacked_out(Players_mon) == True: 
                            print("Game Over")
                            ui = input("> ") 
                          break
                        uiclear()
                        break

                        
                        
              if attack == "2":
                
                if attackget == "w":
                  objects2["pointer"] = [1, 1, " >"]
                  attack = "1"
                  cls() 
                  attackslist()
                  
                elif attackget == "s":
                  objects2["pointer"] = [1, 3, " >"]
                  attack = "3"
                  cls() 
                  attackslist()
                  continue
                  
                elif attackget == keys.ENTER:
                  command = Players_mon.move2[6]
                  if command == Players_mon.move2[6]:
                      if hit_calc(command, Players_mon) == True:
                        if crit_chance(command, Players_mon) == True:
                          multiplier += 1
                        if type_advantage(command, Players_mon, enemy_mon) == True:
                          multiplier += 1
                        if type_disadvantage(command, Players_mon, enemy_mon) == True:
                          multiplier -= 1
                          if multiplier == 0:
                            multiplier += 0.5
                        damage = dmg_calc(command, Players_mon, enemy_mon, multiplier)
                        damage = res_calc(damage, Players_mon)
                        enemy_hp_calc(damage, enemy_mon)
                        multiplier = 1
                        enemy = random_attack(enemy_mon)
                        print(f"\n\nWild {enemy_mon.name} used {enemy}")
                        if crit_chance_enemy(enemy_mon, enemy) == True:
                          multiplier += 1
                        if type_advantage_enemy(Players_mon, enemy_mon, enemy) == True:
                          multiplier += 1
                        if type_disadvantage_enemy(Players_mon, enemy_mon, enemy) == True:
                          multiplier -= 1
                          if multiplier == 0:
                            multiplier += 0.5
                        enemy_attack = dmg_calc_enemy(Players_mon, enemy_mon, multiplier, enemy)
                        enemy_attack = res_calc_enemy(enemy_attack, Players_mon)
                        player_hp_calc(enemy_attack, Players_mon)
                        multiplier = 1
                        if blacked_out(Players_mon) == True:
                          print(  
                            f"""
{Players_mon.name} fainted
You  Blacked out and never woke up
                            """
                          )
                          while win(enemy_mon) == True or blacked_out(Players_mon) == True: 
                            print("Game Over")
                            ui = input("> ") 
                          break
                        if win(enemy_mon) == True:
                          print(
                            f"""
The wild {enemy_mon.name} has fainted
You feel nothing
                            """
                          )
                          while win(enemy_mon) == True or blacked_out(Players_mon) == True: 
                            print("Game Over")
                            ui = input("> ") 
                          break
                        uiclear()
                        break





                      
              if attack == "3":
                if attackget == "w":
                  objects2["pointer"] = [1, 2, " >"]
                  attack = "2"
                  cls() 
                  attackslist()
                  
                if attackget == "s":
                  objects2["pointer"] = [1, 4, " >"]
                  attack = "4"
                  cls() 
                  attackslist()
                  continue
                  
                if attackget == keys.ENTER:
                  command = Players_mon.move3[6]
                  if command == Players_mon.move3[6]:
                      if hit_calc(command, Players_mon) == True:
                        if crit_chance(command, Players_mon) == True:
                          multiplier += 1
                        if type_advantage(command, Players_mon, enemy_mon) == True:
                          multiplier += 1
                        if type_disadvantage(command, Players_mon, enemy_mon) == True:
                          multiplier -= 1
                          if multiplier == 0:
                            multiplier += 0.5
                        damage = dmg_calc(command, Players_mon, enemy_mon, multiplier)
                        damage = res_calc(damage, Players_mon)
                        enemy_hp_calc(damage, enemy_mon)
                        multiplier = 1
                        enemy = random_attack(enemy_mon)
                        print(f"\n\nWild {enemy_mon.name} used {enemy}")
                        if crit_chance_enemy(enemy_mon, enemy) == True:
                          multiplier += 1
                        if type_advantage_enemy(Players_mon, enemy_mon, enemy) == True:
                          multiplier += 1
                        if type_disadvantage_enemy(Players_mon, enemy_mon, enemy) == True:
                          multiplier -= 1
                          if multiplier == 0:
                            multiplier += 0.5
                        enemy_attack = dmg_calc_enemy(Players_mon, enemy_mon, multiplier, enemy)
                        enemy_attack = res_calc_enemy(enemy_attack, Players_mon)
                        player_hp_calc(enemy_attack, Players_mon)
                        multiplier = 1
                        if blacked_out(Players_mon) == True:
                          print(  
                            f"""
{Players_mon.name} fainted
You  Blacked out and never woke up
                            """
                          )
                          while win(enemy_mon) == True or blacked_out(Players_mon) == True: 
                            print("Game Over")
                            ui = input("> ") 
                          break
                        if win(enemy_mon) == True:
                          print(
                            f"""
The wild {enemy_mon.name} has fainted
You feel nothing
                            """
                          )
                          while win(enemy_mon) == True or blacked_out(Players_mon) == True: 
                            print("Game Over")
                            ui = input("> ") 
                          break
                        uiclear()
                        break




                        
              if attack == "4":
                
                if attackget == "w":
                  objects2["pointer"] = [1, 3, " >"]
                  attack = "3"
                  cls() 
                  attackslist()
                  
                elif attackget == keys.ENTER:
                  command = Players_mon.move4[6]
                  if command == Players_mon.move4[6]:
                      if hit_calc(command, Players_mon) == True:
                        if crit_chance(command, Players_mon) == True:
                          multiplier += 1
                        if type_advantage(command, Players_mon, enemy_mon) == True:
                          multiplier += 1
                        if type_disadvantage(command, Players_mon, enemy_mon) == True:
                          multiplier -= 1
                          if multiplier == 0:
                            multiplier += 0.5
                        damage = dmg_calc(command, Players_mon, enemy_mon, multiplier)
                        damage = res_calc(damage, Players_mon)
                        enemy_hp_calc(damage, enemy_mon)
                        multiplier = 1
                        enemy = random_attack(enemy_mon)
                        print(f"\n\nWild {enemy_mon.name} used {enemy}")
                        if crit_chance_enemy(enemy_mon, enemy) == True:
                          multiplier += 1
                        if type_advantage_enemy(Players_mon, enemy_mon, enemy) == True:
                          multiplier += 1
                        if type_disadvantage_enemy(Players_mon, enemy_mon, enemy) == True:
                          multiplier -= 1
                          if multiplier == 0:
                            multiplier += 0.5
                        enemy_attack = dmg_calc_enemy(Players_mon, enemy_mon, multiplier, enemy)
                        enemy_attack = res_calc_enemy(enemy_attack, Players_mon)
                        player_hp_calc(enemy_attack, Players_mon)
                        multiplier = 1
                        if blacked_out(Players_mon) == True:
                          print(  
                            f"""
{Players_mon.name} fainted
You  Blacked out and never woke up
                            """
                          )
                          while win(enemy_mon) == True or blacked_out(Players_mon) == True: 
                            print("Game Over")
                            ui = input("> ") 
                          break
                        if win(enemy_mon) == True:
                          print(
                            f"""
The wild {enemy_mon.name} has fainted
You feel nothing
                            """
                          )
                          while win(enemy_mon) == True or blacked_out(Players_mon) == True: 
                            print("Game Over")
                            ui = input("> ") 
                          break
                        uiclear()
                        break





                        
                        
      elif location == "bag":
        if key == keys.ENTER:
          print("empty")
              
            
          
             
      elif location == "switch":
           if key == keys.ENTER:
            print("You only have one pokemon")
             
      elif location == "run":
          if key == keys.ENTER:
            cls()
            input("got away safely!")
            break

    
# ########################################
  # command = typingInput(user_interface)
  
  # if command == "Fight":
  #   command = typingInput(player_moves)
  #   if command == Players_mon.move1[6]:
  #     if hit_calc(command, Players_mon) == True:
  #       if crit_chance() == True:
  #         multiplier += 1
  #       dmg_calc(command, Players_mon.move1, multiplier)
        
  #   if command == Players_mon.move2[6]:
  #     if hit_calc(command, Players_mon) == True:
  #       if crit_chance() == True:
  #         multiplier += 1
  #       dmg_calc(command, Players_mon.move2, multiplier)
        
  #   if command == Players_mon.move3[6]:
  #     if hit_calc(command, Players_mon) == True:
  #       if crit_chance() == True:
  #         multiplier += 1
  #       dmg_calc(command, Players_mon.move3, multiplier)
        
  #   if command == Players_mon.move4[6]:
  #     if hit_calc(command, Players_mon) == True:
  #       if crit_chance() == True:
  #         multiplier += 1
  #       dmg_calc(command, Players_mon.move4, multiplier)
        
  # if command == "Switch":
  #   print("WIP")
  # if command == "Bag":
  #   print("WIP")
  # if command == "Run":
  #   print("WIP")
    
  
  

# if __name__ == "__main__":
#   main2()























'''
print(
  f"Player encounters a while {encounter}"
  
  f"Player Sends out {Players_mon}"
  
  # Insert UI here
  # Place holder UI
  
"""
FIGHT      BAG
SWITCH     RUN
"""
  
  #> FIGHT
  
"""
Flamethrower    Dragon's Breath
Sunny Day       Roost
"""
  
  #> Dragons Breath
  
  f"Player used Dragons Breath"
  
  f"Enemy used Solar Beam"
  
"""
FIGHT      BAG
SWITCH     RUN
"""
  
  #> FIGHT
  
"""
Flamethrower    Dragon's Breath
Sunny Day       Roost
"""
  
  #> Flamethrower
  
  f"Player used Flamethrower"
  
  f"it was super effective"
  
  f"The wild {encounter} has Fainted"
)

'''