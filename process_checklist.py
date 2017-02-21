from tkinter import *
import sys, glob, os, subprocess

#Set directory of processes
PF_PATH = os.path.expanduser('~/Desktop/process_manager/processes/')

#Search directory for processes of certain file types
os.chdir(PF_PATH)
process_list = glob.glob("*.py")

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
	        subprocess.call("python " + PF_PATH + process_list[i], shell = True)


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



