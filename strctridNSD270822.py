# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 04:16:20 2022

@author: Max-Louis

les doublons ont tous ete enleves, il faut refaire les bdd qui ont ete faites 
"""

import pandas as pd

#DF10 SANS LES DOUBLONS
isd = pd.read_csv(r'C:/Users/Max-Louis/idNSDist.csv')

isdsv = isd.sort_values(['dist','idN','syno2'], ascending = True).reset_index(drop = True)

comptage = pd.read_csv( r'C:/Users/Max-Louis/comptage270822.csv')

df13 = pd.read_csv( r'C:/Users/Max-Louis/df270822.csv')

regroupDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

"""
mot = []

dist = []
index = []

for incr in range (len(isdsv) - 1):
        
    mot.append(isdsv.iloc[incr,0])
    mot.append(isdsv.iloc[incr,1])
    
    for loop in range (2):
        
        dist.append(isdsv.iloc[incr,2])
        index.append(incr)
    
    print(incr)
        
plst = (mot, dist, index)
indexisdsv = pd.DataFrame(plst).transpose()
indexisdsv.columns = ['mot', 'dist', 'index']
comptage = indexisdsv.sort_values(['dist','mot'], ascending = True).reset_index(drop = True)

mot = []
nbDeSyno = []
dist = []
indexDf10 = []

indexByDist = comptage

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
            
    print(incr)
            

plist = (mot, nbDeSyno, indexDf10, dist)
df12 = pd.DataFrame(plist).transpose()
df12.columns = ['mot', 'nbDeSyno','indexDf10', 'dist']


dists = []

for incr in range (len(df13) - 1):
    
    if incr + 1 == len(df13):
            
            dists.append(df13.iloc[incr,3])
    
    else:
        
        if df13.iloc[incr,3] != df13.iloc[incr + 1,3]:
            
            dists.append(df13.iloc[incr,3])

dists.append(801)
    
regroupDists = pd.DataFrame(dists)

"""