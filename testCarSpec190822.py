# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 17:17:23 2022

@author: Max-Louis
"""
import pandas as pd

liCarSpec = ['à','â','ä','é','è','ê','ë','î','ï','ô','ö','ù','û','ü','ÿ','ç','-','.','\'']
carSpec = 0

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/projet_concept/bdd_az/deaazCSV.csv')
startsWithCarSpec = []

for incr in range (len(df) - 1):
    
    syno = df.iloc[incr,2]
    
    carSpec = 0
    
    while carSpec < 19:
        
        if liCarSpec[carSpec] == syno[0]:
            
            if syno != df.iloc[incr+1,2]:
                
                startsWithCarSpec.append(syno)
            
            if incr + 1 == len(df):
                
                if syno != df.iloc[incr+1,2]:
                    
                    startsWithCarSpec.append(df.iloc[incr+1,2])
        
        carSpec += 1
        
    print(incr)