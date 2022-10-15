# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:26:22 2022

@author: Max-Louis
m'a permis de comptabiliser les valeurs maximales et minimales correspondant
sur tous les synonymes de chaque mot d'origine
"""

import pandas as pd

val1006 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\val1009.csv')
mot2 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\mot2MoyMinMax.csv')
specCharMot1 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\spCarMoyMinMax.csv')

val1000 = val1006['val1000']

idNom = val1006['IdNom']
listeSyno = val1006['listeSyno']
prec = 0
suiv = 1
somme = 0
count = 0


mini = 1000
maxi = 0

liste = []
listemin = []
listemax = []
var = 0

for loop in range(382550):
    valprec = val1000[prec]
    valsuiv = val1000[suiv]
    somme = somme + valprec
    count += 1
    if valprec < mini:
        mini = valprec
    if valprec > maxi :
        maxi = valprec
    if idNom[prec] != idNom[suiv]:
        result = (somme/count)
        liste.append(round(result,3))
        print(liste[var])
        listemin.append(round(mini, 3))
        print(listemin[var])
        listemax.append(round(maxi, 3))
        print(listemax[var])
        somme = 0
        count = 0
        mini = valsuiv
        maxi = valsuiv
        var += 1
    prec = suiv
    suiv += 1