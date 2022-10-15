# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 18:06:44 2022

@author: Max-Louis
"""

import pandas as pd

deaaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')

del deaaz['placeSyno']

liContainsChoseColListeSyno = deaaz[deaaz['listeSyno'].str.contains('chose')]
print(liContainsChoseColListeSyno)
# nbLignes  = longueurLiContainsChoseColIdNom
nbLignes = len(liContainsChoseColListeSyno)
print(nbLignes)
# nbLettres  = nbLettreMotColIdNom sauf qu'ici col. ListeSyno
nbLettres = []

var = 0

for loop in range(nbLignes):
    nbLettres.append(len(liContainsChoseColListeSyno.iloc[var, 2]))
    var += 1
    
choseColLynst = liContainsChoseColListeSyno

choseColLynst['nbLettrLynst'] = nbLettres

var = 0
true = 0
false = 0

for loop in range(nbLignes):
    if len(choseColLynst.iloc[var, 2]) == choseColLynst.iloc[var, 4]:
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
for loop in range(nbLignes):
    if choseColLynst.iloc[var, 4] == nbLettrMotChose:
        idNom.append(choseColLynst.iloc[var, 0])
        natNom.append(choseColLynst.iloc[var, 1])
        listeSyno.append(choseColLynst.iloc[var, 2])
        val400.append(choseColLynst.iloc[var, 3])
    var += 1
    
products_list = (idNom, natNom, listeSyno, val400)
choseLynst = pd.DataFrame (products_list).transpose()
choseLynst.columns = ['IdNom','NatNom','motchos','val400']

print(choseLynst)