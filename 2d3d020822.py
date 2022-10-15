# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 04:25:42 2022

@author: Max-Louis
creer une liste dans laquelle sera stockee l index le num de ligne de 
chaque mot
creer une liste qui stocke chaque mot
limiter a 4 pour le 2 dimensions et limiter a 6 pour le 3dimensions
"""

import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/distance18az.csv')
dfL = pd.read_csv(r'C:/Users/Max-Louis/distance18azLower.csv')

limitationNbSyno = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/tsLsMotsSelondistance18az.csv')
refaz18 = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/refaz18.csv')

pour2D = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/pour2D.csv')
pour3D = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/pour3D.csv')

pour2Dsv = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/pour2Dsv.csv')
pour3Dsv = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/pour3Dsv.csv')

nmDLgn3D = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/nmDLgn3D.csv')
numDeLgn2D3D = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/numDeLgn2D3D.csv')

az18Pour2D = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/az18Pour2Dcorrige.csv')
az18Pour3D = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/az18Pour3Dcorrige.csv')

mots = []
numero = []

incr = 0
prec = 0
suiv = 1

for loop in range (len(dfL)):
#for loop in range (2) :
    
    mots.append(dfL.iloc[incr,0])
    numero.append(incr)
    mots.append(dfL.iloc[incr,2])
    numero.append(incr)
    
    incr += 1

plist = (mots, numero)
df2 = pd.DataFrame(plist).transpose()
df2.columns = ['mots', 'numero']
