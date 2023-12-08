#!/usr/bin/env python3

import sys
from absl import app
from absl import flags
from absl import logging
from pprint import pprint

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'file', 'sample.txt', 'the name of the file to process',
    short_name='f')

def process(moves):
  tail_positions = []
  move_table = {
      'L': (-1,0),
      'R': (1,0),
      'U': (0,1),
      'D': (0,-1),
      }
  h = 0, 0
  t = 0, 0

  def add(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]

  def distance(p1, p2):
    x_dist = abs(p1[0] - p2[0])
    y_dist = abs(p1[1] - p2[1])
    return max(x_dist, y_dist)

  def move(direction):
    nonlocal h, t
    new_h = add(move_table[direction], h)
    if distance(new_h, t) > 1:
      t = h
    h = new_h

  for direction, length in moves:
    for i in range(length):
      tail_positions.append(t)
      move(direction)
  tail_positions.append(t)

  return tail_positions


def main(args):
  with open(FLAGS.file) as f:
    lines = [l.strip().split() for l in f]
  moves = [(l[0], int(l[1])) for l in lines]
  pprint(moves)
  tail_positions = process(moves)
  pprint(set(tail_positions))
  print(f'Tail has occupied {len(set(tail_positions))} positions')



if __name__ == '__main__':
  app.run(main)
