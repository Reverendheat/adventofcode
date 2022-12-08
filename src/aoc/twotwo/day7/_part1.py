from __future__ import annotations
from aoc.twotwo.utils.reader import file_reader

class Node:
  def __init__(self, folder_name: str) -> None:
    self.folder_name: str = folder_name
    self.parent: Node | None = None
    self.children: list[Node] = []
    self.size = 0

  def add_child(self, child: Node):
    self.children.append(child)
    child.parent = self


  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level += 1
      p = p.parent
    return level

  def print_tree(self):
    prefix = "-" * self.get_level()
    print(prefix + f"{self.folder_name}:{self.size}")
    if self.children:
      for child in self.children:
        child.print_tree()

  def find_child(self, target):
    if self.children:
      for child in self.children:
        if child.folder_name == target:
          return child
    return self

  def add_size(self, file_size: int):
    self.size += file_size
    p = self.parent
    while p:
      p.size += file_size
      p = p.parent
    

  def calculate_under_100k(self):
    total = 0
    if self.size <= 100000:
      total += self.size
    if self.children:
      for child in self.children:
        total += child.calculate_under_100k()
    return total

root_node = Node("/")

def is_num(line: str):
  try:
    int(line.split()[0])
    return True
  except ValueError:
    return False



def part_one(path: str) -> None:
  current_node: Node = root_node
  for line in file_reader(path):
    if "$ cd " in line:
      if line == "$ cd ..":
        if current_node:
          if current_node.parent:
            current_node = current_node.parent
      else:
        if current_node:
          target_dir = line.split()[2]
          new_node = current_node.find_child(target_dir)
          if new_node is not None:
            current_node = new_node
    elif line.startswith("dir"):
      folder_name = line.split()[1]
      if current_node:
        current_node.add_child(Node(folder_name))
    elif is_num(line):
      file_size = int(line.split()[0])
      if current_node:
          current_node.add_size(file_size)
  root_node.print_tree()
  print(root_node.calculate_under_100k())
