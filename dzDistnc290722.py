# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 17:09:59 2022

@author: Max-Louis
"""
import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/distance18az.csv')
distNb = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/distanceNombre.csv')

cmp1 = df[df['distance'] <= 201].sort_values('idN').reset_index(drop = True)

def synoDeSyno(df):
    
    lendf = len(df)

    incr = 0

    pHt = lendf - 1
    pBs = incr

    ctr = int((lendf - (lendf % 2)) / 2)
           
    milieu = ctr
    milieuSuiv = milieu

    voisins = []
    idxVoisns = []
    mtVoisns = []
    idxOrgn = []
    mtOrgn = []

    while incr != (lendf - 1):
    #for loop in range (100):
        
        difHB = pHt - pBs
        #print('difHB = ' + str(difHB))
        milieu = pBs + int((difHB - (difHB % 2)) / 2)
        
        milieuPrec = milieuSuiv
        milieuSuiv = milieu
        
        incrSyn2 = df.iloc[incr,2]
        incrIN0 = df.iloc[incr,0]
        mliIN0 = df.iloc[milieu,0]
        mliSy2 = df.iloc[milieu,2]
        
        if difHB <= 1 and milieuPrec == milieuSuiv :
            #print('difHB <= 1 and zgPrec == zgSuiv')
            
            incr += 1
            pHt = lendf - 1
            pBs = incr
            
        elif incrSyn2 == mliIN0:
            #print('2==0')
            
            incrI = incrIN0.lower()
            incrS = incrSyn2.lower()
            mliI = mliIN0.lower()
            mliS = mliSy2.lower()
            
            if incrS == mliI and incrI == mliS:
                
                incr += 1
                pHt = lendf - 1
                pBs = incr
            
            else:
                
                voisins.append(mliIN0)
                idxVoisns.append(milieu)
                mtVoisns.append(df.iloc[milieu,2])
                mtOrgn.append(df.iloc[incr,0])
                idxOrgn.append(incr)
                
                prec = milieu
                suiv = milieu + 1
                
                precInv = milieu
                suivInv = milieu - 1
                
                if df.iloc[suiv,0] == mliIN0:
                    #print('prec == suiv')
                    
                    while df.iloc[prec,0] == df.iloc[suiv,0]:
                    
                        voisins.append(df.iloc[prec,0])
                        idxVoisns.append(prec)
                        mtVoisns.append(df.iloc[prec,2])
                        idxOrgn.append(incr)
                        mtOrgn.append(mliIN0)
                        
                        prec = suiv
                        suiv += 1
                        
                    voisins.append(df.iloc[prec,0])
                    idxVoisns.append(prec)
                    mtVoisns.append(df.iloc[prec,2])
                    idxOrgn.append(incr)
                    mtOrgn.append(df.iloc[incr,0])
                
                if df.iloc[suivInv,0] == mliIN0:
                    #print('precInv == suivInv')
                    
                    while df.iloc[precInv,0] == df.iloc[suivInv,0]:
                    
                        voisins.append(df.iloc[precInv,0])
                        idxVoisns.append(precInv)
                        mtVoisns.append(df.iloc[precInv,2])
                        idxOrgn.append(incr)
                        mtOrgn.append(mliIN0)
                        
                        precInv = suivInv
                        suivInv += 1
                        
                    voisins.append(df.iloc[precInv,0])
                    idxVoisns.append(precInv)
                    mtVoisns.append(df.iloc[precInv,2])
                    idxOrgn.append(incr)
                    mtOrgn.append(mliIN0)
                        
                incr += 1
                pHt = lendf - 1
                pBs = 0
                
        elif incrSyn2 < mliIN0:
            #print('<')
                
            pHt = milieu
                
        elif incrSyn2 > mliIN0:
            #print('>')
                
            pBs = milieu
            #print(zzag)
            
        else: 
            print('issue innatendue')
        
        print(incr)
        
    plist = (voisins, mtVoisns, idxVoisns, mtOrgn, idxOrgn)
    global df2
    df2 = pd.DataFrame(plist).transpose()
    df2.columns = ['voisins', 'mtVoisns', 'idxVoisns', 'mtOrgn', 'idxOrgn']
    df3 = df2.sort_values('voisins').reset_index(drop = True)
    
synoDeSyno(cmp1)