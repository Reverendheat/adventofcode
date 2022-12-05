from aoc.twotwo.utils.reader import file_reader

def part_one(path: str):
  INPUT_MAP = {
  "A": "ROCK",
  "B": "PAPER",
  "C": "SCISSORS",
  "X": "ROCK",
  "Y": "PAPER",
  "Z": "SCISSORS"
  }
  GAME_MAP = {
    "SCISSORS": {
      "PAPER": 6,
      "ROCK": 0,
      "SCISSORS": 3,
      "VALUE": 3
    },
    "PAPER": {
      "ROCK": 6,
      "SCISSORS": 0,
      "PAPER": 3,
      "VALUE": 2
    },
    "ROCK": {
      "SCISSORS": 6,
      "PAPER": 0,
      "ROCK": 3,
      "VALUE": 1
    }
  }

  def calc_winner(t:str, u: str):
    return GAME_MAP[INPUT_MAP[u]][INPUT_MAP[t]] + GAME_MAP[INPUT_MAP[u]]["VALUE"]


  total_score = 0
  for line in file_reader(path):
    line = line.strip("\n")
    them, you = line.split()
    total_score += calc_winner(them, you)

  print(total_score)