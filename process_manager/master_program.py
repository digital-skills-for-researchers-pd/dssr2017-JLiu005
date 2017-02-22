###Master program

##Import functions

import os, subprocess
from utility import * 


##Designate & create directories

#Path to process _manager folder
HOME_PATH = os.path.dirname(os.path.abspath(__file__))

#Inputdirectory
INDIR = (HOME_PATH + "/data_input")
create_directory(INDIR)

#Outputdirectory
OUTDIR = (HOME_PATH +"/data_output")
create_directory(OUTDIR)

#Processes directory
PRCSDIR = (HOME_PATH + "/processes")
create_directory(PRCSDIR)

run_program(HOME_PATH + '/checklist_gui.py')

#NOTES:

#%s is place holder for string instide 
#>>> egnum  = "11%s"
#>>> print(egnum %("5"))
#115



