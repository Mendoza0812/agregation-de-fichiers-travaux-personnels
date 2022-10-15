# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 12:15:13 2022

@author: Max-Louis
"""

import pandas as pd

#DF10 SANS LES DOUBLONS
#isd = pd.read_csv(r'C:/Users/Max-Louis/idNSDist.csv')

#NOUVEAU DF10
df10 = pd.read_csv(r'C:/Users/Max-Louis/df10270822.csv')

comptage = pd.read_csv( r'C:/Users/Max-Louis/comptage270822.csv')

df13 = pd.read_csv( r'C:/Users/Max-Louis/df270822.csv')

regroupDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

numCibleDist = 1

cibleDist = regroupDists.iloc[numCibleDist,0]

indexByDist = ((df13[df13['dist'] <= cibleDist]).sort_values('mot')).reset_index(drop = True)

df10ByDist = df10[df10['dist'] <= cibleDist]

dfsv = df10.sort_values(['idN','syno2'], ascending = True).reset_index(drop = True)

# CREATION DE DF12 ET LES DFINFEGVAL
# repere les mots apparaissant le plus souvent

mot = []

nbDeSyno = []
indexDf10 = []
dist = []
progdf11sv = 1

for incr in range (len(indexByDist) - 1):
    
    if indexByDist.iloc[incr,0] == indexByDist.iloc[incr +1,0]:
        
        progdf11sv += 1
                   
    else:
        
        reccurence = incr
        incr1 = progdf11sv
        
        for incr1 in range (progdf11sv):
            
            mot.append(indexByDist.iloc[reccurence,0])
            nbDeSyno.append(progdf11sv)
            
            dist.append(indexByDist.iloc[reccurence,3])
            indexDf10.append(indexByDist.iloc[reccurence,2])
            
            reccurence -= 1
        
        progdf11sv = 1
        
    if incr + 1 == len(indexByDist):
        
        if indexByDist.iloc[incr,0] == indexByDist.iloc[incr +1,0]:
            
            progdf11sv += 1
        
        else:
            
            reccurence = incr
            incr1 = progdf11sv
            
            for incr1 in range (progdf11sv):
                
                mot.append(indexByDist.iloc[reccurence,0])
                nbDeSyno.append(progdf11sv)
                
                dist.append(indexByDist.iloc[reccurence,3])
                indexDf10.append(indexByDist.iloc[reccurence,2])
                
                reccurence -= 1
            
            progdf11sv = 1
            

plist = (mot, nbDeSyno, indexDf10, dist)
df12 = pd.DataFrame(plist).transpose()
df12.columns = ['mot', 'nbDeSyno','indexDf10', 'dist']
df12sv = df12.sort_values(['dist','indexDf10'], ascending = True).reset_index(drop = True)

verifStrctr1 = df12sv

mot_2 = []
nbDeSyno_2 = []
indexDf10_2 = []
dist_2 = []

nbGrade1 = 0

for incr in range (len(verifStrctr1) - 1):
    
    
    if incr + 1 == len(verifStrctr1):
    
        if verifStrctr1.iloc[incr,1] >= 2:
        
            if verifStrctr1.iloc[incr - 1,1] >= 2 and verifStrctr1.iloc[incr,2] == verifStrctr1.iloc[incr - 1, 2]:
                
                print(verifStrctr1.iloc[incr])
                    
                mot_2.append(verifStrctr1.iloc[incr,0])
                nbDeSyno_2.append(verifStrctr1.iloc[incr,1])
                indexDf10_2.append(verifStrctr1.iloc[incr,2])
                dist_2.append(verifStrctr1.iloc[incr,3])
                    
                print(verifStrctr1.iloc[incr - 1])
                    
                mot_2.append(verifStrctr1.iloc[incr - 1,0])
                nbDeSyno_2.append(verifStrctr1.iloc[incr - 1,1])
                indexDf10_2.append(verifStrctr1.iloc[incr - 1,2])
                dist_2.append(verifStrctr1.iloc[incr - 1,3])
                
                nbGrade1 += 1
                
            #else: créer une df qui fait le tour de la structure
                    
    
    elif verifStrctr1.iloc[incr,1] >= 2 and verifStrctr1.iloc[incr + 1,1] >= 2 and verifStrctr1.iloc[incr,2] == verifStrctr1.iloc[incr + 1, 2]:
            
                print(verifStrctr1.iloc[incr])
                
                mot_2.append(verifStrctr1.iloc[incr,0])
                nbDeSyno_2.append(verifStrctr1.iloc[incr,1])
                indexDf10_2.append(verifStrctr1.iloc[incr,2])
                dist_2.append(verifStrctr1.iloc[incr,3])
                
                print(verifStrctr1.iloc[incr + 1])
                
                mot_2.append(verifStrctr1.iloc[incr + 1,0])
                nbDeSyno_2.append(verifStrctr1.iloc[incr + 1,1])
                indexDf10_2.append(verifStrctr1.iloc[incr + 1,2])
                dist_2.append(verifStrctr1.iloc[incr + 1,3])
                
                nbGrade1 += 1
                
print('nbGrade1 = ' + str(nbGrade1))
plist_2 = (mot_2, nbDeSyno_2, indexDf10_2, dist_2)
df13_1 = pd.DataFrame(plist_2).transpose()
df13_1.columns = ['mot_2', 'nbDeSyno_2','indexDf10_2', 'dist']
df13_1svMot = df13_1.sort_values('mot_2', ascending = True).reset_index(drop = True)

nbGrade0 = 0
numGrade0 = []
nbGrade1 = 0
numGrade1 = []
idMot0 = []