import os
import sys
from time import sleep

link_speeds = [25]
delays = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]

for link_speed in link_speeds:
    for delay in delays:
        site = "quic_replay_summary_" + str(link_speed) + "Mbps_" + str(delay) + "ms.txt" 
        sys.stdout.write(str(delay) + " ")
        sys.stdout.flush()
        os.system("python median.py " + site)
