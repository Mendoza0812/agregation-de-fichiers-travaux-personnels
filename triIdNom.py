# -*- coding: utf-8 -*-
"""
Created on Sun May 22 13:59:40 2022

@author: Max-Louis
triIdNom et moncsv1 ont un nombre différent de ligne.
il faudrait comprendre pourquoi
"""

import pandas as pd

moncsv1 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')

triIdNom = moncsv1.sort_values(by=['IdNom'])
colByName = triIdNom['IdNom']
colTriIdNom = triIdNom[0:]
idNom1 = triIdNom.iloc[1:,0]
var0 = 0
var1 = 1
var2 = 2
colTriVar0 = colByName[var0]
colTriVar1 = colByName[var1]
colTriVar02 = colByName[var0:var2]
li0 = colTriVar02[var0]
li1 = colTriVar02[var1]
varDf = 0

df = pd.DataFrame( columns = ['IdNom','NbParu'])
dfIdNom = df['IdNom']
dfNbParu = df['NbParu']
varNbParu = 1

idNom = []
nbParu = []

"""

for colTriVar02 in colByName:
    if li0 != li1 :
        
        idNom.append(li0)
        nbParu.append(varNbParu)
        varNbParu = 1
        varDf += 1
    elif li0 == li1 :
        varNbParu += 1
    else :
        print("Issue innatendue")
    var0 += 1
    var1 += 1
    var2 += 1
"""

for colTriVar02 in colByName:
    print(colTriVar02)

products_list = (idNom, nbParu)
df = pd.DataFrame (products_list).transpose()
df.columns = ['IdNom', 'nbParu']
    