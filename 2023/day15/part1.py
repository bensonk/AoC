#!/usr/bin/env python3

from pprint import pprint
import functools, re, sys, unittest

def hsh(s):
  v = 0
  for c in s:
    v += ord(c)
    v *= 17
    v %= 256
  return v

def main(files):
  for fname in files:
    with open(fname) as f:
      lines = [l.strip().split(',') for l in f]
    strings = sum(lines, [])
    hashes = [hsh(l) for l in strings]
    pprint(list(zip(strings, hashes)))
    print(f'Sum of hashes: {sum(hashes)}')


if __name__ == '__main__':
  main(sys.argv[1:])
