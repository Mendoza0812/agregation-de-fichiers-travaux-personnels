# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 17:52:27 2022

@author: Max-Louis
"""

import pandas as pd

df10 = pd.read_csv(r'C:/Users/Max-Louis/df10Ref.csv')

dfDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

dfSyneurone = pd.read_csv( r'C:/Users/Max-Louis/df12svRef.csv')

print(' --- DEBUT --- ')
strContainsTotal = []

print('strContainsTotal = []')

strContainsDivisibleTotal = []

print('strContainsDivisibleTotal = []')

strContainsName = []

print('strContainsName = []')

incrStrContains = 0

print('incrStrContains = 0')

compteurNameImmediat = 0

print('compteurNameImmediat = 0')

compteurNiveauMax = compteurNameImmediat

print('compteurPourListeAccomplie = compteurNameImmediat')

niveauCompteur = []

print('niveauCompteur = []')

strContainsNameImmediat = 'bon'

print('strContainsNameImmediat = "bon" ')

print('stockage des listes terminees dans les listes suivant: "')

mot = []

print('mot = []')

nbDeSyno = []

print('nbDeSyno = []')

indexDf10 = []

print('indexDf10 = []')

dist = []

print('dist = []')

ref = []

print('ref = []')
print('"')

print('APPLICATION DE LA BOUCLE')
for loop in range(8):
    
    print('BOUCLE NUMERO = ' + str(loop))
    
    incrStrContains = 0
    print('remise a 0 de incrStrContains')
    
    niveauCompteur.append(compteurNameImmediat)
    print('niveauCompteur.append(compteurNameImmediat)')
    
    lenStrContainsNameImmediat = len(strContainsNameImmediat)
    print('(nombre d element contenu dans la chaine de caractere)')
    print('lenStrContainsNameImmediat = ' + str(lenStrContainsNameImmediat))
    
    refStrContainsNameImmediat = str(strContainsNameImmediat) + str(lenStrContainsNameImmediat)
    print('chaine de caractere unique permettant de lister une chaine de caractere specifique')
    print('refStrContainsNameImmediat = ' + str(refStrContainsNameImmediat))
    
    liStrContains = dfSyneurone[dfSyneurone['ref'].str.contains(refStrContainsNameImmediat)]
    print('liste des synonymes de la chaine de caractere')
    print('liStrContains =  \n' + str(liStrContains))
    
    strContainsTotal.append(len(liStrContains))
    print('ajout de la longueur totale du nombre de lignes = ' + str((len(liStrContains))))
    print('dans strContainsTotal')
    
    strContainsDivisibleTotal.append(incrStrContains)
    print('ajout du nombre de lignes deja visite dans cette liste = ' + str(incrStrContains))
    print(' dans strContainsDivisibleTotal')
    
    strContainsName.append(strContainsNameImmediat)
    print('ajout de la chaine de caractere = ' + str(strContainsNameImmediat))
    print('dans strContainsName')
    
    passageIndexDf10 = liStrContains.iloc[incrStrContains,2]
    print('passageIndexDf10 = ' + str(liStrContains.iloc[incrStrContains,2]))
    
    synonymesChoisir = df10.iloc[passageIndexDf10]
    print('synonymesChoisir = \n')
    print(df10.iloc[passageIndexDf10])
    
    if strContainsNameImmediat == synonymesChoisir.iloc[0]:
        
        synoTestSiDeja = synonymesChoisir.iloc[1]
    
    else:
        
        synoTestSiDeja = synonymesChoisir.iloc[0]
        
    print('synoTestSiDeja = ' + str(synoTestSiDeja))
    
    if synoTestSiDeja in strContainsName:
        print('synoTestSiDeja existe deja dans la liste strContainsName')
        print('tant que synoTestSiDeja existe dans strContainsName')
        print('APPLICATION D UNE BOUCLE WHILE')
        
        while synoTestSiDeja in strContainsName:
            print("synoTestSiDeja =" + str(synoTestSiDeja))
            print('existe deja dans la liste de strContainsName')
            
            strContainsDivisibleTotal[compteurNameImmediat] += 1
            print('strContainsDivisibleTotal[compteur] += 1')
        
            incrStrContains += 1
            print('incrStrContains += 1')
            
            if incrStrContains == len(liStrContains):
                
                print('incrStrContains == len(liStrContains)')
                
                print('remise a zero de incrStrContains')
                print('pour stocker toute la liste de ligne 0 a X')
                print('et l enlever du chemin')
                
                incrStrContains = 0
                print('incrStrContains = 0')
                
                print('DEBUT DE BOUCLE WHILE')
                while incrStrContains != len(liStrContains):
                    print('while incrStrContains != (len(liStrContains) - 1)')
                    
                    mot.append(liStrContains.iloc[incrStrContains,0])
                    print('mot.append(liStrContains.iloc[incrStrContains,0])')
                    
                    nbDeSyno.append(liStrContains.iloc[incrStrContains,1])
                    print('nbDeSyno.append(liStrContains.iloc[incrStrContains,1])')
                    
                    indexDf10.append(liStrContains.iloc[incrStrContains,2])
                    print('indexDf10.append(liStrContains.iloc[incrStrContains,2])')
                    
                    dist.append(liStrContains.iloc[incrStrContains,3])
                    print('dist.append(liStrContains.iloc[incrStrContains,3])')
                    
                    ref.append(liStrContains.iloc[incrStrContains,4])
                    print('ref.append(liStrContains.iloc[incrStrContains,4])')
                    
                    incrStrContains += 1
                    print('incrStrContains += 1')
                
                print('FIN DE LA BOUCLE WHILE (incrStrContains == len(liStrContains))')
                
                #incrStrContains depasse len(liStrContains) de 1
                incrStrContains -= 1
                
                #FAIRE LES DEL ICI
                
                compteurNiveauMax = compteurNameImmediat
                print('compteurNiveauMax = compteurNameImmediat')
                
                del strContainsDivisibleTotal[compteurNameImmediat]
                print('del strContainsDivisibleTotal[compteurNameImmediat]')
                
                del strContainsTotal[compteurNameImmediat]
                print('del strContainsTotal[compteurNameImmediat]')
                
                del strContainsName[compteurNameImmediat]
                print('del strContainsName[compteurNameImmediat]')
                
                del niveauCompteur[compteurNameImmediat]
                print('del niveauCompteur[compteurNameImmediat]')
                
                print('compteurNameImmediat = ' + str(compteurNameImmediat))
                
                compteurNameImmediat -= 1
                print('compteurNameImmediat -= 1')

            else:
                
                print('incrStrContains != len(liStrContains)')
                passageIndexDf10 = liStrContains.iloc[incrStrContains,2]
                print('passageIndexDf10 = ' + str(liStrContains.iloc[incrStrContains,2]))
                
                synonymesChoisir = df10.iloc[passageIndexDf10]
                print('synonymesChoisir = \n')
                print(df10.iloc[passageIndexDf10])
                
                if strContainsNameImmediat == synonymesChoisir.iloc[0]:
                    
                    synoTestSiDeja = synonymesChoisir.iloc[1]
                
                else:
                    
                    synoTestSiDeja = synonymesChoisir.iloc[0]
                    
                print('synoTestSiDeja = ' + str(synoTestSiDeja))

    synoSuivant = synoTestSiDeja
    
    strContainsNameImmediat = synoSuivant
    
    compteurNameImmediat += 1

print('strContainsTotal = ' + str(strContainsTotal))
print('strContainsDivisibleTotal = ' + str(strContainsDivisibleTotal))
print('strContainsName = ' + str(strContainsName))


print('mot = ' + str(mot))
print('nbDeSyno = ' + str(nbDeSyno))
print('indexDf10 = ' + str(indexDf10))
print('dist = ' + str(dist))
print('ref = ' + str(ref))