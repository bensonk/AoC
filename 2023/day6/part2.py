#!/usr/bin/env python3
import sys
from pprint import pprint

def compute_distances(time):
  res = []
  for i in range(1, time):
    res.append(i * (time - i))
  return res

def product(l):
  res = 1
  for i in l:
    res = res * i
  return res


def main(files):
  for fname in files:
    with open(fname) as f:
      time, distance = [int(l.split(':')[1].replace(' ', '')) for l in f]
      results = [s for s in compute_distances(time) if s > distance]
      print(len(results))


if __name__ == '__main__':
  main(sys.argv[1:])
