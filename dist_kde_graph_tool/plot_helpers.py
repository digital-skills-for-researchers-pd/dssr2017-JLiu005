import os, glob
from csv import reader
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

#Enable colour changes
sns.set(color_codes=True)


#Plots both graph types
def plot_graph(filename):
    data = pd.read_csv(filename)

    for col in data.columns:
        if not data[col].dtype == np.dtype('O') :
 
            #Split title and measurement units
            split_col = col.split(" ")

	    #Label title & axis
            title = split_col[0]
            x_axis = split_col[1]
            dat = data[col]	#Data of column - one dataset
            
            plot_dist(title,x_axis,dat)
            #Repeat graphing steps for KDE graph
            plot_dist_kde(title,x_axis,dat)

            
#Plots distribution graph
def plot_dist(title,x_axis, dat):

    #Set up new figure
    plt.figure()

    #Label title & axis
    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel("Value")

    #Plot graph (Changeable properties)
    sns.distplot(dat, bins=20, kde=False, color = "g", axlabel=False); #change "g" in color to suit preference

    #Define output filename
    output_name = "Output: " + title

    #Save output
    plt.savefig(output_name)
	
    #Close figure
    plt.close()

#Plots distribution graph with kernel density estimation (kde)
def plot_dist_kde(title,x_axis, dat):

    #Set up new figure
    plt.figure()

    #Label title & axis
    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel("Value")

    #Plot graph (Changeable properties)
    sns.distplot(dat, bins=20, kde=True, color = "g", axlabel=False);  #change "g" in color to suit preference

    #Define output filename
    output_name = "Output: " + title + " KDE"

    #Save output
    plt.savefig(output_name)
	
    #Close figure
    plt.close()

#Plot all .csv files in target directory
def plot_dir(directory):
    file_list = find_scripts(directory)
    for filename in file_list:
        plot_graph(filename)

#Find all .csv files in target directory
def find_scripts(location,types = ['*.csv']):
	location= (os.path.expanduser(location))
	os.chdir(location)
	process_list = []
	for files in types:
   		process_list.extend(glob.glob(files))
	process_list.sort()
	return process_list
        
