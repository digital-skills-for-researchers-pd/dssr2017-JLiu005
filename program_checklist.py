
# coding: utf-8

# In[1]:

#!/usr/bin/python3

from tkinter import *
master = Tk()

def var_states():
   print("QIIME: %d,\nmothur: %d, \nTBD: %d" % (var1.get(), var2.get(), var3.get()))

Label(master, text="Programs available:").grid(row=0, sticky=W)

var1 = IntVar()
Checkbutton(master, text="QIIME", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="mothur", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="TBD", variable=var3).grid(row=3, sticky=W)

Button(master, text='Run', command=var_states).grid(row=4, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=5, sticky=W, pady=4)
mainloop()

