#!/usr/bin/env python3

import sys

LOOKUP = { 'F': '0', 'B': '1', 'L': '0', 'R': '1' }

def parse(passid):
  row, col = passid[:7], passid[7:]
  row = int(''.join(LOOKUP[x] for x in row), 2)
  col = int(''.join(LOOKUP[x] for x in col), 2)
  return row, col

def calculate_id(seat):
  row, col = seat
  return row * 8 + col


def main(args):
  if len(args) != 2:
    sys.exit(f'usage: #{args[0]} <input.txt>')

  with open(args[1]) as f:
    seats = [calculate_id(parse(pass_id.strip())) for pass_id in f]

  seats.sort()
  print('Part 1:')
  print(seats[-1])

  print('Part 2')
  for a, b in zip(seats, seats[1:]):
    if a+1 != b:
      print(a+1)

if __name__ == '__main__':
  main(sys.argv)
