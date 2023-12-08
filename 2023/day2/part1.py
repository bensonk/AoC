#!/usr/bin/env python3
from pprint import pprint
import sys

def check_possible(game, quantities):
  sets = game[1]
  for s in sets:
    for color, count in s.items():
      if color not in quantities:
        return False
      if count > quantities[color]:
        return False
  return True

def parse_set(s):
  colors = [v.strip() for v in s.split(',')]
  ret = dict()
  for c in colors:
    count, color = c.split(' ')
    ret[color] = int(count)
  return ret

def parse(line):
  game, sets = line.split(':')
  game_id = int(game[5:])
  parsed_sets = [parse_set(x) for x in sets.split(';')]
  return (game_id, parsed_sets)

def main(files):
  for fname in files:
    with open(fname) as f:
      games = [parse(line) for line in f]
    pprint(games)
    possible_games = [g for g in games if check_possible(g, {'red': 12, 'green': 13, 'blue': 14})]
    print('\n\nPossible games:')
    pprint(possible_games)
    possible_ids = [g[0] for g in possible_games]
    print(f'Sum of game IDs: {sum(possible_ids)}')

if __name__ == '__main__':
  main(sys.argv[1:])
