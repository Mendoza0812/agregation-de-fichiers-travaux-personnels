# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 22:38:45 2022

@author: Max-Louis
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\idnomazVal1006.csv')


var = 1

prec = 0

suiv = 1
"""
suiv2 = 2

idNom = []
natNom = []

listeSyno = []
"""
numero1 = []
numero2 = []
"""
val1000 = []

for loop in range (382551):
    if df.iloc[prec, 4] == 2 and df.iloc[suiv, 4] == 1 or df.iloc[prec, 4] == 1 and df.iloc[suiv, 4] == 1:
        idNom.append(df.iloc[prec, 0])
        natNom.append(df.iloc[prec, 1])
        listeSyno.append(df.iloc[prec, 2])
        val1000.append(df.iloc[prec, 3])
        numero.append(df.iloc[prec, 4])
    
    prec = suiv
    suiv += 1
    
products_list = (idNom, natNom, listeSyno, val1000, numero)
df = pd.DataFrame (products_list).transpose()
df.columns = ['IdNom', 'NatNom', 'listeSyno', 'val400', 'numero']
print(df)
---------
defesseveNum = df.sort_values('numero', ascending = False)

while var < 382550:
    if defesseveNum.iloc[suiv,2] != defesseveNum.iloc[prec, 2]:
        listeSyno.append(defesseveNum.iloc[prec, 2])
        numero.append(defesseveNum.iloc[prec, 4])
    prec = suiv
    suiv += 1
"""

while suiv < 382551:
        if df.iloc[prec, 2] != df.iloc[suiv, 2]:
            numero2.append(df.iloc[prec, 5])
        prec = suiv
        suiv += 1
"""

while suiv <= 382551:
    
    numero2.append(var)
    if df.iloc[prec, 0] == df.iloc[suiv, 0]:
        var += 1
    else:
        var = 1
    prec = suiv
    suiv += 1
    
df['numero2'] = numero2

print(df)



products_list = (mot2, numero2)
df1 = pd.DataFrame (products_list).transpose()
df1.columns = ['mot2','numero2']
print(df1)
"""