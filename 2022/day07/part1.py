#!/usr/bin/env python3

import sys
from absl import app
from absl import flags
from absl import logging
from pprint import pprint

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'file', 'sample.txt', 'the name of the file to process',
    short_name='f')


def parse(line):
  if line.startswith('$'):
    parts = line.split()
    if parts[1] == 'cd':
      return { 'type': 'cd', 'name': parts[2] }
    if parts[1] == 'ls':
      return { 'type': 'ls' }
  else:
    if line.startswith('dir'):
      return { 'type': 'dir', 'name': line.split(' ')[1] }
    else:
      size, name = line.split(' ')
      return { 'type': 'file', 'name': name, 'size': int(size) }


def add_dir(fs, cwd, name):
  current = fs
  for d in cwd:
    current = current[d]
  current[name] = {}


def add_file(fs, cwd, name, size):
  current = fs
  for d in cwd:
    current = current[d]
  current[name] = size


def process(lines):
  fs = {}
  cwd = []
  for line in lines:
    cmd = parse(line)
    if cmd['type'] == 'ls':
      logging.info(f'Command: ls')

    elif cmd['type'] == 'cd':
      if cmd['name'] == '/':
        cwd = []
      elif cmd['name'] == '..':
        cwd.pop()
      else:
        cwd.append(cmd['name'])

      logging.info(f'Command: cd {cmd["name"]} ; cwd = {cwd}')

    elif cmd['type'] == 'dir':
      add_dir(fs, cwd, cmd['name'])
      logging.info(f'added directory {"/".join(cwd)}/{cmd["name"]}')

    elif cmd['type'] == 'file':
      add_file(fs, cwd, cmd['name'], cmd['size'])

  return fs


def compute_total_sizes(fs):
  results = []
  size = 0
  for name, item in fs.items():
    if type(item) == dict:
      subdir_results = compute_total_sizes(item)
      for subdir_name, subdir_size in subdir_results:
        results.append((name + '/' + subdir_name, subdir_size))
      size += subdir_results[-1][1]
    else:
      size += item
  results.append(('', size))
  return results


def main(args):
  with open(FLAGS.file) as f:
    lines = [l.strip() for l in f]
  fs = process(lines)
  pprint(fs)

  sizes = { '/' + r[0]: r[1] for r in compute_total_sizes(fs) }
  pprint(sizes)

  total = 0
  for path, size in sizes.items():
    if size <= 100000:
      total += size
  print(f'Size sum: {total}')


if __name__ == '__main__':
  app.run(main)
