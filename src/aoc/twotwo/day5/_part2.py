from aoc.twotwo.utils.reader import file_reader
from input import CRATE_STACKS

def get_top_items() -> str:
  output = ""
  for k,v in CRATE_STACKS.items():
    output += v[0]
  return output

def move_multiple(source: str, dest: str, amount: int):
  temp = CRATE_STACKS[source][:amount]
  del CRATE_STACKS[source][:amount]
  for i in range(len(temp) -1, -1, -1):
    CRATE_STACKS[dest].insert(0, temp[i])

def parse_input(line: str):
  split = line.split()
  return [v for v in split if split.index(v) % 2 != 0]

def part_two(path: str):
  for line in file_reader(path):
    amount, source, dest = parse_input(line)
    move_multiple(source, dest, int(amount))
  
  print(get_top_items())