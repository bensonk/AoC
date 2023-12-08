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
      times, distances = [[int(x) for x in l.strip().split()[1:]] for l in f]
      wins = []
      for t, d in zip(times, distances):
        results = [s for s in compute_distances(t) if s > d]
        wins.append(len(results))
      pprint(wins)
      print(product(wins))



if __name__ == '__main__':
  main(sys.argv[1:])
