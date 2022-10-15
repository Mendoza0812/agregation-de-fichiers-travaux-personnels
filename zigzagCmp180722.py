# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 23:25:17 2022

@author: Max-Louis

VERIFIER SI LES LISTES STOCKENT LES BONNES DONNEES
"""

import pandas as pd

dzlian = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzAlphNb.csv')
dzMergeSort = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzMergeSort.csv')
dzHeapSort = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzHeapSort.csv')
dzStable = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzStable.csv')
idN = []
natN = []
syno = []
natS = []
val800 = []

idNSnsDbl = []
natNSnsDbl = []
synoSnsDbl = []
natSSnsDbl = []
val800SnsDbl = []

nbLgnTtl = len(dzlian)

centre = int((nbLgnTtl - (nbLgnTtl % 2)) / 2)

stockTstDbl = []

pgsv = 0

stockZzTr = []
while pgsv < nbLgnTtl:
#for loop in range(8):
    print('pgsv = ' + str(pgsv))
    
    zzTranche = centre
    
    plusBas = 0
    
    plusHaut = nbLgnTtl
    
    dip0 = dzlian.iloc[pgsv, 0]
    #print('dip0 = dzlian.iloc[pgsv, 0]')
    print('dip0 = ' + str(dip0))
    
    dip2 = dzlian.iloc[pgsv, 2]
    #print('dip2 = dzlian.iloc[pgsv, 2]')
    print('dip2 = ' + str(dip2))
    
    nbBoucle = 0
    boucleInf = False 
    
    testSidjPasse = False
    stockTstDbl.sort()
    stockTtl = len(stockTstDbl)
    stockCtr = int((stockTtl - (stockTtl % 2)) / 2)
    stkPlusHaut = stockTtl
    stkPlusBas = 0
    zzStock = stockCtr
    
    while testSidjPasse == False:
        #print('testSidjPasse == False')
        
        stkEcartHB = stkPlusHaut - stkPlusBas
        zzStock = stkPlusBas + int((stkEcartHB - (stkEcartHB % 2)) / 2)
        
        if stockTtl < 1:
            
            testSidjPasse = True
            
        elif pgsv == stockTstDbl[zzStock]:
            #print('pgsv == stockTstDbl[zzStock]')
            
            pgsv += 1
            #print('pgsv = ' + str(pgsv))
            #print('stockTstDbl[zzStock] = ' + str(stockTstDbl[zzStock]))
            testSidjPasse = True
        
        elif stkEcartHB < 1:
            #print('stkEcartHB < 1')
            
            testSidjPasse = True
            
        elif pgsv < stockTstDbl[zzStock]:
            
            stkPlusHaut = zzStock
        
        elif pgsv > stockTstDbl[zzStock]:
            
            del stockTstDbl[zzStock]
        
        else:
            print('Issue boucle while testSiDjPasse non attendue')
            break
        
    finDRechdip2 = False
    
    while finDRechdip2 == False:
        #print('nbBoucle = ' + str(nbBoucle))
        #print('DEBUT BOUCLE WHILE dip2')
        
        ecartHB = plusHaut - plusBas
        #print('ecartHB = ' + str(ecartHB))
        
        zzTranche = plusBas + int((ecartHB - (ecartHB % 2)) / 2)
        #print('zzTranche = ' + str(zzTranche))
        
        testPrec = zzTranche
        
        diz0 = dzlian.iloc[zzTranche, 0]
        #print('diz0 = dzlian.iloc[zzTranche, 0]')
        #print('diz0 = ' + str(diz0))
        #print('dip2 = dzlian.iloc[pgsv, 2]')
        #print('dip2 = ' + str(dip2))
        
        
        diz2 = dzlian.iloc[zzTranche, 2]
        #print('diz2 = dzlian.iloc[zzTranche, 2]')
        #print('diz2 = ' + str(diz2))
        #print('dip0 = dzlian.iloc[pgsv, 0]')
        #print('dip0 = ' + str(dip0))
        
        if dip2 == diz0 :
            #print('dip2 == diz0')
            
            if dip0 == diz2 :
                #print('dip0 == diz2')
                
                idN.append(dip0)
                natN.append(dzlian.iloc[pgsv, 1])
                syno.append(diz2)
                natS.append(dzlian.iloc[zzTranche, 1])
                val800.append(dzlian.iloc[pgsv, 3] + dzlian.iloc[zzTranche, 3])
                
                stockTstDbl.append(zzTranche)
                
                #print('diz0 = ' + str(diz0))
                #print('dip2 = ' + str(dip2))
                #print('diz2 = ' + str(diz2))
                #print('dip0 = ' + str(dip0))
                
                finDRechdip2 = True
                #print('finDRechdip2 = True')
                
            else: 
                #print('dip0 != diz2')
                finDRechdip0 = False
                inf = False
                sup = False
                borneAtteinte = 0
                
                while finDRechdip0 == False:
                    
                    diz0 = dzlian.iloc[zzTranche, 0]
                    
                    diz2 = dzlian.iloc[zzTranche, 2]
                    
                    #print('DEBUT BOUCLE WHILE dip0')
                    #print('diz0 = dzlian.iloc[zzTranche, 0]')
                    #print('diz0 = ' + str(diz0))
                    #print('dip2 = dzlian.iloc[pgsv, 2]')
                    #print('dip2 = ' + str(dip2))
                    
                    #print('diz2 = dzlian.iloc[zzTranche, 2]')
                    #print('diz2 = ' + str(diz2))
                    #print('dip0 = dzlian.iloc[pgsv, 0]')
                    #print('dip0 = ' + str(dip0))
                    
                    if dip0 == diz2 :
                        #print('dip0 == diz2')
                        
                        idN.append(dip0)
                        natN.append(dzlian.iloc[pgsv, 1])
                        syno.append(diz2)
                        natS.append(dzlian.iloc[zzTranche, 1])
                        val800.append(dzlian.iloc[pgsv, 3] + dzlian.iloc[zzTranche, 3])
                        
                        stockTstDbl.append(zzTranche)
                        
                        #print('diz0 = ' + str(diz0))
                        #print('dip2 = ' + str(dip2))
                        #print('diz2 = ' + str(diz2))
                        #print('dip0 = ' + str(dip0))
                        
                        finDRechdip0 = True
                        #print('finDRechdip0 = True')
                        
                        finDRechdip2 = True
                        #print('finDRechdip2 = True')
                    
                    elif borneAtteinte == 2:
                        #print('borneAtteinte == 2')
                        
                        idNSnsDbl.append(dip0)
                        natNSnsDbl.append(dzlian.iloc[pgsv, 1])
                        synoSnsDbl.append(dzlian.iloc[pgsv, 2])
                        natSSnsDbl.append('')
                        val800SnsDbl.append(dzlian.iloc[pgsv,3] * 2)
                        
                        #print('diz0 = ' + str(diz0))
                        #print('dip2 = ' + str(dip2))
                        #print('diz2 = ' + str(diz2))
                        #print('dip0 = ' + str(dip0))
                        
                        finDRechdip0 = True
                        #print('finDRechdip0 = True')
                        
                        finDRechdip2 = True
                        #print('finDRechdip2 = True')
                        
                    elif dip2 < diz0:
                        #print('dip2 < diz0')
                        #print('plafond dip2 atteint, zzTranche +incremente')
                        
                        zzTranche -= 1
                        #print('zzTranche -= 1')
                        inf = True
                        sup = False
                        borneAtteinte += 1
                        
                    elif dip2 > diz0:
                        #print('dip2 > diz0')
                        #print('plancher dip2 atteint, zzTranche -decremente')
                        
                        zzTranche += 1
                        #print('zzTranche += 1')
                        inf = False
                        sup = True
                        borneAtteinte += 1
                        
                    elif inf == True:
                        #print('inf == True')
                        #print('plancher dip2 atteint 1 fois')
                        
                        zzTranche -= 1
                        #print('zzTranche -= 1')
                    
                    elif sup == True:
                        #print('sup == True')
                        #print('plafond dip2 atteint 1 fois')
                        
                        zzTranche += 1
                        #print('zzTranche += 1')
                    
                    else:
                        
                        zzTranche += 1
                        #print('zzTranche += 1')
                        
        elif int((ecartHB - (ecartHB % 2)) / 2) == 0:
            #print('ecartHB - (ecartHB % 2)) / 2) == 0')
            
            if zzTranche == 382550:
                #print('zzTranche == 382550')
                
                idNSnsDbl.append(dip0)
                natNSnsDbl.append(dzlian.iloc[pgsv, 1])
                synoSnsDbl.append(dzlian.iloc[pgsv, 2])
                natSSnsDbl.append('')
                val800SnsDbl.append(dzlian.iloc[pgsv,3] * 2)
                
                #print('diz0 = ' + str(diz0))
                #print('dip2 = ' + str(dip2))
                #print('diz2 = ' + str(diz2))
                #print('dip0 = ' + str(dip0))
                
                finDRechdip2 = True
                #print('finDRechrch = True') 
                
            else:
                dip2NbLtr = len(dip2)
                #print(dip2NbLtr)
                liCarSpec = dzlian[dzlian['IdNom'].str.contains(dip2)]
                #print(liCarSpec)
                
                indexCS = []
                
                synocs = []
                
                var = 0
                for loop in range (len(liCarSpec)):
                    if len(liCarSpec.iloc[var,0]) == dip2NbLtr:
                        indexCS.append(liCarSpec.iloc[var].name)
                        synocs.append(liCarSpec.iloc[var,2])
                        #print(liCarSpec.iloc[var])
                    var += 1
                var = 0
                indexName = []
                for loop in range(len(synocs)):
                    if synocs[var] == dip0:
                        indexName = indexCS[var]
                    var += 1
                
                if indexName.size == 0:
                    idNSnsDbl.append(dip0)
                    natNSnsDbl.append(dzlian.iloc[pgsv, 1])
                    synoSnsDbl.append(dzlian.iloc[pgsv, 2])
                    natSSnsDbl.append('')
                    val800SnsDbl.append(dzlian.iloc[pgsv,3] * 2)
                    
                    #print('diz0 = ' + str(diz0))
                    #print('dip2 = ' + str(dip2))
                    #print('diz2 = ' + str(diz2))
                    #print('dip0 = ' + str(dip0))
                    
                    finDRechdip2 = True
                    #print('finDRechrch = True') 
                elif dzlian.iloc[indexName, 2] == dip0:
                    #print('dzlian.iloc[indexName]')
                    #print(dzlian.iloc[indexName])
                    
                    idN.append(dip0)
                    natN.append(dzlian.iloc[pgsv, 1])
                    syno.append(dzlian.iloc[indexName, 0])
                    natS.append(dzlian.iloc[indexName, 1])
                    val800.append(dzlian.iloc[pgsv, 3] + dzlian.iloc[indexName, 3])
                    
                    stockTstDbl.append(indexName)
                    
                    #print('dip0 = ' + str(dip0))
                    #print('dzlian.iloc[pgsv, 1] = ' + str(dzlian.iloc[pgsv, 1]))
                    #print('dzlian.iloc[indexName, 0] = ' + str(dzlian.iloc[indexName, 0]))
                    #print('dzlian.iloc[indexName, 1] = ' + str(dzlian.iloc[indexName, 1]))
                    #print('dzlian.iloc[pgsv, 3] + dzlian.iloc[indexName, 3] = ' + str(dzlian.iloc[pgsv, 3] + dzlian.iloc[indexName, 3]))
                    
                    finDRechdip2 = True
                    #print('finDRechdip2 = True')
                else:
                    print('pas bon')
                break
        
        elif dip2 < diz0:
            #print('dip2 = \"' + str(dip2) + '\" < diz0 = \"'+ str(diz0)+ '\"')
            
            plusHaut = zzTranche
            #print('plusHaut = ' + str(plusHaut))
            
        elif dip2 > diz0:
            #print('dip2 = \"' + str(dip2) + '\" > diz0 = \"'+ str(diz0)+ '\"')
            
            plusBas = zzTranche
            #print('plusBas = ' + str(plusBas))
        
        else:
            print('are not == or !=')
            break
        
        #print('diz0 = ' + str(diz0))
        #print('dip2 = ' + str(dip2))
        #print('diz2 = ' + str(diz2))
        #print('dip0 = ' + str(dip0))
        nbBoucle += 1
        
    pgsv += 1
    print(pgsv)