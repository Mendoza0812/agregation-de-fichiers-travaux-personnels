# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 08:52:25 2022

@author: Max-Louis

"""

import pandas as pd

"""
dzAlphNb est le csv dans lequel la colonne idNom est classée 
par ordre alphabétique. dzAlphNb et dzInvAlphNb sont les mm bdd
sauf que dzInvAlphNb est trié sur la colonne SYN
"""
dzAlphNb = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzAlphNb.csv')
dzInvAlphNb = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzInvAlphNb.csv')

"""
pour faciliter la compréhension et la comparaison, dzInvAlphNb 
a les colonnes IN et SYN qui sont permutés de sorte à ce que quand
je vais nommer un emplacement dans la bdd, je puisse lire sur la 
mm colmn les mots classés par ordre alphabetique

a noter que les mots classés par ordre alphabetique correspondent pour
 chacun a une lgn sur laquelle il y a la nat du modorgn, son syn et 
 la proxmté déterminé par une val entre 0 et 400, 0 le plus eloigné 
 et 400 le plus rapproché
"""
dzInvAlphNb = dzInvAlphNb[['listeSyno','NatNom','IdNom','val400','AlphNb']]

#création des listes sur lesquelles seront supprimés les lignes qui sont
# des quasi dbls avec pour seule modfction val400 et natSyno
# val800 est un cumul des 2 val 400 ou alors dans le cas d'une abs de
#doublon dans la ligne c'est val400 fois 2

idN = []
natN = []
syno = []
natS = []
val800 = []

"""
varCompIN et varCompSYN doivent avoir la même valeur a chaque incrementation
ces var vont permettre de compter sur une partie de la bdd où ts ls 
mots commncnt par la mm initiale. Cela prmet au pgm d'eviter de 
chercher sur trop de lgns. Si le mot rchrché commnc par a, il serait 
inutile de rechercher un potentiel doublon sur d'autmot sils commnc
pas par a

la colmn AlphNb va de 0 a 28. 0 sont ts les mots commncnt par des 
majscl, de 1 a 26 c'est de a a z et 27 sont ts ls mots commcant par 
des carSpec

De cette maniere varCompIN et varCompSYN permettent avc la colmn
AlphNb de classer les 2 bdd par l'initiale
"""
varCompSYN = 0
varCompIN = 0

for loop in range(28):
    
#Les comprtmnts vnt prmttr de compartimenter la bdd en plusrs pties

    compartimentSYN = dzInvAlphNb[dzInvAlphNb['AlphNb'] == varCompSYN]
    compartimentIN = dzAlphNb[dzAlphNb['AlphNb'] == varCompIN]
    
#liVarIN va permettre de mesurer par len le nb de mots retrouves dans IN
# mais aussi de retrouver dans quelle ligne le modorgn a ete pris
    liVarIN = []
    
    """
varIN et varSYN sont des variables qui vont fonctionner comme un compteur
dans la 1ere boucle while, varSYN va permettre de dtrminer les dbls 
entre chq mts de la clmn IN et de la clmn SYN. 2 choix snt possibles
soit le mot a un doublon auquel cas natS stockera la nat du Syno et 
où val800 cumulera val400 des lgn corrspndantes
Si ce n'est pas le cas, le mot visé par varSYN de la colonne listeSyno 
issue de la bdd dzInvAlphNb n'a pas de doublon, dnc n'a pas de natS 
et son val800 sera le val400 fois 2.
Si la variable varSYN est égale a la lgueur du nb de lgn du comprtmtSYN
c'est que varSYN sra passé par toutes les lgn de cmprtmtSYN
A noter que comptmSYN et cmptmtIN peuvent avoir une taille differnt 
mm si varCompIN et varCompSYN restent idntqs
"""
    varSYN = 0
    varIN = 0
    
    while varSYN < len(compartimentSYN):
        #print('while varSYN < len(comparimentSYN')
        
        """
        la cdtion if len(cmptmIN) == 0 prmt decarter cmptmtIN qd il 
        n'a pas de lgn. Cela est le cas lorsque vrCmpIN et vrCmpSYN 
        sont egale a 0 ou a 27. En effet, dzAlphNb etant trie sur 
        la colmn IN et qu'aucun mot de la clmn IN ne possd de mjscl 
        ou de carSpec en dbt de mot, dzAlphNb ne comporte pas de lgn 
        lrsq vrCmpIN  = 0 ou 26. De ce fait, les mots commncnt par des 
        mjscl ou des carSpec ne possd pas de dbln car elles n'xst q
         dns la clmn SYN et pas dans la colmn IN
        """
        if len(compartimentIN) == 0:
            print('if len(compartimentIN) == 0:')
            
            idN.append(compartimentSYN.iloc[varSYN,0])
            natN.append(compartimentSYN.iloc[varSYN,1])
            syno.append(compartimentSYN.iloc[varSYN,2])
            natS.append('')
            val800.append(compartimentSYN.iloc[varSYN,3] * 2)
            varSYN += 1
            print('varSYN if = ' + str(varSYN))
            varIN = 0
            
            """
            varIN et varSYN incrmntent la ligne respctvmt de la colmn IN dans dzAlphNb 
            et de la colmn SYN dans dzInvAlphNb
            ayant permute les colonnes dans la bdd dzInvAlphNb, listeSyno est dans la colmn zero
            pour fciliter la comprehension et eviter les erreurs.
            Il est evident qu'un doublon aura la mm iloc dans l mm num de colmn que ce soit pour le 
            modorgn dans la colmn IN ou pour le syno dns la colmn SYN
            """
        elif compartimentIN.iloc[varIN,0] == compartimentSYN.iloc[varSYN,0]:
            print('elif compartimentIN.iloc[varIN,0] == compartimentSYN.iloc[varSYN,0]:')
            
            if compartimentIN.iloc[varIN,2] == compartimentSYN.iloc[varSYN,2]:
                print('elif compartimentIN.iloc[varIN,2] == compartimentSYN.iloc[varSYN,2]:')
                
                idN.append(compartimentIN.iloc[varIN,0])
                
                liVarIN.append(compartimentIN.iloc[varIN,0])
                
                natN.append(compartimentIN.iloc[varIN,1])
                syno.append(compartimentIN.iloc[varIN,2])
                natS.append(compartimentSYN.iloc[varSYN,1])
                val800.append(compartimentIN.iloc[varIN,3] + compartimentSYN.iloc[varIN,3])
                varSYN += 1
                print('varSYN elif =' + str(varSYN))
                varIN = 0
                
            else:
                
                varIN += 1
        else:
            
            varIN += 1
            
            precSYN = varSYN - 1

            suivSYN = varSYN
            print('varSYN else ='+ str(varSYN))
            
            # etablir un prec/suiv pour eviter la remise des cmptr a 0
            if varIN == len(compartimentIN):
                print('if varIN == len(compartimentIN):')
                
                idN.append(compartimentSYN.iloc[varSYN,0])
                natN.append(compartimentSYN.iloc[varSYN,1])
                syno.append(compartimentSYN.iloc[varSYN,2])
                natS.append('')
                val800.append(compartimentSYN.iloc[varSYN,3] * 2)
                
                varSYN += 1
                varIN = 0
            
                if varSYN == len(compartimentSYN):
                    break
                    
                elif compartimentSYN.iloc[precSYN,0] == compartimentSYN.iloc[suivSYN,0]:
                    print('compartimentSYN.iloc[precSYN,0] == compartimentSYN.iloc[suivSYN,0]:')
                    
                    while compartimentSYN.iloc[precSYN,0] == compartimentSYN.iloc[suivSYN,0]:
                        
                        idN.append(compartimentSYN.iloc[varSYN,0])
                        natN.append(compartimentSYN.iloc[varSYN,1])
                        syno.append(compartimentSYN.iloc[varSYN,2])
                        natS.append('')
                        val800.append(compartimentSYN.iloc[varSYN,3] * 2)
                        
                        varSYN += 1
                        precSYN = varSYN - 1
                        suivSYN = varSYN
                        
                        print('varSYN ='+ str(varSYN))
                        
                        if varSYN == len(compartimentSYN):
                            print("varSYN == len(compartimentSYN)")
                            varSYN - 1
                            break
                    
    #Test pour savoir si tous les mots de la colonne IN ont ete faits, y compris les mots IN sans dbls            
    if len(liVarIN) < len(compartimentIN):
        print('len(liVarIN) < len(compartimentIN):')
        
        varIN = 0
        varSYN = 0
        
        while varIN < len(compartimentIN):
            print('while varIN < len(compartimentIN):')
            
            if compartimentIN.iloc[varIN,0] == compartimentSYN.iloc[varSYN,0]:
                print('if compartimentIN.iloc[varIN,0] == compartimentSYN.iloc[varSYN,0]:')
                
                if compartimentIN.iloc[varIN,2] == compartimentSYN.iloc[varSYN,0]:
                    print('if compartimentIN.iloc[varIN,2] == compartimentSYN.iloc[varSYN,2]:')
                 
                    varIN += 1
                    print(varIN)
                    varSYN = 0
                
                else:
                
                    varSYN += 1
            else:
                print('compartimentIN.iloc[varIN,0] != compartimentSYN.iloc[varSYN,0]')
                varSYN += 1
                
                precIN = varIN - 1
                
                suivIN = varIN
                print('varIN else ='+ str(varIN))
                
                if varSYN == len(compartimentSYN):
                    print('if varSYN == len(compartimentSYN):')
                    
                    idN.append(compartimentIN.iloc[varIN,0])
                    natN.append(compartimentIN.iloc[varIN,1])
                    syno.append(compartimentIN.iloc[varIN,2])
                    natS.append('')
                    val800.append(compartimentIN.iloc[varIN,3] * 2)
                    
                    varIN += 1
                    print(varIN)
                    varSYN = 0
                
                    if varIN == len(compartimentIN):
                        print('varIN == len(compartimentIN)')
                        break
                    
                    elif compartimentIN.iloc[precIN,0] == compartimentIN.iloc[suivIN,0]:
                        print('compartimentIN.iloc[precIN,0] == compartimentIN.iloc[suivIN,0]:')
                        
                        while compartimentIN.iloc[precIN,0] == compartimentIN.iloc[suivIN,0]:
                            print('while compartimentIN.iloc[precIN,0] == compartimentIN.iloc[suivIN,0]:')
                            
                            idN.append(compartimentIN.iloc[varIN,0])
                            natN.append(compartimentIN.iloc[varIN,1])
                            syno.append(compartimentIN.iloc[varIN,2])
                            natS.append('')
                            val800.append(compartimentIN.iloc[varIN,3] * 2)
                               
                            varIN += 1
                            precIN = suivIN - 1
                            suivIN = varIN
                            
                            print('varIN ='+ str(varIN))
                            
                            if varIN == len(compartimentIN):
                                print("varIN == len(compartimentIN)")
                                varIN - 1
                                break
                
    varCompIN += 1
    print(varCompIN)
    varCompSYN += 1