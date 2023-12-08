#!/usr/bin/env python3

import sys


def pairs(fs):
  a = int(fs.readline())
  for b in fs:
    b = int(b)
    yield a, b
    a = b

def main(fname):
  with open(fname) as f:
    count = 0
    for a, b in pairs(f):
      if b > a:
        count += 1
  print(count)


if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.exit("Usage: {} <inputfile>")
  main(sys.argv[1])
