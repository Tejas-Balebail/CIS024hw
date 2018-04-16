
import sys
import argparse
import sorthelper

parser = argparse.ArgumentParser(description='Sort integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',help='Sorting.')
args = parser.parse_args()
print(sorthelper.sortNumbers(args.integers))