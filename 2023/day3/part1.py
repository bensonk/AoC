#!/usr/bin/env python3
from pprint import pprint
import sys

symbols = {'#', '$', '%', '&', '*', '+', '-', '/', '=', '@'}

def find_numbers(line, line_number):
  numbers = []
  i = 0
  while i < len(line):
    if line[i].isdigit():
      start = i
      while line[i].isdigit():
        i += 1
      numbers.append(((line_number, start), (line_number, i-1)))
    i += 1
  return numbers

def get_value(coord, grid):
  s = ''
  for i in range(coord[0][1], coord[1][1]+1):
    s += grid[coord[0][0]][i]
  return int(s)

def enumerate_adjacent_cells(coords):
  yield (coords[0][0], coords[0][1]-1)
  yield (coords[1][0], coords[1][1]+1)
  for i in range(coords[0][1]-1, coords[1][1]+2):
    yield (coords[0][0]-1, i)
  for i in range(coords[0][1]-1, coords[1][1]+2):
    yield (coords[0][0]+1, i)

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

def adjacent_cells(coords, grid):
  for coord in enumerate_adjacent_cells(coords):
    if possible_coordinate(coord, grid):
      yield coord

def eligibility_check(coords, grid):
  print(f'Looking for symbols near {coords}')
  for cell in adjacent_cells(coords, grid):
    print(f'Checking cell {cell}')
    if grid[cell[0]][cell[1]] in symbols:
      print(f'Found symbol: {grid[cell[0]][cell[1]]}')
      return True
  return False

def main(files):
  for fname in files:
    with open(fname) as f:
      grid = [list(x.strip()) for x in f]
    pprint(grid)
    number_positions = []
    for i, l in enumerate(grid):
      number_positions.extend(find_numbers(l, i))

    values = []
    for number_coords in number_positions:
      value = get_value(number_coords, grid)
      eligible = eligibility_check(number_coords, grid)
      print(f'{value}: {eligible}  -- {number_coords}')
      if eligible:
        values.append(value)
        
    pprint(values)
    print(f'Result: {sum(values)}')


if __name__ == '__main__':
  main(sys.argv[1:])
