#!/usr/bin/env python3
import sys

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    }


def rightmost(line):
  while line:
    for val in numbers:
      if line.endswith(val):
        return numbers[val]
    line = line[:-1]
  return -1


def leftmost(line):
  while line:
    for val in numbers:
      if line.startswith(val):
        return numbers[val]
    line = line[1:]
  return -1


def numify(line):
  return 10 * leftmost(line) + rightmost(line)


def main(files):
  for fname in files:
    with open(fname) as f:
      numbers = [numify(line) for line in f]
      print(numbers)
      print(f'Sum: {sum(numbers)}')


if __name__ == '__main__':
  main(sys.argv[1:])
