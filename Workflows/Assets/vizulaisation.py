#!/usr/bin/python
import sys
#importing function from other py files
sys.path.append('/Assets')
import numpy as np
import matplotlib.pyplot as plt


data = [[0,1,0,0,0,4,0,0,0,-1,0],
            [1,0,0,0,0,2,0,0,1,0,0]]

def makeGraph(data):
    fig, ax = plt.subplots()
    ax.matshow(data, interpolation='none', cmap="bwr")
    for (i, j), z in np.ndenumerate(data):
        print (i, j), z
        ax.text(j, i, z, ha='center', va='center')
    plt.show()
