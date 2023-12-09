#!/usr/bin/env python3

from pprint import pprint
import functools, re, sys, unittest

def parse(line):
  return [int(x) for x in line.split()]

def all_zeros(seq):
  for x in seq:
    if x != 0:
      return False
  return True

def find_next(seq, depth=0):
  diffs = [b - a for a, b in zip(seq, seq[1:])]
  if all_zeros(diffs):
    return seq[0]
  else:
    return seq[0] - find_next(diffs)


def main(files):
  for fname in files:
    with open(fname) as f:
      lines = list(map(parse, f))

    nexts = [find_next(l) for l in lines]
    print(nexts)
    print(f'Sum: {sum(nexts)}')

class MapsTest(unittest.TestCase):
  def setUp(self):
    pass

  def test_stuff(self):
    pass

if __name__ == '__main__':
  main(sys.argv[1:])
