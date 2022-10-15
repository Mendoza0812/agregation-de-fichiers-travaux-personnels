# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 20:20:49 2022

@author: Max-Louis
"""

import pandas as pd

df10 = pd.read_csv(r'C:/Users/Max-Louis/df10Ref.csv')

dfDists = pd.read_csv(r'C:/Users/Max-Louis/regroupDists270822.csv')

dfSyneurone = pd.read_csv( r'C:/Users/Max-Louis/df12svRef.csv')

dfNiveau3 = pd.read_csv(r'C:/Users/Max-Louis/dfNiveau3.csv')

dfNivMystere = pd.read_csv(r'C:/Users/Max-Louis/dfNiveauMystere.csv')

structureNiveau1ATerminer = pd.read_csv(r'C:/Users/Max-Louis/structureNiveau1ATerminer.csv')
motCible = 'bon'

nombreDeNouveauxMotsAjoutes = 0

def creation_RefDeMotCible_ListeDesSynonymesDuMotCible(motCible):
    
    global motCibleRef
    motCibleRef = str(motCible) + str(len(motCible))
    
    global listeMotCible
    listeMotCible = dfSyneurone[dfSyneurone['ref'].str.contains(motCibleRef)]

def affichageListeMotCible():
    
    print(listeMotCible)

def initiationDesListesStructurelles():
    
    global motsParcourusAuxSynonymesDejaStockes
    
    motsParcourusAuxSynonymesDejaStockes = []
    
    global motsParcourusAuxSynonymePasEncoreStockes
    
    motsParcourusAuxSynonymePasEncoreStockes = []

    
def filtrage_binome(numeroDeLigne):
    
    binome = df10.iloc[listeMotCible.iloc[numeroDeLigne,2]]
        
    global synonyme
        
    if motCible == binome.iloc[0]:
            
        synonyme = binome.iloc[1]
        
    else:
            
        synonyme = binome.iloc[0]
        
def filtrage_booleen(laValeur, laListe):
    
    rechercheTermine = False
    
    laListe.sort()
    
    plusBas = (0)
    
    if len(laListe) == 1:
        
        plusHaut = len(laListe)
    
    else:
        
        plusHaut = (len(laListe) - 1)
    
    nbDeBoucle = 0
    
    global estDansLaListeDesMotsParcourus
    
    global erreur
    erreur = False
    
    while rechercheTermine == False:
        
        nbDeBoucle += 1
        
        diffHautBas = plusHaut - plusBas
        sondeur = int(plusBas) + int((diffHautBas - (diffHautBas % 2)) / 2)
        
        if len(laListe) == 0 or laValeur > laListe[(len(laListe)-1)] or laValeur < laListe[0]:
            
            rechercheTermine = True
            
            estDansLaListeDesMotsParcourus = False
            
        elif nbDeBoucle >= 100:
            
            print('nbDeBoucle anormalement excessif: depasse 100')
            print('boucle concerne while rechercheTermine == False')
            print('fonction = sondeurDoublon')
            print('laValeur = ' + str(laValeur))
            print('laListe = ' + str(laListe))
            erreur = True
            break    
            
        elif diffHautBas == 1:
            #print('diffHB == 1')
          
            if laValeur != laListe[sondeur]:
                
                rechercheTermine = True
                
                estDansLaListeDesMotsParcourus = False
            
            elif laValeur == laListe[sondeur]:
                
                rechercheTermine = True
                
                estDansLaListeDesMotsParcourus = True
            
            else:
                
                print('ERREUR INNATENDUE LIGNE 136')
                break
            
        elif laValeur > laListe[sondeur]:
            #print('>')
                
            plusBas = sondeur
            
        elif laValeur < laListe[sondeur]:
            #print('<')
            
            plusHaut = sondeur
        
        elif laValeur == laListe[sondeur]:
            #print('==')
            
            rechercheTermine = True
            
            estDansLaListeDesMotsParcourus = True
        
        else:
            
            print('issue innatendue ligne 116')
            break
        


def ajouterDansLesListes(numeroDeLigne):
    
    motsParcourusAuxSynonymesDejaStockes.append(synonyme)
    
    global nombreDeNouveauxMotsAjoutes
    nombreDeNouveauxMotsAjoutes += 1

def transpositionDesListesEnTableau(plst):
    
    global dfMotCible
    dfMotCible = pd.DataFrame(plst)
    dfMotCible.columns = ['mots']

def miseEnStructure(motCible):
    
    creation_RefDeMotCible_ListeDesSynonymesDuMotCible(motCible)
    
    motsParcourusAuxSynonymePasEncoreStockes.append(motCible)
    
    for incrementeur in range (len(listeMotCible)):
        
        filtrage_binome(incrementeur)
        filtrage_booleen(synonyme,motsParcourusAuxSynonymePasEncoreStockes)
        if erreur == True:
            break
        else:
            if estDansLaListeDesMotsParcourus == False:
                ajouterDansLesListes(incrementeur)
    
    transpositionDesListesEnTableau(motsParcourusAuxSynonymesDejaStockes)
                
# MISE EN EXECUTION DU FICHIER EN DESSOUS DE CETTE LIGNE

niveauDeLaStructure = 0

initiationDesListesStructurelles()

filtrage_booleen(motCible,motsParcourusAuxSynonymePasEncoreStockes)

if estDansLaListeDesMotsParcourus == False:
    
    miseEnStructure(motCible)

# PROBLEME NON REPERE A PARTIR DES LIGNES EN DESSOUS = RESOLU
# nbDeBoucle anormalement excessif: depasse 100 = RESOLU

#dfMotCible = dfNivMystere

while nombreDeNouveauxMotsAjoutes != 0:
    
    nombreDeNouveausMotsAjoutes = 0
    
    dfMotCiblePrecedent = dfMotCible
    
    for incrementeur2 in range (len(dfMotCible)):
        
        motCible = dfMotCible.iloc[incrementeur2,0]
        
        filtrage_booleen(motCible,motsParcourusAuxSynonymePasEncoreStockes)
        
        print(incrementeur2)
        
        if estDansLaListeDesMotsParcourus == False:
            
            miseEnStructure(motCible)
        
    dfConcateneur = pd.concat([dfMotCiblePrecedent,dfMotCible], join ='inner', ignore_index = True)
