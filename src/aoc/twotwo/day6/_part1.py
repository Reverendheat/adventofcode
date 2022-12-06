from aoc.twotwo.utils.reader import file_reader

def has_duplicates(ci: dict[str,int]) -> bool:
  for v in ci.values():
    if v > 1:
      return True
  return False

# I know about collections.Counter, just wanted to implement.
def count_items(char: str, char_list: list[str]) -> dict[str, int]:
  count_dict = {}
  for i in char_list:
    if i not in count_dict:
      count_dict[i] = 0
    count_dict[i] += 1
  return count_dict

def part_one(path: str) -> int | None:
  for line in file_reader(path):
    for i in range(len(line) - 1):
      l = list(line[i:i+4])
      ci = count_items(line[i], l)
      if not has_duplicates(ci):
        print(i+4)
        return i+4