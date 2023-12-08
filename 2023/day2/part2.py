#!/usr/bin/env python3
from pprint import pprint
import sys

def compute_power(game):
  values = {'red': [], 'green': [], 'blue': []}
  sets = game[1]
  for s in sets:
    for color, count in s.items():
      values[color].append(count)
  r, g, b = max(values['red']), max(values['green']), max(values['blue'])
  return r*g*b

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
    powers = map(compute_power, games)
    print(f'Total power: {sum(powers)}')


if __name__ == '__main__':
  main(sys.argv[1:])
