#!/usr/bin/env python3

import sys


def main(fname):
  with open(fname) as f:
    values = [int(line) for line in f]
  count = 0
  for a, b in zip(values, values[1:]):
    if b > a:
      count += 1
  print(count)


if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.exit("Usage: {} <inputfile>")
  main(sys.argv[1])
