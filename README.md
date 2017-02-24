# dssr2017-yliu453

#Project: 	Process Manager 

##Author: 
Yao-Chin (Jonathan) Liu

## Objectives
To create a program with the ability to log and manage bioinformatic pipelines (or other processes).

##Context:	 
A multitude of bioinformatics programs are needed to gather sufficient data for analysis of samples. Manually running and logging these programs is tedious, and may lead to errors after many repetitions. A program could automate this otherwise boring task.

##Features: 	
1) Able to find scripts (bash and python by default) in a given folder 
2) Can create an option list of processes that can be run 
3) Is able to run the programs sequentially 
4) Will create a log file detailing what scripts were run at what time

##Project status:	
Complete

##Possible future directions:	
1) Can specify the input and output files of the processes run	
2) Can find processes at a selected range (potentially up to within the whole computer) 
3) Can designate which part of the processes/programs to be run	
4) Will display the % status of current process	
5) Make Graphical User Interface more aesthetically pleasing

##Dependencies
Python v3.6
	-Tkinter v8.5

##User instructions
1)Download <process_manager> folder
2)Run <master_program.py> with python on the terminal and confirm the presence of a GUI with 2 buttons. Click 'Quit' and confirm it closes
3)Move process scripts into the <processes> folder OR change the DIRECTORY LINE in <checklist_gui.py> to the folder containing the processes to run
4)Run <master_program.py> again. Mulitple processes should show. Check the ones needed and click 'Run Processes'
5)Check the <data_output> directory for the <process_completion_log.txt>. This file contains information of what processes are run and the time they began
6)The message 'Processes finished running' will appear on the terminal when all the designated processes have been run
7)Select more processes to run OR close the program using the 'Quit' button
