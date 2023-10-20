#Step 0 download an IDE, like Canopy Enthought Express

#Step 1 download all the associated libraries needed for analysis. Some libraries may already be built into your IDE (Integrated Development Environment)
import csv,numpy as np,matplotlib.mlab as m
from pylab import csv2rec
import matplotlib.pyplot as plt
from pylab import *

# Step 2 Import data and clean Python workspace and close all previously opened graphs.
plt.close("all") # Close all pre-existing graphs
file_path=raw_input("What is the hyperlink of the file you are working in?") # User input for datafile location
data=m.csv2rec(file_path,delimiter=',') # converts csv file into a python rec data file
data=map(list,data) # converts rec file into a mapable list data array
# At this point you will index the data file as an array 
# For example InstalledCost40=np.array([float(i) for i in data[19][1:23]]). Very important to convert data into a np.array aka a numpy.array.

# Step 3 Plot graphs
fig1=plt.figure(1)
# For example Re_25_40,=plt.plot(New_Battery_Cost_40,AvgDBenefit_25_Re_40, color="blue", linewidth=2.5, linestyle="--")
plt.xlabel('xlabel')
plt.ylabel('ylabel')
title='Title'
# Boom graphs and awesomeness for free!