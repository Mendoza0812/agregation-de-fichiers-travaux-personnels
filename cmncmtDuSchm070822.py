# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:14:54 2022

@author: Max-Louis

probleme = synonymes du mot dieu sont jaugees au maximum alors que
ce nest pas le cas, erreur trouve dans le deaazCSV mais pas dans le
 touslesD
"""
import pandas as pd

dfL = pd.read_csv(r'C:/Users/Max-Louis/distance18azLower.csv')
distNb = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/distanceNombre.csv')
refaz18 = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/refaz18.csv')

incr = 0
idStrDist = 0

idStructure1 = 0
idStructure2 = 0
dnsTop4 = True
dnsTop6 = True


top4s = []
top6s = []
idStructures = []
sizeIdStrctrs = []
mot = []
joinStrctr = []



#for loop in range (len(distNb)):
for loop in range (1):
    
    grpParDist = dfL[dfL['distance'] == distNb.iloc[incr,0]]
    print (grpParDist)
    lgrDuGrp = len(grpParDist)
    print(lgrDuGrp)
    clssmtStrctr = refaz18[refaz18['numero'] <= lgrDuGrp].reset_index(drop = True)
    print(clssmtStrctr)
    
    prec = 0
    suiv = 1
    
    incrStrctr = 0
    idStructure = 0
    sizeIdStrctr = 1
    
    while len(idStructures) < (len(clssmtStrctr)-1) :
        
        idStructures.append(idStructure)
        sizeIdStrctrs.append(sizeIdStrctr)
        mot.append(clssmtStrctr.iloc[incr,0])
        top4s.append(dnsTop4)
        top6s.append(dnsTop6)
        
        if clssmtStrctr.iloc[prec,0] != clssmtStrctr.iloc[suiv,0]:
            
            idStructure += 1
            sizeIdStrctr = 1
            
            if suiv == (len(clssmtStrctr)-1):
                
                if clssmtStrctr.iloc[prec,0] != clssmtStrctr.iloc[suiv,0]:
                    
                    idStructure += 1
                    sizeIdStrctr = 1
                
                else:
                    
                    sizeIdStrctr += 1
                    
                if sizeIdStrctr <= 4:
                    
                    dnsTop4 = True
                    dnsTop6 = True
                    
                else:
                    
                    dnsTop4 = False
                    
                    if sizeIdStrctr <= 6:
                    
                        dnsTop6 = True
                
                    else:
                    
                        dnsTop6 = False
                
                idStructures.append(idStructure)
                sizeIdStrctrs.append(sizeIdStrctr)
                top4s.append(dnsTop4)
                top6s.append(dnsTop6)
        
        else:
            joinStrctr.append(clssmtStrctr.iloc[incr,1])
            sizeIdStrctr += 1
        
        if sizeIdStrctr <= 4:
            
            dnsTop4 = True
            dnsTop6 = True
            
        else:
            
            dnsTop4 = False
            
            if sizeIdStrctr <= 6:
            
                dnsTop6 = True
        
            else:
            
                dnsTop6 = False
            
        prec = suiv
        suiv += 1
        
    clssmtStrctr['idStructures'] = idStructures
    clssmtStrctr['sizeIdStrctrs'] = sizeIdStrctrs
    clssmtStrctr['top4s'] = top4s
    clssmtStrctr['top6s'] = top6s
    
    """
    il faut retrouver les lignes dans lesquelles on est deja passe
    """
    
    incr += 1
    idStrDist += 1