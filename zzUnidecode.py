# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 03:11:09 2022

@author: Max-Louis
"""
import pandas as pd
import unidecode 

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzAlphNb.csv')

idN0 = []
natN = []
syno2 = []
val400 = []
apparu = False
var = 0

while var != (382551):
    
    undcdIN = unidecode.unidecode(df.iloc[var,0])
    
    if '-' in undcdIN:
        txt = str(undcdIN).replace('-',' ')
        idN0.append(txt)
        apparu = True
        
    elif '.' in undcdIN:
        txt = str(undcdIN).replace('.',' ')
        idN0.append(txt)
        apparu = True
    
    else:
        if apparu == False:
            idN0.append(undcdIN)
    apparu = False
    natN.append(df.iloc[var,1])
    
    undcdSYN = unidecode.unidecode(df.iloc[var,2])
    
    if '-' in undcdSYN:
        txt = str(undcdSYN).replace('-',' ')
        syno2.append(txt)
        apparu = True
        
    elif '.' in undcdSYN:
        txt = str(undcdSYN).replace('.',' ')
        syno2.append(txt)
        apparu = True
    
    else:
        if apparu == False:
            syno2.append(undcdSYN)
            
    
    val400.append(df.iloc[var,3])
    
    print(unidecode.unidecode(df.iloc[var,0]))
    apparu = False
    var += 1
    print(var)
    
plist = (idN0, natN, syno2, val400)
df = pd.DataFrame(plist).transpose()
df.columns = ['idN0','natN', 'syno2', 'val400']
df.to_csv('zzUnidecode2.csv', index = False)