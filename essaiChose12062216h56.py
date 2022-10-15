# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:44:52 2022

@author: Max-Louis
"""
import pandas as pd

deaaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')
#works
del deaaz['placeSyno']
liContainsChoseColIdNom = deaaz[deaaz['IdNom'].str.contains('chose')]
#works
longueurLiContainsChoseColIdNom = len(liContainsChoseColIdNom)

nbrLettreMotColIdNom = []

var = 0

for loop in range(longueurLiContainsChoseColIdNom):
    nbrLettreMotColIdNom.append(len(liContainsChoseColIdNom.iloc[var, 0]))
    var += 1
    
liChoseColIdNom = liContainsChoseColIdNom

liChoseColIdNom['nbLettrIdNom'] = nbrLettreMotColIdNom

var = 0
true = 0
false = 0

for loop in range(longueurLiContainsChoseColIdNom):
    if len(liChoseColIdNom.iloc[var, 0]) == liChoseColIdNom.iloc[var, 4]:
        true += 1
    else:
        false += 1
print(true)
print('Nombre d\'erreurs :')
print(false)

var = 0

idNom = []
natNom = []
listeSyno = []
val400 = []
nbLettrMotChose = len('chose')
for loop in range(longueurLiContainsChoseColIdNom):
    if liChoseColIdNom.iloc[var, 4] == nbLettrMotChose:
        idNom.append(liChoseColIdNom.iloc[var, 0])
        natNom.append(liChoseColIdNom.iloc[var, 1])
        listeSyno.append(liChoseColIdNom.iloc[var, 2])
        val400.append(liChoseColIdNom.iloc[var, 3])
    var += 1
    
products_list = (idNom, natNom, listeSyno, val400)
choseIdNom = pd.DataFrame (products_list).transpose()
choseIdNom.columns = ['IdNom','NatNom','motchos','val400']

print(choseIdNom)