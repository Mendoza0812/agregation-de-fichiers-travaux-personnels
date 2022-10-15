# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 22:57:42 2022

@author: Max-Louis
des mots dont les initiales ne commencent ni par mjscl ni par carspec 
se trouvent soit en doublon soit uniquement dans colmn SYN soit unqmt 
dns la colmn IN
"""

import pandas as pd

deaazz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')
#works
del deaazz['placeSyno']
deaaz = pd.DataFrame(deaazz)
deaazzInv = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\deaazzInv.csv')

p1erIN = []
d2emeSYN = []

majuscule = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
carSpec = ['à','á','â','æ','ç','è','é','ê','ë','ì','í','î','ï','ñ','ò','ó','ô','œ','ù','ú','û','ü','ý','ÿ',' ','É','À','Á','Â','Ã','Ä','Å','Æ','Ç','È','É','Ê','Ë','Ì','Í','Î','Ï','Ð','Ñ','Ò','Ó','Ô','Õ','Ö','Ø','Œ','Š','þ','Ù','Ú','Û','Ü','Ý','Ÿ']
alphabet = [majuscule,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',carSpec]

idNom = 'IdNom'
liSyno = 'listeSyno'

varNbLgn = 0

# CONTINUER AVEC UPPRCS ET VARUPPRCS

def saisiLetr(df,colmn,letr):
    var = 0
    
    global colmnSup
    colmnSup = []
    for loop in range(382551):
        string = df.iloc[var,colmn]
        if letr == 1:
            if len(string) == 1:
                print(string)
                colmnSup.append(' ')
        else:
            colmnSup.append(string[letr])
        #probleme a regler ici
        var += 1

# traduis les initiales en chiffre pour faciliter le tri
def tradAlphaNb(liColmn):
    
    varTrad = 0
    varNbLgn = 0
    varMajscl = 0
    global testMjscl
    testMjscl = []
    varCarSpc = 0
    global liTrad
    liTrad = []
    
    while varNbLgn < len(liColmn):
        print(varNbLgn)
        print(varTrad)
        print(liColmn[varNbLgn])
        if varTrad > 27:
            varTrad = 0
            
        elif liColmn[varNbLgn] == alphabet[varTrad]:
            
            liTrad.append(varTrad)
            
            varNbLgn += 1
            
        else:
                
                if liColmn[varNbLgn] == majuscule[varMajscl]:
                    if alphabet[varTrad] == majuscule:
                        liTrad.append(varTrad)
                        varNbLgn += 1
                    else:
                        varTrad += 1
                    
                elif liColmn[varNbLgn] == carSpec[varCarSpc]:
                    if alphabet[varTrad] == carSpec:
                        liTrad.append(varTrad)
                        varNbLgn += 1
                    else:
                        varTrad += 1
                    
                else:
                    varCarSpc += 1
                    if varCarSpc > 58:
                        varTrad += 1
                        varCarSpc = 0
                        print(varCarSpc)
                        
                    varMajscl += 1
                    if varMajscl > 25:
                        varTrad += 1
                        varMajscl = 0
                        print(varMajscl)
                        
                    else:
                
                        varTrad += 1
                
                
                    
"""
attribue un numero par initial de chaque mot pour faciliter le tri
 et effectuer des incrémentations 
 (A = 0, Z = 0, a = 1, b = 2,..., z = 26, carSpec (àéî etc.) = 27)
 concatener liInitialNb00 et 01 en les séparant d'un chiffre entre 
 les deux pour determiner la colonne ou l'emplacement et eviter les
confusions
Pour cela creer liste assimilier la concatenation a partir dune var 
la question vient sur la maniere detablir le chfr pour IN SYN /
 initiale 0 (soit string[0]) ou initiale 1 (soit string[1])


alphaNumIN = []
alpheNumSYN = []
 
saisiLetr(deaazz,0,0)
colmn00 = colmnSup
tradAlphaNb(colmn00)
liInitialAlphNb00 = liTrad


saisiLetr(deaazz,0,1)
colmn01 = colmnSup
tradAlphaNb(colmn01)
liInitialAlphNb01 = liTrad
"""

#carspec et majscl sont comptes xclsvmnt dns deaazzInv dnt le clssmt
#par ordr alphbtq est etablie sur la colmn listeSyno
#Ne pas oublier de sort_value liSyno
saisiLetr(deaazzInv,2,0)
colmn20 = colmnSup
tradAlphaNb(colmn20)
liInitialAlphNb20 = liTrad

"""
saisiLetr(deaazzInv,2,1)
colmn21 = colmnSup
tradAlphaNb(colmn21)
liInitialAlphNb21 = liTrad
"""

