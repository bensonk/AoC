#!/usr/bin/env python3
from pprint import pprint
import sys

def replace_char(s, i, c):
    return s[:i] + c + s[i+1:]

class Collection(object):
  def __init__(self, line):
    self.springs, clusters = line.strip().split()
    self.clusters = [int(c) for c in clusters.split(',')]

  def __repr__(self):
    return f'Collection<{self.springs}, {self.clusters}>'

  def legal(self, s):
    wildcards = s.count('?')
    springs = s.count('#')
    total_springs = sum(self.clusters)

    if wildcards == 0:
      pass
    if springs > total_springs:
      print(f'Rejecting {s} because too many springs')
      return False
    elif s.count('?') + s.count('#') < total_springs:
      print(f'Rejecting {s} because too few springs')
      return False
    elif s.count('?') + s.count('#') > total_springs:
      return True

    groups = []
    size = 0
    in_group = False
    for c in s:
      if c == '#':
        size += 1
        if not in_group:
          in_group = True
      elif c == '.':
        if in_group:
          in_group = False
          groups.append(size)
          size = 0
    if size > 0:
      groups.append(size)

    for a,b in zip(self.clusters, groups):
      if a != b:
        return False
    return True

  def permutations(self):
    def p(s):
      if not self.legal(s):
        return []
      elif s.count('?') == 0:
        return [s]
      i = s.find('?')
      return p(replace_char(s, i, '.')) + p(replace_char(s, i, '#'))
    
    return p(self.springs)

def main(files):
  for fname in files:
    with open(fname) as f:
      collections = [Collection(line) for line in f]
      for c in collections:
        print(c)
        print(c.permutations())


if __name__ == '__main__':
  main(sys.argv[1:])
