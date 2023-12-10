#!/usr/bin/env python3

from grid import Grid
from pprint import pprint
import functools, re, sys, unittest


class PipeGrid(Grid):
  def find_adjacent(self, point):
    val = self.get(point)
    if val == '7':
      return [self.left(point), self.down(point)]
    elif val == '|':
      return [self.up(point), self.down(point)]
    elif val == 'J':
      return [self.up(point), self.left(point)]
    elif val == '-':
      return [self.left(point), self.right(point)]
    elif val == 'L':
      return [self.up(point), self.right(point)]
    elif val == 'F':
      return [self.down(point), self.right(point)]

  def find_path(self, prev, current):
    if self.get(current) == 'S':
      return 1
    options = self.find_adjacent(current)
    if options[0] == prev:
      next_point = options[1]
    elif options[1] == prev:
      next_point = options[0]
    else:
      raise Exception("Previous point wasn't found.")
    self.mark('green', current)
    return 1 + self.find_path(current, next_point)

  def begin(self, start):
    up = self.up(start)
    down = self.down(start)
    left = self.left(start)
    right = self.right(start)

    if self.get(up) != '.':
      return up
    if self.get(down) != '.':
      return down
    if self.get(left) != '.':
      return left
    if self.get(right) != '.':
      return right

def main(files):
  for fname in files:
    with open(fname) as f:
      grid = PipeGrid(f)
    grid.mark('yellow', lambda _, v: v == 'S')

    start = grid.find('S')[0]
    first_step = grid.begin(start)
    path_length = grid.find_path(start, first_step)
    print(grid)
    print(path_length/2)


if __name__ == '__main__':
  sys.setrecursionlimit(40000)
  main(sys.argv[1:])
