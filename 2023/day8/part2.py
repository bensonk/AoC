#!/usr/bin/env python3

import functools
from pprint import pprint
import re
import sys
import unittest

class Nav(object):
  def __init__(self, directions):
    self.nodes = {}
    self.directions = [d for d in directions if d in ('L', 'R')]

  def add_link(self, l):
    m = re.match(r'(...) = \((...), (...)\)', l)
    if m:
      src, left, right = m.groups()
      self.nodes[src] = {'L': left, 'R': right}
    else:
      print(f'There was an error, regex didn\'t match line: {l}')

  def dump(self):
    print('digraph nav {')
    for src, dest in self.nodes.items():
      print(f'  {src} -> {dest["L"]};')
      print(f'  {src} -> {dest["R"]};')
    print('}')

  def navigate(self):
    current = [ n for n in self.nodes if n.endswith('A') ]
    steps = 0
    while True:
      for direction in self.directions:
        for i in range(len(current)):
          current[i] = self.nodes[current[i]][direction]
        steps += 1

        incomplete = [n for n in current if not n.endswith('Z')]
        if not incomplete:
          return steps


def main(files):
  for fname in files:
    with open(fname) as f:
      nav = Nav(next(f))
      next(f)
      for l in f:
        nav.add_link(l)
      print(nav.navigate())


class MapsTest(unittest.TestCase):
  def setUp(self):
    pass

  def test_stuff(self):
    pass

if __name__ == '__main__':
  main(sys.argv[1:])
