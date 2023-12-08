#!/usr/bin/env python3

import sys
from absl import app
from absl import flags
from absl import logging
from pprint import pprint

import termcolor

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'file', 'sample.txt', 'the name of the file to process',
    short_name='f')

def display(grid, visibility):
  print('Grid:')
  for line, viz in zip(grid, visibility):
    for height, v in zip(line, viz):
      print(termcolor.colored(height, 'green' if v else 'red'), end='')
    print()
  print()


def scenic_score(row, col, grid):
  tree = grid[row][col]
  viz = [[False for x in r] for r in grid]
  viz[row][col] = True

  # Right
  right = 0
  for i in range(col+1, len(grid[0])):
    right += 1
    viz[row][i] = True
    if tree <= grid[row][i]:
      break

  # Left
  left = 0
  for i in range(col-1, -1, -1):
    left += 1
    viz[row][i] = True
    if tree <= grid[row][i]:
      break

  # Top
  top = 0
  for i in range(row - 1, -1, -1):
    top += 1
    viz[i][col] = True
    if tree <= grid[i][col]:
      break

  # Bottom
  bottom = 0
  for i in range(row + 1, len(grid)):
    bottom += 1
    viz[i][col] = True
    if tree <= grid[i][col]:
      break

  print(f'visibility:\n\ttop: {top}\n\tright: {right}\n\tbottom: {bottom}\n\tleft: {left}')
  return top * right * bottom * left


def main(args):
  with open(FLAGS.file) as f:
    lines = [l.strip() for l in f]
  grid = [[int(i) for i in line] for line in lines]
  scenic = []
  for i, row in enumerate(grid):
    for j, col in enumerate(row):
      scenic.append(scenic_score(i, j, grid))

  pprint(max(scenic))


if __name__ == '__main__':
  app.run(main)
