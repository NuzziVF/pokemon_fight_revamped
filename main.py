import os, sys, time
from fight import *
from termcolor import colored
from getkey import getkey, keys

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
  
def sprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
    
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
location = "bottom"
gotpokemon = False
gotitem = False
def introprint():
  text = colored("""
               _                                ⢱⣄⠀⠀⠀⠀⠀⠀⠀⠀
   _ __   ___ | | _____ _ __ ___   ___  _ __     ⢻⣦⣶⣤⡶⠟⠋⠀⢀
  | '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \    ⢸⣿⣿⣿⣧⣶⣾⣿⡟
  | |_) | (_) |   <  __/ | | | | | (_) | | | |   ⢸⣿⣿⣿⣧⡽⠉⠀⠀
  | .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|   ⢸⣿⣿⣿⣿⠁⠀⠀⠀
  |_|                                            ⠨⠿⠛⠛⠇⠀⠀⠀⠀
        """, 'blue')
  print(text)
  input("               Press enter to continue. ")
  
  
def introprint2():
    sprint(
    """
    Welcome to the wonderous world of pokemon!
    Look we are all too busy for that whole story. 
    You are a 10 year old that fights your pets for profit,
    now get out into the woods and find a pokemon to exploit.
    """
    )

def name():
  name = input("What is your name? ")
  return name

def map():
  for y in range(mapA[1]):
    line = ""
    numbery = y + 1
    for x in range(mapA[0]):
        numberx = x + 1
        for place in objects:
            if objects [place] [:2] == [numberx, numbery]:
                line += objects [place] [2]
                break
        else:
            line += "░░"        
    print(line)
#exploring phase
def mapcls():
  cls()
  map()

mapA = [31, 25]
  
playerx = 15
playery = 22

objects = {}



def mapSize(x, y):
    global mapS
    mapS = [x, y]

def addObject(name, x, y, symbol):
    objects[name] = [x, y, symbol]
  
#data
addObject("Player", playerx, playery, "🅿 ")

addObject("PokemonBall1", 7, 6, "◓ ") 
addObject("PokemonBall2", 9, 6, " ◓") 
addObject("PokemonBall3", 11, 6, " ◓") 

addObject("elementsfire", 7, 5, "🔥")
addObject("elementswater", 9, 5, "💧") 
addObject("elementsgrass", 11, 5, "🌿") 

addObject("Battle", 17, 14, "枩")

addObject("top1", 3, 3, "==")
addObject("top2", 4, 3, "==")
addObject("top3", 5, 3, "==")
addObject("top4", 6, 3, "==")
addObject("top5", 7, 3, "==")
addObject("top6", 8, 3, "==")
addObject("top7", 9, 3, "==")
addObject("top8", 10, 3, "==")
addObject("top9", 11, 3, "==")
addObject("top10", 12, 3, "==")
addObject("top11", 13, 3, "==")
addObject("top12", 14, 3, "==")

addObject("left1", 3, 4, "||")
addObject("left2", 3, 5, "||")
addObject("left3", 3, 6, "||")
addObject("left4", 3, 7, "||")

addObject("bottom1", 3, 8, "==")
addObject("bottom2", 4, 8, "==")
addObject("bottom3", 5, 8, "==")
addObject("bottom4", 6, 8, "==")
addObject("bottom5", 7, 8, "==")
addObject("bottom6", 8, 8, "░░")
addObject("bottom7", 9, 8, "░░")
addObject("bottom8", 10, 8, "==")
addObject("bottom9", 11, 8, "==")
addObject("bottom10", 12, 8, "==")
addObject("bottom11", 13, 8, "==")
addObject("bottom12", 14, 8, "==")

addObject("right1", 14, 4, "||")
addObject("right2", 14, 5, "||")
addObject("right3", 14, 6, "||")
addObject("right4", 14, 7, "||")

addObject("left5", 7, 9, "||")
addObject("left6", 7, 10, "||")
addObject("left7", 7, 11, "||")
addObject("left8", 10, 9, "||")
addObject("left9", 10, 10, "||")
addObject("left10", 10, 11, "||")

addObject("top13", 7, 12, "==")
addObject("top14", 6, 12, "==")
addObject("top15", 5, 12, "==")
addObject("top16", 4, 12, "==")
addObject("top17", 3, 12, "==")
addObject("top18", 2, 12, "==")
addObject("top19", 8, 12, "░░")
addObject("top20", 9, 12, "░░")
addObject("top21", 10, 12, "==")
addObject("top22", 11, 12, "==")
addObject("top23", 12, 12, "==")
addObject("top24", 13, 12, "==")
addObject("top25", 14, 12, "==")
addObject("top26", 15, 12, "==")
addObject("top27", 16, 12, "==")
addObject("top28", 17, 12, "==")
addObject("top29", 18, 12, "==")
addObject("top30", 19, 12, "==")

addObject("left11", 2, 13, "||")
addObject("left12", 2, 14, "||")
addObject("left13", 2, 15, "||")

addObject("right11", 19, 13, "||")
addObject("right12", 19, 14, "||")
addObject("right13", 19, 15, "||")

addObject("bottom13", 7, 16, "==")
addObject("bottom14", 6, 16, "==")
addObject("bottom15", 5, 16, "==")
addObject("bottom16", 4, 16, "==")
addObject("bottom17", 3, 16, "==")
addObject("bottom18", 2, 16, "==")
addObject("bottom19", 8, 16, "==")
addObject("bottom20", 9, 16, "==")
addObject("bottom21", 10, 16, "==")
addObject("bottom22", 11, 16, "==")
addObject("bottom23", 12, 16, "==")
addObject("bottom24", 13, 16, "==")
addObject("bottom25", 14, 16, "░░")
addObject("bottom26", 15, 16, "░░")
addObject("bottom27", 16, 16, "==")
addObject("bottom28", 17, 16, "==")
addObject("bottom29", 18, 16, "==")
addObject("bottom30", 19, 16, "==")

addObject("left14", 13, 17, "||")
addObject("left15", 13, 18, "||")
addObject("left16", 13, 19, "||")
addObject("left17", 13, 20, "||")
addObject("left18", 13, 21, "||")
addObject("left19", 13, 22, "||")


addObject("right14", 16, 17, "||")
addObject("right15", 16, 18, "||")
addObject("right16", 16, 19, "||")
addObject("right17", 16, 20, "||")
addObject("right18", 16, 21, "||")
addObject("right19", 16, 22, "||")

addObject("bottom31", 13, 23, "==")
addObject("bottom32", 14, 23, "==")
addObject("bottom33", 15, 23, "==")
addObject("bottom34", 16, 23, "==")


def mapout(location):
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

  print("")
  gotpokemon = False
  map()
  
  while True:
    while location == "fight":
      play_fight(Players_mon)
    movement = getkey()
    
    if location == "bottom":
      if movement == "w" or movement == keys.UP:
        objects["Player"] = [15, 14, "🅿 "]
        location = "righthall"
        mapcls()
        continue
      else:
        print("can't move there.")
        
    if location == "righthall":
      if movement == "a" or movement == keys.LEFT:
        objects["Player"] = [8, 14, "🅿 "]
        location = "lefthall"
        mapcls()
        continue
      if movement == "s" or movement == keys.DOWN:
        objects["Player"] = [15, 22, "🅿 "]
        location = "bottom"
        mapcls()
        
      elif movement == "d" or movement == keys.RIGHT:
        if gotpokemon == True:
          location = "fight"
          cls()
          continue


          
        else:
          print ("Hey wait, dangerous wild pokemon live in the tall grass!!")
      else:
        print("can't move there.")
        
    if location == "lefthall":
      
      if movement == "a" or movement == keys.LEFT:
        objects["Player"] = [4, 14, "🅿 "]
        objects["Item"] = [0, 0, "  "]
        location = "itemlocation"
        gotitem = True
        mapcls()
        continue
        
      elif movement == "d" or movement == keys.RIGHT:
         objects["Player"] = [15, 14, "🅿 "]
         location = "righthall"
         mapcls()
         continue
        
      elif movement == "w" or movement == keys.UP:
        if gotpokemon == False:
          while True:
              location = "pokeball"
              pokemonchoice = input("fire type, water type, or grass type? ")
              
              if pokemonchoice == "fire" or pokemonchoice == "fire type" or pokemonchoice == "Fire":
                Players_mon = charizard
                gotpokemon = True
                objects["Player"] = [7, 6, "🅿 "]
                objects["PokemonBall1"] = [ 0, 0, "  "]
                mapcls()
                break
                
              if pokemonchoice == "water" or pokemonchoice == "water type" or pokemonchoice == "Water":
                Players_mon = blastoise
                gotpokemon = True
                objects["Player"] = [9, 6, "🅿 "]
                objects["PokemonBall2"] = [ 0, 0, "  "]
                mapcls()
                break
                
              if pokemonchoice == "grass" or pokemonchoice == "grass type" or pokemonchoice == "Grass":
                Players_mon = venusaur
                gotpokemon = True
                objects["Player"] = [11, 6, "🅿 "]
                objects["PokemonBall3"] = [ 0, 0, "  "]
                mapcls()
                break
        else: 
            print("only one pokemon.")
      else: 
        print("can't move there")
  
    if location == "pokeball":
      if movement == "s" or movement == keys.DOWN:
        objects["Player"] = [8, 14, "🅿 "]
        location = "lefthall"
        mapcls()
      else:
        print("can't move there.")
        
        
  
    if location == "itemlocation":
      if movement == "d" or movement == keys.RIGHT:
        objects["Player"] = [8, 14, "🅿 "]
        location = "lefthall"
        mapcls()
      else:
        print("can't move there.")

    if location == "fightspot":
      mapcls()
      if movement == "a" or movement == keys.LEFT:
        objects["Battle"] = [17, 14, "🅿 "]
        location = "lefthall"
        mapcls()
      else:
        print("can't move there.")
        
from replit import audio
def audioplay():
  source = audio.play_file("101-opening.mp3")

def main():
  
  introprint()
  audioplay()
  introprint2()
  mapout(location)


if __name__ == "__main__":
  main()