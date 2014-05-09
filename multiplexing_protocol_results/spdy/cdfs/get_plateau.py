import os
import sys
from time import sleep

link_speeds = [0.2, 0.34199519, 0.58480355, 1, 1.70997595, 2.92401774, 5, 8.54987973, 14.62008869, 25]
delays = [300]

for link_speed in link_speeds:
    for delay in delays:
        site = "replay_summary_" + str(link_speed) + "Mbps_" + str(delay) + "ms.txt" 
        sys.stdout.write(str(link_speed) + " ")
        sys.stdout.flush()
        os.system("python 90.py " + site)
