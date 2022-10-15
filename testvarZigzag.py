# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 00:42:10 2022

@author: Max-Louis
"""

import random

total = 382550

espion = random.randrange(0,382550)
print('espion = ' + str(espion))

def moduloMoitie(valeur):
    
    global moitie
    moitie = int((valeur - (valeur % 2)) / 2)

moduloMoitie(total)

traqueur = moitie
print('traqueur = '+ str(traqueur))
capacite = 0

plusHaut = 382550
plusBas = 0


comptageBoucle = 0

while traqueur != espion:
    print('--- DEBUT DE BOUCLE ---')
    print(' BOUCLE NUMERO = ' + str(comptageBoucle))
    
    
    if traqueur < espion:
        print('traqueur < espion')
        
        plusBas = traqueur
        print('plusBas = ' + str(plusBas))
        
        print('espion = ' + str(espion))
        
        print('distance traqueur espion = ' + str(traqueur - espion))
        
    elif traqueur > espion:
        print('traqueur > espion')
        
        plusHaut = traqueur
        print('plusHaut = ' + str(plusHaut))
        
        print('espion = ' + str(espion))
        
        print('distance traqueur espion = ' + str(traqueur - espion))
    else:
        print('espion introuvable')
        
    diffPhPb = plusHaut - plusBas
    if diffPhPb < 2:
        print('ERREUR: plusHAUT et plusBAS se rejoignent')
    print('diffPhPb = ' + str(diffPhPb))
    
    traqueur = plusBas + int((diffPhPb -(diffPhPb % 2))/2)
    print('traqueur = plusBas + int(diffPhPb -(diffPhPb % 2)/2)')
    print('Traqueur apres formule = ' + str(traqueur))
    print('--- FIN DE BOUCLE ---')
    if espion == traqueur:
        print('espion == traqueur')
        capacite += 1
        print('LE TRAQUEUR A TROUVE L\'ESPION A LA BOUCLE NUMERO ' + str(comptageBoucle))
    comptageBoucle += 1
    