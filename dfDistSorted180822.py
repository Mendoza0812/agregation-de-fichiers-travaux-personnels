# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 22:21:21 2022

@author: Max-Louis
"""

import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/ttLowerSnsAccent.csv')

df8 = pd.read_csv(r'C:/Users/Max-Louis/sansDoublon170822.csv')

# DES MOTS SANS ACCENTS SE RENDANT IDENTIQUES A DAUTRES ONT ETE SUPR DANS DF 9

df9 = pd.read_csv(r'C:/Users/Max-Louis/df9180822.csv')

df10 = pd.read_csv(r'C:/Users/Max-Louis/dfDistSorted.csv')
"""
#CREATION DE DF9
liste = []
num = []

for progdf8 in range(len(df8)):
    
    if df8.iloc[progdf8,0] == df8.iloc[progdf8,2]:
        liste.append(df8.iloc[progdf8,0])

        df8.drop([progdf8])
        
    print(progdf8)
    
# FIN CREATION DF9


# CREATION DE DF10

distance = []

for progdf9 in range(len(df9)):
    
    distance.append(801 - df9.iloc[progdf9,4])
    
#FIN DF10

"""