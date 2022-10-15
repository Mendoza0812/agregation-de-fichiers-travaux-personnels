# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 18:23:53 2022

@author: Max-Louis
"""

import pandas as pd

dzlian = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzAlphNb.csv')

var = 0
prec = 0
suiv = 1

idN = []
idNS = []
idxNmeSup = []
idxNme = []
asc = False
ttlNbLgnSup = 0
encoreDesCarSpec = True
nbTour = 0
eskessaiFini = 0

while encoreDesCarSpec == True:
    
    var = 0
    prec = 0
    suiv = 1
    ttlNbLgnSup = 0
    
    if nbTour == 0:
        
        while var != 382550:
        #for loop in range(25):
            if dzlian.iloc[prec, 0] <= dzlian.iloc[suiv, 0]:
                print('<=')
                
                asc = False
                idxNme.append(dzlian.iloc[prec].name)
                print(' idxNme.append(dzlian.iloc[prec].name) = ')
                print(dzlian.iloc[prec].name)
                
                idN.append(dzlian.iloc[prec,0])
                
            else:
                print('>')
                
                #pour eviter out of range
                idxNme.append(dzlian.iloc[prec].name)
                print(' idxNme.append(dzlian.iloc[prec].name) = ')
                print(dzlian.iloc[prec].name)
                
                idN.append(dzlian.iloc[prec,0])
                
                asc = True
                nbLgnSup = 1
                precInv = prec
                suivInv = prec - 1
                
                if suivInv == -1:
                    print('suivInv == -1')
                    
                    idxNmeSup.append(dzlian.iloc[precInv].name)
                    idNS.append(dzlian.iloc[precInv,0])
                    
                elif dzlian.iloc[precInv, 0] == dzlian.iloc[suivInv, 0]:
                    print('precInv == suivInv')
                    
                    while dzlian.iloc[precInv, 0] == dzlian.iloc[suivInv, 0]:
                        
                        nbLgnSup += 1
                        
                        del idxNme[precInv - ttlNbLgnSup]
                        del idN[precInv - ttlNbLgnSup]
                        
                        precInv = suivInv
                        suivInv -= 1
                        
                        print('precInv = ' + str(precInv))
                        print('suivInv = ' + str(suivInv))
                    
                    del idxNme[precInv - ttlNbLgnSup]
                    del idN[precInv - ttlNbLgnSup]
                    
                    ttlNbLgnSup = ttlNbLgnSup + nbLgnSup
                    precRepass = precInv
                    suivRepass = precInv + 1
                    
                    print('precRepass = ' + str(precRepass))
                    print('suivRepass = ' + str(suivRepass))
                    print('nbLgnSup = ' + str(nbLgnSup))
                    
                    for loop in range(nbLgnSup):
                        
                        idxNmeSup.append(dzlian.iloc[precRepass].name)
                        idNS.append(dzlian.iloc[precRepass,0])
                        
                        precRepass = suivRepass
                        suivRepass += 1
                        print('precRepass = ' + str(precRepass))
                        print('suivRepass = ' + str(suivRepass))
                        
                elif dzlian.iloc[precInv, 0] != dzlian.iloc[suivInv, 0]:
                    print('precInv != suivInv')
                    print('1 seul carSpec entre deux sans')
                    
                    del idxNme[precInv - ttlNbLgnSup]
                    del idN[precInv - ttlNbLgnSup]
                    
                    ttlNbLgnSup = ttlNbLgnSup + nbLgnSup
                    
                    idxNmeSup.append(dzlian.iloc[precInv].name)
                    idNS.append(dzlian.iloc[precInv,0])
                        
            prec = suiv
            suiv += 1
            var += 1
            print('prec = ' + str(prec))
            print('suiv = ' + str(suiv))
            print('var = ' + str(var))
            
    
    else:
        
         while var != 382550:
         #for loop in range(25):
             
             if dzlian.iloc[prec, 0] > dzlian.iloc[suiv, 0]:    
                 print('>')
                 
                 asc = True
                 nbLgnSup = 1
                 precInv = prec
                 suivInv = prec - 1
                     
                 if dzlian.iloc[precInv, 0] == dzlian.iloc[suivInv, 0]:
                     print('precInv == suivInv')
                     
                     while dzlian.iloc[precInv, 0] == dzlian.iloc[suivInv, 0]:
                         
                         nbLgnSup += 1
                         
                         del idxNme[precInv - ttlNbLgnSup]
                         del idN[precInv - ttlNbLgnSup]
                         
                         precInv = suivInv
                         suivInv -= 1
                         
                         print('precInv = ' + str(precInv))
                         print('suivInv = ' + str(suivInv))
                     
                     del idxNme[precInv - ttlNbLgnSup]
                     del idN[precInv - ttlNbLgnSup]
                     
                     ttlNbLgnSup = ttlNbLgnSup + nbLgnSup
                     precRepass = precInv
                     suivRepass = precInv + 1
                     
                     print('precRepass = ' + str(precRepass))
                     print('suivRepass = ' + str(suivRepass))
                     print('nbLgnSup = ' + str(nbLgnSup))
                     
                     for loop in range(nbLgnSup):
                         
                         idxNmeSup.append(dzlian.iloc[precRepass].name)
                         idNS.append(dzlian.iloc[precRepass,0])
                         
                         precRepass = suivRepass
                         suivRepass += 1
                         print('precRepass = ' + str(precRepass))
                         print('suivRepass = ' + str(suivRepass))
                         
                 elif dzlian.iloc[precInv, 0] != dzlian.iloc[suivInv, 0]:
                    print('precInv != suivInv')
                    print('1 seul carSpec entre deux sans')
                    
                    del idxNme[precInv - ttlNbLgnSup]
                    del idN[precInv - ttlNbLgnSup]
                    
                    ttlNbLgnSup = ttlNbLgnSup + nbLgnSup
                    
                    idxNmeSup.append(dzlian.iloc[precInv].name)
                    idNS.append(dzlian.iloc[precInv,0])
             else:
                 eskessaiFini += 1
                 if eskessaiFini == len(dzlian):
                     encoreDesCarSpec = True
                         
             prec = suiv
             suiv += 1
             var += 1
             #print('prec = ' + str(prec))
             #print('suiv = ' + str(suiv))
             print('var = ' + str(var))
    nbTour += 1 
    
plist = (idN, idxNme)
df = pd.DataFrame(plist).transpose()
df.columns = ['idN','idxNme']
df.to_csv('retriCrctrZz2.csv', index = False)

plist1 = (idNS, idxNmeSup)
df1 = pd.DataFrame(plist1).transpose()
df1.columns = ['idNS','idxNmeSup']
df1.to_csv('retriCrctrZzCarSpec2.csv', index = False)
            
    