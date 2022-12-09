from aoc.twotwo.utils.reader import file_reader

def scenic_value_north(forest: list[list[str]], treeline_idx: int, tree_idx: int) -> int:
  current_score = 0
  next_treeline_idx = treeline_idx
  while next_treeline_idx > 0:
    next_treeline_idx -= 1
    if forest[next_treeline_idx][tree_idx] >= forest[treeline_idx][tree_idx]:
      current_score += 1
      return current_score
    current_score += 1
  return current_score

def scenic_value_south(forest: list[list[str]], treeline_idx: int, tree_idx: int) -> int:
  next_treeline_idx = treeline_idx
  current_score = 0
  while next_treeline_idx < len(forest) - 1:
    next_treeline_idx += 1
    if forest[next_treeline_idx][tree_idx] >= forest[treeline_idx][tree_idx]:
      current_score += 1
      return current_score
    current_score += 1
  return current_score

def scenic_value_east(forest: list[list[str]], treeline_idx: int, tree_idx: int) -> int:
  next_tree_idx = tree_idx
  current_score = 0
  while next_tree_idx < len(forest[treeline_idx]) - 1:
    next_tree_idx += 1
    if forest[treeline_idx][next_tree_idx] >= forest[treeline_idx][tree_idx]:
      current_score += 1
      return current_score
    current_score += 1
  return current_score

def scenic_value_west(forest: list[list[str]], treeline_idx: int, tree_idx: int) -> int:
  next_tree_idx = tree_idx
  current_score = 0
  while next_tree_idx > 0:
    next_tree_idx -= 1
    if forest[treeline_idx][next_tree_idx] >= forest[treeline_idx][tree_idx]:
      current_score += 1
      return current_score
    current_score += 1
  return current_score

def calc_scenic_score(forest: list[list[str]], treeline_idx: int, tree_idx: int) -> int:
  return (
    scenic_value_north(forest, treeline_idx, tree_idx) *
    scenic_value_west(forest, treeline_idx, tree_idx) *
    scenic_value_south(forest, treeline_idx, tree_idx) *
    scenic_value_east(forest, treeline_idx, tree_idx)
  )

def part_two(path: str):
  forest = []
  highest_scenic_value = 0
  for line in file_reader(path):
    forest.append(line)
  for treeline_idx in range(len(forest)):
    for tree_idx in range(len(forest[treeline_idx])):
      next_scenic_value = calc_scenic_score(forest, treeline_idx, tree_idx)
      if next_scenic_value > highest_scenic_value:
        highest_scenic_value = next_scenic_value
  print(highest_scenic_value)