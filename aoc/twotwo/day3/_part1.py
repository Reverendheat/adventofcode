from utils.reader import file_reader
import string

def part_one(path: str):
  total = 0
  for line in file_reader(path):
    middle_index = int(len(line) / 2)
    first_half = line[:middle_index]
    second_half = line[middle_index:]
    s = set(first_half).intersection(set(second_half))
    for i in s:
      total += string.ascii_letters.index(i) + 1
  print(total)