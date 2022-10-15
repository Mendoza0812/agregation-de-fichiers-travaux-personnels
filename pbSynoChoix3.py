# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 23:19:53 2022

@author: Max-Louis
"""

import pandas as pd

deaazz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')
#works
del deaazz['placeSyno']

deaaz = pd.DataFrame(deaazz)

def researchByInitial(initial,column):
    
    researchWord = deaaz[deaaz[column].str.match(initial)]

    nbLignes = len(researchWord)
    
    var = 0

    idNom = []
    natNom = []
    listeSyno = []
    val400 = []
    
    #tri les mots dt la lgueur ne corrsp pas au modorgn
    for loop in range(nbLignes):
        idNom.append(researchWord.iloc[var, 0])
        natNom.append(researchWord.iloc[var, 1])
        listeSyno.append(researchWord.iloc[var, 2])
        val400.append(researchWord.iloc[var, 3])
        var += 1
        
    products_list = (idNom, natNom, listeSyno, val400)
    global modorgn
    modorgn = pd.DataFrame (products_list).transpose()
    modorgn.columns = ['IdNom','NatNom','Syno','val400']

def trier(initial):
    global liste
    liste = pd.DataFrame()
    researchByInitial(initial,'IdNom')
    liste = pd.concat([liste, modorgn])
    researchByInitial(initial,'listeSyno')
    liste = pd.concat([liste, modorgn])
    
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

total = pd.DataFrame()

varAlph = 0
for loop in range(len(alphabet)):
    trier(alphabet[varAlph])
    print(alphabet[varAlph])
    total = pd.concat([total, liste])
    varAlph += 1
    

print(total)