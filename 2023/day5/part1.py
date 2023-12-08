#!/usr/bin/env python3
import sys
from pprint import pprint

def get_chunks(f):
  buf = []
  for line in f:
    if line == '\n':
      yield buf
      buf = []
    else:
      buf.append(line.strip())
  yield buf


class MapRange(object):
  def __init__(self, dest, src, length):
    self.dest = dest
    self.src = src
    self.length = length

  def __contains__(self, val):
    if val >= self.src and val <= self.src + self.length:
      return True
    return False

  def __repr__(self):
    return f'MapRange<src: {self.src}, dest: {self.dest}, length: {self.length}>'

  def use(self, val):
    if val not in self:
      raise Exception(f'Uh oh, {val} isn\'t in {self}')
    return val - self.src + self.dest


class Map(object):
  def __init__(self, lines):
    self.name = lines[0].split()[0]
    ranges = [[int(x) for x in l.split()] for l in lines[1:]]
    self.ranges = [MapRange(*l) for l in ranges]

  def __repr__(self):
    return f'Map<name: "{self.name}">'

  def apply(self, val):
    for r in self.ranges:
      if val in r:
        return r.use(val)
    return val


def parse_seeds(line):
  return [int(x) for x in line.split()[1:]]

def parse(f):
  chunks = get_chunks(f)
  seeds = parse_seeds(next(chunks)[0])
  maps = [Map(c) for c in chunks]
  return seeds, maps


def use(value, maps):
  for m in maps:
    value = m.apply(value)
  return value


def main(files):
  for fname in files:
    with open(fname) as f:
      seeds, maps = parse(f)

    print('Seeds:')
    pprint(seeds)
    print('Maps:')
    pprint(maps)

    locations = [use(s, maps) for s in seeds]
    pprint(locations)
    print(f'Min location: {min(locations)}')

if __name__ == '__main__':
  main(sys.argv[1:])
