# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 18:10:21 2022

@author: Max-Louis
"""

import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/dzDistance.csv')
distNb = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/distanceNombre.csv')

cmp1 = df[df['distance'] <= 201].sort_values('idN').reset_index(drop = True)

def synoDeSyno(df):
    
    lgrMg800 = len(df)

    var = 0

    pHt = lgrMg800 - 1
    pBs = 0

    ctr = int((lgrMg800 - (lgrMg800 % 2)) / 2)
           
    zzag = ctr
    zzagSuiv = zzag

    voisins = []
    idxVoisns = []
    mtVoisns = []
    idxOrgn = []
    mtOrgn = []

    while var != (lgrMg800 - 1):
    #for loop in range (100):
        
        difHB = pHt - pBs
        #print('difHB = ' + str(difHB))
        zzag = pBs + int((difHB - (difHB % 2)) / 2)
        
        zzagPrec = zzagSuiv
        zzagSuiv = zzag
        
        varSy2 = df.iloc[var,2]
        varIN0 = df.iloc[var,0]
        zgIN0 = df.iloc[zzag,0]
        zgSy2 = df.iloc[zzag,2]
        
        if difHB <= 1 and zzagPrec == zzagSuiv :
            #print('difHB <= 1 and zgPrec == zgSuiv')
            
            var += 1
            pHt = lgrMg800 - 1
            pBs = 0
            
        elif varSy2 == zgIN0:
            #print('2==0')
            
            varI = varIN0.lower()
            varS = varSy2.lower()
            zgI = zgIN0.lower()
            zgS = zgSy2.lower()
            
            if varS == zgI and varI == zgS:
                
                var += 1
                pHt = lgrMg800 - 1
                pBs = 0
            
            else:
                
                voisins.append(zgIN0)
                idxVoisns.append(zzag)
                mtVoisns.append(df.iloc[zzag,2])
                mtOrgn.append(df.iloc[var,0])
                idxOrgn.append(var)
                
                prec = zzag
                suiv = zzag + 1
                
                precInv = zzag
                suivInv = zzag - 1
                
                if df.iloc[suiv,0] == zgIN0:
                    #print('prec == suiv')
                    
                    while df.iloc[prec,0] == df.iloc[suiv,0]:
                    
                        voisins.append(df.iloc[prec,0])
                        idxVoisns.append(prec)
                        mtVoisns.append(df.iloc[prec,2])
                        idxOrgn.append(var)
                        mtOrgn.append(zgIN0)
                        
                        prec = suiv
                        suiv += 1
                        
                    voisins.append(df.iloc[prec,0])
                    idxVoisns.append(prec)
                    mtVoisns.append(df.iloc[prec,2])
                    idxOrgn.append(var)
                    mtOrgn.append(df.iloc[var,0])
                
                if df.iloc[suivInv,0] == zgIN0:
                    #print('precInv == suivInv')
                    
                    while df.iloc[precInv,0] == df.iloc[suivInv,0]:
                    
                        voisins.append(df.iloc[precInv,0])
                        idxVoisns.append(precInv)
                        mtVoisns.append(df.iloc[precInv,2])
                        idxOrgn.append(var)
                        mtOrgn.append(zgIN0)
                        
                        precInv = suivInv
                        suivInv += 1
                        
                    voisins.append(df.iloc[precInv,0])
                    idxVoisns.append(precInv)
                    mtVoisns.append(df.iloc[precInv,2])
                    idxOrgn.append(var)
                    mtOrgn.append(zgIN0)
                        
                var += 1
                pHt = lgrMg800 - 1
                pBs = 0
                
        elif varSy2 < zgIN0:
            #print('<')
                
            pHt = zzag
                
        elif varSy2 > zgIN0:
            #print('>')
                
            pBs = zzag
            #print(zzag)
            
        else: 
            print('issue innatendue')
        
        print(var)
        
    plist = (voisins, mtVoisns, idxVoisns, mtOrgn, idxOrgn)
    global df2
    df2 = pd.DataFrame(plist).transpose()
    df2.columns = ['voisins', 'mtVoisns', 'idxVoisns', 'mtOrgn', 'idxOrgn']

synoDeSyno(cmp1)