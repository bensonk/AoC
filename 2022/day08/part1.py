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
  for line, viz in zip(grid, visibility):
    for height, v in zip(line, viz):
      print(termcolor.colored(height, 'green' if v else 'red'), end='')
    print()


def scenic_score(row, col, grid):
  tree = grid[row][col]
  viz = [[False for x in r] for r in grid]

  # Right
  right = len(grid[0])
  for i in range(col, len(grid[0])):
    if tree <= grid[row][i]:
      right = i
      break
    else:
      viz[row][i] = True

  # Left
  left = 0
  for i in range(col, 0, -1):
    if tree <= grid[row][i]:
      left = i
      break
    else:
      viz[row][i] = True

  # Top
  top = i, 0
  for i in range(row, 0, -1):
    if tree <= grid[i][col]:
      top = i
      break
    else:
      viz[i][col] = True

  # Bottom
  bottom = i, len(grid)
  for i in range(row, len(grid)):
    if tree <= grid[i][col]:
      bottom = i
      break
    else:
      viz[i][col] = True

  display(grid, viz)
  return top * right * bottom * left


def compute_visibility(grid, visibility):
  # Horizontal
  for line, viz in zip(grid, visibility):
    tallest = -1
    for i, tree in enumerate(line):
      if tree > tallest:
        viz[i] = True
        tallest = tree
    tallest = -1
    for i, tree in reversed(list(enumerate(line))):
      if tree > tallest:
        viz[i] = True
        tallest = tree

  # Vertical
  for col in range(len(grid[0])):
    tallest = -1
    for row in range(len(grid)):
      tree = grid[row][col]
      if tree > tallest:
        visibility[row][col] = True
        tallest = tree
    tallest = -1
    for row in reversed(range(len(grid))):
      tree = grid[row][col]
      if tree > tallest:
        visibility[row][col] = True
        tallest = tree


def count_visible(visibility):
  total = 0
  for row in visibility:
    total += len([x for x in row if x])
  return total


def main(args):
  with open(FLAGS.file) as f:
    lines = [l.strip() for l in f]
  grid = [[int(i) for i in line] for line in lines]
  visibility = [[False for i in line] for line in lines]
  display(grid, visibility)
  print()
  compute_visibility(grid, visibility)
  display(grid, visibility)
  print(f'Total visible trees: {count_visible(visibility)}')


if __name__ == '__main__':
  app.run(main)
