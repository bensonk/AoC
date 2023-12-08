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

def parse_move(m):
  # move {count} from {source} to {dest}
  parts = m.split(' ')
  count = int(parts[1])
  source = int(parts[3])
  dest = int(parts[5])
  return { 'count': count,
           'source': source,
           'dest': dest }

def parse_state(lines):
  index = 0
  columns = []
  for i, l in enumerate(lines):
    if l.startswith(' 1   2'):
      index = i
      columns = [int(x) for x in l.split()]
      break
  logging.info(f'Found columns: {columns}')

  stacks = {c: [] for c in columns}
  for c in columns:
    column_index = lines[index].index(str(c))
    for row in reversed(lines[0:index]):
      if row[column_index] == ' ':
        break
      stacks[c].append(row[column_index])
  moves = [parse_move(l) for l in lines[index+2:]]
  return stacks, moves

def move(stacks, move):
  logging.info(f'Making move:\n\t{move}')
  start, end = len(stacks[move['source']]) - move['count'], len(stacks[move['source']])
  stacks[move['dest']].extend(stacks[move['source']][start:end])
  del stacks[move['source']][start:end]


def show_state(stacks):
  for k in sorted(stacks.keys()):
    print(f'{k}: ' + ' '.join(stacks[k]))


def main(args):
  with open(FLAGS.file) as f:
    lines = [l for l in f]
  stacks, moves = parse_state(lines)
  print('Initial state: ')
  show_state(stacks)
  print()

  for m in moves:
    move(stacks, m)
    show_state(stacks)
    print()

if __name__ == '__main__':
  app.run(main)
