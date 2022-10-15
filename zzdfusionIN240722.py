# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:13:46 2022

@author: Max-Louis
"""

import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzAlphNb.csv')

prec = 0
suiv = 1
var = 0
ttl = len(df)

dfusionIN = []
dfusionName = []

stockIN = []
stockName = []

while suiv != ttl:

    
    if df.iloc[prec, 0] <= df.iloc[suiv,0]:
        print('<=')
        
        dfusionIN.append(df.iloc[prec,0])
        dfusionName.append(df.iloc[prec,1])
        
        var += 1
        if var == len(df):
            print('var == len(df)')
    
    else:
        print('>')
        
        stockIN.append(df.iloc[prec,0])
        stockName.append(df.iloc[prec,1])
        
        var += 1
        if var1 == len(df1):
            print('var == len(df)')
            
            while var != len(df):
                dfusionIN.append(df.iloc[var,0])
                dfusionName.append(df.iloc[var,1])
                var += 1
                
        print('var1 = ' + str(var1))
        
    var2 = var + var1