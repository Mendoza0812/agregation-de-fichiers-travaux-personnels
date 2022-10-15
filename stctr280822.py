# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:10:30 2022

@author: Max-Louis

APPUYER SUR F5
Continuer avec les synonymes de efficace: pb, le programme doit 
reconnaitre qu'il est deja passe au meme endroit en stockant la var 
indexDf10 ou le mot ref dans une liste et etablir une condition 
'if tel indexDf10 in listeStock...' ou inversement 'if ... not in ...'
ici indexDf10 de 25322 est le synonyme de performant (deja passe avec 27334
en ayant etabli une condition if permettant de reconnaitre si idN ou syno
ne soit pas confondu avec le modorgn                                                      
lui meme synonyme de bon
"""

import pandas as pd

#df10 = pd.read_csv(r'C:/Users/Max-Louis/df10270822.csv')

df10 = pd.read_csv(r'C:/Users/Max-Louis/df10Ref.csv')

regroupDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

regroupNbSyno = pd.read_csv(r'C:/Users/Max-Louis/regroupMotSyno.csv')

#df12sv = pd.read_csv( r'C:/Users/Max-Louis/analysStctr280822.csv')

df12sv = pd.read_csv( r'C:/Users/Max-Louis/df12svRef.csv')

pssgeIndex = []
pssgeMot = []

nbStctr = 0

cibleNbSyno = 0
prog = 0

"""
# REGROUPMOTSYNO.CSV
for incr in range (len(df12sv)-1):
    
    if incr + 1 == len(df12sv):
        
        if df12sv.iloc[incr,0] != df12sv.iloc[incr-1,0]:
            
            mot.append(df12sv.iloc[incr,0])
            nbDeSyno.append(df12sv.iloc[incr,1])
    
    if df12sv.iloc[incr,0] != df12sv.iloc[incr+1,0]:
        
        mot.append(df12sv.iloc[incr,0])
        nbDeSyno.append(df12sv.iloc[incr,1])
    
    print(incr)

plst = (mot, nbDeSyno)
dfMotParNbSyno  = pd.DataFrame(plst).transpose()
dfMotParNbSyno.columns = ['mot','nbDeSyno']
"""
    
indexDf12 = prog

mot = []
nbDeSyno = []
mot2 = []
indexDf10 = []
dist = []
numStctr = []

    
#for incr in range (regroupNbSyno.iloc[cibleNbSyno,1]):
for incr in range (1):
            
            mot.append(df12sv.iloc[indexDf12,0])
            
            pssgeMot.append(df12sv.iloc[indexDf12,0])
            
            nbDeSyno.append(df12sv.iloc[indexDf12,1])
            indexDf10.append(df12sv.iloc[indexDf12,2])
            
            pssgeIndex.append(df12sv.iloc[indexDf12,2])
            
            dist.append(df12sv.iloc[indexDf12,3])
            numStctr.append(nbStctr)
            
            print(df12sv.iloc[indexDf12])
            
            indexSynoDf10 = df12sv.iloc[indexDf12,2]
            synoGrade1 = df10.iloc[indexSynoDf10,1]
            
            mot2.append(synoGrade1)
            mot.append(synoGrade1)
            
            refS1 = (str(synoGrade1) + str(len(synoGrade1)))
            liSynoGrade1 = df12sv[df12sv['ref'].str.contains(refS1)]
            
            print(liSynoGrade1)
            
            for incr in range (len(liSynoGrade1)):
                
                
                if liSynoGrade1.iloc[incr,2] not in pssgeIndex :
                    
                    indexSynoDf10_2 = liSynoGrade1.iloc[incr,2]
                    
                    dist.append(df10.iloc[indexSynoDf10_2,2])
                    nbDeSyno.append(df10.iloc[indexSynoDf10_2,1])
                    indexDf10.append(df12sv.iloc[incr,1])
                    numStctr.append(nbStctr)
                    
                    pssgeIndex.append(indexSynoDf10_2)
                    
                    if df10.iloc[indexSynoDf10_2,1] not in pssgeMot:
                        
                        synoGrade2 = df10.iloc[indexSynoDf10_2,0]
                        
                    else:
                        
                        synoGrade2 = df10.iloc[indexSynoDf10_2,1]
                    
                    
                    pssgeMot.append(synoGrade2)
                    
                    mot2.append(synoGrade2)
                    mot.append(synoGrade2)
                    
                    print(synoGrade2)
                    
                    refS2 = (str(synoGrade2) + str(len(synoGrade2)))
                    liSynoGrade2 = df12sv[df12sv['ref'].str.contains(refS2)]
                    
                    print(liSynoGrade2)
                    
            indexDf12 += 1


plist = (mot,nbDeSyno, mot2, indexDf10, dist, numStctr)
dfStctr = pd.DataFrame(plist).transpose()
dfStctr.columns = ['mot', 'nbDeSyno', 'mot2', 'indexDf10', 'dist', 'numStrctr']

"""
#DF12SVREF.CSV
ref = []

for incr in range (len(df12sv)):
    
    ref.append(str(df12sv.iloc[incr,0])+str(len(df12sv.iloc[incr,0])))
    
df12sv['ref'] = ref

#fin de df12svRef

#DF10REF.CSV

ref = []

for incr in range (len(df10)):
    
    ref.append(str(df10.iloc[incr,0])+str(len(df10.iloc[incr,0])))
    
df10['ref'] = ref
"""