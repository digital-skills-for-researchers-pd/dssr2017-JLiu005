import glob, os

#Set directory of file to search for processes

os.chdir(os.path.expanduser("~/Desktop/process_manager/processes"))

#Set file types to be found
types = ('*.py', '*.sh')

#Add found files into list

process_list = []
for files in types:
    process_list.extend(glob.glob(files))

#Print list
print (process_list)


#NOTES:
#process_list =[]
#process_list.append(..)
#for proc in process_list:
#	run(proc)
#numbers = [1,2,3]
#for num in numbers:
#	print(num)
