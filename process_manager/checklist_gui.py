from tkinter import *
from utility import * 
import sys, glob, os, subprocess, datetime


#Set directory of processes
HOME_PATH = os.path.dirname(os.path.abspath(__file__))
PRCS_PATH = HOME_PATH + '/processes/'

#Search directory for processes of certain file types
process_list = find_scripts(PRCS_PATH)

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)
if __name__ == '__main__':
   root = Tk()


lng = Checkbar(root, process_list)
lng.pack(side=TOP,  fill=X)
lng.config(relief=GROOVE, bd=2)

#Runs selected processes upon clicking 'Run Processes' button
def allstates(): 
	state = list(lng.state())
	for i in range(len(state)):
		if state[i] == 1:
			run_program(PRCS_PATH + process_list[i])
			with open(HOME_PATH + '/data_output/process_completion_log', 'a') as f:
				print(str(datetime.datetime.now()) + " "+ PRCS_PATH + process_list[i], file=f)

	print("Processes finished running")

Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
Button(root, text='Run Processes', command=allstates).pack(side=RIGHT)
root.mainloop()


##NOTES

#process_list = ['a1.py','a2.py','a3.py']
#state = list(lng.state())
#state = [0,0,1]


#PF_PATH = "~/Desktop/process"
#for i in range(len(state)):
#    if state[i] is 1:
#        print("cd "+ PF_PATH +"; python " + process_list[i])

#Launch subprocess using bash shell
#subprocess.call("exit 1", shell=True)



