# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 16:25:43 2022

@author: Max-Louis
"""

import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/projet_concept/bdd_az/deaazCSV.csv')
liCarSpec = ['à','â','ä','é','è','ê','ë','î','ï','ô','ö','ù','û','ü','ÿ','ç','-','.','\'']
carSpec = 0
boolCarSpec = False
idN = []

syno2 = []

df['listeSyno'] = df['listeSyno'].str.lower()

incr = 0

for loop in range (len(df) - 1):
#for loop in range (1000):
    
    boolCarSpec = False
    carSpec = 0
    
    string0 = str(df.iloc[incr,0])
    
    while carSpec < 19:
        
        if liCarSpec[carSpec] in string0:
                
                boolCarSpec = True
                
                if carSpec <= 2:
                    
                    string0 = string0.replace(liCarSpec[carSpec],'a')
                    carSpec = 0
                    
                elif carSpec >= 3 and carSpec <= 6:
                    
                    string0 = string0.replace(liCarSpec[carSpec],'e')
                    carSpec = 0
                    
                elif carSpec >= 7 and carSpec <= 8:
                    
                    string0 = string0.replace(liCarSpec[carSpec],'i')
                    carSpec = 0
                    
                elif carSpec >= 9 and carSpec <= 10:
                    
                    string0 = string0.replace(liCarSpec[carSpec],'o')
                    carSpec = 0
                    
                elif carSpec >= 11 and carSpec <= 13:
                    
                    string0 = string0.replace(liCarSpec[carSpec],'u')
                    carSpec = 0
                    
                elif carSpec == 14:
                    
                    string0 = string0.replace(liCarSpec[carSpec],'y')
                    carSpec = 0
                    
                elif carSpec == 15:
                    
                    string0 = string0.replace(liCarSpec[carSpec],'c')
                    carSpec = 0
                    
                elif carSpec > 15:
                    
                    string0 = string0.replace(liCarSpec[carSpec],' ')
                    carSpec = 0
                    
                carSpec += 1
                #♣print(string0)
                
        carSpec += 1
        
    carSpec = 0
        
    string2 = str(df.iloc[incr,2])
        
    while carSpec < 19:
            
            if liCarSpec[carSpec] in string2:
                    
                    boolCarSpec = True
                    
                    if carSpec <= 2:
                        
                        string2 = string2.replace(liCarSpec[carSpec],'a')
                        carSpec = 0
                        
                    elif carSpec >= 3 and carSpec <= 6:
                        
                        string2 = string2.replace(liCarSpec[carSpec],'e')
                        carSpec = 0
                        
                    elif carSpec >= 7 and carSpec <= 8:
                        
                        string2 = string2.replace(liCarSpec[carSpec],'i')
                        carSpec = 0
                        
                    elif carSpec >= 9 and carSpec <= 10:
                        
                        string2 = string2.replace(liCarSpec[carSpec],'o')
                        carSpec = 0
                        
                    elif carSpec >= 11 and carSpec <= 13:
                        
                        string2 = string2.replace(liCarSpec[carSpec],'u')
                        carSpec = 0
                        
                    elif carSpec == 14:
                        
                        string2 = string2.replace(liCarSpec[carSpec],'y')
                        carSpec = 0
                        
                    elif carSpec == 15:
                        
                        string2 = string2.replace(liCarSpec[carSpec],'c')
                        carSpec = 0
                        
                    elif carSpec > 15:
                        
                        string2 = string2.replace(liCarSpec[carSpec],' ')
                        carSpec = 0
                        
                    carSpec += 1
                    #print(string2)
                    
            carSpec += 1
            
    idN.append(string0)
    syno2.append(string2)
    
    incr += 1
    print(incr)

natN = df['NatNom']
val400 = df['val400']


