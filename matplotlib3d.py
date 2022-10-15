# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 17:23:51 2022

@author: Max-Louis
"""
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111, projection='3d')

ax.scatter(2,3,4) # plot the point (2,3,4) on the figure

plt.show()