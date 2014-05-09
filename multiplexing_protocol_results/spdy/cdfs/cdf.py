import os
import sys
from array import *

#If P(x) is CDF that is age of fish in lake, then P(10) is probability random fish is 10 or less months old.


replay_summary = sys.argv[1]
times = []
with open(replay_summary) as f:
    for line in f:
        times.append(line.split(" ")[1].strip("\n"))

#times is list of page load times...now for each, we iterate through and find number of those that are less or equal and divide by total


for curr in times:
    lessorequal = 0
    for comp in times:
        if (float(comp) <= float(curr) ):
            lessorequal = lessorequal + 1
    ratio = float(lessorequal)/float(len(times))
    print (curr + " " + str(ratio))
