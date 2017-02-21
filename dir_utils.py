#Designate directories

import os

#Designate directory and create if it doesn't exist

def create_directory(location):
	location= (os.path.expanduser(location))
	if not os.path.exists(location):
		os.mkdir(location)

#NOTES:
#(os.expanduser('~/Desktop/') expands ~/ to HOME environment variable

#Check if directory exists, create if not
#if not os.path.exists(directory):
#    os.makedirs(directory)



