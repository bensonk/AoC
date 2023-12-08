#!/usr/bin/env python3
import sys

def clean(line):
  digits = [x for x in line if x.isdigit()]
  return int(digits[0] + digits[-1])

def main(files):
  for fname in files:
    with open(fname) as f:
      numbers = [clean(line) for line in f]
      print(numbers)
      print(f'Sum: {sum(numbers)}')


if __name__ == '__main__':
  main(sys.argv[1:])
