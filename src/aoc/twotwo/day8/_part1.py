from aoc.twotwo.utils.reader import file_reader

def visible_north(forest: list[list[str]], treeline_idx: int, tree_idx: int) -> bool:
  next_treeline_idx = treeline_idx - 1
  while next_treeline_idx >= 0:
    if forest[next_treeline_idx][tree_idx] >= forest[treeline_idx][tree_idx]:
      return False
    next_treeline_idx -= 1
  return True

def visible_south(forest: list[list[str]], treeline_idx: int, tree_idx: int) -> bool:
  next_treeline_idx = treeline_idx + 1
  while next_treeline_idx < len(forest):
    if forest[next_treeline_idx][tree_idx] >= forest[treeline_idx][tree_idx]:
      return False
    next_treeline_idx += 1
  return True

def visible_east(forest: list[list[str]], treeline_idx: int, tree_idx: int) -> bool:
  next_tree_idx = tree_idx + 1
  while next_tree_idx < len(forest[treeline_idx]):
    if forest[treeline_idx][next_tree_idx] >= forest[treeline_idx][tree_idx]:
      return False
    next_tree_idx += 1
  return True

def visible_west(forest: list[list[str]], treeline_idx: int, tree_idx: int) -> bool:
  next_tree_idx = tree_idx - 1
  while next_tree_idx >= 0:
    if forest[treeline_idx][next_tree_idx] >= forest[treeline_idx][tree_idx]:
      return False
    next_tree_idx -= 1
  return True

def part_one(path: str):
  forest = []
  visible_trees = 0
  for line in file_reader(path):
    forest.append(line)
  for treeline_idx in range(len(forest)):
    for tree_idx in range(len(forest[treeline_idx])):
      if visible_north(forest, treeline_idx, tree_idx):
        visible_trees += 1
      elif visible_south(forest, treeline_idx, tree_idx):
        visible_trees += 1
      elif visible_east(forest, treeline_idx, tree_idx):
        visible_trees += 1
      elif visible_west(forest, treeline_idx, tree_idx):
        visible_trees += 1
  print(visible_trees)