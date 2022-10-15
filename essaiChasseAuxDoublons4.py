# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 18:17:57 2022

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

while variable <= 382550:
	if initIdnIdn[varIdnIdn] == 'a': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if alla.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if alla.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if alla.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if alla.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if alla.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if alla.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if alla.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if alla.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if alla.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if alla.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if alla.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if alla.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if alla.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if alla.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if alla.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if alla.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if alla.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if alla.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if alla.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if alla.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if alla.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if alla.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if alla.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if alla.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if alla.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if alla.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == alla.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alla.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + alla.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'b': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allb.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allb.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allb.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allb.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allb.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allb.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allb.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allb.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allb.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allb.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allb.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allb.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allb.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allb.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allb.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allb.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allb.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allb.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allb.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allb.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allb.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allb.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allb.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allb.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allb.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allb.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allb.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allb.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allb.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'c': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allc.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allc.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allc.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allc.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allc.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allc.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allc.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allc.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allc.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allc.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allc.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allc.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allc.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allc.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allc.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allc.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allc.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allc.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allc.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allc.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allc.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allc.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allc.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allc.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allc.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allc.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allc.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allc.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allc.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'd': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if alld.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if alld.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if alld.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if alld.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if alld.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if alld.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if alld.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if alld.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if alld.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if alld.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if alld.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if alld.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if alld.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if alld.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if alld.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if alld.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if alld.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if alld.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if alld.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if alld.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if alld.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if alld.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if alld.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if alld.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if alld.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if alld.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == alld.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alld.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + alld.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'e': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if alle.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if alle.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if alle.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if alle.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if alle.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if alle.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if alle.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if alle.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if alle.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if alle.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if alle.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if alle.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if alle.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if alle.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if alle.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if alle.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if alle.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if alle.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if alle.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if alle.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if alle.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if alle.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if alle.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if alle.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if alle.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if alle.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == alle.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alle.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + alle.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'f': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allf.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allf.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allf.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allf.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allf.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allf.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allf.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allf.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allf.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allf.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allf.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allf.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allf.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allf.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allf.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allf.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allf.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allf.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allf.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allf.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allf.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allf.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allf.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allf.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allf.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allf.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allf.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allf.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allf.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'g': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allg.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allg.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allg.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allg.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allg.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allg.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allg.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allg.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allg.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allg.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allg.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allg.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allg.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allg.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allg.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allg.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allg.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allg.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allg.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allg.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allg.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allg.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allg.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allg.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allg.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allg.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allg.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allg.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allg.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'h': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allh.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allh.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allh.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allh.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allh.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allh.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allh.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allh.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allh.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allh.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allh.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allh.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allh.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allh.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allh.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allh.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allh.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allh.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allh.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allh.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allh.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allh.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allh.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allh.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allh.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allh.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allh.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allh.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allh.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'i': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if alli.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if alli.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if alli.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if alli.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if alli.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if alli.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if alli.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if alli.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if alli.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if alli.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if alli.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if alli.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if alli.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if alli.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if alli.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if alli.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if alli.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if alli.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if alli.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if alli.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if alli.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if alli.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if alli.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if alli.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if alli.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if alli.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == alli.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alli.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + alli.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'j': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allj.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allj.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allj.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allj.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allj.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allj.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allj.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allj.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allj.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allj.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allj.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allj.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allj.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allj.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allj.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allj.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allj.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allj.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allj.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allj.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allj.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allj.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allj.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allj.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allj.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allj.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allj.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allj.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allj.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'k': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allk.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allk.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allk.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allk.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allk.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allk.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allk.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allk.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allk.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allk.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allk.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allk.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allk.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allk.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allk.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allk.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allk.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allk.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allk.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allk.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allk.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allk.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allk.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allk.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allk.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allk.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allk.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allk.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allk.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'l': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if alll.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if alll.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if alll.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if alll.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if alll.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if alll.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if alll.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if alll.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if alll.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if alll.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if alll.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if alll.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if alll.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if alll.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if alll.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if alll.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if alll.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if alll.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if alll.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if alll.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if alll.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if alll.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if alll.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if alll.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if alll.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if alll.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == alll.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alll.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + alll.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'm': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allm.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allm.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allm.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allm.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allm.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allm.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allm.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allm.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allm.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allm.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allm.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allm.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allm.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allm.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allm.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allm.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allm.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allm.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allm.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allm.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allm.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allm.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allm.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allm.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allm.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allm.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allm.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allm.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allm.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'n': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if alln.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if alln.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if alln.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if alln.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if alln.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if alln.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if alln.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if alln.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if alln.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if alln.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if alln.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if alln.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if alln.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if alln.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if alln.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if alln.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if alln.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if alln.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if alln.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if alln.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if alln.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if alln.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if alln.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if alln.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if alln.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if alln.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == alln.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alln.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + alln.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'o': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allo.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allo.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allo.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allo.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allo.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allo.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allo.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allo.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allo.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allo.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allo.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allo.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allo.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allo.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allo.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allo.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allo.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allo.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allo.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allo.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allo.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allo.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allo.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allo.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allo.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allo.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allo.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allo.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allo.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'p': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allp.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allp.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allp.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allp.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allp.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allp.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allp.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allp.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allp.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allp.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allp.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allp.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allp.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allp.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allp.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allp.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allp.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allp.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allp.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allp.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allp.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allp.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allp.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allp.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allp.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allp.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allp.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allp.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allp.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'q': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allq.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allq.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allq.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allq.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allq.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allq.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allq.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allq.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allq.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allq.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allq.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allq.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allq.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allq.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allq.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allq.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allq.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allq.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allq.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allq.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allq.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allq.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allq.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allq.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allq.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allq.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allq.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allq.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allq.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'r': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allr.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allr.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allr.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allr.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allr.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allr.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allr.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allr.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allr.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allr.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allr.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allr.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allr.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allr.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allr.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allr.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allr.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allr.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allr.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allr.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allr.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allr.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allr.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allr.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allr.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allr.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allr.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allr.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allr.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 's': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if alls.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if alls.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if alls.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if alls.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if alls.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if alls.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if alls.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if alls.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if alls.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if alls.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if alls.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if alls.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if alls.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if alls.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if alls.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if alls.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if alls.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if alls.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if alls.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if alls.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if alls.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if alls.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if alls.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if alls.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if alls.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if alls.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == alls.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(alls.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + alls.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 't': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allt.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allt.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allt.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allt.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allt.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allt.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allt.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allt.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allt.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allt.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allt.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allt.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allt.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allt.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allt.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allt.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allt.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allt.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allt.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allt.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allt.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allt.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allt.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allt.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allt.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allt.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allt.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allt.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allt.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'u': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allu.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allu.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allu.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allu.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allu.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allu.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allu.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allu.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allu.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allu.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allu.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allu.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allu.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allu.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allu.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allu.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allu.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allu.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allu.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allu.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allu.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allu.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allu.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allu.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allu.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allu.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allu.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allu.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allu.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'v': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allv.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allv.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allv.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allv.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allv.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allv.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allv.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allv.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allv.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allv.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allv.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allv.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allv.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allv.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allv.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allv.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allv.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allv.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allv.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allv.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allv.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allv.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allv.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allv.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allv.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allv.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allv.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allv.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allv.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'w': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allw.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allw.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allw.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allw.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allw.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allw.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allw.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allw.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allw.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allw.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allw.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allw.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allw.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allw.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allw.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allw.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allw.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allw.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allw.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allw.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allw.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allw.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allw.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allw.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allw.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allw.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allw.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allw.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allw.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'x': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allx.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allx.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allx.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allx.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allx.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allx.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allx.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allx.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allx.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allx.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allx.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allx.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allx.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allx.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allx.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allx.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allx.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allx.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allx.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allx.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allx.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allx.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allx.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allx.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allx.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allx.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allx.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allx.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allx.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'y': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if ally.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if ally.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if ally.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if ally.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if ally.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if ally.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if ally.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if ally.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if ally.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if ally.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if ally.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if ally.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if ally.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if ally.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if ally.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if ally.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if ally.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if ally.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if ally.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if ally.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if ally.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if ally.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if ally.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if ally.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if ally.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if ally.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == ally.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(ally.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + ally.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	elif initIdnIdn[varIdnIdn] == 'z': 
	 	if initIdnLys[variable] == 'a': 
 	 	 	 if allz.iloc[var1, 0] == alla1.iloc[var2, 2]: 
 	 	 	 	 if alla1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alla1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alla1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'b': 
 	 	 	 if allz.iloc[var1, 0] == allb1.iloc[var2, 2]: 
 	 	 	 	 if allb1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allb1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allb1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'c': 
 	 	 	 if allz.iloc[var1, 0] == allc1.iloc[var2, 2]: 
 	 	 	 	 if allc1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allc1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allc1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'd': 
 	 	 	 if allz.iloc[var1, 0] == alld1.iloc[var2, 2]: 
 	 	 	 	 if alld1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alld1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alld1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'e': 
 	 	 	 if allz.iloc[var1, 0] == alle1.iloc[var2, 2]: 
 	 	 	 	 if alle1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alle1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alle1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'f': 
 	 	 	 if allz.iloc[var1, 0] == allf1.iloc[var2, 2]: 
 	 	 	 	 if allf1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allf1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allf1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'g': 
 	 	 	 if allz.iloc[var1, 0] == allg1.iloc[var2, 2]: 
 	 	 	 	 if allg1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allg1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allg1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'h': 
 	 	 	 if allz.iloc[var1, 0] == allh1.iloc[var2, 2]: 
 	 	 	 	 if allh1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allh1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allh1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'i': 
 	 	 	 if allz.iloc[var1, 0] == alli1.iloc[var2, 2]: 
 	 	 	 	 if alli1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alli1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alli1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'j': 
 	 	 	 if allz.iloc[var1, 0] == allj1.iloc[var2, 2]: 
 	 	 	 	 if allj1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allj1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allj1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'k': 
 	 	 	 if allz.iloc[var1, 0] == allk1.iloc[var2, 2]: 
 	 	 	 	 if allk1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allk1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allk1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'l': 
 	 	 	 if allz.iloc[var1, 0] == alll1.iloc[var2, 2]: 
 	 	 	 	 if alll1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alll1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alll1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'm': 
 	 	 	 if allz.iloc[var1, 0] == allm1.iloc[var2, 2]: 
 	 	 	 	 if allm1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allm1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allm1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'n': 
 	 	 	 if allz.iloc[var1, 0] == alln1.iloc[var2, 2]: 
 	 	 	 	 if alln1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alln1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alln1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'o': 
 	 	 	 if allz.iloc[var1, 0] == allo1.iloc[var2, 2]: 
 	 	 	 	 if allo1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allo1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allo1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'p': 
 	 	 	 if allz.iloc[var1, 0] == allp1.iloc[var2, 2]: 
 	 	 	 	 if allp1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allp1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allp1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'q': 
 	 	 	 if allz.iloc[var1, 0] == allq1.iloc[var2, 2]: 
 	 	 	 	 if allq1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allq1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allq1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'r': 
 	 	 	 if allz.iloc[var1, 0] == allr1.iloc[var2, 2]: 
 	 	 	 	 if allr1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allr1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allr1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 's': 
 	 	 	 if allz.iloc[var1, 0] == alls1.iloc[var2, 2]: 
 	 	 	 	 if alls1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(alls1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(alls1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 't': 
 	 	 	 if allz.iloc[var1, 0] == allt1.iloc[var2, 2]: 
 	 	 	 	 if allt1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allt1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allt1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'u': 
 	 	 	 if allz.iloc[var1, 0] == allu1.iloc[var2, 2]: 
 	 	 	 	 if allu1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allu1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allu1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'v': 
 	 	 	 if allz.iloc[var1, 0] == allv1.iloc[var2, 2]: 
 	 	 	 	 if allv1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allv1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allv1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'w': 
 	 	 	 if allz.iloc[var1, 0] == allw1.iloc[var2, 2]: 
 	 	 	 	 if allw1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allw1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allw1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'x': 
 	 	 	 if allz.iloc[var1, 0] == allx1.iloc[var2, 2]: 
 	 	 	 	 if allx1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allx1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allx1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'y': 
 	 	 	 if allz.iloc[var1, 0] == ally1.iloc[var2, 2]: 
 	 	 	 	 if ally1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(ally1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(ally1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
	 	elif initIdnLys[variable] == 'z': 
 	 	 	 if allz.iloc[var1, 0] == allz1.iloc[var2, 2]: 
 	 	 	 	 if allz1.iloc[var1, 0] == allz.iloc[var2, 2]: 
 	 	 	 	 	 mot1.append(allz.iloc[var2, 2]) 
 	 	 	 	 	 mot2.append(allz1.iloc[var1, 2]) 
 	 	 	 	 	 booleenDoublon = True 
 	 	 	 	 	 doublon.append(booleenDoublon) 
 	 	 	 	 	 val800.append(allz1.iloc[var1, 3] + allz.iloc[var2, 3]) 
 	 	 	 	 	 variable += 1 
 	 	 	 	 	 var1 += 1 
 	 	 	 	 	 var2 = 0 
 	 	 	 	 	 varIdnIdn += 1 
 	 	 	 	 	 print(alla.iloc[var2, 2]) 
 	 	 	 	 else: 
 	 	 	 	 	 var2 += 1 
