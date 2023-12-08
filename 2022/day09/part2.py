#!/usr/bin/env python3

import sys
from absl import app
from absl import flags
from absl import logging
from pprint import pprint

import pdb

FLAGS = flags.FLAGS
flags.DEFINE_string(
    'file', 'sample2.txt', 'the name of the file to process',
    short_name='f')


def clamp(val, min_value=-1, max_value=1):
  return min(max(val, min_value), max_value)


def distance(head, tail):
  dx = abs(head[0] - tail[0])
  dy = abs(head[1] - tail[1])
  if dx == 1 and dy == 1:
    return False
  if dx + dy < 2:
    return False
  return True

def follow(head, tail):
  d = head[0] - tail[0], head[1] - tail[1]
  if not distance(head, tail):
    return tail
  move = tuple(map(clamp, d))
  return tail[0] + move[0], tail[1] + move[1]


def display(rope, char=None):
  grid = [['.' for _ in range(25)] for _ in range(25)]
  for i, (x, y) in enumerate(rope):
    if i == 0:
      i = char or 'H'
    if grid[y][x] == '.':
      grid[y][x] = char or str(i)
    grid[y][x] = char or str(i)
  for line in reversed(grid):
    print(' '.join(line))


def process(moves):
  tail_positions = []
  move_table = {
      'L': (-1,0),
      'R': (1,0),
      'U': (0,1),
      'D': (0,-1),
      }
  rope = [(0,0) for i in range(10)]

  def move(direction):
    nonlocal rope
    print(f'moving: {direction}')
    vector = move_table[direction]
    rope[0] = rope[0][0] + vector[0], rope[0][1] + vector[1]
    for i in range(1, len(rope)):
      rope[i] = follow(rope[i-1], rope[i])

  for direction, length in moves:
    for i in range(length):
      move(direction)
      tail_positions.append(rope[-1])
      #display(rope)

  return tail_positions


def main(args):
  with open(FLAGS.file) as f:
    lines = [l.strip().split() for l in f]
  moves = [(l[0], int(l[1])) for l in lines]
  pprint(moves)
  tail_positions = process(moves)
  pprint(tail_positions)
  #display(tail_positions)
  print(f'Tail has occupied {len(set(tail_positions))} positions')


if __name__ == '__main__':
  app.run(main)
