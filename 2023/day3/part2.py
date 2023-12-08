#!/usr/bin/env python3
from termcolor import colored
from pprint import pprint
import sys

def enumerate_adjacent_cells(coord):
  yield (coord[0]-1, coord[1]-1)
  yield (coord[0]-1, coord[1])
  yield (coord[0]-1, coord[1]+1)
  yield (coord[0], coord[1]+1)
  yield (coord[0]+1, coord[1]+1)
  yield (coord[0]+1, coord[1])
  yield (coord[0]+1, coord[1]-1)
  yield (coord[0], coord[1]-1)

def possible_coordinate(coord, grid):
  height = len(grid)
  width = len(grid[0])

  if coord[0] < 0:
    return False
  if coord[1] < 0:
    return False
  if coord[0] >= height:
    return False
  if coord[1] >= width:
    return False
  return True

def adjacent_cells(coord, grid):
  for new_coord in enumerate_adjacent_cells(coord):
    if possible_coordinate(new_coord, grid):
      yield new_coord

def find_gear_symbols(grid):
  for i, line in enumerate(grid):
    for j, value in enumerate(line):
      if value == '*':
        yield (i, j)

def find_gears(grid):
  for coord in find_gear_symbols(grid):
    labels = find_labels(coord, grid)
    if len(labels) == 2:
      yield labels[0] * labels[1], coord

def find_labels(coord, grid):
  labels = set()
  for cell in adjacent_cells(coord, grid):
    if grid[cell[0]][cell[1]].isdigit():
      labels.add(find_number(cell, grid))
  return [l[0] for l in labels]

def find_number(coord, grid):
  line = grid[coord[0]]
  left = coord[1]
  while left >= 0 and line[left].isdigit():
    left -= 1
  if not line[left].isdigit():
    left += 1

  right = coord[1]
  while right < len(line) and line[right].isdigit():
    right += 1
  if not line[right].isdigit():
    right -= 1

  value = int(''.join(line[left:right+1]))
  return (value, (coord[0], left), (coord[0], right))

def display(grid, gears):
  gear_coords = dict()
  for value, coord in gears:
    gear_coords[coord] = value

  for i, line in enumerate(grid):
    for j, c in enumerate(line):
      if c == '*':
        if (i, j) in gear_coords:
          c = colored(c, 'green')
        else:
          c = colored(c, 'red')
      print(c,end='')
    print()


def main(files):
  for fname in files:
    with open(fname) as f:
      grid = [list(x.strip()) for x in f]

    gears = list(find_gears(grid))
    pprint(gears)
    print(sum([g[0] for g in gears]))

    display(grid, gears)



if __name__ == '__main__':
  main(sys.argv[1:])
