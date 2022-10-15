# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 16:07:04 2022

@author: Max-Louis
"""

import pandas as pd

dzli6L = pd.read_csv(r'C:/Users/Max-Louis/li6Lsv.csv')
dzli6LInvAS = pd.read_csv(r'C:/Users/Max-Louis/li6LsvInv.csv')
dzli6LInv = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/li6LsvAscendingFalse.csv')

plusBas = 0
plusHaut = len(dzli6L) - 1
print(plusHaut)
incrementeur = 0

zigzag = int((plusHaut -(plusHaut % 2)) / 2)
print(zigzag)

print(dzli6L)

print(dzli6L.iloc[incrementeur, 4])
print(dzli6L.iloc[zigzag, 5])
print(dzli6L.iloc[incrementeur])
print(dzli6L.iloc[zigzag])
nbdeBoucle = 0

#while dzli6L.iloc[incrementeur, 4] != dzli6LInv.iloc[zigzag, 4]:
for loop in range (10):
    print(zigzag)
    if dzli6L.iloc[incrementeur, 4] < dzli6LInv.iloc[zigzag, 4]:
        plusBas = zigzag
        
    elif dzli6L.iloc[incrementeur, 4] > dzli6LInv.iloc[zigzag, 4]:
        plusHaut = zigzag
        
    diffPhPb = plusHaut - plusBas
    zigzag = plusBas + int((diffPhPb - (diffPhPb % 2)) / 2)
    nbdeBoucle += 1

print('resultat')
print(dzli6L.iloc[incrementeur])
print(dzli6L.iloc[zigzag])
print('nbdeBoucle = ' + str(nbdeBoucle))
