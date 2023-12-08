#!/usr/bin/env python3

import sys
from absl import app

def parse_input(line):
  p1, p2 = line.split()
  return ord(p1) - ord('A'), ord(p2) - ord('X')

# A, X = Rock
# B, Y = Paper
# C, Z = Scissors

#                lose, draw, win
def evaluate(pair):               # Opponent play:
  play_matrix = ((2,   0,    1),  # Rock
                 (0,   1,    2),  # Paper
                 (1,   2,    0))  # Scissors
  play_names = [ 'rock', 'paper', 'scissors' ]
  outcome_names = [ 'lose', 'draw', 'win', ]
  outcome_score = [ 0, 3, 6 ]
  print(f'opponent play: {play_names[pair[0]]}\noutcome: {outcome_names[pair[1]]}')
  play = play_matrix[pair[0]][pair[1]]
  print(f'play: {play_names[play]}')
  print(f'{1 + play} + {outcome_score[pair[1]]} = {1 + play + outcome_score[pair[1]]}')
  print()
  return 1 + play + outcome_score[pair[1]]


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
