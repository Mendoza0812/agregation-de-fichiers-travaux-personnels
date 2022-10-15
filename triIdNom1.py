# -*- coding: utf-8 -*-
"""
Created on Sun May 22 16:16:22 2022

@author: Max-Louis
"""

import pandas as pd

moncsv1 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')

triIdNom = moncsv1.sort_values(by=['IdNom'])
colByName = triIdNom['IdNom']
colByName100 = colByName[0:]
var0 = 0
var1 = 1
colPrec = colByName100[var0]
colSuiv = colByName100[var1]

colMonCsv1 = moncsv1['IdNom']

idNom = []
nbParu = []


x = 0
y = 0
h = 1
"""
for j in colByName10 :
    for i in colMonCsv1 :
        mot = j
        if i != mot:
            x += 1
        elif i == mot:
            print(mot)
            print(x)
        else:
            print("Innatendu")
    x = 0
"""

for colSuiv in colByName100[1:] :
    colPrec = colByName100.iloc[var0]
    colSuiv = colByName100.iloc[var1]
    if colSuiv != colPrec :
        print(colPrec)
        print(h)
        
        idNom.append(colPrec)
        nbParu.append(h)
        
        h = 1
    elif colSuiv == colPrec :
        h += 1
    else :
        print('Innatendu')
    var0 += 1
    var1 += 1
    
products_list = (idNom, nbParu)
df = pd.DataFrame (products_list).transpose()
df.columns = ['IdNom', 'nbParu']