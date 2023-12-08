#!/usr/bin/env python3

import sys

class Password(object):
  def __init__(self, s):
    policy, self.password = s.strip().split(': ')
    policy_range, self.policy_char = policy.split(' ')
    self.policy_range = [int(x) for x in policy_range.split('-')]

  def evaluate(self):
    matches = self.password.count(self.policy_char)
    if ((matches >= self.policy_range[0]) and
        (matches <= self.policy_range[1])):
      return True
    else:
      return False

  def evaluate_stupid(self):
    c1 = self.password[self.policy_range[0]-1]
    c2 = self.password[self.policy_range[1]-1]
    chars = [c1, c2]
    matches = [x == self.policy_char for x in chars]
    return sum(matches) == 1


  def __repr__(self):
    policy = '-'.join(map(str, self.policy_range))
    return f'Password<"{policy} {self.policy_char}: {self.password}">'


def main(args):
  if len(args) != 2:
    sys.exit(f'usage: {args[0]} <input-file.txt>')
  with open(args[1]) as f:
    passwords = [Password(x) for x in f]
  matching_passwords = [p for p in passwords if p.evaluate()]
  print('part 1 solution:')
  print(len(matching_passwords))

  stupid = [p.evaluate_stupid() for p in passwords]
  print('part 2 solution:')
  print(sum(stupid))


if __name__ == '__main__':
  main(sys.argv)
