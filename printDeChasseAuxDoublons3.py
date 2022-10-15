# -*- coding: utf-8 -*-
"""
Created on Tue May 31 23:31:19 2022

@author: Max-Louis
"""

import pandas as pd

idnomaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\idnomAzInit.csv')
listeSynoaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\lystazInit.csv')

var = 0
varAz = 0

liAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

boucleIf = ['if', 'elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','elif','else']

fichier = open("data10.txt", "a")

for loop in range(26):
    fichier.write("\t"+boucleIf[varAz] + " initIdnIdn[varIdnIdn] == '"+liAlphabet[varAz]+"': \n")
    for initGroup in range(26):
        fichier.write("\t \t"+boucleIf[var]+" initIdnLys[variable] == '"+ liAlphabet[var] + "': \n \t \t \t if all"+ liAlphabet[varAz] +".iloc[var1, 0] == all"+ liAlphabet[var] +"1.iloc[var2, 2]: \n \t \t \t \t if all"+ liAlphabet[var] +"1.iloc[var1, 0] == all"+ liAlphabet[varAz] +".iloc[var2, 2]: \n \t \t \t \t \t mot1.append(all"+ liAlphabet[varAz] +".iloc[var2, 2]) \n \t \t \t \t \t mot2.append(all"+ liAlphabet[var] +"1.iloc[var1, 2]) \n \t \t \t \t \t booleenDoublon = True \n \t \t \t \t \t doublon.append(booleenDoublon) \n \t \t \t \t \t val800.append(all"+ liAlphabet[var] +"1.iloc[var1, 3] + all"+ liAlphabet[varAz] +".iloc[var2, 3]) \n \t \t \t \t \t variable += 1 \n \t \t \t \t \t var1 += 1 \n \t \t \t \t \t var2 = 0 \n \t \t \t \t \t varIdnIdn += 1 \n \t \t \t \t \t print(alla.iloc[var2, 2]) \n \t \t \t \t else: \n \t \t \t \t \t var2 += 1 \n")
        var += 1
    varAz += 1
    var = 0

fichier.close

with open("data10.txt", "r") as fichier:
	print(fichier.read())