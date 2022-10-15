# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 04:33:58 2022

@author: Max-Louis
"""

import pandas as pd

dzli6L = pd.read_csv(r'C:/Users/Max-Louis/li6Lsv.csv')
dzli6LInv = pd.read_csv(r'C:/Users/Max-Louis/li6LsvInv.csv')

idN = []
natN = []
syno = []
natS = []
val800 = []

def moduloMoitie(valeur):
    
    global moitie
    moitie = int((valeur - (valeur % 2)) / 2)
    
    global unQuart
    unQuart = int((moitie - (moitie % 2)) / 2)
    
    global troisQuart
    troisQuart = int((moitie - (moitie % 2)) / 2) + moitie
    
def ternaire(valeur):
    
    global unTiers
    unTiers = int((valeur - (valeur % 3)) / 3)
    
    global deuxTiers
    deuxTiers = unTiers + unTiers
    
# la longueur de la liste chez IN et SYN sont la meme car la bdd est la mm    
totalIN = len(dzli6L)

moduloMoitie(totalIN)
print(moitie)

un = unQuart

deux = moitie

trois = troisQuart

plusBas = 0
plusHaut = totalIN

espion = 0

nbDbl = 0

liPotentielsDoublons = []

while espion < totalIN:
        
    diffPhPb = plusHaut - plusBas
    if diffPhPb == 1:
            
        idN.append(dzli6L.iloc[espion,0])
        natN.append(dzli6L.iloc[espion,1])
        syno.append(dzli6L.iloc[espion,2])
        natS.append('')
        val800.append(dzli6L.iloc[espion,3] * 2)
        
        espion += 1
        deux = moitie
        
    if dzli6L.iloc[espion,4] == dzli6LInv.iloc[deux,5]:
        
        liPotentielsDoublons.append[dzli6L.iloc[espion,4]]
        totalINDbl =  len(liPotentielsDoublons)
        
        plusHautDbl = totalINDbl
        plusBasDbl = 0
        deuxDbl = int((totalINDbl - (totalINDbl % 2)) / 2)
        unDbl = int((deuxDbl - (deuxDbl % 2)) / 2)
        troisDbl = deuxDbl + unDbl 
        espionDbl = 0
        
        solution = False
        
        while solution == False:
            print('while espion')
            
            diffPhPbDbl = plusHautDbl - plusBasDbl
            
            if diffPhPbDbl == 1:
                
                idN.append(dzli6L.iloc[espion,0])
                natN.append(dzli6L.iloc[espion,1])
                syno.append(dzli6L.iloc[espion,2])
                natS.append(dzli6L.iloc[deux,1])
                val800.append(dzli6L.iloc[deux,3] + dzli6L.iloc[espion,3])
                espion += 1
                deuxDbl = moitie
                solution == True
                break
                print('break')
                
            if dzli6L.iloc[espion,4] == liPotentielsDoublons[deuxDbl]:
                
                #doublon, ligne a ignorer, espion incr
                nbDbl += 1
                espion += 1
                solution == True
                break
                print('break')
                print('Nb de doublon trouve = ' + str(nbDbl))
                
            elif dzli6L.iloc[espion,4] < liPotentielsDoublons[unDbl]:
                    
                plusHautDbl = unDbl
                
            elif dzli6L.iloc[espion,4] < liPotentielsDoublons[deuxDbl] and dzli6L.iloc[espion,4] > liPotentielsDoublons[unDbl]:
                
                plusBasDbl = unDbl
                plusHautDbl = deuxDbl
            
            elif dzli6L.iloc[espion,4] > liPotentielsDoublons[deuxDbl] and dzli6L.iloc[espion,4] < liPotentielsDoublons[troisDbl]:
                
                plusBasDbl = deuxDbl
                plusHautDbl = troisDbl
            
            elif dzli6L.iloc[espion,4] > liPotentielsDoublons[troisDbl]:
                
                plusBasDbl = troisDbl
            
            deuxDbl = plusBasDbl + int((diffPhPbDbl -(diffPhPbDbl % 2))/2)
            unDbl = plusBasDbl + int((deuxDbl - (deuxDbl % 2)) / 2)
            troisDbl = plusBasDbl + deuxDbl + unDbl 
            print('espion = ' + str(espion))
            print('deuxDbl = ' + str(deuxDbl))
            
    elif dzli6L.iloc[espion,4] < dzli6LInv.iloc[un,5]:
            
        plusHaut = un
            
    elif dzli6L.iloc[espion,4] < dzli6LInv.iloc[deux,5] and dzli6L.iloc[espion,4] > dzli6LInv.iloc[un,5]:
        
        plusBas = un
        plusHaut = deux
    
    elif dzli6L.iloc[espion,4] > dzli6LInv.iloc[deux,5] and dzli6L.iloc[espion,4] < dzli6LInv.iloc[trois,5]:
        
        plusBas = deux
        plusHaut = trois
    
    elif dzli6L.iloc[espion,4] > dzli6LInv.iloc[trois,5]:
        
        plusBas = trois
    
    #deux = traqueur
    deux = plusBas + int((diffPhPb -(diffPhPb % 2))/2)
    un = plusBas + int((deux - (deux % 2)) / 2)
    trois = plusBas + deux + un
    
    print('espion = ' + str(espion))
    print('traqueur = ' + str(deux))