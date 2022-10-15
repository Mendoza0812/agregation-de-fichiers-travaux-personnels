# -*- coding: utf-8 -*-
"""
Created on Sat May 21 02:57:29 2022

@author: Max-Louis
compter le nb de mots
classer séparément IdNom et listeSyno par ordre alphabétique
et compter l'itération de chaque mot
Peut être établir un tableau de 2 lignes avec tous les mots référencés,
après avoir enlevé les doublons de telescopage (IdNom/listeSyno)
Faire une moyenne val400 résultat des doublons
Vérifier et comprendre l'absence de doublon sur certains mots
Faire une moyenne du nombre de synonymes par mot

"""
import pandas as pd

moncsv1 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\deaazCSV.csv')

moyenneVal400 = moncsv1['val400'].mean()

idNom10 = moncsv1.iloc[0:9,0]
incr = 0
rechV = 1
placeSyno = moncsv1['placeSyno']

nbMot = 46104
triIdNom = moncsv1.sort_values(by=['IdNom'])
idNom10 = triIdNom.iloc[0:9,0]
triListeSyno = moncsv1.sort_values(by=['listeSyno'])
df = pd.DataFrame(columns = ['MotOrgn', 'NatMotOrgn', 'MotTlscp', 'NatMotTlscp', 'val800']) 
liIdNomSnsDbl = pd.dataFrame(columns = ['idNom2', 'nbParu'])
LiSynoSnsDbl = pd.dataFrame(columns = ['ListeSyno2', 'nbParu'])
#DETERMINE LE NOMBRE DE MOTS QUE CONTIENT LA PLAGE DE SYNONYMES

"""
for i in range :
    motDOrigine = idNom[incr]
    motTelescope = placeSyno[incr]
    motCandidatOrigine = placeSyno[rechV]
    motCandidatTelescope = idNom[rechV]
    if motDOrigine == motCandidatOrigine :
        if motTelescope == motCandidatTelescope 
"""