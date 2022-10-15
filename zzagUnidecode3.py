# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 19:12:56 2022

@author: Max-Louis

stocklgn ne supprime par les valeurs inférieures à var, a verifier
"""

import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/zzUnidecode3.csv')

lgr = len(df)
pHaut = lgr
pBas = 0
ctr = int((lgr - (lgr % 2)) / 2 )
zzag = ctr
var = 0

idNS = []
natNS = []
synoS = []
natSS = []
val800 = []

testStkLgn = False

stockLgn = []

zzagSuiv = 0
zzagPrec = zzagSuiv

while var != lgr:
#for loop in range(3500):
    
    nbLiStkLgn = len(stockLgn)
    
    
    if nbLiStkLgn > 0:
        #print('nbLiStkLgn > 0')
        
        stockLgn.sort()
        
        nbBoucle= 0
        
        pBStk = 0
        pHStk = nbLiStkLgn
        
        suivStk = 0
        precStk = suivStk
        precPrecStk = precStk
        
        while testStkLgn == False:
        #for loop in range (10):
            #print('testStkLgn == False')
            
            #print('pHStk = ' + str(pHStk))
            #print('pBStk = ' + str(pBStk))
            
            diffHBStk = pHStk - pBStk
            
            #print('diffHBStk = ' + str(diffHBStk))
            if nbBoucle == 0:
                #print('nbBoucle == 0')
                
                varStkLgn = 0
            
            else:
                #print('nbBoucle > 0')
                
                varStkLgn = pBStk + int((diffHBStk - (diffHBStk % 2)) / 2)
                #print('varStkLgn = ' + str(varStkLgn))
                
                precStk = suivStk
                
                if nbBoucle > 1:
                    #print('nbBoucle > 1')
                    
                    precPrecStk = precStk
                    
                    if precStk == suivStk and precPrecStk == precStk:
                        #print('precStk == suivStk == precPrecStk')
                        
                        testStkLgn = True
                        break
                    
            suivStk = varStkLgn
            
            if var == stockLgn[varStkLgn]:
                #print('var == stockLgn[varStkLgn]')
                
                del stockLgn[varStkLgn]
                
                var += 1
                pBas = var
                
                testStkLgn = True
            
            elif var > stockLgn[varStkLgn]:
                #print('var > stockLgn[varStkLgn]')
                
                while var > stockLgn[varStkLgn]:
                    #print('loop while de var et stklgn')
                    
                    del stockLgn[varStkLgn]
                
                    pBStk = varStkLgn
                
            elif var < stockLgn[varStkLgn]:
                #print('var < stockLgn[varStkLgn]')
                #print('var = ' + str(var))
                #print('varStkLgn = ' + str(varStkLgn))
                #print('stockLgn = ' + str(stockLgn))
                #print('stockLgn[varStkLgn] = ' + str(stockLgn[varStkLgn]))
                
                pHStk = varStkLgn
                #print('pHStk = varStkLgn')
                #print('varStkLgn = ' + str(varStkLgn))
                #print('pHStk = ' + str(pHStk))
                
            nbBoucle += 1
                    
    diffHB = pHaut - pBas
    #print('diffHB = ' + str(diffHB))
    
    zzag = pBas + int((diffHB - (diffHB % 2)) / 2)
    #print('zzag = ' + str(zzag))
    
    if nbBoucle == 0:
        zzagSuiv = zzag
    
    else:
        zzagPrec = zzagSuiv
        zzagSuiv = zzag
        
        if zzagSuiv == zzagPrec and diffHB <= 1:
            #print('diffHB == 0')
            
            idNS.append(df.iloc[var,0])
            natNS.append(df.iloc[var,1])
            synoS.append(df.iloc[var,2])
            natSS.append('')
            val800.append((df.iloc[var,3] * 2))
            
            testStkLgn = False
            
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
                #print('borneAtteinte == 2')
                
                idNS.append(df.iloc[var,0])
                natNS.append(df.iloc[var,1])
                synoS.append(df.iloc[var,2])
                natSS.append('')
                val800.append((df.iloc[var,3] * 2))
                
                couche2 = True
                
                testStkLgn = False
                
                var += 1
                pHaut = lgr
                pBas = var
            
            elif df.iloc[var,0] == df.iloc[prec,2]:
                #print('df.iloc[var,0] == df.iloc[prec,2]')
                
                idNS.append(df.iloc[var,0])
                natNS.append(df.iloc[var,1])
                synoS.append(df.iloc[prec,0])
                natSS.append(df.iloc[prec,1])
                val800.append(df.iloc[var,3] + df.iloc[prec,3])
                
                stockLgn.append(prec)
                
                couche2 = True
                
                testStkLgn = False
                
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
    
    print(var)
    
    
    
    
    