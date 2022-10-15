# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:08:28 2022

@author: Max-Louis
"""

import pandas as pd

df10 = pd.read_csv(r'C:/Users/Max-Louis/df10Ref.csv')

dfDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

dfSyneurone = pd.read_csv( r'C:/Users/Max-Louis/df12svRef.csv')

totalNb = []
parcouruNb = []
parcouruNoms = []
incrementeur = 0
numeroDeListe = 0
niveauCompteur = []
motCible = 'bon'

mot = []
nbDeSyno = []
indexDf10 = []
dist = []
ref = []

lgrListeAccomplished = 0


for loop in range(9):
    print(' --- --- ---')
    increMotCible = 0
    
    longueurMotCible = len(motCible)
    referenceMotCible = str(motCible) + str(longueurMotCible)
    
    listeMotCible = dfSyneurone[dfSyneurone['ref'].str.contains(referenceMotCible)]
    
    niveauCompteur.append(numeroDeListe)
    totalNb.append(len(listeMotCible))
    parcouruNb.append(increMotCible)
    parcouruNoms.append(motCible)
    
    passageIndexDf10 = listeMotCible.iloc[incrementeur,2]
    synonymesChoisir = df10.iloc[passageIndexDf10]
    
    if motCible == synonymesChoisir.iloc[0]:
        
        synoTest = synonymesChoisir.iloc[1]
    
    else:
        
        synoTest = synonymesChoisir.iloc[0]
    
    if synoTest in parcouruNoms:
        
        while synoTest in parcouruNoms:
            print('while1')
            print(synoTest)
            print(parcouruNoms)
            
            incrementeur += 1
            
            if increMotCible == len(listeMotCible) :
                print(listeMotCible)
                
                incrementeur = 0
                
                while increMotCible != len(listeMotCible):
                    print('while2_1')
                    
                    mot.append(listeMotCible.iloc[increMotCible,0])
                    nbDeSyno.append(listeMotCible.iloc[increMotCible,1])
                    indexDf10.append(listeMotCible.iloc[increMotCible,2])
                    dist.append(listeMotCible.iloc[increMotCible,3])
                    ref.append(listeMotCible.iloc[increMotCible,4])
                    
                    incrementeur += 1
                    
                    lgrListeAccomplished += 1
                    
                incrementeur = 0
                
                while increMotCible != lgrListeAccomplished:
                    print('while2_2')
                    print('compteurNameImmediat = ' + str(numeroDeListe))
                    
                    del parcouruNb[numeroDeListe]
                    del totalNb[numeroDeListe]
                    del parcouruNoms[numeroDeListe]
                    del niveauCompteur[numeroDeListe]
                    
                    numeroDeListe -= 1
                    lgrListeAccomplished -= 1
                
                listeMotCible = parcouruNoms[numeroDeListe]
            
                
            parcouruNb[numeroDeListe] = incrementeur
            
            passageIndexDf10 = listeMotCible.iloc[incrementeur,2]
            synonymesChoisir = df10.iloc[passageIndexDf10]
            
            if motCible == synonymesChoisir.iloc[0]:
                
                synoTest = synonymesChoisir.iloc[1]
            
            else:
                
                synoTest = synonymesChoisir.iloc[0]
            
    passageIndexDf10 = listeMotCible.iloc[incrementeur,2]
    synonymesChoisir = df10.iloc[passageIndexDf10]
    
    if motCible == synonymesChoisir.iloc[0]:
        
        synoTest = synonymesChoisir.iloc[1]
    
    else:
        
        synoTest = synonymesChoisir.iloc[0]
    
    synoSuivant = synoTest
    
    motCible = synoSuivant
    
    numeroDeListe += 1

plst = (parcouruNoms, parcouruNb, totalNb)
tableau = pd.DataFrame(plst).transpose()
tableau.columns = ['nom','parcouru','total']

print(tableau)

plst2 = (mot, nbDeSyno, indexDf10, ref)
tableau2 = pd.DataFrame(plst2).transpose()
tableau2.columns = ['mot','nbDeSyno','indexDf10','ref']

print(tableau2)
