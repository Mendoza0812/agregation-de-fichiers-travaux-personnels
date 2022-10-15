# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:46:18 2022

@author: Max-Louis
"""
import pandas as pd

df1 = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/leFichierSansDoublon.csv')

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/mega800.csv')

lgrMg800 = len(df)

var = 0

pHt = lgrMg800 - 1
pBs = 0

ctr = int((lgrMg800 - (lgrMg800 % 2)) / 2)
       
zzag = ctr
zzagSuiv = zzag

voisins = []
idxVoisns = []
idxOrgn = []

while var != (lgrMg800 - 1):
#for loop in range (100):
    
    difHB = pHt - pBs
    print('difHB = ' + str(difHB))
    zzag = pBs + int((difHB - (difHB % 2)) / 2)
    
    zzagPrec = zzagSuiv
    zzagSuiv = zzag
    
    varSy2 = df.iloc[var,2]
    
    zgIN0 = df.iloc[zzag,0]
    
    if difHB <= 1 and zzagPrec == zzagSuiv :
        print('difHB <= 1 and zgPrec == zgSuiv')
        
        var += 1
        pHt = lgrMg800 - 1
        pBs = 0
        
    elif varSy2 == zgIN0:
        print('2==0')
        
        voisins.append(zgIN0)
        idxVoisns.append(zzag)
        idxOrgn.append(var)
        
        prec = zzag
        suiv = zzag + 1
        
        precInv = zzag
        suivInv = zzag - 1
        
        if df.iloc[suiv,0] == zgIN0:
            print('prec == suiv')
            
            while df.iloc[prec,0] == df.iloc[suiv,0]:
            
                voisins.append(df.iloc[prec,0])
                idxVoisns.append(prec)
                idxOrgn.append(var)
                
                prec = suiv
                suiv += 1
                
            voisins.append(df.iloc[prec,0])
            idxVoisns.append(prec)
            idxOrgn.append(var)
        
        if df.iloc[suivInv,0] == zgIN0:
            print('precInv == suivInv')
            
            while df.iloc[precInv,0] == df.iloc[suivInv,0]:
            
                voisins.append(df.iloc[precInv,0])
                idxVoisns.append(precInv)
                idxOrgn.append(var)
                
                precInv = suivInv
                suivInv += 1
                
            voisins.append(df.iloc[precInv,0])
            idxVoisns.append(precInv)
            idxOrgn.append(var)
                
        var += 1
        pHt = lgrMg800 - 1
        pBs = 0
        
    elif varSy2 < zgIN0:
        print('<')
        
        pHt = zzag
        
    elif varSy2 > zgIN0:
        print('>')
        
        pBs = zzag
        print(zzag)
    
    else: 
        print('issue innatendue')
    
    print(var)
    
plist = (voisins, idxVoisns, idxOrgn)
df2 = pd.DataFrame(plist).transpose()
df2.columns = ['voisins', 'idxVoisns', 'idxOrgn']
        