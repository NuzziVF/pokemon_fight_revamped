import random

def hit_calc(command, Players_mon):
#  list = [Players_mon.move1, Players_mon.move2, #Players_mon.move3, Players_mon.move4]
#  for element in list:
  if command == Players_mon.move1[6]:
    hit = random.randint(0, 100)
    return int(hit) <= int(Players_mon.move1[1])
  if command == Players_mon.move2[6]:
    hit = random.randint(0, 100)
    return int(hit) <= int(Players_mon.move2[1])
  if command == Players_mon.move3[6]:
    hit = random.randint(0, 100)
    return int(hit) <= int(Players_mon.move3[1])
  if command == Players_mon.move4[6]:
    hit = random.randint(0, 100)
    return int(hit) <= int(Players_mon.move4[1])
  