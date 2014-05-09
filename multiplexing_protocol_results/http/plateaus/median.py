import os
import sys
from array import *
import numpy

#If P(x) is CDF that is age of fish in lake, then P(10) is probability random fish is 10 or less months old.


replay_summary = sys.argv[1]
times = []
with open(replay_summary) as f:
    for line in f:
        times.append(int(line.split(" ")[1].strip("\n")))

#times is list of page load times...now for each, we iterate through and find number of those that are less or equal and divide by total

print numpy.median(times)
