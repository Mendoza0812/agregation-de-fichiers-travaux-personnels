# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 11:29:28 2022

@author: Max-Louis
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

def fouille (nbRange, strCntn, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2):
    
    global sansIssue
    sansIssue = False
    
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
            
        else:
            
            print('strCntn.iloc[incr,2] in sortIndexDf10')
            print('strCntn.iloc[incr,2] = ' + str(strCntn.iloc[incr,2]) )
            print('sortIndexDf10 = ' + str(sortIndexDf10))
            print('incr = ' + str(incr))
            print('nbRange = ' + str(nbRange))
            
            print(len(strCntn))
            
            if incr == (len(strCntn) - 1) and len(strCntn) == 1:
                print('incr == (len(StrCntn - 1)')
                print('oulala')
                print('strCntn = \n' + str(strCntn))
                print('strCntn2 = \n' + str(strCntn2))
                
                sansIssue = True
            
            #elif


fouille (1, dfNSyn, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

prev = strCntn2

fouille (2, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

midle = prev
prev = strCntn2

fouille (2, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

if sansIssue == True:
    
    fouille (1, prev, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

front = midle
midle = prev
prev = strCntn2

fouille (2, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

if sansIssue == True:
    
    fouille (1, prev, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

front = midle
midle = prev
prev = strCntn2

fouille (2, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

if sansIssue == True:
    
    fouille (1, prev, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

front = midle
midle = prev
prev = strCntn2

fouille (1, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

if sansIssue == True:
    
    fouille (1, prev, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

front = midle
midle = prev
prev = strCntn2

fouille (2, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

if sansIssue == True:
    
    fouille (1, prev, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

front = midle
midle = prev
prev = strCntn2

fouille (1, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

if sansIssue == True:
    
    fouille (2, front, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
    
front = midle
midle = prev
prev = strCntn2

fouille (1, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

if sansIssue == True:
    
    fouille (2, front, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
    
front = midle
midle = prev
prev = strCntn2

fouille (2, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

if sansIssue == True:
    
    fouille (2, front, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
    
front = midle
midle = prev
prev = strCntn2

fouille (2, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

if sansIssue == True:
    
    fouille (2, front, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
    
front = midle
midle = prev
prev = strCntn2

fouille (1, strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

if sansIssue == True:
    
    fouille ((len(front)), front, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
    
front = midle
midle = prev
prev = strCntn2

fouille ((len(strCntn2)), strCntn2, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)

if sansIssue == True:
    
    fouille (3, midle, sortIndexDf10, mot0, nSyn, dist, idxDf10, mot2)
    
front = midle
midle = prev
prev = strCntn2

plst = (mot0, nSyn, mot2, dist, idxDf10)
df = pd.DataFrame(plst).transpose()
df.columns = ['mot0', 'nSyn', 'mot2', 'dist', 'idxDf10']