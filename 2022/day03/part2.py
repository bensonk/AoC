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

def grouper(items, count=3):
  current = []
  for item in items:
    current.append(item)
    if len(current) == count:
      yield current
      current = []

def value(item):
  if item.islower():
    return 1 + ord(item) - ord('a')
  elif item.isupper():
    return 27 + ord(item) - ord('A')
  logging.fatal(f'Tried to find value of non-letter item: \'{item}\'')

def find_dup_item(knapsacks):
  knapsacks = [set(k) for k in knapsacks]
  overlap = knapsacks[0].intersection(knapsacks[1])
  overlap = overlap.intersection(knapsacks[2])
  logging.info(f'Overlap found: {overlap}')
  if len(overlap) != 1:
    logging.fatal(f'Overlap contained more than one item: {overlap}')

  return list(overlap)[0]


def main(args):
  with open(FLAGS.file) as f:
    knapsacks = [l.strip() for l in f]
  dups = [find_dup_item(k) for k in grouper(knapsacks)]
  pprint(dups)
  values = [value(item) for item in dups]
  pprint(values)
  print(f'\nResult: {sum(values)}')

if __name__ == '__main__':
  app.run(main)
