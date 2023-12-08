#!/usr/bin/env python3

import sys
from pprint import pprint
from functools import reduce


class Grid(object):
  def __init__(self, lines):
    self.grid = []
    for line in lines:
      self.parse(line)

  def parse(self, line):
    self.grid.append([x == '#' for x in line])
    self.grid_width = len(self.grid[-1])

  def evaluate(self, dx, dy):
    x, y, count = 0, 0, 0
    while y < len(self.grid):
      self.print_row(x, y)
      if self.grid[y][x]:
        count += 1
      x += dx
      x = x % self.grid_width
      y += dy
    return count

  def print_row(self, x, y):
    row = [ '#' if x else '.' for x in self.grid[y]]
    row[x] = '@'
    row = ''.join(row)
    print(row)


def main(args):
  if len(args) != 2:
    sys.exit(f'usage: #{args[0]} <input.txt>')

  with open(args[1]) as f:
    lines = [l.strip() for l in f]

  grid = Grid(lines)
  results = [
    grid.evaluate(1, 1),
    grid.evaluate(3, 1),
    grid.evaluate(5, 1),
    grid.evaluate(7, 1),
    grid.evaluate(1, 2),
    ]
  pprint(results)
  print(reduce(lambda x,y: x*y, results))


if __name__ == '__main__':
  main(sys.argv)
