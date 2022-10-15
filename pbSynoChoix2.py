# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 13:45:45 2022

@author: Max-Louis
"""

import pandas as pd

deaazz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')
#works
del deaazz['placeSyno']

deaaz = pd.DataFrame(deaazz)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def researchGlobalInitial(initial,column):
    
    researchWord = deaaz[deaaz[column].str.match(initial)]

    nbLignes = len(researchWord)
    
    var = 0

    idNom = []
    natNom = []
    listeSyno = []
    val400 = []
    
    for loop in range(nbLignes):
        idNom.append(researchWord.iloc[var, 0])
        natNom.append(researchWord.iloc[var, 1])
        listeSyno.append(researchWord.iloc[var, 2])
        val400.append(researchWord.iloc[var, 3])
        var += 1
        
    products_list = (idNom, natNom, listeSyno, val400)
    global globalInitial
    globalInitial = pd.DataFrame (products_list).transpose()
    globalInitial.columns = ['IdNom','NatNom','Syno','val400']

def research(string,column):
    
    researchWord = deaaz[deaaz[column].str.contains(string)]

    nbLignes = len(researchWord)
    
    nbLettre = []

    var = 0
    
    if column == 'IdNom':
        for loop in range(nbLignes):
            nbLettre.append(len(researchWord.iloc[var, 0]))
            var += 1
        
    elif column == 'listeSyno':
        for loop in range(nbLignes):
            nbLettre.append(len(researchWord.iloc[var, 2]))
            var += 1
    else:
        print('ERREUR: PROBLEME SUR LE NOM DE LA COLONNE')
    
    #ajoute la msr du nb de lettre de chaque mot contenant word
    researchWord['nbLettr'] = nbLettre
    
    var = 0

    idNom = []
    natNom = []
    listeSyno = []
    val400 = []
    nbLettrString= len(string)
    
    #tri les mots dt la lgueur ne corrsp pas au modorgn
    for loop in range(nbLignes):
        if researchWord.iloc[var, 4] == nbLettrString:
            idNom.append(researchWord.iloc[var, 0])
            natNom.append(researchWord.iloc[var, 1])
            listeSyno.append(researchWord.iloc[var, 2])
            val400.append(researchWord.iloc[var, 3])
        var += 1
        
    products_list = (idNom, natNom, listeSyno, val400)
    global modorgn
    modorgn = pd.DataFrame (products_list).transpose()
    modorgn.columns = ['IdNom','NatNom','Syno','val400']



def ecraseDoublonEtMoyenniseVal(liste1, liste2):
    idNom = []
    natNom = []
    syno = []
    natSyno = []
    val800 = []
    colmn0 = 0
    colmn2 = 0
    carSpec = 0

    nbLgnLynst = len(liste2)

    while True :
        
        if len(liste1) == 0:
            while nbLgnLynst > carSpec:
                syno.append(liste2.iloc[carSpec, 0])
                natSyno.append(liste2.iloc[carSpec, 1])
                idNom.append(liste2.iloc[carSpec, 2])
                natNom.append('')
                val800.append(liste2.iloc[carSpec,3] * 2)
                carSpec += 1
            if carSpec == nbLgnLynst:
                carSpec = 0
                colmn0 += 1
        
        elif len(liste2) == 0:
            while len(liste1) > carSpec:
                idNom.append(liste1.iloc[carSpec, 0])
                natNom.append(liste1.iloc[carSpec, 1])
                syno.append(liste1.iloc[carSpec, 2])
                natSyno.append('')
                val800.append(liste1.iloc[carSpec,3] * 2)
                carSpec += 1
            if carSpec == len(liste1):
                carSpec = 0
                colmn0 += 1
                
        elif liste1.iloc[colmn0, 2] == liste2.iloc[colmn2, 0]:
            idNom.append(liste1.iloc[colmn0, 0])
            natNom.append(liste1.iloc[colmn0, 1])
            syno.append(liste1.iloc[colmn0, 2])
            natSyno.append(liste2.iloc[colmn2, 1])
            val800.append(liste1.iloc[colmn0,3] + liste2.iloc[colmn2,3])
            colmn0 += 1
            colmn2 = 0
        else:
            colmn2 += 1
            if colmn2 == nbLgnLynst :
                idNom.append(liste1.iloc[colmn0, 0])
                natNom.append(liste1.iloc[colmn0, 1])
                syno.append(liste1.iloc[colmn0, 2])
                natSyno.append('')
                val800.append(liste1.iloc[colmn0,3] * 2)
                colmn0 += 1
                colmn2 = 0
        
        if colmn0 == len(liste1) :
            break

    products_list = (idNom, natNom, syno, natSyno, val800)
    snsDbl800 = pd.DataFrame (products_list).transpose()
    snsDbl800.columns = ['IdNom','NatNom','Syno','natSyno', 'val800']
    global snsDbl800Tri
    snsDbl800Tri = snsDbl800.sort_values('val800', ascending = False)
    
# Debut de l'application des fonctions

def lister(string):
    research(string,'IdNom')
    liste1 = modorgn
    research(string,'listeSyno')
    liste2 = modorgn
    ecraseDoublonEtMoyenniseVal(liste1,liste2)

vari = 0
var1000 = 0
prec = 0
suiv = 1

varAlpha = 0

df = pd.DataFrame ()

def varColumn(nomColumn):
    researchGlobalInitial(alphabet[varAlpha], nomColumn)
    string = globalInitial.iloc[prec, 0]
    research(string,nomColumn)
    varAlpha += 1

def triParti (nomColumn, numeroListe):
    global varAlpha
    varAlpha = 0
    for loop in range(len(alphabet)):
        researchGlobalInitial(alphabet[varAlpha], nomColumn)
        if researchGlobalInitial(prec, 0) != researchGlobalInitial(suiv, 0):
            string = globalInitial.iloc[prec, 0]
        research(string,nomColumn)
        global numeroListe
        numeroListe = modorgn
        
triParti('IdNom')
liste1 = numeroListe
triParti('Syno')
liste2 = numeroListe
ecraseDoublonEtMoyenniseVal(liste1, liste2)
    
for loop in range (len(deaaz)):
    if deaaz.iloc[prec, 0] != deaaz.iloc[suiv, 0]:
        string = deaaz.iloc[prec, 0]
        lister(string)
        df = pd.concat([df, snsDbl800Tri])
    prec = suiv
    suiv += 1
    vari += 1
    var1000 += 1
    if vari == 1000:
        print(var1000)
        vari = 0

#ptcsv = '.csv'
#snsDbl800Tri.to_csv(string+ptcsv, index = False)
"""
# Calcul relatif a l'emplacement de string dans la liste

ptcsv = '.csv'
var = 0

for loop in range(len(listeString)):
    lister(listeString.iloc[var, 2])
    dataNiv1 = str(listeString.iloc[var, 2])
    snsDbl800Tri.to_csv(dataNiv1+ptcsv, index = False)        
    var += 1


CONTINUER PB MEDIANE MOYENNE MIN MAX PLACE
les 4 synonymes d'un mot contenant 10 n'est pas en proportion d'un autre
mot en contenant 100, vise à se faire alors ici une proportion en fonction
de la place du modorgn sur le synonyme ainsi que du val800 min max moyenne
mediane. Il semble evident que la mediane sera plus representative que la
 moyenne ne prenant pas en compte les valeurs trop dispersées
 
def reciprocite():
    mean800 = snsDbl800Tri['val800'].mean()
    var = 0
    nbLignes = len(snsDbl800Tri)
    for loop in range(nbLignes):
        synoNiv1 = lister(snsDbl800Tri.iloc[var, 2])
        nbLgnNiv1 = len(synoNiv1)
        incrNumModorgn = 0
        placeModorgn = 0
        moy = synoNiv1['val800'].mean()
        mini = min(synoNiv1['val800'])
        maxi = max(synoNiv1['val800'])
        for loop in range(nbLgnNiv1):
            if synoNiv1[incrNumModorgn, 2] == string:
                placeModorgn.append(incrNumModorgn)
            else:
                incrNumModorgn += 1
        proportionPlace = (placeModorgn/nbLgnNiv1)*100
    """