# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 17:16:59 2022

@author: Max-Louis
"""

import pandas as pd


df10 = pd.read_csv(r'C:/Users/Max-Louis/df10Ref.csv')

dfDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

dfSyneurone = pd.read_csv( r'C:/Users/Max-Louis/df12svRef.csv')

motCible = "bon"

def initialisation_colonnes():
    
    global colonneModorgn
    colonneModorgn = []
    
    global colonneSynonyme
    colonneSynonyme = []
    
    global colonneSynonymesCommuns
    colonneSynonymesCommuns = []
    
    global colonneTotalDeSynonymes
    colonneTotalDeSynonymes = []
    
    global colonneRatioCommunTotal1
    colonneRatioCommunTotal1 = []
    
    global colonneDistance
    colonneDistance = []
    
    global colonneRatioCommunTotal0
    colonneRatioCommunTotal0 = []
    
    global colonneRatioCommunTotal2
    colonneRatioCommunTotal2 = []
    
    global colonneRatioCommunTotal3
    colonneRatioCommunTotal3 = []
    
def creation_listeDuMotCible(motCible):
    
    global motCibleRef
    motCibleRef = str(motCible) + str(len(motCible))
    
    global listeMotCible
    listeMotCible = dfSyneurone[dfSyneurone['ref'].str.contains(motCibleRef)]

def filtrage_synonyme(motCible, numeroDeLigne):
    
    binome = df10.iloc[numeroDeLigne]
        
    global synonyme
        
    if motCible == binome.iloc[0]:
            
        synonyme = binome.iloc[1]
        
    else:
            
        synonyme = binome.iloc[0]
    
    print(synonyme)


def filtrage_automatique_synonymes_et_placement_dans_listes(motCible, listeMotCible):
    
    for incrementeur in range (len(listeMotCible)):
        
        numDeLigne = listeMotCible.iloc[incrementeur,2]
        
        filtrage_synonyme(motCible,numDeLigne)
        
        colonneModorgn.append(motCible)
        colonneSynonyme.append(synonyme)
        
        distance = round((listeMotCible.iloc[incrementeur,3]/801),4)
        colonneDistance.append(distance)

        
initialisation_colonnes()

creation_listeDuMotCible(motCible)

modorigine = motCible

listeModorgn = listeMotCible

filtrage_automatique_synonymes_et_placement_dans_listes(motCible, listeMotCible)

for incrementeur in range(len(colonneSynonyme)):
    
    creation_listeDuMotCible(colonneSynonyme[incrementeur])
    nombreCommun = 0
    total = 0
    for incrementeur2 in range (len(listeMotCible)):
        
        numDeLigne = listeMotCible.iloc[incrementeur2,2]
        filtrage_synonyme(listeMotCible.iloc[incrementeur2,0],numDeLigne)
        
        if synonyme in colonneSynonyme:
            
            nombreCommun += 1
        
        total += 1
    colonneSynonymesCommuns.append(nombreCommun)
    colonneTotalDeSynonymes.append(total)
    ratio1 = round(nombreCommun / total,4)
    colonneRatioCommunTotal1.append(ratio1)
    ratio0 = round(nombreCommun / 239,4)
    colonneRatioCommunTotal0.append(ratio0)
    ratio2 = round(((ratio0 + ratio1) / 2),4)
    colonneRatioCommunTotal2.append(ratio2)
    ratio3 = round(((ratio0 + ratio1 + (1-colonneDistance[incrementeur])) / 3), 4)
    colonneRatioCommunTotal3.append(ratio3)
    
plst = (colonneModorgn, colonneSynonyme, colonneSynonymesCommuns, colonneTotalDeSynonymes, colonneDistance, colonneRatioCommunTotal2, colonneRatioCommunTotal3)
df = pd.DataFrame(plst).transpose()
df.columns = ['modorgn','synonyme','commun','total','distance','ratio2','ratio3']
df.sort_values(['ratio2','distance'] , ascending = False)