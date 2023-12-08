#!/usr/bin/env python3
import sys


def parse(line):
  card, body = line.split(': ')
  number_string, winner_string = body.split(' | ')
  numbers = set(int(x) for x in number_string.strip().split(' ') if x)
  winners = set(int(x) for x in winner_string.strip().split(' ') if x)
  count = 0
  for n in numbers:
    if n in winners:
      count += 1
  if count == 0:
    score = 0
  else:
    score = 2 ** (count - 1)
  return { 'id': id,
           'numbers': numbers,
           'winners': winners,
           'count': count,
           'score': score }


def main(files):
  for fname in files:
    with open(fname) as f:
      cards = [parse(line) for line in f]

    scores = [c['score'] for c in cards]
    print(sum(scores))


if __name__ == '__main__':
  main(sys.argv[1:])
