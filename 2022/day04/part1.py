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

def parse(line):
  pair = tuple(tuple(int(x) for x in p.split('-')) for p in line.split(','))
  logging.info(pair)
  return pair

def fully_contained(pair):
  elf1, elf2 = pair
  if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
    return True
  elif elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
    return True
  else:
    return False

def main(args):
  with open(FLAGS.file) as f:
    lines = [l.strip() for l in f]
  pairs = [parse(line) for line in lines]
  contained = [fully_contained(p) for p in pairs]
  logging.info(contained)
  contained_count = len([x for x in contained if x])
  print(f'Fully contained assignements: {contained_count}')

if __name__ == '__main__':
  app.run(main)
