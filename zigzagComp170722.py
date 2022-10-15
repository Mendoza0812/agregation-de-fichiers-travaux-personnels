# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 00:22:39 2022

@author: Max-Louis

Chaque mot traité par le programme doit être immédiatement classé 
de sorte à ce que le nb de lgn necessaire a faire la recherche d'un 
mot precis se reduise au fil d l xction du pgm. les modorgn et les syno
 ciblés par pgsvIN et pgsvSYN sont rechrch dns la bdd de l'autre ( la 
 variable pgsvIN cible le modorgn dans la bdd clss par OrdAlphbtq selon 
 la colonne IdNom et va ê comparé au mot que cible zzTrancheSYN,
en effet, la variable zzTranche fait des zigags et tranche dans la 1ere 
boucle sur la longueur totale du nombre de lignes en redefnis
sant les variables plusHaut et plusBas en fonction si le mot cible 
par la variable pgsv est inferieur ou superieur au mot cible par 
la variable zzTrancheSYN dans la bdd clss par OrdAlphtq selon la 
 colonne SYN.) La zone dans laquelle sera recherché le modorgn sera alors
réduit de moitié. Si la difference entre les variables plusHaut et plusBas
sont inferieures a 2, cela signifie que la lgn cible par pgsv n'a pas 
de doublon. Quand une ligne n'a pas de doublon, on copie et colle 
dans les listes dans lesquelles sont stockées les mots sans doublon.
Plus précisément, un mot peut avoir été écrit plusieurs fois dans la 
mm ligne ou écrite plusieurs fois dans une colonne differente mais avoir 
un synonyme introuvable. Dans ce cas, la ligne correspondante est unique.
Pour éviter de compter plusieurs fois les mêmes lignes, il faut se 
rendre compte que nous utilisons deux bdd identiques où l'une est classée 
par ordre alphabetique selon la colonne IN (dzlian) et l'autre selon la 
colone SYN (dzliinvan). Le classmnt par OrdreAlphabetique permet d'utiliser
 la technique permettant de determiner si un mot est inf ou sup par rap
 port a un autre mot permettant d'eviter
 d'utiliser un test ligne par ligne comme 
 le brute force. si le mot recherché est plus haut que le mot cible 
 la variable ciblant le mot suspecté imprègne la variable plusHaut.
 De cette manière plus haut descend de moitie puis la var centre 
 est recentré sur plusHaut/plusBas.
 Une liste devra stocker les variables qui déterminent un doublon 
 permutable entre un mot de la colmn IN et un mot de la colmn SYN
  sur la mm lgn qui sera sup a la variable pgsv.
  Une liste devra stocker les variables qui fixent les lgn uniques 
  deja traités par une des deux bdd.
"""

import pandas as pd

dzlian = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzAlphNb.csv')
dzliinvan = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzInvAlphNb.csv')

dzliinvan = dzliinvan[['listeSyno','NatNom','IdNom','val400','AlphNb']]

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

varComp = 0

for loop in range(2):
    
    print(' --- varComp = ' + str(varComp))
    
    compSYN = dzliinvan[dzliinvan['AlphNb'] == varComp]
    compIN = dzlian[dzlian['AlphNb'] == varComp]
    
    pgsvIN = 0
    pgsvSYN = 0
    
    nbLgnCmpIN = len(compIN)
    centreIN = int((nbLgnCmpIN - (nbLgnCmpIN % 2)) / 2)
    
    nbLgnCmpSYN = len(compSYN)
    centreSYN = int((nbLgnCmpSYN - (nbLgnCmpSYN % 2)) / 2)
    
    stockTstDblSYN = []
    
    if varComp == 0 or varComp == 27:
        print('nbLgnCmpIN == 0')
        
        while pgsvSYN < nbLgnCmpSYN:
            
            idNSnsDbl.append(compSYN.iloc[pgsvSYN,0])
            natNSnsDbl.append(compSYN.iloc[pgsvSYN,1])
            synoSnsDbl.append(compSYN.iloc[pgsvSYN,2])
            natSSnsDbl.append('')
            val800SnsDbl.append(compSYN.iloc[pgsvSYN,3] * 2)
            pgsvSYN += 1
        
        pgsvSYN = 0
        
    #varComp est a pgsv ce que la minute est a la seconde   
    elif varComp > 0 or varComp < 27:
        print('varComp > 0 or varComp < 27 \n')
        
        
        for loop in range(3):
            
            zzTrancheIN = centreIN
            
            zzTrancheSYN = centreSYN
            print('zzTrancheSYN = ' + str(zzTrancheSYN))
            
            plusBasIN = 0
            plusHautIN = nbLgnCmpIN
            
            plusBasSYN = 0
            plusHautSYN = nbLgnCmpSYN
            
            #les 2 variables cI prennent la mme ligne
            #Ici, la logique est de suivre le clssmt par OrdAlph dl clmn IN
            #En incrementant la variable pgsvIN
            #Modorgn pour Syno classe par ordre alphbtq dns la clmn IN (cmpIN)
            cIip0 = compIN.iloc[pgsvIN, 0]
            print('cIip0 = compIN.iloc[pgsvIN, 0]')
            print('cIip0 = ' + str(cIip0))
            
            #Syno pour Modorgn clss par ordr alphbtq dn la clmn IN (cmpIN)
            cIip2 = compIN.iloc[pgsvIN, 2]
            print('cIip2 = compIN.iloc[pgsvIN, 2]')
            print('ciIp2 = ' + str(cIip2))
            #nbLtrCmpIN2 = len(cIip2)
            #print('nbLtrCmpIN2 = ' + str(nbLtrCmpIN2) + '\n')
    
            #lgnPgvIN = compIN.iloc[prgrsv]
            
            #les 2 variables cS prennent la mme ligne
            #Ici, la logique est de suivre le clssmt par OrdAlph dl clmn SYN
            #En incrementant la variable prgrsv
            #Syno pour Modorgn classe par ordre alphbtq dns la clmn SYN (cmpSYN)
            cSip0 = compSYN.iloc[pgsvSYN, 0]
            print('cSip0 = ' + str(cSip0))
            #nbLtrCmpSYN0 = len(cSip0)
            #print('nbLtrCmpSYN0 = ' + str(nbLtrCmpSYN0) + '\n')
            
            #Modorgn pour Syno classe par ordre alphbtq dns la clmn SYN (cmpSYN)
            cSip2 = compSYN.iloc[pgsvSYN, 2]
            print('csIp2 = ' + str(cSip2))
            #nbLtrCmpSYN2 = len(cSip2)
            #print('nbLtrCmpSYN2 = ' + str(nbLtrCmpSYN2) + '\n')
            
            #lgnPgvSYN = compSYN.iloc[prgrsv]
            
            cIiz0 = compIN.iloc[zzTrancheIN, 0]
            
            cIiz2 = compIN.iloc[zzTrancheIN, 2]
            
            cSiz0 = compSYN.iloc[zzTrancheSYN, 0]
            
            cSiz2 = compSYN.iloc[zzTrancheSYN, 2]
            
            print('phase de recherche de tous les cIip0 apparaissant dans la clmn SYN de cmpSYN avec cSiz0')
            nbBoucle = 0
            finDRechrch = False
            
            while finDRechrch == False:
                
                print(' ---- nbBoucle = ' + str(nbBoucle) + ' ---- ')
                #test Modorgn (dns la bdd clss pOrdAlph IN) pour Syno (dns la bdd clss pOrdAlph SYN)
                cSiz0 = compSYN.iloc[zzTrancheSYN, 0]
                print('cSiz0 = ' + str(cSiz0))
                
                cSiz2 = compSYN.iloc[zzTrancheSYN, 2]
                print('cSiz2 = ' + str(cSiz2))
                
                print('cIip0 = ' + str(cIip0))
                print('ciIp2 = ' + str(cIip2))
                
                ecartHBSYN = plusHautSYN - plusBasSYN
                print('ecartHBSYN = ' + str(ecartHBSYN))
                
                zzTrancheSYN = plusBasSYN + int((ecartHBSYN - (ecartHBSYN % 2)) / 2)
                print('zzTrancheSYN = ' + str(zzTrancheSYN))
                            
                    
                if cIip0 == cSiz0 :
                    print('cIip0 == cSiz0')
                    
                    print('test pour le synonyme de cIip0 soit cIip2')
                    
                    if cIip2 == cSiz2 :
                        print('cIip2 == cSiz2')
                        #ajout dans les listes doublons et stockage de la variable zzTrancheSYN dans une liste en vue d eviter les doublons
                        #cette liste stockTstDblSYN doit etre utilisee pour verifier si une ligne recupere par zzTrancheSYN ne soit pas rajoute   
                    
                        idN.append(cIip0)
                        natN.append(compIN.iloc[pgsvIN, 1])
                        syno.append(cSiz2)
                        natS.append(compSYN.iloc[zzTrancheSYN, 1])
                        val800.append(compIN.iloc[pgsvIN, 3] + compSYN.iloc[zzTrancheSYN, 3])
                        
                        stockTstDblSYN.append(zzTrancheSYN)
                        
                        finDRechrch = True
                        print('finDRechrch = True')
                        print('recherche de doublon termine sur cette lgn pgsvIN')
                    
                    else:
                        print('la ligne trouve par zzTrancheSYN ne correspond pas a celle recherchee')
                        # pour aligner
                        break
                    
                elif ecartHBSYN < 1:
                    print('ecartHBSYN < 1')
                    print('Aucun doublon de cIip0 trouve dans colmn SYN de cmpSYN avc var cSiz0')
                    
                    idNSnsDbl.append(cIip0)
                    natNSnsDbl.append(compIN.iloc[pgsvIN, 1])
                    synoSnsDbl.append(compIN.iloc[pgsvIN, 2])
                    natSSnsDbl.append('')
                    val800SnsDbl.append(compIN.iloc[pgsvIN,3] * 2)
                    
                    finDRechrch = True
                    print('finDRechrch = True')
                    print('recherche de doublon termine sur cette lgn pgsvIN')
                
                elif cIip0 < cSiz0:
                    print('cIip0 < cSiz0')
                    
                    plusHautSYN = zzTrancheSYN
                    
                elif cIip0 > cSiz0:
                    print('cIip0 < cSiz0')
                    
                    plusBasSYN = zzTrancheSYN
                
                else:
                    print('lgnPgvIN and lgnPgvSYN are not == or !=')
                    
                
                nbBoucle += 1
            pgsvIN += 1
            pgsvSYN += 1
           
    
    varComp += 1