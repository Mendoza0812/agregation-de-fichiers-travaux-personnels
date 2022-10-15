# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 23:20:02 2022

@author: Max-Louis

https://www.pythoniste.fr/python/a-quoi-servent-les-fonctions-lambdas-en-python/

https://realpython.com/fast-flexible-pandas/

https://www.w3resource.com/python-exercises/pandas/index.php

"""

import pandas as pd

df10 = pd.read_csv(r'C:/Users/Max-Louis/df10Ref.csv')

dfDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

dfSyneurone = pd.read_csv( r'C:/Users/Max-Louis/df12svRef.csv')

exempleBon = pd.read_csv( r'C:/Users/Max-Louis/exempleBon.csv')

# SEGMENTS EST LE RESULTAT DE LAPPLICATION DU PRESENT PROGRAMME
segments = pd.read_csv(r'C:/Users/Max-Louis/synonymeSegment.csv' )

# CELUI LA AUSSI
segmentsPlus = pd.read_csv(r'C:/Users/Max-Louis/segmentPlus.csv' )

#ldmdduss = liste des mots diposant d un seul synonyme
listeSynonymeEgale1 = dfSyneurone[dfSyneurone['nbDeSyno'] == 1 ]

synonyme1 = []
motCible1 = []
indexDf10_1 = []
dist1 = []

synonymePlus = []
motCiblePlus = []
indexDf10Plus = []
distPlus = []

def creation_listeDuMotCible(motCible):
    
    global motCibleRef
    motCibleRef = str(motCible) + str(len(motCible))
    
    global listeMotCible
    listeMotCible = dfSyneurone[dfSyneurone['ref'].str.contains(motCibleRef)]

def filtrage_synonyme(motCible, listeCible, numeroDeLigne):
    
    global incrementeurDist
    
    incrementeurDist = listeCible.iloc[numeroDeLigne,3]
    
    global incrementeurIndexDf10
    
    incrementeurIndexDf10 = listeCible.iloc[numeroDeLigne,2]
    
    binome = df10.iloc[incrementeurIndexDf10]
        
    global synonyme
        
    if motCible == binome.iloc[0]:
            
        synonyme = binome.iloc[1]
        
    else:
            
        synonyme = binome.iloc[0]
    
    #print(synonyme)

segment = 0
segmentPlus = 0
for index, row in segmentsPlus.iterrows():
    
    motCible = row['motCible']
    
    filtrage_synonyme(motCible,segmentsPlus,index)
    
    creation_listeDuMotCible(synonyme)
    
    if len(listeMotCible) > 2:
        
        segmentPlus += 1
        
        motCiblePlus.append(motCible)
        synonymePlus.append(synonyme)
        indexDf10Plus.append(incrementeurIndexDf10)
        distPlus.append(incrementeurDist)
    
    else:
        
        segment += 1
        
        motCible1.append(motCible)
        synonyme1.append(synonyme)
        indexDf10_1.append(incrementeurIndexDf10)
        dist1.append(incrementeurDist)
        
    print(index)
print('segment = ' + str(segment))
print('segmentPlus = ' + str(segmentPlus))

plstPlus = (motCiblePlus, synonymePlus, indexDf10Plus, distPlus)
plst1 = (motCible1, synonyme1, indexDf10_1, dist1)
dfPlus = pd.DataFrame(plstPlus).transpose()
df1 = pd.DataFrame(plst1).transpose()
dfPlus.columns = ['motCible', 'synonyme','indexDf10','dist']
df1.columns = ['motCible', 'synonyme','indexDf10','dist']