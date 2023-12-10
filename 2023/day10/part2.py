#!/usr/bin/env python3

from grid import Grid
from pprint import pprint
import functools, re, sys, unittest


class PipeGrid(Grid):
  def find_adjacent(self, point):
    val = self.get(point)
    if val == '7':
      return [self.left(point, 2), self.down(point, 2)]
    elif val == '|':
      return [self.up(point, 2), self.down(point, 2)]
    elif val == 'J':
      return [self.up(point, 2), self.left(point, 2)]
    elif val == '-':
      return [self.left(point, 2), self.right(point, 2)]
    elif val == 'L':
      return [self.up(point, 2), self.right(point, 2)]
    elif val == 'F':
      return [self.down(point, 2), self.right(point, 2)]

  def find_path(self, prev, current):
    print(prev, current)
    if self.get(current) == 'S':
      return 1

    options = self.find_adjacent(current)
    print(options)
    if options[0] == prev:
      next_point = options[1]
    elif options[1] == prev:
      next_point = options[0]
    else:
      raise Exception("Previous point wasn't found.")
    self.mark('green', current)
    intermediate = int((current[0]+prev[0])/2), int((current[1]+prev[1])/2)
    self.mark('green', intermediate)
    self.set(intermediate, '+')
    return 1 + self.find_path(current, next_point)

  def begin(self, start):
    up = self.up(start, 2)
    down = self.down(start, 2)
    left = self.left(start, 2)
    right = self.right(start, 2)

    if self.get(up) != '.':
      return up
    if self.get(down) != '.':
      return down
    if self.get(left) != '.':
      return left
    if self.get(right) != '.':
      return right

def expand(text):
  for line in text:
    line = ''.join(x+'`' for x in line.rstrip())
    yield line
    yield '`' * len(line)

def main(files):
  for fname in files:
    with open(fname) as f:
      grid = PipeGrid(expand(f))

    start = grid.find('S')[0]
    first_step = grid.begin(start)
    path_length = grid.find_path(start, first_step)
    print(grid)

    grid.flood_fill('yellow', (0,0))


if __name__ == '__main__':
  sys.setrecursionlimit(40000)
  main(sys.argv[1:])
