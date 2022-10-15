# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 00:30:56 2022

@author: Max-Louis
"""
# importing matplotlib module 
from matplotlib import pyplot as plt
import pandas as pd

df10 = pd.read_csv(r'C:/Users/Max-Louis/df10Ref.csv')

dfDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

dfSyneurone = pd.read_csv( r'C:/Users/Max-Louis/df12svRef.csv')

exempleBon = pd.read_csv( r'C:/Users/Max-Louis/exempleBon.csv')

motCible = "bon"
plt.axis([-10, 10, -10, 10])

# x-axis values
xA = [0]
# Y-axis values
yA = [0]
xB = 2
yB = 2
xC = 3
yC = 3
  
# Function to plot scatter
plt.scatter(xA, yA)

pointA = plt.scatter(xA, yA)

pointB = plt.scatter(xB, yB)

pointC = plt.scatter(xC, yC)

plt.legend()
# function to show the plot
plt.show(pointA)
plt.show(pointB)
plt.show(pointC)
