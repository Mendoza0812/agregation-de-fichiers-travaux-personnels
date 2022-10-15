# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 22:56:56 2022

@author: Max-Louis
"""

import pandas as pd

df10 = pd.read_csv(r'C:/Users/Max-Louis/dfDistSorted.csv')

index = pd.read_csv(r'C:/Users/Max-Louis/df11Idxdf10180822.csv')

regroupDists = pd.read_csv(r'C:/Users/Max-Louis/dist180822.csv')

cibleDist = regroupDists.iloc[0,0]

indexByDist = ((index[index['dist'] <= cibleDist]).sort_values('mot')).reset_index(drop = True)

df10ByDist = df10[df10['distance'] <= cibleDist]

#dfsvidN pour enlever les doublons
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
            

plist = (mot, nbDeSyno, indexDf10, dist)
df12 = pd.DataFrame(plist).transpose()
df12.columns = ['mot', 'nbDeSyno','indexDf10', 'dist']
df12sv = df12.sort_values('nbDeSyno', ascending = False).reset_index(drop = True)
dfInfEgVal = df12sv[df12sv['nbDeSyno'] >= 1]

dfieg = dfInfEgVal

verifStrctr = dfieg.sort_values( ['nbDeSyno','mot','indexDf10', 'dist'], ascending = False).reset_index(drop = True)

"""
grade1 = 0
nGrade1 = []

for incr in range (len(verifStrctr) - 1):
    
    nGrade1.append(grade1)
    
    if verifStrctr.iloc[incr,0] != verifStrctr.iloc[incr +1,0]:
        
        grade1 += 1
        
nGrade1.append(grade1)

verifStrctr['nGrade1'] = nGrade1
"""

verifStrctr1 = dfieg.sort_values( 'indexDf10', ascending = True).reset_index(drop = True)

mot_2 = []
nbDeSyno_2 = []
indexDf10_2 = []
dist_2 = []

nbGrade1 = 0

for incr in range (len(verifStrctr1) - 1):
    
    if incr + 1 == len(verifStrctr1):
        
        if verifStrctr1.iloc[incr,1] >= 2 :
            
            if verifStrctr1.iloc[incr - 1,1] >= 2:
                
                if verifStrctr1.iloc[incr,2] == verifStrctr1.iloc[incr - 1, 2]:
                
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
    
    if verifStrctr1.iloc[incr,1] >= 2 :
        
        if verifStrctr1.iloc[incr + 1,1] >= 2:
            
            if verifStrctr1.iloc[incr,2] == verifStrctr1.iloc[incr + 1, 2]:
            
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
df13 = pd.DataFrame(plist_2).transpose()
df13.columns = ['mot_2', 'nbDeSyno_2','indexDf10_2', 'dist']
df13svMot = df13.sort_values('mot_2', ascending = True).reset_index(drop = True)


"""
stockdist = []

mot_3 = []
nbDeSyno_3 = []
indexDf10_3 = []
dist_3 = []

for incr in range (len(df13) - 1):
    
    if incr + 1 == len(df13):
        
        if df13svMot.iloc[incr,0] == df13svMot.iloc[incr-1,0]:
            
            if df13.iloc[incr,2] == df13.iloc[incr-1,2]:
                
                if df13.iloc[incr,0] != df13.iloc[incr - 1,0]:
                    
                    if df13svMot.iloc[incr,2] != df13svMot.iloc[incr-1,2]:
                        
                        print('___')
                        print(df13.iloc[incr])
                        
                        stockdist.append(df13.iloc[incr,3])
                        stockdist.append(df13svMot.iloc[incr - 1,3])
                        
    
    if df13svMot.iloc[incr,0] == df13svMot.iloc[incr+1,0]:
        
        if df13.iloc[incr,2] == df13.iloc[incr+1,2]:
            
            if df13.iloc[incr,0] != df13.iloc[incr + 1,0]:
                
                if df13svMot.iloc[incr,2] != df13svMot.iloc[incr+1,2]:
                    
                    print('___')
                    print(df13.iloc[incr])
            
                    stockdist.append(df13.iloc[incr,3])
                    stockdist.append(df13svMot.iloc[incr - 1,3])
    
    else: 
        
        mot_3.append(df13.iloc[incr,0])
        nbDeSyno_3.append(df13.iloc[incr,1])
        indexDf10_3.append(df13.iloc[incr,2])
        dist_3.append(df13.iloc[incr,3])
        


# A PERMIS DE CREER IDNSDIST SOIT DF10 SANS DOUBLON

idN = []
syno2 = []
dist = []

incr = 0

for i in range (len(dfsv) - 1):
    
    if dfsv.iloc[incr,0] == dfsv.iloc[incr,2]:
        
        print(dfsv.iloc[incr])
        
        incr += 1

        
    elif dfsv.iloc[incr,0] == dfsv.iloc[incr + 1,0]:
        
        if dfsv.iloc[incr,2] == dfsv.iloc[incr + 1, 2]:
            
            print(dfsv.iloc[incr,0])
            #idN.append(dfsv.iloc[incr, 0])
            print(dfsv.iloc[incr, 2])
            #syno2.append(dfsv.iloc[incr,2])
            #dist.append(dfsv.iloc[incr,4])
            print(dfsv.iloc[incr + 1,0])
            print(dfsv.iloc[incr + 1,2])
                
            incr += 1
            
        else:
            
            idN.append(dfsv.iloc[incr,0])
            syno2.append(dfsv.iloc[incr,2])
            dist.append(dfsv.iloc[incr,4])
            
            incr += 1
    
    else:
        
        idN.append(dfsv.iloc[incr,0])
        syno2.append(dfsv.iloc[incr,2])
        dist.append(dfsv.iloc[incr,4])
        
        incr += 1

plst = (idN, syno2, dist)
idNSDist = pd.DataFrame(plst).transpose()
idNSDist.columns = ['idN','syno2','dist']

"""