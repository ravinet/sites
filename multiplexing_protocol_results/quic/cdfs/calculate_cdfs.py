import os
import sys
from time import sleep

link_speeds = [0.2, 0.34199519, 0.58480355, 1, 1.70997595, 2.92401774, 5, 8.54987973, 14.62008869, 25]
delays = [rtt / 2 for rtt in [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]]

for link_speed in link_speeds:
    for delay in delays:
        rtt = int(delay)*2
        file_name = "quic_replay_summary_" + str(link_speed) + "Mbps_" + str(rtt) + "ms.txt"
        cdf_name = "cdf_" + str(link_speed) + "_" + str(rtt) + ".txt"
        os.system("python cdf.py " + file_name + " > temp")
        os.system("sort -n -k 2 temp > " + cdf_name)
        os.system("rm temp")
