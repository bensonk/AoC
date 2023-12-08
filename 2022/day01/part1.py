#!/usr/bin/env python3

import sys
from absl import app

def parse_input(fname):
  with open(fname) as f:
    lines = [x.strip() for x in f]
    groups = []
    current_group = []
    for line in lines:
      if line:
        current_group.append(int(line))
      else:
        groups.append(current_group)
        current_group = []
    if current_group:
      groups.append(current_group)
  return groups


def process_file(fname):
  groups = parse_input(fname)
  print(max(map(sum, groups)))


def main(args):
  if len(args) != 2:
    sys.exit(f'Usage: {args[0]} <inputfile>')
  process_file(args[1])


if __name__ == '__main__':
  app.run(main)
