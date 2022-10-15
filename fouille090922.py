# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:28:43 2022

@author: Max-Louis
"""

import pandas as pd

df10 = pd.read_csv(r'C:/Users/Max-Louis/df10Ref.csv')

dfDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

dfSyneurone = pd.read_csv( r'C:/Users/Max-Louis/df12svRef.csv')

dfNiveau3 = pd.read_csv(r'C:/Users/Max-Louis/dfNiveau3.csv')

# structureNiveau1 = Tous les synonymes de synonymes du mot bon,
# df etant le resultat du code ci apres
# pour refaire la meme chose il faudra reconstituer les listes
# l une permettant de stocker les synonymes
# l autre permettant de stocker les mots dont les synonymes ont deja ete
# recuperes et pose dans la liste des synonymes
structureNiveau1ATerminer = pd.read_csv(r'C:/Users/Max-Louis/structureNiveau1ATerminer.csv')
motCible = 'bon'

dejaParcouruTousSynonymesInclus = ['bon']
dejaParcouruSeulementMotCibleNiveau1 = []

ajout = 0
optimiseur = False

dejaParcouruTousSynonymesInclusNiveau3 = []

def listeDesSynonymesDe(motCible,dfSyneurone, dejaParcouruTousSynonymesInclus, dejaParcouruSeulementMotCibleNiveau1, ajout, optimiseur, dejaParcouruTousSynonymesInclusNiveau3):
    
    motCibleRef = str(motCible) + str(len(motCible))
    listeMotCible = dfSyneurone[dfSyneurone['ref'].str.contains(motCibleRef)]
    
    incrementeur = 0
    
    listeModorgn = []
    idxDf10 = []
    synonymes = []
    distances = []
    references = []
    
    for incrementeur in range (len(listeMotCible)):
    
        binome = df10.iloc[listeMotCible.iloc[incrementeur,2]]
        
        global synonyme
        
        if motCible == binome.iloc[0]:
            
            synonyme = binome.iloc[1]
        
        else:
            
            synonyme = binome.iloc[0]
        
        if optimiseur == False:
            
            if synonyme not in dejaParcouruTousSynonymesInclus:
            
                listeModorgn.append(motCible)
                idxDf10.append(listeMotCible.iloc[incrementeur,2])
                synonymes.append(synonyme)
                dejaParcouruTousSynonymesInclus.append(synonyme)
                distances.append(listeMotCible.iloc[incrementeur,3])
                references.append(motCibleRef)
                
                ajout += 1
        
        else:
            
            executerOptimiseur(synonyme,dejaParcouruTousSynonymesInclus, dejaParcouruSeulementMotCibleNiveau3)
    
    dejaParcouruTousSynonymesInclus.append(listeMotCible.iloc[0,0])
    dejaParcouruSeulementMotCibleNiveau1.append(listeMotCible.iloc[0,0])
    
    plst = (listeModorgn, idxDf10, synonymes, distances, references)
    global dfMotCible
    dfMotCible = pd.DataFrame(plst).transpose()
    dfMotCible.columns = ['modorgn','idxDf10','synonymes','distances','references']

def executerOptimiseur(synonyme,dejaParcouruTousSynonymesInclusNiveau3):
    
    dejaParcouruTousSynonymesInclusNiveau3.sort()
    dejaParcouruSeulementMotCibleNiveau3.sort()
    
    totalTousSynonymesDejaParcouruNiveau3 = (len(dejaParcouruTousSynonymesInclusNiveau3) - 1)
    plusHautSynDejaParc = totalTousSynonymesDejaParcouruNiveau3
    plusBasSynDejaParc = 0
    diffHautBas = plusHautSynDejaParc - plusBasSynDejaParc
    sondeurTousSynonymes = int(plusBasSynDejaParc) + int((diffHautBas - (diffHautBas % 2)) / 2)
    #moitie = int((valeur - (valeur % 2)) / 2)
    
    rechercheTermine = False
    
    while rechercheTermine == False:
        
        diffHautBas = plusHautSynDejaParc - plusBasSynDejaParc
        sondeurTousSynonymes = int(plusBasSynDejaParc) + int((diffHautBas - (diffHautBas % 2)) / 2)
        
        global estDejaDansLaListe
        
        if diffHautBas == 1:
          
            if synonyme != sondeurTousSynonymes:
                
                rechercheTermine = True
                
                estDejaDansLaListe = False
            
        elif synonyme > sondeurTousSynonymes:
            
            plusBasSynDejaParc = sondeurTousSynonymes
            
        elif synonyme < sondeurTousSynonymes:
            
            plusHautSynDejaParc = sondeurTousSynonymes
        
        elif synonyme == sondeurTousSynonymes:
            
            rechercheTermine = True
            
            estDejaDansLaListe = True
            
        
listeDesSynonymesDe(motCible, dfSyneurone, dejaParcouruTousSynonymesInclus, dejaParcouruSeulementMotCibleNiveau1, ajout,optimiseur, dejaParcouruTousSynonymesInclusNiveau3)

dfMotDeBase = dfMotCible
dfConcateneur = dfMotCible
incrementeur2 = 0

for incrementeur2 in range (len(dfMotDeBase)):
    
    listeDesSynonymesDe(dfMotDeBase.iloc[incrementeur2,2], dfSyneurone, dejaParcouruTousSynonymesInclus, dejaParcouruSeulementMotCibleNiveau1, ajout,optimiseur, dejaParcouruTousSynonymesInclusNiveau3 )
    dfConcateneur = pd.concat([dfConcateneur,dfMotCible], join ='inner', ignore_index = True)
    
    incrementeur2 += 1
    print(incrementeur2)

print(dfConcateneur)
dfNiveau1 = dfConcateneur


for incrementeur3 in range (len(dfNiveau1)):
    
    if dfNiveau1.iloc[incrementeur3,2] not in dejaParcouruSeulementMotCibleNiveau1 :
        
        listeDesSynonymesDe(dfNiveau1.iloc[incrementeur3,2], dfSyneurone, dejaParcouruTousSynonymesInclus, dejaParcouruSeulementMotCibleNiveau1, ajout, optimiseur, dejaParcouruTousSynonymesInclusNiveau3 )
        dfConcateneur = pd.concat([dfConcateneur,dfMotCible], join ='inner', ignore_index = True)
    
    incrementeur3 += 1
    print(incrementeur3)

dfNiveau2 = dfConcateneur

for incrementeur4 in range (len(dfNiveau2)):
    
    if dfNiveau2.iloc[incrementeur4,2] not in dejaParcouruSeulementMotCibleNiveau1 :
        
        listeDesSynonymesDe(dfNiveau2.iloc[incrementeur4,2], dfSyneurone, dejaParcouruTousSynonymesInclus, dejaParcouruSeulementMotCibleNiveau1, ajout, optimiseur, dejaParcouruTousSynonymesInclusNiveau3 )
        dfConcateneur = pd.concat([dfConcateneur,dfMotCible], join ='inner', ignore_index = True)
    
    incrementeur4 += 1
    print(incrementeur4)

#dfNiveau3 = dfConcateneur

dejaParcouruTousSynonymesInclusNiveau3 = []
dejaParcouruSeulementMotCibleNiveau3 = []

for incrementeur5 in range (len(dfNiveau3)):
    
    dejaParcouruTousSynonymesInclusNiveau3.append(dfNiveau3.iloc[incrementeur5,2])
    
    if incrementeur5 + 1 == (len(dfNiveau3)):
        
        if dfNiveau3.iloc[incrementeur5,0] != dfNiveau3.iloc[incrementeur5 - 1,0]:
            
            dejaParcouruSeulementMotCibleNiveau3.append(dfNiveau3.iloc[incrementeur5,0])
    
    else:
        
        if dfNiveau3.iloc[incrementeur5,0] != dfNiveau3.iloc[incrementeur5 + 1,0]:
        
            dejaParcouruSeulementMotCibleNiveau3.append(dfNiveau3.iloc[incrementeur5,0])


        
        