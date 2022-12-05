from aoc.twotwo.utils.reader import file_reader

def part_one(path: str):
  highest_val = 0
  current_val = 0
  for line in file_reader(path):
    if line == "":
      if current_val > highest_val:
        highest_val = current_val
      current_val = 0
    else:
      current_val += int(line)

  print(highest_val)