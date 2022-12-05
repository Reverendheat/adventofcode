from aoc.twotwo.utils.reader import file_reader
from aoc.twotwo.day5.input import CRATE_STACKS

def get_top_items() -> str:
  output = ""
  for _,v in CRATE_STACKS.items():
    output += v[0]
  return output

def move(source: str, dest: str):
  CRATE_STACKS[dest].insert(0,CRATE_STACKS[source].pop(0))

def parse_input(line: str):
  split = line.split()
  return [v for v in split if split.index(v) % 2 != 0]

def part_one(path: str):
  for line in file_reader(path):
    amount, source, dest = parse_input(line)
    for i in range(int(amount)):
      move(source, dest)
  
  print(get_top_items())