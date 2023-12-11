#!/usr/bin/env python3

from grid import Grid
from pprint import pprint
import functools, re, sys, unittest

def find_empties(lines):
  cols = []
  for x in range(len(lines[0])):
    if '#' not in (line[x]['val'] for line in lines):
      cols.append(x)

  rows = []
  for i, line in enumerate(lines):
    y = len(lines) - i - 1
    if '#' not in [x['val'] for x in line]:
      rows.append(y)

  return cols, rows


def count_tripwires(a, b, xs, ys):
  total = 0
  start = min(a[0], b[0])
  end = max(a[0], b[0])
  for i in range(start, end+1):
    if i in xs:
      total += 1
  start = min(a[1], b[1])
  end = max(a[1], b[1])
  for i in range(start, end+1):
    if i in ys:
      total += 1
  return total * (1000000 - 1)


def main(files):
  for fname in files:
    with open(fname) as f:
      lines = [l.strip() for l in f]

    grid = Grid(lines)
    grid.mark('magenta', lambda _, v: v == '#')

    points = grid.find('#')

    xs, ys = find_empties(grid.grid)
    print(xs)
    print(ys)
    grid.mark('red', lambda p, _: p[0] in xs)
    grid.mark('yellow', lambda p, _: p[1] in ys)

    print(grid)

    distances = []
    for i, point in enumerate(points):
      for other in points[i:]:
        print(f'Comparing {point} to {other}')
        dist = abs(point[0] - other[0]) + abs(point[1] - other[1])
        tw = count_tripwires(point, other, xs, ys)
        print(f'Found {tw} tripwires')
        distances.append(dist+tw)

    print(f'Distance sum: {sum(distances)}')


if __name__ == '__main__':
  main(sys.argv[1:])
