# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 18:28:28 2022

@author: Max-Louis
"""

import pandas as pd

idnomaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\idnomAzInit.csv')
listeSynoaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\lystazInit.csv')

alphaB = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

variable = 0
varIdnIdn = 0
variable1 = 1
var0 = 0
var1 = 1

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

tousa = pd.concat([alla, alla1])
tousb = pd.concat([allb, allb1])
tousc = pd.concat([allc, allc1])
tousd = pd.concat([alld, alld1])
touse = pd.concat([alle, alle1])
tousf = pd.concat([allf, allf1])
tousg = pd.concat([allg, allg1])
toush = pd.concat([allh, allh1])
tousi = pd.concat([alli, alli1])
tousj = pd.concat([allj, allj1])
tousk = pd.concat([allk, allk1])
tousl = pd.concat([alll, alll1])
tousm = pd.concat([allm, allm1])
tousn = pd.concat([alln, alln1])
touso = pd.concat([allo, allo1])
tousp = pd.concat([allp, allp1])
tousq = pd.concat([allq, allq1])
tousr = pd.concat([allr, allr1])
touss = pd.concat([alls, alls1])
toust = pd.concat([allt, allt1])
tousu = pd.concat([allu, allu1])
tousv = pd.concat([allv, allv1])
tousw = pd.concat([allw, allw1])
tousx = pd.concat([allx, allx1])
tousy = pd.concat([ally, ally1])
tousz = pd.concat([allz, allz1])

shapea = tousa.shape
shapeb = tousb.shape
shapec = tousc.shape
shaped = tousd.shape
shapee = touse.shape
shapef = tousf.shape
shapeg = tousg.shape
shapeh = toush.shape
shapei = tousi.shape
shapej = tousj.shape
shapek = tousk.shape
shapel = tousl.shape
shapem = tousm.shape
shapen = tousn.shape
shapeo = touso.shape
shapep = tousp.shape
shapeq = tousq.shape
shaper = tousr.shape
shapes = touss.shape
shapet = toust.shape
shapeu = tousu.shape
shapev = tousv.shape
shapew = tousw.shape
shapex = tousx.shape
shapey = tousy.shape
shapez = tousz.shape

idNom = []
liSyn = []
val800 = []
doublon = []
booleenDoublon = False

while var0 <= 36614:
    if tousa.iloc[var0, 0] == tousa.iloc[var1, 2]:
        if tousa.iloc[var1, 0] == tousa.iloc[var0, 2]:
            idNom.append(tousa.iloc[var1,0])
            liSyn.append(tousa.iloc[var0,0])
            booleenDoublon = True 
            doublon.append(booleenDoublon) 
            val800.append(alla1.iloc[var0, 3] + alla.iloc[var1, 3]) 
            variable += 1 
            var0 += 1 
            var1 = 0
        else:
            var1 += 1
    else:
        var1 += 1
        if var1 >= 36615:
            var0 += 1
            var1 = 0
    print(var0)