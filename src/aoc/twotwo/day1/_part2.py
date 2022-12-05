from aoc.twotwo.utils.reader import file_reader

def part_two(path: str):
  totals_per_elf = []
  current_val = 0
  for line in file_reader(path):
    if line == "":
      totals_per_elf.append(current_val)
      current_val = 0
    else:
      current_val += int(line)
  s = sorted(totals_per_elf)

  print(sum(s[-3:]))