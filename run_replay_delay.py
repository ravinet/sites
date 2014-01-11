import os
import sys
#dirs =  os.listdir(".")
#dirs.remove( "record_info.txt" )
#print dirs

site_list = sys.argv[1]
delay = sys.argv[2]
with open(site_list) as f:
    for line in f:
        site = line.split( " " )[0]
        folder = line.split(" ")[1].strip("\n")
        #os.system( "replayshell /home/ravi/mahimahi/record_all/" + folder + " /usr/local/bin/delayshell " + str(delay) + " /usr/bin/python /home/ravi/mahimahi/load_page.py " + site + " " +  str(delay) + " replay"
        os.system( "replayshell /home/ravi/mahimahi/record_all/" + folder + " /usr/local/bin/delayshell " + str(delay) + " /usr/local/bin/cellshell 12Mbps_trace.txt 12Mbps_trace.txt /usr/bin/python /home/ravi/mahimahi/load_page.py " + site + " " +  str(delay) + " replay")
