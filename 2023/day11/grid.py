#!/usr/bin/env python3

from termcolor import colored

class Grid(object):
  def __init__(self, lines):
    self.grid = [[{'val': x} for x in l] for l in lines]
    self.height = len(self.grid)
    self.width = max(len(l) for l in self.grid)

  def mark(self, color, predicate):
    if type(predicate) == tuple:
      self.set_meta(predicate, 'color', color)
      return

    for x in range(self.width):
      for y in range(self.height):
        coord = (x, y)
        point = self._get((x, y))
        if predicate(coord, point['val']):
          point['color'] = color

  def flood_fill(self, color, start):
    start_d = self._get(start)
    prev_color = start_d['color'] if 'color' in start_d else None
    start_d['color'] = color

    coords = [c for c in (self.up(start), self.down(start), self.left(start), self.right(start)) if c]
    for point in coords:
      target = self._get(point)
      if 'color' in target:
        if (target['color'] == prev_color):
          self.flood_fill(color, point)
      elif (color not in target) and prev_color == None:
        self.flood_fill(color, point)

  def find(self, c):
    positions = []
    for y_inverse, line in enumerate(self.grid):
      for x, point in enumerate(line):
        if point['val'] == c:
          y = self.height - (y_inverse+1)
          positions.append((x, y))
    return positions

  def get_meta(self, point, key):
    return self._get(point)[key]

  def set_meta(self, point, key, val):
    self._get(point)[key] = val

  def _get(self, point):
    return self.grid[self.height-point[1]-1][point[0]]

  def get(self, point):
    return self._get(point)['val']

  def set(self, point, val):
    self._get(point)['val'] = val

  def up(self, point, dist=1):
    if point[1] <= (self.height - dist):
      return point[0], point[1]+dist

  def down(self, point, dist=1):
    if point[1] > 0:
      return point[0], point[1]-dist

  def left(self, point, dist=1):
    if point[0] > 0:
      return point[0]-dist, point[1]

  def right(self, point, dist=1):
    if point[0] <= (self.width - dist - 1):
      return point[0]+dist, point[1]

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
      g.mark('green', lambda _, v: v == 'A')
      print(g)
      g.flood_fill('yellow', (0,0))
      g.flood_fill('blue', (32, 32))
      print(g)

if __name__ == '__main__':
  import sys
  main(sys.argv[1:])
