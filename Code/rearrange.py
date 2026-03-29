import sys

from random import shuffle

inputs = sys.argv[1:]
shuffle(inputs)

print(' '.join(inputs))