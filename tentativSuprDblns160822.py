# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 20:58:23 2022

@author: Max-Louis

ajouter la ligne df.iloc[382550]

probleme les mots dans lesquels on a enlevé les accents sont devenus
des mots identiques alors quils ne le sont pas dans le sens exact
"""

import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/ttLowerSnsAccent.csv')

df = df.sort_values('idN').reset_index(drop = True)

df2 = pd.read_csv(r'C:/Users/Max-Louis/pourSuprDbl.csv')

df3 = pd.read_csv(r'C:/Users/Max-Louis/queLesDbls.csv')

df4 = pd.read_csv(r'C:/Users/Max-Louis/sortDbls.csv')

df5 = pd.read_csv(r'C:/Users/Max-Louis/lgnUnq.csv')

df6 = pd.read_csv(r'C:/Users/Max-Louis/listedf6.csv')

df7 = pd.read_csv(r'C:/Users/Max-Louis/df7.csv')

df8SnsDbl = pd.read_csv(r'C:/Users/Max-Louis/sansDoublon170822.csv')

dfErr = pd.read_csv(r'C:/Users/Max-Louis/dfErr.csv')

"""
#RESULTAT DE DF3
lgr = len(df2)

dblsName = []
dbls2 = []

par100 = 0

doublons = df2[df2['prems'] == True]

for incr in range (len(doublons)):
        
    dblsName.append(doublons.iloc[incr].name)
    dbls2.append(doublons.iloc[incr,0])
    
    par100 += 1
    if par100 == 100:
        par100 = 0
        print(incr)
        
#FIN DE DF3

#RESULTAT DE DF4
sortDbls = []

for incr in range (len(df3)):
    
    sortDbls.append(df3.iloc[incr,0])
    sortDbls.append(df3.iloc[incr,1])
#FIN DE DF4

#CREATION DE DF5 QUI INCLUT TOUTES LES LIGNES SANS DOUBLON

lgnUnq = []

incr = 0
bougePasTrop = 0

while incr != 382551:
    
   if incr < df4.iloc[bougePasTrop,0]:
        
        while incr < df4.iloc[bougePasTrop,0]:
        
            lgnUnq.append(incr)
            
            incr += 1
    
   incr += 1
   bougePasTrop += 1
   print(incr)
   
#FIN DE DF5

#ETABLISSEMENT DF6 ET DF7
liste = []
liste2 = []
atilUnDoublon = []

progdf5 = 0
incr = 0

while progdf5 != (len(df5)):
    
    if df2.iloc[incr,1] == True:
        
        liste.append(incr)
        liste2.append(df2.iloc[incr,0])
        atilUnDoublon.append(True)
        
    else:
        
        if incr == df5.iloc[progdf5,0]:
            
            liste.append(df5.iloc[progdf5,0])
            liste2.append(df5.iloc[progdf5,0])
            atilUnDoublon.append(False)
            progdf5 += 1
            print(progdf5)
    
    incr += 1
    print(incr)

#FIN DE DF6 ET DF7


# ETABLISSEMENT DE LA DF SANS DOUBLON SOIT DF8

idN = []
natN = []
syno2 = []
natS = []
val800 = []
reportDesErreurs = []

nbDErreurs = 0

incr = 0
progdf6 = 0
progdf7 = 0

while progdf7 != len(df7):
    
    modorgn = df7.iloc[progdf7,0]
    emplDuSyno = df7.iloc[progdf7,1]
    
    idN.append(df.iloc[modorgn,0])
    natN.append(df.iloc[modorgn,1])
    
    if modorgn == emplDuSyno:
        
        syno2.append(df.iloc[emplDuSyno,2])
        natS.append('')
        
        if df7.iloc[progdf7,2] == True:
            print('erreur')
            nbDErreurs += 1
            reportDesErreurs.append(progdf7)
        
    else:
        
        syno2.append(df.iloc[emplDuSyno,0])
        natS.append(df.iloc[emplDuSyno,1])
    
    val800.append(df.iloc[modorgn,3] + df.iloc[emplDuSyno,3])
    
    progdf7 += 1
    print(progdf7)


plist = (idN, natN, syno2, natS, val800)

df8 = pd.DataFrame(plist).transpose()

df8.columns = ['idN', 'natN','syno2','natS','val800']

# FIN DF8
"""
#ANALYSE REPORT DERREURS

