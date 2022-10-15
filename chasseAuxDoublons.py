# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:06:06 2022

@author: Max-Louis
"""

import pandas as pd

idnomaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\idnomAzInit.csv')
listeSynoaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\lystazInit.csv')

variable = 0
variable1 = 1

alla = idnomaz[idnomaz['IdNom'].str.startswith('a')]
allb = idnomaz[idnomaz['IdNom'].str.startswith('b')]
allc = idnomaz[idnomaz['IdNom'].str.startswith('c')]
alld = idnomaz[idnomaz['IdNom'].str.startswith('d')]
alle = idnomaz[idnomaz['IdNom'].str.startswith('e')]
allf = idnomaz[idnomaz['IdNom'].str.startswith('f')]
allg = idnomaz[idnomaz['IdNom'].str.startswith('g')]
allh = idnomaz[idnomaz['IdNom'].str.startswith('h')]
alli = idnomaz[idnomaz['IdNom'].str.startswith('i')]
allj = idnomaz[idnomaz['IdNom'].str.startswith('j')]
allk = idnomaz[idnomaz['IdNom'].str.startswith('k')]
alll = idnomaz[idnomaz['IdNom'].str.startswith('l')]
allm = idnomaz[idnomaz['IdNom'].str.startswith('m')]
alln = idnomaz[idnomaz['IdNom'].str.startswith('n')]
allo = idnomaz[idnomaz['IdNom'].str.startswith('o')]
allp = idnomaz[idnomaz['IdNom'].str.startswith('p')]
allq = idnomaz[idnomaz['IdNom'].str.startswith('q')]
allr = idnomaz[idnomaz['IdNom'].str.startswith('r')]
alls = idnomaz[idnomaz['IdNom'].str.startswith('s')]
allt = idnomaz[idnomaz['IdNom'].str.startswith('t')]
allu = idnomaz[idnomaz['IdNom'].str.startswith('u')]
allv = idnomaz[idnomaz['IdNom'].str.startswith('v')]
allw = idnomaz[idnomaz['IdNom'].str.startswith('w')]
allx = idnomaz[idnomaz['IdNom'].str.startswith('x')]
ally = idnomaz[idnomaz['IdNom'].str.startswith('y')]
allz = idnomaz[idnomaz['IdNom'].str.startswith('z')]

alla1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('a')]
allb1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('b')]
allc1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('c')]
alld1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('d')]
alle1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('e')]
allf1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('f')]
allg1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('g')]
allh1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('h')]
alli1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('i')]
allj1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('j')]
allk1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('k')]
alll1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('l')]
allm1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('m')]
alln1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('n')]
allo1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('o')]
allp1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('p')]
allq1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('q')]
allr1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('r')]
alls1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('s')]
allt1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('t')]
allu1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('u')]
allv1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('v')]
allw1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('w')]
allx1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('x')]
ally1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('y')]
allz1 = listeSynoaz[listeSynoaz['listeSyno'].str.startswith('z')]

idNom1 = idnomaz['IdNom']
listeSyno1 = idnomaz['listeSyno']
val4001 = idnomaz['val400']
initIdnIdn = idnomaz['InitId']
initIdnLys = idnomaz['InitLys']

idNom2 = listeSynoaz['IdNom']
listeSyno2 = listeSynoaz['listeSyno']
val4002 = listeSynoaz['val400']
initLysIdn = listeSynoaz['InitId']
initLysLys = listeSynoaz['InitLys']

val800 = []
doublon = []
ref = []
booleenDoublon = False

while variable <= 382550:
    while variable1 <= 382550:
        
        if initIdnIdn[variable] == 'a' :
            
            if idNom1[variable] == listeSyno2[variable1]:
                break
            
            else:
                variable1 += 1
                if variable1 > 382550:
                    print('pas de doublon')
                    booleenDoublon = False
                    doublon.append(booleenDoublon)
                    val800.append(val4001[variable]*2)
                    ref.append('NaN')
                    variable1 = 0
                    variable += 1
            
                
            if idNom2[variable1] == listeSyno1[variable]:
                print(idNom1[variable])
                print(listeSyno2[variable1])
                print(True)
                print(variable1)
                booleenDoublon = True
                doublon.append(booleenDoublon)
                val800.append(val4001[variable] + val4001[variable1])
                ref.append(variable1)
                variable += 1
                variable1 = 0
            else:
                variable1 += 1
                if variable1 > 382550:
            print('pas de doublon')
            booleenDoublon = False
            doublon.append(booleenDoublon)
            val800.append(val4001[variable]*2)
            ref.append(0)
            variable1 = 0
            variable += 1
    
moncsv1['val800'] = val800
moncsv1['doublon'] = doublon
moncsv1['reference'] = ref