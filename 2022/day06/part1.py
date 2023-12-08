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

def find_marker(l):
  for i, items in enumerate(zip(l, l[1:], l[2:], l[3:])):
    if len(set(items)) == len(items):
      return 4 + i

def main(args):
  with open(FLAGS.file) as f:
    lines = [l.strip() for l in f]

  for l in lines:
    m = find_marker(l)
    print(m)

if __name__ == '__main__':
  app.run(main)
