# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 02:31:09 2022

@author: Max-Louis
enlever de idnomaz1 tous les synonymes commmençant par des caractères spéciaux.
Le shape après cela devrait être identique entre les 2 tableaux
"""

import pandas as pd

idnomaz1 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\idnomAzInit2.csv')

idNomCarSpec1 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\carSpec1.csv')

liSynaz2 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\sansCharSpec.csv')

liSynCarSpec2 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\carSpec2.csv')

var = 0
juste = 0
faux = 0

while var < 13233:
    if idNomCarSpec1.iloc[var, 0] == liSynCarSpec2.iloc[var, 0]:
        juste += 1
        var += 1
        print(juste)
        print(var)
    else:
        faux += 1
        var += 1
        print(faux)
print('juste ='+str(juste)+' \n faux='+str(faux))