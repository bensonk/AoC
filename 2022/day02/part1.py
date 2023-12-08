#!/usr/bin/env python3

import sys
from absl import app

def parse_input(line):
  p1, p2 = line.split()
  return ord(p1) - ord('A'), ord(p2) - ord('X')

# A, X = Rock
# B, Y = Paper
# C, Z = Scissors

def evaluate(pair):
  win_matrix = [['tie', 'win', 'loss'],
                ['loss', 'tie', 'win'],
                ['win', 'loss', 'tie']]
  
  outcome_score = { 'win': 6, 'tie': 3, 'loss': 0 }
  return 1 + pair[1] + outcome_score[win_matrix[pair[0]][pair[1]]]


def process_file(fname):
  with open(fname) as f:
    lines = [parse_input(l) for l in f]
  results = list(map(evaluate, lines))
  print(sum(results))

def main(args):
  if len(args) != 2:
    sys.exit(f'Usage: {args[0]} <inputfile>')
  process_file(args[1])


if __name__ == '__main__':
  app.run(main)
