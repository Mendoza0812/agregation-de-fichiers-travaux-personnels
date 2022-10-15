# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:45:07 2022

@author: Max-Louis

TESTER LE PROGRAMME CAR IL SEMBLE ETRE TERMINE
"""
import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/ttLowerSnsAccent.csv')

df = df.sort_values('idN').reset_index(drop = True)

incr = 0


liDblOrNot = []
prems = []
atilUnDoublon = []

liTest = []

lgr = len(df)
mesure = 0
milieu = int((lgr - (lgr % 2))/2)
par100 = 0

for incr in range (lgr):
#for incr in range (20):
    
    trouve = False
    paDeDoublon = False
    dejaDansLaListe = False
    pasDansLaListe = False
    
    motidN = df.iloc[incr,0]
    motSyno2 = df.iloc[incr,2]
    #print(motidN)
    #print(motSyno2)
    
    sortedLiTest = liTest.sort()
    
    pB1 = 0
    
    pH1 = len(liTest)
    
    pH = lgr - 1
    pB = incr
    
    diffHB = pH - pB
    zzag = int(pB + ((diffHB - (diffHB % 2)) / 2))
    
    zzagidN = df.iloc[zzag, 0]
    #print(zzagidN)
    zzagSyno2 = df.iloc[zzag,2]
    #print(zzagSyno2)
    
    while pasDansLaListe == False and dejaDansLaListe == False:
        
        
        diffHB1 = pH1 - pB1
        zzag1 = int(pB1 + ((diffHB1 - (diffHB1 % 2)) / 2))
        
        if diffHB1 <= 2 or liTest == 0:
            
            pasDansLaListe = True
        
        elif incr == liTest[zzag1]:
            
            dejaDansLaListe = True
            prems.append(False)
            atilUnDoublon.append(True)
            liDblOrNot.append(liTest[zzag1])
            
        elif incr > liTest[pB1]:
            
            pB1 = zzag1
            
        elif incr < liTest[zzag1]:
            
            pH1 = zzag1
        
        else:
            
            print('issue innatendue 1')
            break
    
    if pasDansLaListe == True and dejaDansLaListe == False:
        
        while trouve == False and paDeDoublon == False:
            
            diffHB = pH - pB
            zzag = int(pB + ((diffHB - (diffHB % 2)) / 2))
            zzagidN = df.iloc[zzag, 0]
            
            if diffHB <= 1:
                
                liDblOrNot.append(incr)
                liTest.append(incr)
                prems.append(False)
                atilUnDoublon.append(False)
                paDeDoublon = True
                #print('paDeDoublon = True ')
                
            elif motSyno2 == zzagidN:
                
                #print('motSyno2 == zzagidN')
                #print('motSyno2 = ' + str(motSyno2))
                #print('zzagidN = ' + str(zzagidN))
                #print(zzagidN)
                
                trouve = True
                #print('trouve = True')
                trouve2 = False
                unMotSurDeux = False
                
                comparateurInf = zzag - 1
                curseurZzag = zzag
                comparateurSup = zzag + 1
                
                borne = 0
                
                while trouve2 == False and unMotSurDeux == False and borne < 2:
                
                    doublonPotentiel = df.iloc[curseurZzag,2]
                    doublonPotentielSup = df.iloc[comparateurSup,2]
                    doublonPotentielInf = df.iloc[comparateurInf,2]
                    
                    zzagidNPrec = df.iloc[comparateurInf,0]
                    zzagidN = df.iloc[curseurZzag,0]
                    zzagidNSuiv = df.iloc[comparateurSup,0]
                     
                    if motidN == doublonPotentiel:
                        #print('motidN == doublonPotentiel')
                        
                        liDblOrNot.append(curseurZzag)
                        liTest.append(curseurZzag)
                        prems.append(True)
                        atilUnDoublon.append(True)
                        trouve2 = True
                        #print(motidN)
                        #print(doublonPotentiel)
                        #print('trouve2 = True')
                        #print(curseurZzag)
                        
                        
                    elif borne == 1:
                        #print('borne == 1')
                        
                        if zzagidNPrec != zzagidN:
                            #print('zzagidNPrec != zzagidN')
                            
                            borne += 1
                            
                            if motidN == doublonPotentiel:
                        
                                liDblOrNot.append(curseurZzag)
                                liTest.append(curseurZzag)
                                prems.append(True)
                                atilUnDoublon.append(True)
                                trouve2 = True
                                #print(curseurZzag)
                                #print(motidN)
                                #print(doublonPotentiel)
                                
                            else:
                                
                                prems.append(False)
                                atilUnDoublon.append(False)
                                liDblOrNot.append(incr)
                                liTest.append(incr)
                                
                                #print('dejaDedans.append(False)')
                                #print('liDblOrNot.append(incr)')
                                #print('incr = ' + str(incr))
                                
                                unMotSurDeux = True
                                #print('unMotSurDeux = True')
                        else:
                            
                            curseurZzag = comparateurInf
                            comparateurInf -= 1
                            
                    
                    elif zzagidNSuiv != zzagidN:
                        #print('zzagidNSuiv != zzagidN')
                        
                        borne += 1
                        #print('borne += 1')
                        
                    else:
                        
                        curseurZzag = comparateurSup
                        comparateurSup += 1
                        comparateurInf += 1
                
            elif motSyno2 > zzagidN:
                
                pB = zzag
                #print('pB = ' + str(pB))
                
            elif motSyno2 < zzagidN:
                
                pH = zzag
                #print("pH = " + str(pB))
                
            else:
                
                print('issue innatendue 2')
                break
    
    
    par100 += 1
    if par100 == 100:
        par100 = 0
        print(incr)
     
plist = (liDblOrNot, prems, atilUnDoublon)
df2 = pd.DataFrame(plist).transpose()
df2.columns = ['liDblOrNot', 'prems','atilUnDoublon']

print(df2)
