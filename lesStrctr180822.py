# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 01:48:38 2022

@author: Max-Louis
"""

import pandas as pd

df10 = pd.read_csv(r'C:/Users/Max-Louis/dfDistSorted.csv')

listOfDists = pd.read_csv(r'C:/Users/Max-Louis/dist180822.csv')

df11 = pd.read_csv(r'C:/Users/Max-Louis/df11Idxdf10180822.csv')

df11SortV = ((df11[df11['dist'] == 1]).sort_values('mot')).reset_index(drop = True)

dist1 = df10[df10['distance'] == 1]

"""
# CREATION DE LISTOFDISTS

distances = []

for incr in range (len(df10)):
    
    if incr == len(df10):
        
        if df10.iloc[incr,4] != df10.iloc[incr - 1, 4]:
            
            distances.append(df10.iloc[incr,4])
            break
    
    if df10.iloc[incr,4] != df10.iloc[incr + 1, 4]:
        
        distances.append(df10.iloc[incr,4])
        
# FIN DE CREATION DE LISTOFDISTS

# CREATION DE DF11 AVEC INDEXDEDF10 SUR CHAQUE MOT
mot = []
dist = []
indexDf10 = []

for incr in range (len(df10)):
    
    mot.append(df10.iloc[incr,0])
    dist.append(df10.iloc[incr,4])
    indexDf10.append(incr)
    
    mot.append(df10.iloc[incr,2])
    dist.append(df10.iloc[incr,4])
    indexDf10.append(incr)
    
plist = (mot, dist, indexDf10)
df11 = pd.DataFrame(plist).transpose()
df11.columns = ['mot','dist','indexDf10']

# FIN DF11

#CREATION DF11SORTV

nbMax = 0

nombr = 1

for incr in range (len(df11SortV) - 1):
    
    if df11SortV.iloc[incr,0] == df11SortV.iloc[incr + 1,0]:
        
        nombr += 1
        
    else:
        
        nombr = 1
    
    if nbMax < nombr:
        
        nbMax = nombr
        string = df11SortV.iloc[incr,0]
        aConnaitre = df11SortV.iloc[incr,2]

print(nbMax)

#FIN DE CREATION DF11SORTV
"""

# CREATION DE DF12
# repere les mots apparaissant le plus souvent

mot = []
nbDistIdtq = []
progdf11sv = 1

for incr in range (len(df11SortV) - 1):
    
    if df11SortV.iloc[incr,0] == df11SortV.iloc[incr +1,0]:
        
        progdf11sv += 1
                   
    else:
        
        mot.append(df11SortV.iloc[incr,0])
        nbDistIdtq.append(progdf11sv)
        progdf11sv = 1
        
    if incr + 1 == len(df11SortV):
        
        if df11SortV.iloc[incr,0] == df11SortV.iloc[incr +1,0]:
            
            progdf11sv += 1
        
        else:
            
            mot.append(df11SortV.iloc[incr+1,0])
            nbDistIdtq.append(progdf11sv)
            progdf11sv = 1

plist = (mot, nbDistIdtq)
df12 = pd.DataFrame(plist).transpose()
df12.columns = ['mot', 'nbDistIdtq']
df12sv = df12.sort_values('nbDistIdtq', ascending = False).reset_index(drop = True)
