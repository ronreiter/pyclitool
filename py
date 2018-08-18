#!/usr/bin/env python
import os, sys
import re
import argparse

parser = argparse.ArgumentParser(description='pyclitool is a command line utility that allow you to map/filter/reduce'
                                             'your input with a Python one liner, line by line.\n'
                                             'On map and filter functions, the variable x represents the input.\n'
                                             'On a reduce function, the variables x and y represent the input.')
parser.add_argument('mapfunc', nargs='+', help='The map function')

parser.add_argument('-s', '--skip', action='store_true', help='skip first line')
parser.add_argument('-r', '--reduce', action='store_true', help='run a reduce command')
parser.add_argument('-f', '--filter', action='store_true', help='run a filter command')
args = parser.parse_args()

mapfunc = " ".join(args.mapfunc)

if args.skip:
    sys.stdin.readline()

if args.reduce:
    y = sys.stdin.readline().rstrip('\n')

    for x in sys.stdin:
        y = eval(mapfunc, {'x': x.rstrip('\n'), 'y': y}, {'re': re})

    print(y)

elif args.filter:
    for x in sys.stdin:
        output = eval(mapfunc, {'x': x.rstrip('\n')}, {'re': re})
        if output:
            print(x)

else:

    for x in sys.stdin:
        output = eval(mapfunc, {'x': x.rstrip('\n')}, {'re': re})
        if output is not None:
            print(output)

