# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 18:38:05 2022

@author: Max-Louis

seules les lignes sans aucun caractère spécial en initial
 sont constitués de doublons. Il serait donc plus judicieux 
de filtrer selon tous les mots de la colonne listeSyno commençant 
par la lettre correspondante

En effet, seule la colonne listeSyno contient des mots dont l'initiale 
contient des caractères spéciaux, ce qui signifie qu'on traiterait 
plus facilement les lignes contenant des carspec en initiale en les
 séparant des lignes n'en ayant pas. On crée une moyenne sur les doublons
 

"""

import pandas as pd

#base de donnees entiere
deaazz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')
#works
del deaazz['placeSyno']

deaaz = pd.DataFrame(deaazz)

# cette fonction selectionne tous les mots dune ctgrie sln une clmn spcfq
def pOrdAlphbtq(initial):
    
    motsParInitial = deaaz[deaaz['listeSyno'].str.match(initial)]
    nbLignes = len(motsParInitial)
    
    var = 0
    
    #creation des listes q stckrnt la ctgrie de mt vise
    idNom = []
    natNom = []
    listeSyno = []
    val400 = []
    
    #ajout de chq info dns chq lste de gch a drt et de ht en bas
    for loop in range(nbLignes):
        
        idNom.append(motsParInitial.iloc[var, 0])
        natNom.append(motsParInitial.iloc[var, 1])
        listeSyno.append(motsParInitial.iloc[var, 2])
        val400.append(motsParInitial.iloc[var, 3])
        var += 1
        
    products_list = (idNom, natNom, listeSyno, val400)
    global globalInitial
    globalInitial = pd.DataFrame (products_list).transpose()
    globalInitial.columns = ['IdNom','NatNom','listeSyno','val400']

#1ere etape, la bdd est fractionne par ordre alphabetique
#cette fonction declare la variable df pour SYN commencant par la lettre a ou autre 


def passageALaMachine(gobel):
    decompte = 0
    prec = 0
    suiv = 1
    for loop in range (len(gobel)-1):
        if gobel.iloc[prec, 0] != gobel.iloc[suiv, 0]:
            print("string numero :"+ str(prec))
            string = gobel.iloc[prec, 0]
            print("listerMotChoisi")
            listerMotChoisi(string, gobel)
        prec = suiv
        suiv += 1
        decompte += 1
        if decompte == 1000:
            print(suiv)
            decompte = 0
        if suiv == (len(gobel)-1):
            if gobel.iloc[suiv, 0] != gobel.iloc[prec, 0]:
                string = gobel.iloc[suiv, 0]
                print("listerMotChoisi dernier")
                listerMotChoisi(string, gobel)

def listerMotChoisi(string, gobel):
    # df = gobelSYN  
    nbLettre = []
        
    precizWord = gobel[gobel['listeSyno'].str.contains(string)]
    var = 0
    nbLignes = len(precizWord)
    for loop in range(nbLignes):
        nbLettre.append(len(precizWord.iloc[var, 0]))
        var += 1
    
    var = 0

    idNom = []
    natNom = []
    listeSyno = []
    val400 = []
    
    #ajoute la msr du nb de lettre de chaque mot contenant word
    precizWord['nbLettr'] = nbLettre
    nbLettrString= len(string)
    print("ajout de la colonne pour comparaison nblettre et nbltrString")
    #tri les mots dt la lgueur ne corrsp pas au modorgn
    for loop in range(nbLignes):
        if precizWord.iloc[var, 4] == nbLettrString:
            idNom.append(precizWord.iloc[var, 0])
            natNom.append(precizWord.iloc[var, 1])
            listeSyno.append(precizWord.iloc[var, 2])
            val400.append(precizWord.iloc[var, 3])
            print("var nbLettrString :" + str(var))
        var += 1
        
    products_list = (idNom, natNom, listeSyno, val400)
    global listeMotPrecise
    listeMotPrecise = pd.DataFrame (products_list).transpose()
    listeMotPrecise.columns = ['IdNom','NatNom','listeSyno','val400']
    print(listeMotPrecise)
    print('listeMotPrecise')

def ecraseDoublonEtMoyenniseVal(liste1):
    idNom = []
    natNom = []
    syno = []
    natSyno = []
    val800 = []
    colmn0 = 0
    colmn2 = 0
    carSpec = 0

    nbLgnLynst = len(liste1)

    while True :
        print("colmn0 :" + colmn0+" colmn2 :" + colmn2)
        if len(liste1) == 0:
            print("len(liste) egale 0")
            while nbLgnLynst > carSpec:
                syno.append(liste1.iloc[carSpec, 0])
                natSyno.append(liste1.iloc[carSpec, 1])
                idNom.append(liste1.iloc[carSpec, 2])
                natNom.append('')
                val800.append(liste1.iloc[carSpec,3] * 2)
                carSpec += 1
            if carSpec == nbLgnLynst:
                carSpec = 0
                colmn0 += 1
                
        elif liste1.iloc[colmn0, 2] == liste1.iloc[colmn2, 0]:
            idNom.append(liste1.iloc[colmn0, 0])
            natNom.append(liste1.iloc[colmn0, 1])
            syno.append(liste1.iloc[colmn0, 2])
            natSyno.append(liste1.iloc[colmn2, 1])
            val800.append(liste1.iloc[colmn0,3] + liste1.iloc[colmn2,3])
            colmn0 += 1
            colmn2 = 0
        else:
            colmn2 += 1
            if colmn2 > nbLgnLynst :
                print("INNATENDU")
                
        if colmn0 == len(liste1) :
            break

    products_list = (idNom, natNom, syno, natSyno, val800)
    snsDbl800 = pd.DataFrame (products_list).transpose()
    snsDbl800.columns = ['IdNom','NatNom','Syno','natSyno', 'val800']
    global snsDbl800Tri
    snsDbl800Tri = snsDbl800.sort_values('val800', ascending = False)
    print(snsDbl800Tri)
    
varAlpha = 0
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
totalDf = pd.DataFrame()

#allInitialColmns(alphabet[0])
for loop in range(len(alphabet)):
    
     print("pOrdAlphabtq")
     pOrdAlphbtq(alphabet[varAlpha])
     global gobelSYN
     gobelSYN = globalInitial
     print(gobelSYN)
     print("gobelSYN")
     
     print("passageALaMachine")
     passageALaMachine(gobelSYN)
     ensMotAvcSynos2 = listeMotPrecise
     
     ecraseDoublonEtMoyenniseVal(ensMotAvcSynos2)
     totalDf = pd.concat([totalDf, snsDbl800Tri])
     print('TotalDf :'+totalDf)
     
     varAlpha += 1