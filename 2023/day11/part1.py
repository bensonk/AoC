#!/usr/bin/env python3

from grid import Grid
from pprint import pprint
import functools, re, sys, unittest

def expand(lines):
  cols_to_expand = []
  for x in range(len(lines[0])):
    col = [line[x] for line in lines]
    if '#' not in col:
      cols_to_expand.append(x)

  grid = []
  for line in lines:
    new_line = []
    for x, v in enumerate(line):
      if x in cols_to_expand:
        new_line.append(v)
        new_line.append(v)
      else:
        new_line.append(v)
    if '#' not in new_line:
      grid.append(new_line)
    grid.append(new_line)

  return grid


def main(files):
  for fname in files:
    with open(fname) as f:
      lines = [l.strip() for l in f]

    grid = Grid(expand(lines))
    grid.mark('magenta', lambda _, v: v == '#')
    print(grid)

    points = grid.find('#')
    print(points)

    distances = []
    for i, point in enumerate(points):
      for other in points[i:]:
        print(f'Comparing {point} to {other}')
        distances.append(abs(point[0] - other[0]) + abs(point[1] - other[1]))

    pprint(distances)
    print(f'Distance sum: {sum(distances)}')


if __name__ == '__main__':
  main(sys.argv[1:])
