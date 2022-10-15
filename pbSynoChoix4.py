# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 23:34:19 2022

@author: Max-Louis
"""

import pandas as pd

deaazz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')
#works
del deaazz['placeSyno']

dscAz = pd.read_csv(r'C:\Users\Max-Louis\dscAz.csv')
dscAzIn = pd.read_csv(r'C:\Users\Max-Louis\dscAzIN.csv')
dscAz = dscAz[['listeSyno','NatNom','IdNom','val400']]

variable0 = 0

variable1 = 0
var = 0

idNomD = []
natNomD = []
synoD = []
val400D = []

idNomSd = []
natNomSd = []
synoSd = []
val400Sd = []

while variable0 < len(dscAz):
    
    if dscAzIn.iloc[variable0,0] == dscAz.iloc[variable1,0]:
        
        idNomD.append(dscAzIn.iloc[variable0,0])
        natNomD.append(dscAzIn.iloc[variable0,1])
        synoD.append(dscAzIn.iloc[variable0,2])
        val400D.append(dscAzIn.iloc[variable0,3])
        
        variable0 += 1

    else:
        
        idNomSd.append(dscAz.iloc[variable1,0])
        natNomSd.append(dscAz.iloc[variable1,1])
        synoSd.append(dscAz.iloc[variable1,2])
        val400Sd.append(dscAz.iloc[variable1,3])
        
        variable1 += 1
        var += 1
        if variable1 == len(dscAz):
            print('mot dans IdNom nest pas dans listeSyno')
            idNomD.append(dscAz.iloc[variable0,0])
            natNomD.append(dscAz.iloc[variable0,1])
            synoD.append(dscAz.iloc[variable0,2])
            val400D.append(dscAz.iloc[variable0,3])
            
        
    print(variable0)
    print(variable1)
    

product_lists1 = (idNomD, natNomD, synoD, val400D)
df0 = pd.DataFrame(product_lists1).transpose()
df0.columns = ['IdNom','NatNom','Syno', 'val800']

product_lists0 = (idNomSd, natNomSd, synoSd, val400Sd)
df1 = pd.DataFrame(product_lists0).transpose()
df1.columns = ['IdNom','NatNom','Syno', 'val800']