# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 18:13:23 2022

@author: Max-Louis
"""
import pandas as pd

sans = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/retriCrctrZz1.csv')
carSpec = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/retriCrctrZzCarSpec1.csv')

ttl = len(sans) + len(carSpec)

varSans = 0
varCS = 0

liName = []
liIdN = []

termine = False

while termine == False:
#for loop in range (500):
    if varSans == len(sans):
        print('varSans == len(sans)')
        
        if varSans + varCS == ttl:
            print('varSans + varCS == ttl')
            termine == True
        
        liName.append(carSpec.iloc[varCS,1])
        liIdN.append(carSpec.iloc[varCS,0])
        
        varCS += 1
        print('varCS = ' + str(varCS))
        
    elif varCS == len(carSpec):
        print('varCS == len(carSpec)')
        
        if varSans + varCS == ttl:
            print('varSans + varCS == ttl')
            termine == True
        
        liName.append(sans.iloc[varSans,1])
        liIdN.append(sans.iloc[varSans,0])
        
        varSans += 1
        print('varSans = ' + str(varSans))
        
    
    elif sans.iloc[varSans,0] < carSpec.iloc[varCS,0]:
        print(sans.iloc[varSans,0] + ' < ' + carSpec.iloc[varCS,0])
        
        liName.append(sans.iloc[varSans,1])
        liIdN.append(sans.iloc[varSans,0])
        
        varSans += 1
        print('varSans = ' + str(varSans))
        
    elif sans.iloc[varSans,0] > carSpec.iloc[varCS,0]:
        print(sans.iloc[varSans,0] +' > '+ carSpec.iloc[varCS,0])
        
        liName.append(carSpec.iloc[varCS,1])
        liIdN.append(carSpec.iloc[varCS,0])
        
        varCS += 1
        print('varCS = ' + str(varCS))
    
    else:
        print('issue imprévue')
        if sans.iloc[varSans,0] == carSpec.iloc[varCS,0]:
            print('==')
        break

plist = (liName, liIdN)
df = pd.DataFrame(plist).transpose()
df.columns = ['liName','liIdN']