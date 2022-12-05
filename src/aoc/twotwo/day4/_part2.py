from aoc.twotwo.utils.reader import file_reader

def hypen_to_list(s: str) -> list[int]:
  start, end = s.split("-")
  if start == end:
    return [int(start)]
  return list(range(int(start), int(end) + 1))

def overlaps(smaller: list, bigger: list) -> bool:
  for i in smaller:
    if i in bigger:
      return True
  return False

def part_two(path: str):
  total = 0
  for line in file_reader(path):
    group1, group2 = line.split(",")
    l1 = hypen_to_list(group1)
    l2 = hypen_to_list(group2)
    if len(l1) < len(l2):
      if overlaps(l1, l2):
        total += 1
    else:
      if overlaps(l2, l1):
        total += 1
  print(total)