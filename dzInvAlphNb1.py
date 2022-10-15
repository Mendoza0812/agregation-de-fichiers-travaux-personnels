# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 02:09:53 2022

@author: Max-Louis
rechercher les doublons à partir de la colonne alphnb
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

varAlphNb = []


for loop in range(28):
    varCompSYN = 0
    varCompIN = 1
    varCompLgn0 = 0
    varCompLgn1 = 0
    varVerifSYN = 0
    liVerifSYN = []
    varLiVerifSYN = 0
    varNbLgn = 0
    compartimentSYN = dzInvAlphNb[dzInvAlphNb['AlphNb'] == varCompSYN]
    compartimentIN = dzAlphNb[dzAlphNb['AlphNb'] == varCompIN]
    colmnANSYN = dzInvAlphNb['AlphNb']
    
    if colmnANSYN[varNbLgn] == 0 or colmnANSYN[varNbLgn] == 27:
        idN.append(compartimentSYN.iloc[varNbLgn,0])
        natN.append(compartimentSYN.iloc[varNbLgn,1])
        syno.append(compartimentSYN.iloc[varNbLgn,2])
        natS.append('')
        val800.append(compartimentSYN.iloc[varNbLgn,3] * 2)
        varNbLgn += 1
        
    else:
        varCompSYN += 1
        while varCompLgn0 < len(compartimentSYN):
            if compartimentSYN.iloc[varCompLgn0, 0] == compartimentIN.iloc[varCompLgn1, 0]:
                idN.append(compartimentIN.iloc[varCompLgn0,0])
                liVerifSYN.append(compartimentIN.iloc[varCompLgn0,0])
                natN.append(compartimentIN.iloc[varCompLgn0,1])
                syno.append(compartimentIN.iloc[varCompLgn0,2])
                natS.append(compartimentSYN.iloc[varCompLgn1,1])
                val800.append(compartimentIN.iloc[varCompLgn0,3] + compartimentSYN.iloc[varCompLgn1,3])
                varCompLgn0 += 1
                varVerifSYN += 1
                varNbLgn += 1
            else:
                varCompLgn1 += 1
                if varCompLgn1 == len(compartimentSYN):
                    idN.append(compartimentIN.iloc[varCompLgn0,0])
                    natN.append(compartimentIN.iloc[varCompLgn0,1])
                    syno.append(compartimentIN.iloc[varCompLgn0,2])
                    natS.append('')
                    val800.append(compartimentSYN.iloc[varCompLgn0,3] * 2)
                    varNbLgn += 1
                    varCompLgn0 += 1
                    varVerifSYN += 1
                    varCompLgn1 = 0
                    
        if varVerifSYN < len(compartimentSYN):
            if len(liVerifSYN) == varVerifSYN:
                while varVerifSYN < len(compartimentSYN):
                    varCompLgn1 = 0
                    varVerifSYN = 0
                    if compartimentSYN[varCompLgn1] == liVerifSYN[varLiVerifSYN] :
                        varLiVerifSYN = 0
                        varVerifSYN += 1
                        varCompLgn1 += 1
                        
                    else:
                        varLiVerifSYN += 1
                        if varLiVerifSYN == len(liVerifSYN):
                            idN.append(compartimentSYN.iloc[varCompLgn1,0])
                            natN.append(compartimentSYN.iloc[varCompLgn1,1])
                            syno.append(compartimentSYN.iloc[varCompLgn1,2])
                            natS.append('')
                            val800.append(compartimentSYN.iloc[varCompLgn1,3] * 2)
                            varCompLgn1 += 1
                            varVerifSYN += 1
                            varNbLgn += 1
                            varLiVerifSYN = 0
                liVerifSYN = []
            else:
                print('erreur entre liVerifSYN et varVerifSYN')
        
        varCompIN += 1