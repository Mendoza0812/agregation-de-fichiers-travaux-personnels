# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:27:33 2022

@author: Max-Louis
"""
import pandas as pd

idnomaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\IdNomtrie2.csv')
listeSynoaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\listeSynotrieFalse.csv')

variable = 0

initialIdNom = []
initialListeSyno = []

while variable <= 382550 :
    initialIdId = listeSynoaz.iloc[variable, 0]
    initialIdLi = listeSynoaz.iloc[variable, 2]
    initialIdId1 = initialIdId[0]
    initialIdLi1 = initialIdLi[0]
    initialIdNom.append(initialIdId1)
    initialListeSyno.append(initialIdLi1)
    variable += 1