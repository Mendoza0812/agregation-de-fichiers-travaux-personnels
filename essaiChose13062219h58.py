# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 19:34:26 2022

@author: Max-Louiss
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

liContainsChoseColListeSyno = deaaz[deaaz['listeSyno'].str.contains('chose')]
# nbLignes  = longueurLiContainsChoseColIdNom
nbLignes = len(liContainsChoseColListeSyno)
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

idNom = []
natNom = []
syno = []
natSyno = []
val800 = []
varSearchChoseIdNom = 0
varSearchChoseLynst = 0
varFind = 0

longueurLiContainsChoseColLynst = len(choseLynst)

while True :

    if choseIdNom.iloc[varSearchChoseIdNom, 2] == choseLynst.iloc[varSearchChoseLynst, 0]:
        idNom.append(choseIdNom.iloc[varSearchChoseIdNom, 0])
        natNom.append(choseIdNom.iloc[varSearchChoseIdNom, 1])
        syno.append(choseIdNom.iloc[varSearchChoseIdNom, 2])
        natSyno.append(choseLynst.iloc[varSearchChoseLynst, 1])
        val800.append(choseIdNom.iloc[varSearchChoseIdNom,3] + choseLynst.iloc[varSearchChoseLynst,3])
        varSearchChoseIdNom += 1
        varSearchChoseLynst = 0
    else:
        varSearchChoseLynst += 1
        if varSearchChoseLynst == longueurLiContainsChoseColLynst :
            idNom.append(choseIdNom.iloc[varSearchChoseIdNom, 0])
            natNom.append(choseIdNom.iloc[varSearchChoseIdNom, 1])
            syno.append(choseIdNom.iloc[varSearchChoseIdNom, 2])
            natSyno.append('')
            val800.append(choseIdNom.iloc[varSearchChoseIdNom,3] * 2)
            varSearchChoseIdNom += 1
            varSearchChoseLynst = 0
    
    if varSearchChoseIdNom == len(choseIdNom) :
        break

products_list = (idNom, natNom, syno, natSyno, val800)
chose800 = pd.DataFrame (products_list).transpose()
chose800.columns = ['IdNom','NatNom','Syno','natSyno', 'val800'] 
chose800sv = chose800.sort_values('val800', ascending = False)
print(chose800sv)