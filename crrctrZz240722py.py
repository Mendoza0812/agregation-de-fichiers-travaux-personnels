# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 00:10:04 2022

@author: Max-Louis
"""

import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/zzdfusionIN.csv')

var = 0
prec = 0
suiv = 1
gardeIN = []
gardeName = []

dfusionIN1 = []
dfusionName = []

while var != len(df):
    
    if df.iloc[prec,0] <= df.iloc[suiv,0]:
        gardeIN.append(df.iloc[prec, 0])
        gardeName.append(df.iloc[prec,1])
        
    elif df.iloc[prec,0] > df.iloc[suiv,0]:
        print(df.iloc[prec,1])
        print(df.iloc[suiv, 1])
        print('>')
        
        dfusionIN1.append(df.iloc[prec,0])
        dfusionName.append(df.iloc[prec,1])
        
    var += 1
    prec = suiv
    suiv += 1
"""

dzlian = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzAlphNb.csv')

liCarSpec = ['à','â','ä','é','è','ê','ë','î','ï','ô','ö','ù','û','ü','ÿ','ç','-','.']

var = 0

mtCarSpec = []
nameCarSpec = []

sans = []
nameSans = []

carSpec = 0
boolCarSpec = False

prec = 0
suiv = 1


while var < len(dzlian):
    
    while carSpec < 18:
        
        if liCarSpec[carSpec] in dzlian.iloc[var,0]:
            
            if boolCarSpec == False:
                
                mtCarSpec.append(dzlian.iloc[var,0])
                nameCarSpec.append(dzlian.iloc[var].name)
                boolCarSpec = True
        
        carSpec += 1
    
    if boolCarSpec == False:
        
        if var >= 2:
            if sans[prec] > sans[suiv]:
                print(sans[prec])
                print(sans[suiv])
                print('>')
                break
        
        sans.append(dzlian.iloc[var,0])
        nameSans.append(dzlian.iloc[var].name)
    
    var += 1
    print(var)
    carSpec = 0
    boolCarSpec = False
        
"""