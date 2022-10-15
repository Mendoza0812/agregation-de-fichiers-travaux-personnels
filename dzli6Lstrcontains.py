# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 18:34:22 2022

@author: Max-Louis

employer les 2 techniques, celles du zigzag combiné avec celle de 
compartimenter
"""

import pandas as pd

dzli = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/projet_concept/bdd_az/deaazCSV.csv')
dzliInv = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/deaazzInv.csv')

dzlian = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzAlphNb.csv')
dzliinvan = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzInvAlphNb.csv')

del dzli['placeSyno']
var = 0
totalLgn = len(dzlian)
plusHaut = totalLgn
centre = int((totalLgn - (totalLgn % 2)) / 2)
plusBas = 0
motRecherche = dzlian.iloc[var, 0]
traqueur = centre
motCandidat = dzliinvan.iloc[traqueur, 2]

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

idNLs = []
natNLs = []
synoLs = []
natSLs = []
val800Ls = []

varCompSYN = 0
varCompIN = 0

nbBcle = 0

for loop in range(28):
    var = 0
    totalLgn = len(dzlian)
    compartimentSYN = dzliinvan[dzliinvan['AlphNb'] == varCompSYN]
    compartimentIN = dzlian[dzlian['AlphNb'] == varCompIN]
    
    if len(compartimentIN) == 0:
        print('if len(compartimentIN) == 0:')
        
        idNSnsDbl.append(compartimentSYN.iloc[var,0])
        natNSnsDbl.append(compartimentSYN.iloc[var,1])
        synoSnsDbl.append(compartimentSYN.iloc[var,2])
        natSSnsDbl.append('')
        val800SnsDbl.append(compartimentSYN.iloc[var,3] * 2)
        varCompIN += 1
        print('varSYN if = ' + str(var))
        varCompSYN += 1
    
    while var < len(compartimentIN):
    
        plusHaut = totalLgn
        plusBas = 0
        traqueur = centre
        var += 1
        #print('var += 1 soit var = ' + str(var))
        motRecherche = compartimentIN.iloc[var, 0]
        #print('Nouveau motRecherche = ' + str(motRecherche))
        
        traqueur = centre
        motCandidat = compartimentIN.iloc[traqueur, 2]
        print(str(var))
        
        motTrouve = False
        
        varSYN = 0
        varIN = 0
        
        
        while motTrouve == False:
            
            diffHautBas = plusHaut - plusBas
            #print('diffHautBas = ' + str(diffHautBas))
            
            traqueur = plusBas + int((diffHautBas - (diffHautBas % 2)) / 2)
            #print('traqueur = ' + str(traqueur))
            
            motCandidat = dzliInv.iloc[traqueur, 2]
            #print('motCandidat = ' + str(motCandidat))
            
            
            
            if diffHautBas < 2:
                #print('DIFF HAUT BAS < 2')
                    
                idNSnsDbl.append(motRecherche)
                natNSnsDbl.append(compartimentIN.iloc[var, 1])
                synoSnsDbl.append(compartimentIN.iloc[var, 2])
                natSSnsDbl.append('')
                val800SnsDbl.append(compartimentIN.iloc[var,3] * 2)
                
                motTrouve = True
                #print('motTrouve = True')
            
            elif motRecherche == motCandidat:
                #print(' motRecherche = "' + str(motRecherche) +'" == motCandidat "' + str(motCandidat) + ' " ')
                
                traqueur2 = centre
                
                plusBas2 = 0
                plusHaut2 = len(compartimentIN)
                
                motTrouve2 = False
                while motTrouve2 == False:
                    
                    motRecherche2 = compartimentIN.iloc[var, 2]
                    
                    
                    diffHautBas2 = plusHaut2 - plusBas2
                    #print('diffHautBas2 = ' + str(diffHautBas2))
                    
                    traqueur2 = plusBas2 + int((diffHautBas2 - (diffHautBas2 % 2)) / 2)
                    #print('traqueur2 = ' + str(traqueur2))
                    
                    motCandidat2 = compartimentSYN.iloc[traqueur2, 2]
                    #print('motCandidat2 = ' + str(motCandidat2))
                    
                    if diffHautBas2 < 2:
                        #print('DIFF HAUT BAS < 2')
                            
                        idNSnsDbl.append(compartimentIN.iloc[var, 0])
                        natNSnsDbl.append(compartimentIN.iloc[var, 1])
                        synoSnsDbl.append(compartimentIN.iloc[var, 2])
                        natSSnsDbl.append('')
                        val800SnsDbl.append(compartimentIN.iloc[var,3] * 2)
                        
                        motTrouve2 = True
                        #print('motTrouve = True')
                        
                    elif motRecherche2 == motCandidat2:
                        #print('motRecherche 2 == motCandidat2')
                        
                        idN.append(compartimentIN.iloc[var, 0])
                        natN.append(compartimentIN.iloc[var, 1])
                        syno.append(compartimentSYN.iloc[])
                        natS.append(dzliInv.iloc[centre, 1])
                        val800.append(dzli.iloc[var, 3] + dzliInv.iloc[centre, 3])
                        
                        motTrouve2 = True
                        #print('motTrouve2 = True')
                    
                    elif motRecherche2 > motCandidat2:
                        #print('motRecherche2 > motCandidat2')
                        #print(motCandidat2)
                        
                        plusBas2 = traqueur2
                        
                        #print('traqueur2 = '+ str(traqueur2))
                        
                    elif motRecherche2 < motCandidat2:
                        #print('motRecherche2 < motCandidat2')
                        #print(motCandidat2)
                        
                        plusHaut2 = traqueur2
                        
                        #print('traqueur2 = '+ str(traqueur2))
                    nbBcle += 1
                    #print('nbBoucle = ' +str(nbBcle))
                        
                motTrouve = True
                #print('motTrouve = True')
                
            elif motRecherche > motCandidat:
                #print('motRecherche > motCandidat')
                #print(motCandidat)
                
                plusBas = traqueur
                
                #print(traqueur)
    
                
            elif motRecherche < motCandidat:
                #print('motRecherche < motCandidat')
                #print(motCandidat)
                
                plusHaut = traqueur
                
                #print(traqueur)
    varCompIN += 1
    varCompSYN += 1
    nbBcle += 1
    #print('nbBoucle = ' +str(nbBcle))
        
    
       
"""   
var = 0
totalLgn = len(dzli)
plusHaut = totalLgn
centre = int((totalLgn - (totalLgn % 2)) / 2)
plusBas = 0
motRecherche = dzli.iloc[var, 2]
traqueur = centre
motCandidat = dzliInv.iloc[traqueur, 0]

nbBcle = 0
      
while var < len(dzli):  
    while motRecherche != motCandidat:
        
        diffHautBas = plusHaut - plusBas
        
        traqueur = plusBas + int((diffHautBas - (diffHautBas % 2)) / 2)
        
        motCandidat = dzliInv.iloc[traqueur, 0]
        
        if diffHautBas < 2:
                
            idNLs.append(motRecherche)
            natNLs.append(dzli.iloc[var, 1])
            synoLs.append(dzli.iloc[var, 2])
            natSLs.append('')
            val800Ls.append(dzli.iloc[var,3] * 2)
            
            var += 1
            traqueur = centre
        
        elif motRecherche == motCandidat:
            print(' motRecherche = "' + str(motRecherche) +'" == motCandidat "' + str(motCandidat) + ' " ')
            
            print('ceci est pas normal car cela signifie que des doublons n ont pas ete filtre')
            
            var += 1
            traqueur = centre
            
        elif motRecherche > motCandidat:
            print('motRecherche > motCandidat')
            print(motCandidat)
            
            plusBas = traqueur
            
            print(traqueur)
            
        elif motRecherche < motCandidat:
            print('motRecherche < motCandidat')
            print(motCandidat)
            
            plusHaut = traqueur
            
            print(traqueur)
        
        nbBcle += 1
        print('nbBoucle =' +str(nbBcle))
        motRecherche = dzli.iloc[var, 0]
"""