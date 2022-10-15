# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 14:51:39 2022

@author: Max-Louis

sentence = ""
for word in words_list:
    sentence += str(word) + "."
print(sentence)
"""
import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/projet_concept/bdd_az/deaazCSV.csv')
liCarSpec = ['à','â','ä','é','è','ê','ë','î','ï','ô','ö','ù','û','ü','ÿ','ç','-','.','\'']
carSpec = 0
boolCarSpec = False
idN = []

syno2 = []

df['listeSyno'] = df['listeSyno'].str.lower()

incr = 6

#for loop in range (len(df) - 1):
for loop in range (1):
    print(incr)
    boolCarSpec = False
    carSpec = 0
    print(df.iloc[incr,0])
    print(df.iloc[incr,2])
    
    while carSpec < 19:
        
        if liCarSpec[carSpec] in df.iloc[incr,0]:
            print('liCarSpec[carSpec] in df.iloc[incr,0]')
            print(df.iloc[incr,0])
            
            incrLetter = 0
            motidN = df.iloc[incr,0]
            incrStr = ""
            
            while len(incrStr) != len(motidN):
            
                while carSpec < 19 and liCarSpec[carSpec] in motidN[incrLetter] :
                    print(' while carSpec < 19 and liCarSpec[carSpec] in df.iloc[incr,0] ')
                    
                    boolCarSpec = True
                    
                    if carSpec <= 2:
                        
                        strg0 = df.iloc[incr,0].replace(liCarSpec[carSpec],'a')
                        
                    elif carSpec >= 3 and carSpec <= 6:
                        
                        strg0 = df.iloc[incr,0].replace(liCarSpec[carSpec],'e')
                        
                    elif carSpec >= 7 and carSpec <= 8:
                        
                        strg0 = df.iloc[incr,0].replace(liCarSpec[carSpec],'i')
                    
                    elif carSpec >= 9 and carSpec <= 10:
                        
                        strg0 = df.iloc[incr,0].replace(liCarSpec[carSpec],'0')
                        
                    elif carSpec >= 11 and carSpec <= 13:
                        
                        strg0 = df.iloc[incr,0].replace(liCarSpec[carSpec],'u')
                    
                    elif carSpec == 14:
                        
                        strg0 = df.iloc[incr,0].replace(liCarSpec[carSpec],'y')
                    
                    elif carSpec == 15:
                        
                        strg0 = df.iloc[incr,0].replace(liCarSpec[carSpec],'c')
                    
                    else:
                        
                        strg0 = df.iloc[incr,0].replace(liCarSpec[carSpec],' ')
                        
                    carSpec += 1
                
        carSpec += 1
        
    if boolCarSpec == False:
        
        strg0 = df.iloc[incr,0]
        
    carSpec = 0
    
    while carSpec < 19:
        #print(carSpec)
        
        if liCarSpec[carSpec] in df.iloc[incr,2]:
            print('liCarSpec[carSpec] in df.iloc[incr,2]')
            print(df.iloc[incr,2])
            
            while carSpec < 19 and liCarSpec[carSpec] in df.iloc[incr,2] :
                print('carSpec < 19 and liCarSpec[carSpec] in df.iloc[incr,2]')
                
                boolCarSpec = True
                    
                if carSpec <= 2:
                    print('carSpec <= 2')
                    
                    strg2 = df.iloc[incr,2].replace(liCarSpec[carSpec],'a')
                    print(strg2)
                    
                elif carSpec >= 3 and carSpec <= 6:
                    #print('carSpec >= 3 and carSpec <= 6')
                    #print('carSpec = ' + str(carSpec))
                    #print('liCarSpec[carSpec] = ' + str(liCarSpec[carSpec]))
                    #print('incr = ' + str(incr))
                        
                    strg2 = df.iloc[incr,2].replace(str(liCarSpec[carSpec]),'e')
                        
                elif carSpec >= 7 and carSpec <= 8:
                        
                    strg2 = df.iloc[incr,2].replace(liCarSpec[carSpec],'i')
                    
                elif carSpec >= 9 and carSpec <= 10:
                        
                    strg2 = df.iloc[incr,2].replace(liCarSpec[carSpec],'0')
                        
                elif carSpec >= 11 and carSpec <= 13:
                        
                    strg2 = df.iloc[incr,2].replace(liCarSpec[carSpec],'u')
                    
                elif carSpec == 14:
                        
                    strg2 = df.iloc[incr,2].replace(liCarSpec[carSpec],'y')
                    
                elif carSpec == 15:
                        
                    strg2 = df.iloc[incr,2].replace(liCarSpec[carSpec],'c')
                    
                else:
                        
                    strg2 = df.iloc[incr,2].replace(liCarSpec[carSpec],' ')
                
                carSpec += 1
                
        carSpec += 1
    
    if boolCarSpec == False:
        
        strg2 = df.iloc[incr,2]
    
    idN.append(strg0)
    syno2.append(strg2)
    print(strg0)
    print(strg2)
    
    incr += 1

natN = df['NatNom']
val400 = df['val400']

        
        