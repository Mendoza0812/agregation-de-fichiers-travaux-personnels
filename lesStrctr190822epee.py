# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 23:44:08 2022

@author: Max-Louis
"""

import pandas as pd

# df10 = df classe de distance 1 a 800, de a a z

df10 = pd.read_csv(r'C:/Users/Max-Louis/dfDistSorted.csv')

listOfDists = pd.read_csv(r'C:/Users/Max-Louis/dist180822.csv')

df11 = pd.read_csv(r'C:/Users/Max-Louis/df11Idxdf10180822.csv')

cibleLOD = listOfDists.iloc[0,0]

df11SortV = ((df11[df11['dist'] <= cibleLOD]).sort_values('mot')).reset_index(drop = True)

distInfEg = df10[df10['distance'] <= cibleLOD]

#df12svDist1 = pd.read_csv(r'C:/Users/Max-Louis/df12svDist1.csv')

#dfInfEgVal201 = pd.read_csv(r'C:/Users/Max-Louis/dfInfEgVal201.csv')
dfInfEgVal268 = pd.read_csv(r'C:/Users/Max-Louis/dfInfEgVal268.csv')


# CREATION DE DF12 ET LES DFINFEGVAL
# repere les mots apparaissant le plus souvent

mot = []
nbDistInfEgVal = []
progdf11sv = 1

for incr in range (len(df11SortV) - 1):
    
    if df11SortV.iloc[incr,0] == df11SortV.iloc[incr +1,0]:
        
        progdf11sv += 1
                   
    else:
        
        mot.append(df11SortV.iloc[incr,0])
        nbDistInfEgVal.append(progdf11sv)
        progdf11sv = 1
        
    if incr + 1 == len(df11SortV):
        
        if df11SortV.iloc[incr,0] == df11SortV.iloc[incr +1,0]:
            
            progdf11sv += 1
        
        else:
            
            mot.append(df11SortV.iloc[incr+1,0])
            nbDistInfEgVal.append(progdf11sv)
            progdf11sv = 1

plist = (mot, nbDistInfEgVal)
df12 = pd.DataFrame(plist).transpose()
df12.columns = ['mot', 'nbDistInfEgVal']
df12sv = df12.sort_values('nbDistInfEgVal', ascending = False).reset_index(drop = True)
dfInfEgVal = df12sv[df12sv['nbDistInfEgVal'] >= 2]


#dfInfEgVal268.to_csv('dfInfEgVal268.csv', index = False)

numStctr = 0
liNumStrctr = []
comparateur = []
mot2eDegre = []

for incr in range (len(dfInfEgVal)):
#for incr in range(34):
    
    mot = dfInfEgVal.iloc[incr,0]
    
    lgrMot = len(dfInfEgVal.iloc[incr,0])
    
    strCntnMot = distInfEg [ distInfEg ['idN'].str.contains(mot)].reset_index(drop = True)
    strCntnMot2 =  distInfEg [ distInfEg ['syno2'].str.contains(mot)].reset_index(drop = True)
    
    #print(strCntnMot)
    #print(strCntnMot2)
    
    
    for incr1 in range (len(strCntnMot2)):
        
        if len(strCntnMot2.iloc[incr1,2]) == len(mot):
        
            nbLiensMot1erDegre = dfInfEgVal268[dfInfEgVal268['mot'].str.contains(strCntnMot2.iloc[incr1,0])]
            #print(nbLiensMot1erDegre)
            
            nbLiensReel = 0
            
            for incr2 in range(len(nbLiensMot1erDegre)):
                
                if len(nbLiensMot1erDegre.iloc[incr2,0]) == len(strCntnMot2.iloc[incr1,0]):
                    
                    nbLiensReel += 1
                    mot2eDegre.append(nbLiensMot1erDegre.iloc[incr2,0])
            
                    #print(nbLiensReel)
                
                if nbLiensReel > 1:
                    
                    print(mot2eDegre)
    
                    # Si > 1, le mot degre zero a un mot 1er degre en rapport avec un autre synonyme
               
                #print('incr2 = ' + str(incr2))     
        #print('incr1 = ' + str(incr1))
    #print('incr = ' + str(incr))