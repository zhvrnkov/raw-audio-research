#!/usr/bin/env python

import sys
from numpy import *
from matplotlib.pyplot import *

def subscript(index: int, default):
  try:
    return sys.argv[index]
  except IndexError:
    return default

filename = sys.argv[1]
frames = int(sys.argv[2])
second = int(subscript(3, "0"))
fps = int(subscript(4, "8000"))
position = second * fps

file = open(filename, "rb")
samples = list(bytearray(file.read()))[position:position+frames]

x = linspace(0, len(samples), len(samples))
y = samples
plot(x, y)
show()
