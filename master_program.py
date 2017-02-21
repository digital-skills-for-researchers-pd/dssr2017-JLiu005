###Master program

##Import functions

import os
from dir_utils import * 


##Designate & create directories

#Path to process _manager folder
PM_PATH = '~/Desktop/process_manager'

#Inputdirectory
INDIR = (PM_PATH + "/data_input")
create_directory(INDIR)

#Outputdirectory
OUTDIR = (PM_PATH +"/data_output")
create_directory(OUTDIR)

#Processes directory
PRCSDIR = (PM_PATH + "/processes")
create_directory(PRCSDIR)

#NOTES:

#%s is place holder for string instide 
#>>> egnum  = "11%s"
#>>> print(egnum %("5"))
#115



