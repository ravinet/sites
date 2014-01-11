import os
import sys

site_list = sys.argv[1]

with open(site_list) as f:
    for line in f:
        folder = line.split(" ")[1].strip("\n")
        os.system( "du -hbs " + folder + " >> page_sizes.txt" )
