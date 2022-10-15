# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 02:50:43 2022

@author: Max-Louis
"""

import pandas as pd

df10 = pd.read_csv(r'C:/Users/Max-Louis/df10Ref.csv')

dfDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

dfSyneurone = pd.read_csv( r'C:/Users/Max-Louis/df12svRef.csv')

dfNiveau3 = pd.read_csv(r'C:/Users/Max-Louis/dfNiveau3.csv')

dfNivMystere = pd.read_csv(r'C:/Users/Max-Louis/dfNiveauMystere.csv')

structureNiveau1ATerminer = pd.read_csv(r'C:/Users/Max-Louis/structureNiveau1ATerminer.csv')
motCible = 'bon'

nombreDeNouveauxMotsAjoutes = 0

niveau = 0

nbSynonymesParcourus = 0
listeTotauxNiveaux = 0
def creation_listeMotCible(motCible):
    
    global motCibleRef
    motCibleRef = str(motCible) + str(len(motCible))
    
    global listeMotCible
    listeMotCible = dfSyneurone[dfSyneurone['ref'].str.contains(motCibleRef)]

creation_listeMotCible(motCible)

print(len(listeMotCible))

totalListeMotCible = len(listeMotCible)

while nbSynonymesParcourus != totalListeMotCible:
    
    nbSynonymesParcourus += 1