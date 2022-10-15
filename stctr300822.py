# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 03:40:44 2022

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

df10 = pd.read_csv(r'C:/Users/Max-Louis/df10Ref.csv')

incrDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

dfNSyn = pd.read_csv( r'C:/Users/Max-Louis/df12svRef.csv')

mot0 = []
nSyn = []
mot2 = []
dist = []
idxDf10 = []

sortIndexDf10 = []
sortRef = []

"""
mot0.append(dfNSyn.iloc[0,0])
nSyn.append(dfNSyn.iloc[0,1])
mot2.append(df10.iloc[dfNSyn.iloc[0,2],1])
print(df10.iloc[dfNSyn.iloc[0,2]])
dist.append(dfNSyn.iloc[0,3])
idxDf10.append(dfNSyn.iloc[0,2])
sortIndexDf10.append(dfNSyn.iloc[0,2])

strCntn = dfNSyn[dfNSyn['mot'].str.contains(df10.iloc[dfNSyn.iloc[0,2],1])]
print(dfNSyn[dfNSyn['mot'].str.contains(df10.iloc[dfNSyn.iloc[0,2],1])])
"""
def fouille (nbRange, strCntn, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2):
    
    for incr in range (nbRange):
        
        if strCntn.iloc[incr,2] not in sortIndexDf10:
             
            mot0.append(strCntn.iloc[incr,0])
            nSyn.append(strCntn.iloc[incr,1])
            
            
            print(df10.iloc[strCntn.iloc[incr,2]])
            dist.append(strCntn.iloc[incr,3])
            idxDf10.append(strCntn.iloc[incr,2])
            sortIndexDf10.append(strCntn.iloc[incr,2])
            
            if strCntn.iloc[incr,0] == df10.iloc[strCntn.iloc[incr,2],0]:
                
                motSuivant = df10.iloc[strCntn.iloc[incr,2],1]
            
            else:
                
                motSuivant = df10.iloc[strCntn.iloc[incr,2],0]
            
            mot2.append(motSuivant)
            
            refEff = str(motSuivant) + str(len(motSuivant))
            
            global strCntn2
            strCntn2 = dfNSyn[dfNSyn['ref'].str.contains(refEff)]
            print(strCntn2)

fouille (1, dfNSyn, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
fouille (2, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
fouille (2, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
fouille (2, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
fouille (2, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
fouille (1, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
fouille (2, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
"""           
for incr in range (len(strCntn)):
    
    if strCntn.iloc[incr,2] not in sortIndexDf10:
         
        mot0.append(strCntn.iloc[incr,0])
        nSyn.append(strCntn.iloc[incr,1])
        
        
        print(df10.iloc[strCntn.iloc[incr,2]])
        dist.append(strCntn.iloc[incr,3])
        idxDf10.append(strCntn.iloc[incr,2])
        sortIndexDf10.append(strCntn.iloc[incr,2])
        
        if strCntn.iloc[incr,0] == df10.iloc[strCntn.iloc[incr,2],0]:
            
            motSuivant = df10.iloc[strCntn.iloc[incr,2],1]
        
        else:
            
            motSuivant = df10.iloc[strCntn.iloc[incr,2],0]
        
        mot2.append(motSuivant)
        
        refEff = str(motSuivant) + str(len(motSuivant))
        global strCntn2
        strCntn2 = dfNSyn[dfNSyn['ref'].str.contains(refEff)]
        print(strCntn2)
        
        for incr1 in range(2):
            
            if strCntn2.iloc[incr1,2] not in sortIndexDf10:
                 
                mot0.append(strCntn2.iloc[incr1,0])
                nSyn.append(strCntn2.iloc[incr1,1])
                
                print(df10.iloc[strCntn2.iloc[incr1,2]])
                dist.append(strCntn2.iloc[incr1,3])
                idxDf10.append(strCntn2.iloc[incr1,2])
                sortIndexDf10.append(strCntn2.iloc[incr1,2])
                
                if strCntn2.iloc[incr1,0] == df10.iloc[strCntn2.iloc[incr1,2],0]:
                    
                    motSuivant2 = df10.iloc[strCntn2.iloc[incr1,2],1]
                
                else:
                    
                    motSuivant2 = df10.iloc[strCntn2.iloc[incr1,2],0]
                
                mot2.append(motSuivant2)
                
                refEff2 = str(motSuivant2) + str(len(motSuivant2))
                strCntn3 = dfNSyn[dfNSyn['ref'].str.contains(refEff2)]
                print(strCntn3)
        #if incr == len(strCntn)
"""

plst = (mot0, nSyn, mot2, dist, idxDf10)
df = pd.DataFrame(plst).transpose()
df.columns = ['mot0', 'nSyn', 'mot2', 'dist', 'idxDf10']