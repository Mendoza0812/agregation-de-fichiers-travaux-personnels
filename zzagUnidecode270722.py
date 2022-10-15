# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 00:14:48 2022

@author: Max-Louis
"""

import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/zzUnidecode3.csv')
df1 = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/correspUnidecode2.csv')

var = 0

varsrt = 1
precSrt = 0
suivSrt = varsrt

idN = []
natN = []
syno2 = []
natS = []
val800 = []

naan = False

while var != (len(df) - 1):
#for loop in range (256):
    #print(' --- DEBUT DE BOUCLE ---')
        
    if df1.iloc[precSrt,2] == df1.iloc[suivSrt,2]:
        print('df1.iloc[precSrt,2] == df1.iloc[suivSrt,2]')
        
        varsrt += 1
        precSrt = suivSrt
        suivSrt = varsrt
            
    elif df.iloc[var].name > df1.iloc[varsrt,2]:
        print('df.iloc[var].name > df1.iloc[varsrt,2]')
                
        varsrt += 1
        precSrt = suivSrt
        suivSrt = varsrt
    
    elif df.iloc[var].name == df1.iloc[varsrt,2]:
        
        print('df.iloc[var].name == df1.iloc[varsrt,2]]')
        
        varsrt += 1
        precSrt = suivSrt
        suivSrt = varsrt
        
        var += 1
    
    elif df.iloc[var].name > df1.iloc[var,1]:
        print('df.iloc[var].name > df1.iloc[var,1]')
        
        var += 1
        
    elif df1.iloc[var,1] == 382551:
        print('df1.iloc[var,1] == 382551')
        
        idN.append(df.iloc[var,0])
        natN.append(df.iloc[var,1])
        syno2.append(df.iloc[var,2])
        natS.append('')
        val800.append(df.iloc[var,3] * 2)
            
        var += 1
            
            
    else:
        print('else')
        
        emplcDbln = int(df1.iloc[var,1])
    

        idN.append(df.iloc[var,0])
        natN.append(df.iloc[var,1])
        syno2.append(df.iloc[emplcDbln,0])
        natS.append(df.iloc[emplcDbln,1])
        val800.append(df.iloc[var,3] + df.iloc[emplcDbln,3])
        naan = False
        var += 1
    
    print(var)

plist = (idN, natN, syno2, natS, val800)
df2 = pd.DataFrame(plist).transpose()
df2.columns = ['idN', 'natN', 'syno2', 'natS','val800']
        
    
    