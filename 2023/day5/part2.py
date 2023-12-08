#!/usr/bin/env python3
from pprint import pprint
import sys

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

  def domain(self, span):
    return (max(self.src, span[0]), min(self.src+self.length, span[1]))

  def range(self, span):
    return self.use(span[0]), self.use(span[1])


class Map(object):
  def __init__(self, lines):
    self.name = lines[0].split()[0]
    ranges = [[int(x) for x in l.split()] for l in lines[1:]]
    self.ranges = [MapRange(*l) for l in ranges]

  def __repr__(self):
    return f'Map<name: "{self.name}">'



  def spans(self, span):
    domains = [r.domain(span) for r in self.ranges]
    domains.sort(key=lambda x: x[0])

    result = []
    current = span[0]
    for d in domains:
      if current < d[0]:
        result.append((current, d[0]-1))
      current = d[0]
      if span[1] < d[1]:
        break
      result.append((d[0], d[1]))
      current = d[1]+1
    result.append((current, span[1]))

    return result

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


def use_spans(spans, maps):
  if maps == []:
    return spans
  else:
    m = maps[0]
    next_spans = []
    for s in spans:
      next_spans.extend(m.spans(s))

    print(f'Next spans ({len(maps)} left to go):')
    pprint(next_spans)
    print()

    return use_spans(next_spans, maps[1:])


def pairs(l):
  for i in range(len(l)//2):
    yield l[2*i:2*i+2]


def build_spans(input_pairs):
  res = []
  for start, length in input_pairs:
    res.append((start, start+length-1))
  return res


def main(files):
  for fname in files:
    with open(fname) as f:
      seed_ranges, maps = parse(f)
    starting_spans = build_spans(pairs(seed_ranges))
    print('Staring spans:')
    pprint(starting_spans)
    print()

    spans = use_spans(starting_spans, maps)
    starts = [s[0] for s in spans]
    print(f'Min loc: {min(starts)}')
    

if __name__ == '__main__':
  main(sys.argv[1:])
