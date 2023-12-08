#!/usr/bin/env python3

from termcolor import colored

class Grid(object):
  def __init__(self, lines):
    self.grid = [[{'val': x} for x in l.strip()] for l in lines]
    self.height = len(self.grid)
    self.width = max(len(l) for l in self.grid)

  def mark(self, color, predicate):
    for x in range(self.width):
      for y in range(self.height):
        coord = (x, y)
        point = self._get((x, y))
        if predicate(coord, point['val']):
          point['color'] = color

  def get_meta(self, point, key):
    return self.grid[point[1]][point[0]]

  def set_meta(self, point, key, val):
    self.grid[point[1]][point[0]] = val

  def _get(self, point):
    return self.grid[point[1]][point[0]]

  def get(self, point):
    return self.grid[point[1]][point[0]]['val']

  def set(self, point, val):
    self.grid[point[1]][point[0]]['val'] = val

  def __str__(self):
    s = ''
    for line in self.grid:
      for cell in line:
        v = cell['val']
        if 'color' in cell:
          s = s + colored(v, cell['color'])
        else:
          s = s + cell['val']
      s = s + '\n'
    return s

  def __repr__(self):
    return f'Grid<height: {self.height}, width: {self.width}>'

  def display(self):
    print(self)



def main(args):
  for fname in args:
    with open(fname) as f:
      g = Grid(f)
      g.mark('green', lambda _, v: v == '*')
      g.mark('red', lambda _, v: v == '#')
      g.mark('blue', lambda _, v: v == '%')
      g.mark('yellow', lambda _, v: v == '/')
      print(g)

if __name__ == '__main__':
  import sys
  main(sys.argv[1:])
