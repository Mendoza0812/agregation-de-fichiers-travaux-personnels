# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:15:14 2022

@author: Max-Louis

les mots ont tous au moins un synonyme, la base de donnée entière est en structure
pb niveau ne s'incremente pas
"""

import pandas as pd


df10 = pd.read_csv(r'C:/Users/Max-Louis/df10Ref.csv')

dfDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

dfSyneurone = pd.read_csv( r'C:/Users/Max-Louis/df12svRef.csv')

motCible = "bon"

niveau = 0

def initialisation_colonnes():
    
    global colonneModorgn
    colonneModorgn = []
    
    global colonneSynonyme
    colonneSynonyme = []
    
    global colonneNiveau
    colonneNiveau = []

def creation_listeMotCible(motCible):
    
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

def listage_synonyme(motCible, listeMotCible, niveau):
    
    for incrementeur in range (len(listeMotCible)):
        
        numDeLigne = listeMotCible.iloc[incrementeur,2]
        
        #print(numDeLigne)
        
        filtrage_synonyme(motCible, numDeLigne)
        
        #print(synonyme)
        
        colonneModorgn.append(motCible)
        colonneSynonyme.append(synonyme)
        colonneNiveau.append(niveau)
        
def assemblage_des_colonnes_en_tableau():
    
    plst = (colonneModorgn,colonneSynonyme,colonneNiveau)
    
    global dfStructure
    dfStructure = pd.DataFrame(plst).transpose()
    dfStructure.columns = ['motCible','synonyme','niveau']
    #print(dfStructure)


def creation_dfStructure_de_motCible(motCible, niveau):
    
    initialisation_colonnes()
    
    creation_listeMotCible(motCible)
    
    listage_synonyme(motCible, listeMotCible, niveau)
    
    assemblage_des_colonnes_en_tableau()

def creation_structure_motCible_niveauSup(dfStructureDeBase, niveau, precedents_motsCibles):
    
    niveau += 1
    
    dfStructureAccumulee = pd.DataFrame()
    
    for loop in range(len(dfStructureDeBase)):
        
        creation_dfStructure_de_motCible(dfStructureDeBase.iloc[loop,1], niveau)
        
        numerosDeLignesASupprimer = []
        
        for incrementeur in range (len(dfStructure)):
            
            if dfStructure.iloc[incrementeur,1] in precedents_motsCibles:
                
                numerosDeLignesASupprimer.append(incrementeur)
            
            else:
                
                precedents_motsCibles.append(dfStructure.iloc[incrementeur,1])
                
        dfStructureCorrigee = dfStructure.drop(numerosDeLignesASupprimer)
        #print(dfStructureCorrigee)
        
        if loop == 0:
            
            dfStructureAccumulee = dfStructureCorrigee
        
        else:
        
            dfStructureAccumulee = pd.concat([dfStructureAccumulee,dfStructureCorrigee], join ='inner', ignore_index = True)
        
        print(loop)
    
    global dfStructureNiveauSuperieur
    
    dfStructureNiveauSuperieur = dfStructureAccumulee

precedents_motsCibles = []

creation_dfStructure_de_motCible(motCible, niveau)

dfStructure0 = dfStructure

precedents_motsCibles.append(motCible)

creation_structure_motCible_niveauSup(dfStructure0, niveau, precedents_motsCibles)

dfStructure1 = dfStructureNiveauSuperieur

structure_niveaux_accumulees = pd.concat([dfStructure0,dfStructure1], join ='inner', ignore_index = True)

niveau += 1

creation_structure_motCible_niveauSup(dfStructure1, niveau, precedents_motsCibles)

dfStructure2 = dfStructureNiveauSuperieur

structure_niveaux_accumulees = pd.concat([structure_niveaux_accumulees,dfStructure2], join ='inner', ignore_index = True)