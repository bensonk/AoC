#!/usr/bin/env python3

import re
import sys
from pprint import pprint


class Passport(object):
  def __init__(self, records):
    attributes = [rec.split(':') for rec in records]
    self.attributes = dict(attributes)

  def __repr__(self):
    return f'Passport<{str(self.attributes)}>'

  def validate_byr(self):
    return (1920 <= int(self.attributes['byr']) <= 2002)

  def validate_iyr(self):
    return (2010 <= int(self.attributes['iyr']) <= 2020)

  def validate_eyr(self):
    return (2020 <= int(self.attributes['eyr']) <= 2030)

  def validate_hgt(self):
    hgt = self.attributes['hgt']
    if hgt.endswith('cm'):
      v = int(hgt.rstrip('cm'))
      return 150 <= v <= 193
    else:
      v = int(hgt.rstrip('in'))
      return 59 <= v <= 76
  
  def validate_hcl(self):
    return re.match(r'#[0-9a-f]{6}', self.attributes['hcl'])

  def validate_ecl(self):
    eye_colors = 'amb blu brn gry grn hzl oth'.split()
    return self.attributes['ecl'] in eye_colors

  def validate_pid(self):
    return re.match(r'[0-9]{9}', self.attributes['pid'])


  def valid(self):
    mandatory = [
        'byr',  # Birth Year
        'iyr',  # Issue Year
        'eyr',  # Expiration Year
        'hgt',  # Height
        'hcl',  # Hair Color
        'ecl',  # Eye Color
        'pid',  # Passport ID
        ]
    for field in mandatory:
      if field not in self.attributes:
        return False
    return True

  def extended_valid(self):
    if not self.valid():
      return False

    if not self.validate_byr():
      print(f'{self} failed byr validation')
      return False
    if not self.validate_iyr():
      print(f'{self} failed byr validation')
      return False
    if not self.validate_eyr():
      print(f'{self} failed byr validation')
      return False
    if not self.validate_hgt():
      print(f'{self} failed byr validation')
      return False
    if not self.validate_hcl():
      print(f'{self} failed byr validation')
      return False
    if not self.validate_ecl():
      print(f'{self} failed byr validation')
      return False
    if not self.validate_pid():
      print(f'{self} failed byr validation')
      return False

    return True

def main(args):
  if len(args) != 2:
    sys.exit(f'usage: #{args[0]} <input.txt>')

  with open(args[1]) as f:
    lines = [x.strip() for x in f]

  groups = []
  group = []
  for line in lines:
    if line:
      group.extend(line.split(' '))
    else:
      groups.append(group)
      group = []
  groups.append(group)

  passports = [Passport(x) for x in groups]
  valid = [p for p in passports if p.valid()]
  print(f'Part 1: {len(valid)}')
  extended_valid = [p for p in passports if p.extended_valid()]
  print(f'Part 2: {len(extended_valid)}')


if __name__ == '__main__':
  main(sys.argv)
