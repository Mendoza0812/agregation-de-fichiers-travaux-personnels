# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 21:22:59 2022

@author: Max-Louis
"""

import pandas as pd

deaaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')
#works
del deaaz['placeSyno']

#Permet d'avoir la liste de synonymes d'un mot trié sans doublon
def applic(name):
    
    liContainsChoseColIdNom = deaaz[deaaz['IdNom'].str.contains(name)]
    #works
    longueurLiContainsChoseColIdNom = len(liContainsChoseColIdNom)

    nbrLettreMotColIdNom = []

    var = 0

    for loop in range(longueurLiContainsChoseColIdNom):
        nbrLettreMotColIdNom.append(len(liContainsChoseColIdNom.iloc[var, 0]))
        var += 1
        
    liChoseColIdNom = liContainsChoseColIdNom

    liChoseColIdNom['nbLettrIdNom'] = nbrLettreMotColIdNom

    var = 0
    true = 0
    false = 0

    for loop in range(longueurLiContainsChoseColIdNom):
        if len(liChoseColIdNom.iloc[var, 0]) == liChoseColIdNom.iloc[var, 4]:
            true += 1
        else:
            false += 1
    print(true)
    print('Nombre d\'erreurs :')
    print(false)

    var = 0

    idNom = []
    natNom = []
    listeSyno = []
    val400 = []
    nbLettrMotChose = len(name)
    for loop in range(longueurLiContainsChoseColIdNom):
        if liChoseColIdNom.iloc[var, 4] == nbLettrMotChose:
            idNom.append(liChoseColIdNom.iloc[var, 0])
            natNom.append(liChoseColIdNom.iloc[var, 1])
            listeSyno.append(liChoseColIdNom.iloc[var, 2])
            val400.append(liChoseColIdNom.iloc[var, 3])
        var += 1
        
    products_list = (idNom, natNom, listeSyno, val400)
    choseIdNom = pd.DataFrame (products_list).transpose()
    choseIdNom.columns = ['IdNom','NatNom','motchos','val400']

    liContainsChoseColListeSyno = deaaz[deaaz['listeSyno'].str.contains(name)]
    # nbLignes  = longueurLiContainsChoseColIdNom
    nbLignes = len(liContainsChoseColListeSyno)
    # nbLettres  = nbLettreMotColIdNom sauf qu'ici col. ListeSyno
    nbLettres = []

    var = 0

    for loop in range(nbLignes):
        nbLettres.append(len(liContainsChoseColListeSyno.iloc[var, 2]))
        var += 1
        
    choseColLynst = liContainsChoseColListeSyno

    choseColLynst['nbLettrLynst'] = nbLettres

    var = 0
    true = 0
    false = 0

    for loop in range(nbLignes):
        if len(choseColLynst.iloc[var, 2]) == choseColLynst.iloc[var, 4]:
            true += 1
        else:
            false += 1
    print(true)
    print('Nombre d\'erreurs :')
    print(false)

    var = 0

    idNom = []
    natNom = []
    listeSyno = []
    val400 = []
    nbLettrMotChose = len(name)
    for loop in range(nbLignes):
        if choseColLynst.iloc[var, 4] == nbLettrMotChose:
            idNom.append(choseColLynst.iloc[var, 0])
            natNom.append(choseColLynst.iloc[var, 1])
            listeSyno.append(choseColLynst.iloc[var, 2])
            val400.append(choseColLynst.iloc[var, 3])
        var += 1
        
    products_list = (idNom, natNom, listeSyno, val400)
    choseLynst = pd.DataFrame (products_list).transpose()
    choseLynst.columns = ['IdNom','NatNom','motchos','val400']

    idNom = []
    natNom = []
    syno = []
    natSyno = []
    val800 = []
    varSearchChoseIdNom = 0
    varSearchChoseLynst = 0
    varFind = 0

    longueurLiContainsChoseColLynst = len(choseLynst)

    while True :

        if choseIdNom.iloc[varSearchChoseIdNom, 2] == choseLynst.iloc[varSearchChoseLynst, 0]:
            idNom.append(choseIdNom.iloc[varSearchChoseIdNom, 0])
            natNom.append(choseIdNom.iloc[varSearchChoseIdNom, 1])
            syno.append(choseIdNom.iloc[varSearchChoseIdNom, 2])
            natSyno.append(choseLynst.iloc[varSearchChoseLynst, 1])
            val800.append(choseIdNom.iloc[varSearchChoseIdNom,3] + choseLynst.iloc[varSearchChoseLynst,3])
            varSearchChoseIdNom += 1
            varSearchChoseLynst = 0
        else:
            varSearchChoseLynst += 1
            if varSearchChoseLynst == longueurLiContainsChoseColLynst :
                idNom.append(choseIdNom.iloc[varSearchChoseIdNom, 0])
                natNom.append(choseIdNom.iloc[varSearchChoseIdNom, 1])
                syno.append(choseIdNom.iloc[varSearchChoseIdNom, 2])
                natSyno.append('')
                val800.append(choseIdNom.iloc[varSearchChoseIdNom,3] * 2)
                varSearchChoseIdNom += 1
                varSearchChoseLynst = 0
        
        if varSearchChoseIdNom == len(choseIdNom) :
            break

    products_list = (idNom, natNom, syno, natSyno, val800)
    chose800 = pd.DataFrame (products_list).transpose()
    chose800.columns = ['IdNom','NatNom','Syno','natSyno', 'val800']
    global chose800sv
    chose800sv = chose800.sort_values('val800', ascending = False)
    print(chose800sv)    


# le mot dorign estil un des 1er syno de ses prpre syno?
# Priorité de val800 sur lemplcmt du mot dorgn dans quadra du liMotDegre1

def defQuadra(liMotDegre):
    
    #Je garde ici chose800sv pour detacher de liMotDegre
    longueurListeChose800sv = len(chose800sv)
    
    #En respectant la geometrie 2D seulement 4 pts distance centre chose
    if longueurListeChose800sv >= 4:
        synoChoix = chose800sv.iloc[0:4]

        lenSynoChoix = len(synoChoix)
        valeur = []
        natSyno = []
        motss = []
        var = 0
        
        for loop in range (lenSynoChoix):
            motss.append(synoChoix.iloc[var, 2])
            natSyno.append(synoChoix.iloc[var, 3])
            valeur.append(synoChoix.iloc[var, 4])
            var += 1
    else:
        valeur = []
        natSyno = []
        motss = []
        var = 0
        
        for loop in range (longueurListeChose800sv):
            motss.append(synoChoix.iloc[var, 2])
            natSyno.append(synoChoix.iloc[var, 3])
            valeur.append(synoChoix.iloc[var, 4])
            var += 1
    
    global quadra
    # quadra = les 4 premiers syno de liMotDegre0 ou le mot dorign au centre
    products_list = (motss, natSyno, valeur)
    quadra = pd.DataFrame (products_list).transpose()
    quadra.columns = ['syno', 'natSyno', 'val800']

    print(quadra)
    
    
    # lenQuadra nest pas frcmt de 4 si la li est tp petite
    lenQuadra = len(quadra)
    
    var = 0
    
    global liMotDegre1
    liMotDegre1 = []
    
    # applic les prem syno du mot dorign = liMotDegre1
    for loop in range(lenQuadra):
        mot1 = quadra.iloc[var, 0]
        
        mot1str = str(mot1)
        
        applic(mot1str)

        liMotDegre1.append(chose800sv)
        var += 1

def modifCroixModorgn(suriname):
    var = 0
    var1 = 0
    varRemplcmt = 4
    var800sv = 0
    lenLiMotDegre01 = len(liMotDegre01)
    
    testModifSyno = []
    testNatSyno = []
    testVal = []
    
    fautIlRmplcrSyno = ''
    
    for loop in range(lenLiMotDegre01):
        if liMotDegre1[var].iloc[var1, 2] == motAnalyse:
            testModifSyno.append(liMotDegre01[var].iloc[var1, 0])
            testNatSyno.append(liMotDegre01[var].iloc[var1, 1])
            testVal.append(liMotDegre01[var].iloc[var1, 4])
            var += 1
        else:
            var1 += 1
            if var1 == 5:
                if liMotDegre1[var].iloc[var1, 4] < quadra.iloc[var, 2]:
                    print("Pb: val quadra > val liMotDegre1 alors que abs doublon")
                elif liMotDegre1[var].iloc[var1, 4] == quadra.iloc[var, 2]:
                    testModifSyno.append(liMotDegre01[var].iloc[var1, 0]+"/"+quadra.iloc[var, 0])
                    testNatSyno.append(liMotDegre01[var].iloc[var1, 1]+"/"+quadra.iloc[var, 1])
                    testVal.append(liMotDegre01[var].iloc[var1, 4]+"/"+quadra.iloc[var, 2])
                    print('EGALITE val limotDegre / valQuadra :'+ liMotDegre1[var].iloc[var1, 4])
                else:
                    longueurListeChose800sv = len(chose800sv)
                    boolWhile = False
                    while boolWhile == False:
                        fautIlRmplcrSyno = liMotDegre0.iloc[varRemplcmt, 2]
                    
                        applic(fautIlRmplcrSyno)
                        if chose800sv.iloc[var800sv, 2] == motAnalyse:
                            testModifSyno.append(chose800sv.iloc[var800sv, 0])
                            testNatSyno.append(chose800sv.iloc[var800sv, 1])
                            testVal.append(chose800sv.iloc[var800sv, 4])
                        else:
                            var800sv += 1
                            if var800sv == 4:
                                varRemplcmt += 1
                                var800sv = 0
                                if varRemplcmt == longueurListeChose800sv:
                                    boolWhile = True
                        
                        lenTestModifSyno = len(testModifSyno)
                        if lenTestModifSyno == 4:
                            boolWhile = True
                            
    products_list = (testModifSyno, testNatSyno, testVal)
    croixModifie = pd.DataFrame (products_list).transpose()
    croixModifie.columns = ['synoMd', 'natSynoMd', 'val800Md']
    print(croixModifie)
    
#mot a analyser
motAnalyse = 'chose'

# synonymes de chose
applic(motAnalyse)

#maintien de la liste dans une variable liMotDegre0
liMotDegre0 = chose800sv

defQuadra(chose800sv)

liMotDegre01 = liMotDegre1

#Fonction ci dessous a refaire
modifCroixModorgn(liMotDegre1)

"""
Ici, il faut tester si les premiers synonymes considérés comme 
étant le plus proche du mot d'origine
dans la liste issue de motAnalyse, verifier sils
 ont également dans leur liste le mot dorgn correspondant a motAnalyse 
 sur la leur. La priorité va sur la valeur val800 quant a la place
 du mot dorgn sur la li des synos liMotDegre1
 si val800 dans les 4 (ou moins) est > au val800 du modorgn 
 la li des prem syno du modorgn doit e modifie de sortaceque
 le syno concerne soit suppr, que les autr syno avnc dune place et
  que le syno 5e place prenne la 4e etc
"""

                      
        
            