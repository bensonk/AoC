#!/usr/bin/env python3
import sys
from pprint import pprint
import functools
import unittest

hand_order = dict(zip([
    '',
    'high card',
    'one pair',
    'two pairs',
    'three of a kind',
    'full house',
    'four of a kind',
    'five of a kind',
    ], range(50)))
card_order = dict(zip(reversed('AKQJT98765432'), range(50)))

def hand_type(counts):
  values = tuple(sorted(counts.values()))
  if values == (5):
    return 'five of a kind'
  elif values == (1, 4):
    return 'four of a kind'
  elif values == (2, 3):
    return 'full house'
  elif values == (1, 1, 3):
    return 'three of a kind'
  elif values == (1, 2, 2):
    return 'two pairs'
  elif values == (1, 1, 1, 2):
    return 'one pair'
  else:
    return 'high card'

def count(cards):
  counts = {}
  for c in cards:
    if c not in counts:
      counts[c] = 0
    counts[c] += 1
  return counts

def parse_hand(l):
  cards, bid = l.split()
  counts = count(cards)
  t = hand_type(counts)

  return {
      'cards': cards,
      'counts': counts,
      'bid': int(bid),
      'type': t,
      'score': hand_order[t]
      }

def compare_hands(left, right):
  if left['score'] == right['score']:
    for a, b in zip(left['cards'], right['cards']):
      a = card_order[a]
      b = card_order[b]
      if a > b:
        return 1
      elif b > a:
        return -1
    return 0
  elif left['score'] > right['score']:
    return 1
  else:
    return -1

def main(files):
  for fname in files:
    with open(fname) as f:
      hands = [parse_hand(l) for l in f]
      hands = sorted(hands, key=functools.cmp_to_key(compare_hands))
      winnings = [(r+1)*h['bid'] for r, h in enumerate(hands)]
      pprint(hands)
      print(winnings)
      print(f'Winnings: {sum(winnings)}')

class CamelCardsTests(unittest.TestCase):
  def setUp(self):
    self.f = [
        '32T3K 765',
        'T55J5 684',
        'KK677 28',
        'KTJJT 220',
        'QQQJA 483',
        ]
    self.hands = [parse_hand(l) for l in self.f]

  def test_types(self):
    types = [h['type'] for h in self.hands]
    print(types)
    assert types == [ 'one pair', 'three of a kind', 'two pairs', 'two pairs', 'three of a kind' ]

  def test_order(self):
    hands = sorted(self.hands, key=functools.cmp_to_key(compare_hands))
    cards = [c['cards'] for c in hands]
    print(cards)
    assert cards == ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA', ]

if __name__ == '__main__':
  main(sys.argv[1:])
