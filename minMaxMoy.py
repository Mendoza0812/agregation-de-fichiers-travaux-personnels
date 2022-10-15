# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 19:16:12 2022

@author: Max-Louis

CHERCHER SUR GOOGLE = PANDAS MATPLOTLIB
"""

import pandas as pd
#import matplotlib.pyplot as plt

val1009 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\val1009.csv')
mot2 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\mot2MoyMinMax.csv')
spCar = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\spCarMoyMinMax.csv')

numMot2 = mot2['numero']
valsurNb = mot2['valsurNb']
valMin = mot2['valMin']
valMax = mot2['valMax']
var = 0
nb1 = 0
listeMoy1 = []
listeMin1 = []
listeMax1 = []

for loop in range (45990):
    varMoy = valsurNb[var]
    varMin = valMin[var]
    varMax = valMax[var]
    if numMot2[var] == 1:
        nb1 += 1
        listeMoy1.append(varMoy)
        listeMin1.append(varMin)
        listeMax1.append(varMax)
    var += 1
    
products_list = (listeMoy1, listeMin1, listeMax1)
df1 = pd.DataFrame (products_list).transpose()
df1.columns = ['Moy','Min','Max']

