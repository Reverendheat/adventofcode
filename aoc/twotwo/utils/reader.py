from typing import Generator

def file_reader(path: str) -> Generator[str, None, None]:
  o = open(f"./src/aoc2022/{path}")
  lines = o.readlines()
  for line in lines:
    yield line.strip("\n") 
  o.close()