# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 04:20:54 2022

@author: Max-Louis

il faudra tester sil n ya pas des recurrences au niveau des suites d index.
il ne devrait pas y avoir plus dune fois la mme valeur
"""

import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/distance18az.csv')
distNb = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/distanceNombre.csv')
pourEviterLesDoublons = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/refDeCmp1.csv')
incrDblns = 0

cmp1 = df[df['distance'] <= 201].sort_values('idN')

incr = 0
modorgn = df.iloc[incr,0]
nbDeStructures = 0
tailleDeLaStrctr = 0
maxStrctr = 0
continu = False

idxChemin = []
chemContinue = []

filtreNbSup = []
deLaStrctr = []

def chemineMot(bdd, incr):
    print(' --- DEBUT DE FONCTION ---')
    bclWhile1 = 0
    print('incr = ' + str(incr))
    
    lenBdd = len(bdd)

    pHt = lenBdd - 1
    pBs = incr

    ctr = int((lenBdd - (lenBdd % 2)) / 2)
        
    global milieu
    milieu = ctr
    milieuSuiv = milieu

    idxChemin.append(incr)
    
    incrSyn2 = bdd.iloc[incr,2]
    print('incrSyn2 = ' + str(incrSyn2))
    incrIN0 = bdd.iloc[incr,0]
    
    fonctionTermine = False
    
    global continu
    
    while fonctionTermine == False:
        print('fonctionTermine == False')
        bclWhile1 += 1
        
        difHB = pHt - pBs
        print('difHB = ' + str(difHB))
        
        milieu = pBs + int((difHB - (difHB % 2)) / 2)
        print('milieu = ' + str(milieu))
        
        milieuPrec = milieuSuiv
        print('milieu prec = ' + str(milieuPrec))
        
        milieuSuiv = milieu
        print('milieuSuiv = ' + str(milieuSuiv))
        
        mliIN0 = bdd.iloc[milieu,0]
        print('mliIN0 = ' + str(mliIN0))
        mliSy2 = bdd.iloc[milieu,2]
        
        if difHB <= 1 and milieuPrec == milieuSuiv :
            print('HB sans issue')
            
            continu = False
            fonctionTermine = True
            
            chemContinue.append(continu)
            
        
        elif incrSyn2 == mliIN0:
            print(' == ')
            
            incrI = incrIN0.lower()
            incrS = incrSyn2.lower()
            mliI = mliIN0.lower()
            mliS = mliSy2.lower()
            
            if incrS == mliI and incrI == mliS:
                print('lowercase == lowercase')
                
                continu = False
                fonctionTermine = True
                
                chemContinue.append(continu)
             
            else:
                print(' == confirme')
                
                prec = milieu
                suiv = milieu + 1
                
                if df.iloc[suiv,0] == mliIN0:
                    print('prec == suiv')
                    
                    while df.iloc[prec,0] == df.iloc[suiv,0]:
                        
                        prec = suiv
                        print('prec = ' + str(prec))
                        suiv += 1
                        print('suiv = ' + str(suiv))
                        
                    chemContinue.append(continu)
                    
                    fonctionTermine = True
                
                else:
                    
                    continu = True
                    chemContinue.append(continu)

                    fonctionTermine = True
                    
        elif incrSyn2 < mliIN0:
            print('<')
                
            pHt = milieu
            print('pHt = ('+ str(pHt)+ ') = milieu ('+ str(milieu) + ')' )
                
        elif incrSyn2 > mliIN0:
            print('>')
                
            pBs = milieu
            print('pBs = ('+ str(pBs)+ ') = milieu ('+ str(milieu) + ')')
            
        else: 
            print('issue innatendue')
        
        print('incr = ' + str(incr))
        print('nbBoucle While 1 = ' + str(bclWhile1))

    
while incr != (len(cmp1) - 1):
#for loop in range(60):
    
    tailleDeLaStrctr = 1
    
    if continu == False:
        
        chemineMot(cmp1, incr)
        incr += 1
        
    else:
        
        while continu == True:
            
            filtreNbSup.append(milieu)
            chemineMot(cmp1, milieu)
            tailleDeLaStrctr += 1
        
        incr += 1
    
    if tailleDeLaStrctr > maxStrctr:
        maxStrctr = tailleDeLaStrctr
        
    deLaStrctr.append(tailleDeLaStrctr)
    nbDeStructures += 1
    
    

plist = (idxChemin, chemContinue)
df2 = pd.DataFrame(plist).transpose()
df2.columns = ['idxChemin', 'chemContinue']