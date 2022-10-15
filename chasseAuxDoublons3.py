# -*- coding: utf-8 -*-
"""
Created on Mon May 30 22:41:50 2022

@author: Max-Louis
"""

import pandas as pd

idnomaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\idnomAzInit.csv')
listeSynoaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\lystazInit.csv')

variable = 0
varIdnIdn = 0
variable1 = 1
var1 = 0
var2 = 0

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
initIdnLys = idnomaz['InitLyS']

idNom2 = listeSynoaz['IdNom']
listeSyno2 = listeSynoaz['listeSyno']
val4002 = listeSynoaz['val400']
initLysIdn = listeSynoaz['InitId']
initLysLys = listeSynoaz['InitLyS']

val800 = []
doublon = []
mot1 = []

mot2 = []

booleenDoublon = False

prec = ''
suiv = ''

while variable <= 382550:
    #a
        if variable < 36615 :
            if initIdnLys[variable] == 'a':
                if alla.iloc[var1, 0] == alla1.iloc[var2, 2]:
                    if alla1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(alla1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(alla1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'b':
                if alla.iloc[var1, 0] == allb1.iloc[var2, 2]:
                    if allb1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(allb1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(allb1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'c':
                if alla.iloc[var1, 0] == allc1.iloc[var2, 2]:
                    if allc1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(allc1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(allc1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'd':
                if alla.iloc[var1, 0] == alld1.iloc[var2, 2]:
                    if alld1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(alld1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(alld1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'e':
                if alla.iloc[var1, 0] == alle1.iloc[var2, 2]:
                    if alle1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(alle1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(alle1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'f':
                if alla.iloc[var1, 0] == allf1.iloc[var2, 2]:
                    if allf1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(allf1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(allf1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'g':
                if alla.iloc[var1, 0] == allg1.iloc[var2, 2]:
                    if allg1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(allg1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(allg1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'h':
                if alla.iloc[var1, 0] == allh1.iloc[var2, 2]:
                    if allh1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(allh1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(allh1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'i':
                if alla.iloc[var1, 0] == alli1.iloc[var2, 2]:
                    if alli1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(alli1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(alli1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'j':
                if alla.iloc[var1, 0] == allj1.iloc[var2, 2]:
                    if allj1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(allj1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(allj1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'k':
                if alla.iloc[var1, 0] == allk1.iloc[var2, 2]:
                    if allk1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(allk1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(allk1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'l':
                if alla.iloc[var1, 0] == alll1.iloc[var2, 2]:
                    if alll1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(alll1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(alll1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'm':
                if alla.iloc[var1, 0] == allm1.iloc[var2, 2]:
                    if allm1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(allm1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(allm1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            elif initIdnLys[variable] == 'n':
                if alla.iloc[var1, 0] == alln1.iloc[var2, 2]:
                    if alln1.iloc[var1, 0] == alla.iloc[var2, 2]:
                        mot1.append(alla[var2])
                        mot2.append(alln1[var1])
                        booleenDoublon = True
                        doublon.append(booleenDoublon)
                        val800.append(alln1.iloc[var1, 3] + alla.iloc[var2, 3])
                        variable += 1
                        var1 += 1
                        var2 = 0
                    else:
                        var2 += 1
                else:
                    var2 += 1
            #OPQRSTUVWXYZ
            
    #b
        elif variable < 59728 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('b ' +  str(variable))
                prec = suiv
            variable += 1
    #c
        elif variable < 102214 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('c ' +  str(variable))
                prec = suiv
            variable += 1
    #d
        elif variable < 130406 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('d ' +  str(variable))
                prec = suiv
            variable += 1
    #e
        elif variable < 148547 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('e ' +  str(variable))
                prec = suiv
            variable += 1
    #f
        elif variable < 169525 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('f ' +  str(variable))
                prec = suiv
            variable += 1
    #g
        elif variable < 180965 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('g ' +  str(variable))
                prec = suiv
            variable += 1
    #h
        elif variable < 187993 :
           suiv = initIdnIdn[variable]
           if prec != suiv:
               print('h ' +  str(variable))
               prec = suiv
           variable += 1
    #i
        elif variable < 207629 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('i ' +  str(variable))
                prec = suiv
            variable += 1
    #j
        elif variable < 210535 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('j ' +  str(variable))
                prec = suiv
            variable += 1
    #k
        elif variable < 210811 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('k ' +  str(variable))
                prec = suiv
            variable += 1
    #l
        elif variable < 219367 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('l ' +  str(variable))
                prec = suiv
            variable += 1
    #m
        elif variable < 239704 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('m ' +  str(variable))
                prec = suiv
            variable += 1
    #n
        elif variable < 244872 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('n ' +  str(variable))
                prec = suiv
            variable += 1
    #o
        elif variable < 251646 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('o ' +  str(variable))
                prec = suiv
            variable += 1
    #p
        elif variable < 286343 :
           suiv = initIdnIdn[variable]
           if prec != suiv:
               print('p ' +  str(variable))
               prec = suiv
           variable += 1
    #q
        elif variable < 287632:
           suiv = initIdnIdn[variable]
           if prec != suiv:
               print('q ' +  str(variable))
               prec = suiv
           variable += 1
    #r
        elif variable < 313999 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('r ' +  str(variable))
                prec = suiv
            variable += 1
    #s
        elif variable < 352529 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('s ' +  str(variable))
                prec = suiv
            variable += 1
    #t
        elif variable < 371158 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('t ' +  str(variable))
                prec = suiv
            variable += 1
    #u
        elif variable < 372448 :
            suiv = initIdnIdn[variable]
            if prec != suiv:
                print('u ' +  str(variable))
                prec = suiv
            variable += 1
    #v
        elif variable < 381865:
           suiv = initIdnIdn[variable]
           if prec != suiv:
               print('v ' +  str(variable))
               prec = suiv
           variable += 1
    #w
        elif variable < 382004 :
             suiv = initIdnIdn[variable]
             if prec != suiv:
                 print('w ' +  str(variable))
                 prec = suiv
             variable += 1
    #x
        elif variable < 382040 :
             suiv = initIdnIdn[variable]
             if prec != suiv:
                 print('x ' +  str(variable))
                 prec = suiv
             variable += 1
    #y
        elif variable < 382119 :
             suiv = initIdnIdn[variable]
             if prec != suiv:
                 print('y ' +  str(variable))
                 prec = suiv
             variable += 1
    #z
        elif initIdnIdn[variable] == 'z' :
             suiv = initIdnIdn[variable]
             if prec != suiv:
                 print('z ' +  str(variable))
                 prec = suiv
             variable += 1
        else: print('error')