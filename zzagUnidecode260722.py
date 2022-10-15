# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 18:02:20 2022

@author: Max-Louis
"""

import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/zzUnidecode3.csv')
df1 = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/correspUnidecode.csv')

lgr = len(df)
pHaut = lgr
pBas = 0
ctr = int((lgr - (lgr % 2)) / 2 )
zzag = ctr
var = 0
nbBoucle = 0

stockLgn = []
emplOrgn = []

while var != lgr:
#for loop in range(300):
    
    diffHB = pHaut - pBas
    #print('diffHB = ' + str(diffHB))
    
    #print('pHaut = ' + str(pHaut))
    #print('pBas = ' + str(pBas))
    
    zzag = pBas + int((diffHB - (diffHB % 2)) / 2)
    #print('zzag = ' + str(zzag))
    
    if nbBoucle == 0:
        #print('nbBoucle == 0')
        zzagSuiv = zzag
    
    else:
        #print('nbBoucle > 0')
        
        zzagPrec = zzagSuiv
        zzagSuiv = zzag
        
        if zzagSuiv == zzagPrec and diffHB <= 1:
            
            #print('zzagSuiv == zzagPrec and diffHB == 1')
            emplOrgn.append(var)
            stockLgn.append('')
            var += 1
            
            
            pHaut = lgr
            pBas = var
    
    if df.iloc[var,2] == df.iloc[zzag,0]:
        #print('df.iloc[var,2] == df.iloc[zzag,0]')
        
        couche2 = False
        
        borneAtteinte = 0
        creneau = zzag
        prec = creneau
        suiv = creneau + 1
        
        while couche2 == False:
            
            precInv = prec
            suivInv = prec - 1
            
            if borneAtteinte == 2:
                
                emplOrgn.append(var)
                stockLgn.append('')
                
                var += 1
                
                couche2 = True
                pHaut = lgr
                pBas = var
                
            elif df.iloc[var,0] == df.iloc[prec,2]:
                
                emplOrgn.append(var)
                stockLgn.append(prec)
                
                couche2 = True
                
                var += 1
                pHaut = lgr
                pBas = var
            
            elif df.iloc[var,0] != df.iloc[prec,2]:
                
                #print('df.iloc[var,0] != df.iloc[prec,2]')
                
                if borneAtteinte == 1:
                    
                    if df.iloc[precInv,0] != df.iloc[suivInv,0]:
                        
                        borneAtteinte += 1
                    
                    else:
                        
                        prec = suivInv
                        suivInv -= 1
                        
                else:
                    
                    if df.iloc[prec,0] != df.iloc[suiv,0]:
                        
                        borneAtteinte += 1
                    
                    else:
                        prec = suiv
                        suiv += 1
                    
            else:
                print('issue innatendue2')
                break
            
    elif df.iloc[var,2] < df.iloc[zzag,0]:
        #print('<')
        
        pHaut = zzag
        #print('pHaut = ' + str(pHaut))
        
    elif df.iloc[var,2] > df.iloc[zzag,0]:
        #print('>')
        
        pBas = zzag
        #print('pBas = ' + str(pBas))
    
    else:
        print('issue innatendue')
        break
    nbBoucle += 1
    print(var)