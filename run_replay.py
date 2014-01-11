import os
import sys
#dirs =  os.listdir(".")
#dirs.remove( "record_info.txt" )
#print dirs

site_list = sys.argv[1]

with open(site_list) as f:
    for line in f:
        site = line.split( " " )[0]
        folder = line.split(" ")[1].strip("\n")
        os.system( "replayshell /home/ravi/mahimahi/record_all/" + folder + " /usr/bin/python /home/ravi/mahimahi/load_page.py " + site + " replay")
