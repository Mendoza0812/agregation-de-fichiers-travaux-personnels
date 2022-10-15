# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 19:24:52 2022

@author: Max-Louis
"""

import pandas as pd

df10 = pd.read_csv(r'C:/Users/Max-Louis/df10Ref.csv')

incrDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

dfNSyn = pd.read_csv( r'C:/Users/Max-Louis/df12svRef.csv')


idxDf10 = []
sortIndexDf10 = []
sortRef = []
    
surveilMot = []
    
idx10Prev = []
numColmnPrev = []
refPrev = []

lenStrCntn = []

#Sur lenStrCntn
nbLenStrCntn = []

def fouille (nbRange, strCntn, sortIndexDf10, idx10Prev, numColmnPrev):
    
    global sansIssue
    sansIssue = False
    
    for incr in range (nbRange):
        
        if strCntn.iloc[incr,2] not in sortIndexDf10:
            print('strCntn.iloc[incr,2] not in sortIndexDf10')
            
            print(df10.iloc[strCntn.iloc[incr,2]])
            idxDf10.append(strCntn.iloc[incr,2])
            sortIndexDf10.append(strCntn.iloc[incr,2])
            
            idx10Prev.append(strCntn.iloc[incr + 1,2])
        
            if strCntn.iloc[incr,0] == df10.iloc[strCntn.iloc[incr,2],0]:
                
                motSuivant = df10.iloc[strCntn.iloc[incr,2],1]
                
                numColmnPrev.append(1)
                surveilMot.append(df10.iloc[strCntn.iloc[incr,2],1])
            
            else:
                
                motSuivant = df10.iloc[strCntn.iloc[incr,2],0]
            
                numColmnPrev.append(0)
                
                surveilMot.append(df10.iloc[strCntn.iloc[incr,2],0])
        else:
            
            if incr == (len(strCntn) - 1) and len(strCntn) == 1: 
                
                print('strCntn.iloc[incr,2] in sortIndexDf10')
                    
                sansIssue = True
                    
                motSuivant = df10.iloc[idx10Prev[(len(idx10Prev)- 1)],2],numColmnPrev[(len(numColmnPrev) - 1)]
                
                
                del idx10Prev[(len(idx10Prev)-1)]
                    
                del numColmnPrev[(len(numColmnPrev) - 1)]
                
            else:
                print('strCntn.iloc[incr,2] in sortIndexDf10 but len(strCntn) != 1')
                
                print(df10.iloc[strCntn.iloc[incr+1,2]])
                idxDf10.append(strCntn.iloc[incr+1,2])
                sortIndexDf10.append(strCntn.iloc[incr+1,2])
                
                idx10Prev.append(strCntn.iloc[incr + 2,2])
            
                if strCntn.iloc[incr+1,0] == df10.iloc[strCntn.iloc[incr+1,2],0]:
                    
                    motSuivant = df10.iloc[strCntn.iloc[incr+1,2],1]
                    
                    numColmnPrev.append(1)
                    surveilMot.append(df10.iloc[strCntn.iloc[incr+1,2],1])
                
                else:
                    
                    motSuivant = df10.iloc[strCntn.iloc[incr+1,2],0]
                
                    numColmnPrev.append(0)
                    
                    surveilMot.append(df10.iloc[strCntn.iloc[incr+1,2],0])
            
        refEff = str(motSuivant) + str(len(motSuivant))
        refPrev.append(refEff)
        
        global strCntn2
        strCntn2 = dfNSyn[dfNSyn['ref'].str.contains(refEff)]
        print(strCntn2)
        
fouille (1, dfNSyn, sortIndexDf10, idx10Prev, numColmnPrev)
fouille (1, strCntn2, sortIndexDf10,  idx10Prev, numColmnPrev)
fouille (1, strCntn2, sortIndexDf10,  idx10Prev, numColmnPrev)
fouille (1, strCntn2, sortIndexDf10,  idx10Prev, numColmnPrev)
fouille (1, strCntn2, sortIndexDf10,  idx10Prev, numColmnPrev)
fouille (1, strCntn2, sortIndexDf10,  idx10Prev, numColmnPrev)
fouille (1, strCntn2, sortIndexDf10,  idx10Prev, numColmnPrev)
fouille (1, strCntn2, sortIndexDf10,  idx10Prev, numColmnPrev)