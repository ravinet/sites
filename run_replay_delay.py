import os
import sys
from time import sleep

link_speeds = [0.2, 0.34199519, 0.58480355, 1, 1.70997595, 2.92401774, 5, 8.54987973, 14.62008869, 25]
delays = [rtt / 2 for rtt in [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]]

site_list = sys.argv[1]

for link_speed in link_speeds:
    for delay in delays:
        print "link_speed =", link_speed, ", delay =", delay

        with open(site_list) as f:
            for line in f:
                site = line.split( " " )[0]
                folder = line.split(" ")[1].strip("\n")
                bdp = float(link_speed) * 1000 * 2 * int(delay)
                os.system( "replayshell /home/ravi/sites/" + folder + " /usr/local/bin/delayshell " + str(delay) + " /usr/local/bin/linkshell /home/ravi/sites/" + str(link_speed) + "Mbps_trace.txt /home/ravi/sites/" + str(link_speed) + "Mbps_trace.txt " + str(bdp) + " /usr/bin/python /home/ravi/sites/load_page.py " + site + " " + str(delay) + " " + str(link_speed) + " replay")
