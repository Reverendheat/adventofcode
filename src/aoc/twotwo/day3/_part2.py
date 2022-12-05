from utils.reader import file_reader
from collections import deque
import string

def part_two(path: str):
  total = 0
  all_rucksacks = list(deque(file_reader(path))) 
  elf_group = [all_rucksacks[x:x+3] for x in range(0, len(all_rucksacks), 3)]
  for group in elf_group:
    print(group)
    s1 = set(group[0]).intersection(set(group[1]))
    result_set = s1.intersection(set(group[2]))
    for badge in result_set:
      total += string.ascii_letters.index(badge) + 1
  print(total)