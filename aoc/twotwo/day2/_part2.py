from aoc.twotwo.utils.reader import file_reader

def part_two(path: str):
  INPUT_MAP = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN"
  }
  GAME_MAP = {
    "SCISSORS": {
      "WIN": ("ROCK",6, 1),
      "LOSE": ("PAPER", 0, 2),
      "DRAW": ("SCISSORS", 3, 3)
    },
    "PAPER": {
      "WIN": ("SCISSORS",6,3),
      "LOSE": ("ROCK",0,1),
      "DRAW": ("PAPER",3,2),
    },
    "ROCK": {
      "WIN": ("PAPER",6, 2),
      "LOSE": ("SCISSORS",0, 3),
      "DRAW": ("ROCK",3, 1),
    }
  }

  def calc_winner(t:str, u: str):
    return GAME_MAP[INPUT_MAP[t]][INPUT_MAP[u]][1] + GAME_MAP[INPUT_MAP[t]][INPUT_MAP[u]][2]

  total_score = 0
  for line in file_reader(path):
    line = line.strip("\n")
    them, you = line.split()
    total_score += calc_winner(them, you)

  print(total_score)