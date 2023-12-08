#!/usr/bin/env python3
import sys
from pprint import pprint

def parse(line):
  card, body = line.split(': ')
  number_string, winner_string = body.split(' | ')
  numbers = set(int(x) for x in number_string.strip().split(' ') if x)
  winners = set(int(x) for x in winner_string.strip().split(' ') if x)
  count = 0
  for n in numbers:
    if n in winners:
      count += 1
  return { 'id': id,
           'numbers': numbers,
           'winners': winners,
           'count': count,
           'instances': 1,
           }


def main(files):
  for fname in files:
    with open(fname) as f:
      cards = [parse(line) for line in f]

    for i, card in enumerate(cards):
      for j in range(1, card['count']+1):
        cards[i+j]['instances'] += card['instances']

    instances = [c['instances'] for c in cards]
    pprint(instances)
    print(f'Total card count: {sum(instances)}')



if __name__ == '__main__':
  main(sys.argv[1:])
