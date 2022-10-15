# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 22:41:45 2022

@author: Max-Louis
"""
import pandas as pd

val1006 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\val1006.csv')
mot2 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\mot2.csv')
specCharMot1 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\SpecCharMot1.csv')
nbMot = 1
valPrec = 0
valCumul = 0
prec = 0
suiv = 1
idNom = val1006['IdNom']
moyProxMot = []
"""
while suiv < 382551:
        if df.iloc[prec, 0] != df.iloc[suiv, 0]:
            mot1.append(df.iloc[prec, 0])
            numero1.append(df.iloc[prec, 5])
        prec = suiv
        suiv += 1
products_list = (mot1, numero1)
df1 = pd.DataFrame (products_list).transpose()
df1.columns = ['mot2','numero2']
print(df1)
"""
for loop in range(382550):
    valPrec = val1006.iloc[prec, 3]
    if idNom[prec] != idNom[suiv]:
        resultat = round((valCumul / nbMot), 3)
        moyProxMot.append(resultat)
        nbMot = 1
    else:
        valCumul = valCumul + valPrec
        nbMot += 1
    prec = suiv
    suiv += 1
    