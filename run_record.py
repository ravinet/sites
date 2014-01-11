import os
import sys

site_list = sys.argv[1]

results = open("record_info.txt", 'a')

with open(site_list) as f:
    for line in f:
        site = line
        site_parts = site.split( "." )
        if ( site_parts[ 0 ] == "www" ):
            record_folder = site_parts[ 1 ]
        else:
            record_folder = site_parts[ 0 ]
        os.system( "recordshell " + record_folder + " /usr/bin/python /home/ravi/mahimahi/load_page.py " + site.strip("\n") + " record" )
        results.write( site.strip("\n") + " " + record_folder + "\n" ) 
