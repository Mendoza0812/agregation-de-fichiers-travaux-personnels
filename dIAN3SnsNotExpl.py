# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 22:49:13 2022

@author: Max-Louis
"""

import pandas as pd

dzAlphNb = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzAlphNb.csv')
dzInvAlphNb = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzInvAlphNb.csv')

dzInvAlphNb = dzInvAlphNb[['listeSyno','NatNom','IdNom','val400','AlphNb']]

idN = []
natN = []
syno = []
natS = []
val800 = []

varCompSYN = 0
varCompIN = 0

for loop in range(28):
    
    compartimentSYN = dzInvAlphNb[dzInvAlphNb['AlphNb'] == varCompSYN]
    compartimentIN = dzAlphNb[dzAlphNb['AlphNb'] == varCompIN]
    
    liVarIN = []
    
    varSYN = 0
    varIN = 0
    
    while varSYN < len(compartimentSYN):
        
        if len(compartimentIN) == 0:
            print('if len(compartimentIN) == 0:')
            
            idN.append(compartimentSYN.iloc[varSYN,0])
            natN.append(compartimentSYN.iloc[varSYN,1])
            syno.append(compartimentSYN.iloc[varSYN,2])
            natS.append('')
            val800.append(compartimentSYN.iloc[varSYN,3] * 2)
            varSYN += 1
            print('varSYN if = ' + str(varSYN))
            varIN = 0
        
        elif compartimentIN.iloc[varIN,0] == compartimentSYN.iloc[varSYN,0]:
            print('elif compartimentIN.iloc[varIN,0] == compartimentSYN.iloc[varSYN,0]:')
            
            if compartimentIN.iloc[varIN,2] == compartimentSYN.iloc[varSYN,2]:
                print('elif compartimentIN.iloc[varIN,2] == compartimentSYN.iloc[varSYN,2]:')
                
                idN.append(compartimentIN.iloc[varIN,0])
                
                liVarIN.append(compartimentIN.iloc[varIN,0])
                
                natN.append(compartimentIN.iloc[varIN,1])
                syno.append(compartimentIN.iloc[varIN,2])
                natS.append(compartimentSYN.iloc[varSYN,1])
                val800.append(compartimentIN.iloc[varIN,3] + compartimentSYN.iloc[varIN,3])
                varSYN += 1
                print('varSYN elif =' + str(varSYN))
                varIN = 0
                
            else:
                
                varIN += 1
        else:
            
            varIN += 1
            
            precSYN = varSYN - 1

            suivSYN = varSYN
            print('varSYN else ='+ str(varSYN))
            
            if varIN == len(compartimentIN):
                print('if varIN == len(compartimentIN):')
                
                idN.append(compartimentSYN.iloc[varSYN,0])
                natN.append(compartimentSYN.iloc[varSYN,1])
                syno.append(compartimentSYN.iloc[varSYN,2])
                natS.append('')
                val800.append(compartimentSYN.iloc[varSYN,3] * 2)
                
                varSYN += 1
                varIN = 0
            
                if varSYN == len(compartimentSYN):
                    break
                    
                elif compartimentSYN.iloc[precSYN,0] == compartimentSYN.iloc[suivSYN,0]:
                    print('compartimentSYN.iloc[precSYN,0] == compartimentSYN.iloc[suivSYN,0]:')
                    
                    while compartimentSYN.iloc[precSYN,0] == compartimentSYN.iloc[suivSYN,0]:
                        
                        idN.append(compartimentSYN.iloc[varSYN,0])
                        natN.append(compartimentSYN.iloc[varSYN,1])
                        syno.append(compartimentSYN.iloc[varSYN,2])
                        natS.append('')
                        val800.append(compartimentSYN.iloc[varSYN,3] * 2)
                        
                        varSYN += 1
                        precSYN = varSYN - 1
                        suivSYN = varSYN
                        
                        print('varSYN ='+ str(varSYN))
                        
                        if varSYN == len(compartimentSYN):
                            print("varSYN == len(compartimentSYN)")
                            varSYN - 1
                            break
                    
    #Test pour savoir si tous les mots de la colonne IN ont ete faits, y compris les mots IN sans dbls            
    if len(liVarIN) < len(compartimentIN):
        print('len(liVarIN) < len(compartimentIN):')
        
        varIN = 0
        varSYN = 0
        
        while varIN < len(compartimentIN):
            print('while varIN < len(compartimentIN):')
            
            if compartimentIN.iloc[varIN,0] == compartimentSYN.iloc[varSYN,0]:
                print('if compartimentIN.iloc[varIN,0] == compartimentSYN.iloc[varSYN,0]:')
                
                if compartimentIN.iloc[varIN,2] == compartimentSYN.iloc[varSYN,0]:
                    print('if compartimentIN.iloc[varIN,2] == compartimentSYN.iloc[varSYN,2]:')
                 
                    varIN += 1
                    print(varIN)
                    varSYN = 0
                
                else:
                
                    varSYN += 1
            else:
                print('compartimentIN.iloc[varIN,0] != compartimentSYN.iloc[varSYN,0]')
                varSYN += 1
                
                precIN = varIN - 1
                
                suivIN = varIN
                print('varIN else ='+ str(varIN))
                
                if varSYN == len(compartimentSYN):
                    print('if varSYN == len(compartimentSYN):')
                    
                    idN.append(compartimentIN.iloc[varIN,0])
                    natN.append(compartimentIN.iloc[varIN,1])
                    syno.append(compartimentIN.iloc[varIN,2])
                    natS.append('')
                    val800.append(compartimentIN.iloc[varIN,3] * 2)
                    
                    varIN += 1
                    print(varIN)
                    varSYN = 0
                
                    if varIN == len(compartimentIN):
                        print('varIN == len(compartimentIN)')
                        break
                    
                    elif compartimentIN.iloc[precIN,0] == compartimentIN.iloc[suivIN,0]:
                        print('compartimentIN.iloc[precIN,0] == compartimentIN.iloc[suivIN,0]:')
                        
                        while compartimentIN.iloc[precIN,0] == compartimentIN.iloc[suivIN,0]:
                            print('while compartimentIN.iloc[precIN,0] == compartimentIN.iloc[suivIN,0]:')
                            
                            idN.append(compartimentIN.iloc[varIN,0])
                            natN.append(compartimentIN.iloc[varIN,1])
                            syno.append(compartimentIN.iloc[varIN,2])
                            natS.append('')
                            val800.append(compartimentIN.iloc[varIN,3] * 2)
                               
                            varIN += 1
                            precIN = suivIN - 1
                            suivIN = varIN
                            
                            print('varIN ='+ str(varIN))
                            
                            if varIN == len(compartimentIN):
                                print("varIN == len(compartimentIN)")
                                varIN - 1
                                break
                
    varCompIN += 1
    print(varCompIN)
    varCompSYN += 1