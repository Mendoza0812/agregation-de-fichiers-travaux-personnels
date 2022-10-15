# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 07:51:04 2022

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

numCibleDist = 342

cibleDist = regroupDists.iloc[numCibleDist,0]

indexByDist = ((df13[df13['dist'] <= cibleDist]).sort_values('mot')).reset_index(drop = True)

df10ByDist = df10[df10['dist'] <= cibleDist]

dfsv = df10.sort_values('idN', ascending = True).reset_index(drop = True)

# CREATION DE DF12 ET LES DFINFEGVAL
# repere les mots apparaissant le plus souvent

comptage2 = comptage.sort_values(['mot','dist'], ascending = True)


def compteurDeSynonymes(indexByDist):
    
    global mot
    mot = []

    global nbDeSyno
    nbDeSyno = []
    
    global indexDf10
    indexDf10 = []
    
    global dist
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
                
                dist.append(indexByDist.iloc[reccurence,1])
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
                    
                    dist.append(indexByDist.iloc[reccurence,1])
                    indexDf10.append(indexByDist.iloc[reccurence,2])
                    
                    reccurence -= 1
                
                progdf11sv = 1
            

compteurDeSynonymes(comptage2)

plist = (mot, nbDeSyno, indexDf10, dist)
df12 = pd.DataFrame(plist).transpose()
df12.columns = ['mot', 'nbDeSyno','indexDf10', 'dist']
df12sv = df12.sort_values(['nbDeSyno','dist','mot'], ascending = [False,True,True]).reset_index(drop = True)

numStrctr = 0
nbStrctr = []
indexDf10 = []
        

