# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 00:14:07 2022

@author: Max-Louis
"""
import pandas as pd
listeSynoaz = pd.read_csv(r'C:\Users\Max-Louis\lystazInit2.csv')

variable = 0
idNom = []
natNom = []
listeSyno = []
val400 = []
initId = []
initLyS = []

while variable <= 382550:
    idNom.append(listeSynoaz.iloc[variable, 2])
    natNom.append(listeSynoaz.iloc[variable, 1])
    listeSyno.append(listeSynoaz.iloc[variable, 0])
    val400.append(listeSynoaz.iloc[variable, 3])
    initId.append(listeSynoaz.iloc[variable, 6])
    initLyS.append(listeSynoaz.iloc[variable, 5])
    variable += 1
    print(variable)
    
products_list = (idNom, natNom, listeSyno, val400, initId, initLyS)
df = pd.DataFrame (products_list).transpose()
df.columns = ['IdNom', 'NatNom', 'listeSyno', 'val400', 'initId', 'initLyS']
    