# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 23:08:14 2022

@author: Max-Louis
"""

import pandas as pd

dzAlphNb = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzAlphNb.csv')
dzInvAlphNb = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzInvAlphNb.csv')

idN = []
natN = []
syno = []
natS = []
val800 = []
    
varPrgrsv = 0

def moduloMoitie(valeur):
    
    global moitie
    moitie = int((valeur - (valeur % 2)) / 2)
    
# la longueur de la liste chez IN et SYN sont la meme car la bdd est la mm    
totalIN = len(dzAlphNb)
totalSYN = len(dzInvAlphNb)

moduloMoitie(totalIN)
print(moitie)

varZigzag = moitie
varZigzagInv = moitie

boutDuCompte = False

plusBas = 0
plusHaut = totalIN

plusBasInv = 0
plusHautInv = totalSYN

var6L = 0
li6L = []
for loop in range (382551):
    
    string0 = dzAlphNb.iloc[var6L,0]
    string2 = dzAlphNb.iloc[var6L,2]
    string4 = string0[0:3] + string2[0:3]
    li6L.append(string4)
    var6L += 1
    print(var6L)
"""   
while varPrgrsv < totalIN:
        
    if dzAlphNb.iloc[varPrgrsv,0] == dzInvAlphNb.iloc[varZigzag,0]:
            
        if dzInvAlphNb.iloc[varPrgrsv,0] == dzAlphNb.iloc[varZigzag,0]:
            idN.append(dzAlphNb.iloc[varPrgrsv,0])
            natN.append(dzAlphNb.iloc[varPrgrsv,1])
            syno.append(dzAlphNb.iloc[varPrgrsv,2])
            natS.append(dzAlphNb.iloc[varZigzag,1])
            val800.append(dzAlphNb.iloc[varZigzag,3] + dzAlphNb.iloc[varPrgrsv,3])
            varPrgrsv += 1
            varZigzag = moitie
                
            
        elif dzInvAlphNb.iloc[varPrgrsv,0] < dzAlphNb.iloc[varZigzag,0]:
                
            plusBasInv = varZigzagInv
            
        elif dzInvAlphNb.iloc[varPrgrsv,0] > dzAlphNb.iloc[varZigzag,0]:
                
            plusHautInv = varZigzagInv
                
        diffInvPhPb = plusHautInv - plusBasInv
        
        varZigzagInv = plusBasInv + int((diffInvPhPb -(diffInvPhPb % 2))/2)
        
        if diffInvPhPb < 2:
            
            idN.append(dzAlphNb.iloc[varPrgrsv,0])
            natN.append(dzAlphNb.iloc[varPrgrsv,1])
            syno.append(dzAlphNb.iloc[varPrgrsv,2])
            natS.append('')
            val800.append(dzAlphNb.iloc[varPrgrsv,3] * 2)
                
            varPrgrsv += 1
            varZigzagInv = moitie
                
    elif dzAlphNb.iloc[varPrgrsv,0] < dzInvAlphNb.iloc[varZigzag,0]:
            
        plusBas = varZigzag
            
    elif dzAlphNb.iloc[varPrgrsv,0] > dzInvAlphNb.iloc[varZigzag,0]:
            
        plusHaut = varZigzag
        
    diffPhPb = plusHaut - plusBas
    if diffPhPb < 2:
            
        idN.append(dzAlphNb.iloc[varPrgrsv,0])
        natN.append(dzAlphNb.iloc[varPrgrsv,1])
        syno.append(dzAlphNb.iloc[varPrgrsv,2])
        natS.append('')
        val800.append(dzAlphNb.iloc[varPrgrsv,3] * 2)
        
        
        varPrgrsv += 1
        varZigzag = moitie
    
    varZigzag = plusBas + int((diffPhPb -(diffPhPb % 2))/2)
    print(varPrgrsv)
    print(varZigzag)
"""