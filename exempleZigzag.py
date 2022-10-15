# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 03:29:43 2022

@author: Max-Louis
"""

import pandas as pd

dzAlphNb = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzZigzag.csv')

numLgn = []
    
varPrgrsv = 0

def moduloMoitie(valeur):
    
    global moitie
    moitie = int((valeur - (valeur % 2)) / 2)
    
# la longueur de la liste chez IN et SYN sont la meme car la bdd est la mm    
totalIN = len(dzAlphNb)

moduloMoitie(totalIN)
print(moitie)

varZigzag = moitie

plusBas = 0
plusHaut = totalIN


while varPrgrsv < totalIN:
        
    if dzAlphNb.iloc[varPrgrsv,0] == dzAlphNb.iloc[varZigzag,2]:
            
        if dzAlphNb.iloc[varPrgrsv,2] == dzAlphNb.iloc[varZigzag,0]:
            
            numLgn.append(varPrgrsv)
            varPrgrsv += 1
            varZigzag = moitie
                
            
        elif dzAlphNb.iloc[varPrgrsv,2] < dzAlphNb.iloc[varZigzag,0]:
                
            plusBas = varZigzag
            
        elif dzAlphNb.iloc[varPrgrsv,2] > dzAlphNb.iloc[varZigzag,0]:
                
            plusHaut = varZigzag
                
        diffPhPb = plusHaut - plusBas
        if diffPhPb < 2:
                
            varPrgrsv += 1
            varZigzag = moitie
                
    elif dzAlphNb.iloc[varPrgrsv,0] < dzAlphNb.iloc[varZigzag,2]:
            
        plusBas = varZigzag
            
    elif dzAlphNb.iloc[varPrgrsv,0] > dzAlphNb.iloc[varZigzag,2]:
            
        plusHaut = varZigzag
        
    diffPhPb = plusHaut - plusBas
    if diffPhPb < 2:
            
        varPrgrsv += 1
        varZigzag = moitie
    
    varZigzag = plusBas + int((diffPhPb -(diffPhPb % 2))/2)
    print(varPrgrsv)
    print(varZigzag)