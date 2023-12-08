#!/usr/bin/env python3

import sys


def parse(line):
  return int(line.strip())


def find_pairs(numbers, target):
  for a in numbers:
    for b in numbers:
      if a + b == target:
        yield a, b


def find_triplets(numbers, target):
  for a in numbers:
    for b in numbers:
      for c in numbers:
        if a + b + c == target:
          yield a, b, c


def main(args):
  if len(args) != 2:
    sys.exit(f'usage: {args[0]} <input-file.txt>')
  with open(args[1]) as f:
    numbers = [parse(x) for x in f]
  
  for result in find_pairs(numbers, 2020):
    print(f'{result[0]} * {result[1]} = {result[0] * result[1]}')
  
  for result in find_triplets(numbers, 2020):
    print(f'{result[0]} * {result[1]} * {result[2]} = {result[0] * result[1] * result[2]}')


if __name__ == '__main__':
  main(sys.argv)
