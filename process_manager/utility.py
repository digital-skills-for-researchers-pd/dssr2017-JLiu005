#Designate directories

import os, glob, subprocess

#Designate directory and create if it doesn't exist

def create_directory(location):
	location= (os.path.expanduser(location))
	if not os.path.exists(location):
		os.mkdir(location)

def find_scripts(location,types = ['*.py', '*.sh']):
	location= (os.path.expanduser(location))
	os.chdir(location)
	process_list = []
	for files in types:
   		process_list.extend(glob.glob(files))
	return process_list

#Deciding which interpreter is needed to run the program
def run_program(program):
	if '.py' in program:
		subprocess.call("python " + program, shell = True)
		return True
	elif '.sh' in program:
		subprocess.call("bash " + program, shell = True)
		return True
	else:
		print("Do not know how to run", program)
		return False



#NOTES:
#(os.expanduser('~/Desktop/') expands ~/ to HOME environment variable

#Check if directory exists, create if not
#if not os.path.exists(directory):
#    os.makedirs(directory)

#process_list =[]
#process_list.append(..)
#for proc in process_list:
#	run(proc)
#numbers = [1,2,3]
#for num in numbers:
#	print(num)
