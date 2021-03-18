# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 00:30:03 2020

@author: jinfei
"""

import numpy as np
import pandas as pd

data=pd.read_csv("C:/Users/jinfei/Documents/Python Scripts/project/Caicium imaging/Time Trace.csv")

import matplotlib.pyplot as plt


#Creat a figure and axes (empty)
fig, ax = plt.subplots()

ax.plot(data.iloc[:,1:20], linestyle="--", marker='o', markersize=3) # use iloc to index colum 

ax.set_xlabel("Time (second)")

plt.show()


#small multiples

n_cell=data.shape[1] #calculate how many subplots 
start_time=150

fig, axs = plt.subplots(nrows=n_cell,sharex=True, sharey=False,figsize=(8,17))
#here created two objects: a figure object and an array of axs objects. 

#plot each subplots in a for loop
for n in range(0,n_cell):
    axs[n].plot(data.iloc[:,n], color='b')
    axs[n].set_yticklabels([])
    axs[n].axvline(x=start_time, ymin=0.6, ymax=1, color='r')
    axs[n].axhline(y=data.iloc[0:start_time,n].median(), color='g', linestyle='--')
axs[n_cell-1].set_xlabel("Time (second)")   
   
plt.show()  


#==============================================================================
#scatter plot
'''
fig, axs = plt.subplots(nrows=n_cell,sharex=True, sharey=False,figsize=(8,17))
for n in range(0,n_cell):
    axs[n].scatter(data.iloc[:,n], data.iloc[:,-n], color='b')
    axs[n].set_yticklabels([])
axs[n_cell-1].set_xlabel("Time (second)")   
   
plt.show()  
'''
#==============================================================================
#heatmap plot and plot for the average
fig, axs = plt.subplots(nrows=2, sharex=True)
axs[0].matshow(data.transpose(), aspect='auto', cmap='plasma')
axs[0].axvline(x=start_time, ymin=0, ymax=1, color='g',linestyle='--')
axs[1].set_yticklabels([])
axs[1].plot(data.mean(axis=1))
axs[1].axvline(x=start_time, ymin=0, ymax=1, color='g',linestyle='--')
axs[1].set_yticklabels([])
axs[1].set_xlabel("Time (second)")  
plt.show()

#=============================================================================

