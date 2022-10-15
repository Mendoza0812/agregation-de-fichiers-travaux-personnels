# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 00:38:15 2022

@author: Max-Louis
"""
import pandas as pd

val1009 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\val1000.csv')
liChose = pd.read_csv(r'C:\Users\Max-Louis\chose2.csv')

lenChose = len(liChose)

var = 1
liLen = []
varliLen = 0

for loop in range(lenChose):
    motRecherche = liChose.iloc[lenChose-var,0]
    lenMotRech = len(motRecherche)
    liMotRecherche = val1009[val1009['listeSyno'].str.contains(motRecherche)]

    lenliMotRech = len(liMotRecherche)
    for loop in range(lenliMotRech):
        liLen.append(len(liMotRecherche.iloc[varliLen,2]))
        var += 1
    
    liMotRecherche['liLen'] = liLen
    liLen1 = liMotRecherche['liLen']
    trimot = []
    idNom = []
    natNom = []
    listeSyno = []
    val1000 = []
    lenght = []
    var = 0

    for loop in range(lenliMotRech):
        idNom.append(liMotRecherche.iloc[var,0])
        natNom.append(liMotRecherche.iloc[var,1])
        trimot.append(liMotRecherche.iloc[var,2])
        val1000.append(liMotRecherche.iloc[var,3])
        lenght.append(len(liMotRecherche.iloc[var, 2]))
        var += 1
    
    products_list = (idNom, natNom, trimot, val1000, lenght)
    df1 = pd.DataFrame (products_list).transpose()
    df1.columns = ['IdNom','NatNom','motchos','val1000', 'lenght']
        
    trimot = []
    idNom = []
    natNom = []
    listeSyno = []
    val1000 = []
    var = 0

    for loop in range(lenliMotRech):
        if df1.iloc[var, 4] == lenMotRech:
            idNom.append(df1.iloc[var,0])
            natNom.append(df1.iloc[var,1])
            trimot.append(df1.iloc[var,2])
            val1000.append(df1.iloc[var,3])
        var += 1
        
    products_list = (idNom, natNom, trimot, val1000)
    df2 = pd.DataFrame (products_list).transpose()
    df2.columns = ['IdNom','NatNom','motchos','val1000']
    df3 = df2.sort_values('val1000')
    df3.to_csv('chose2.csv', index = False)