# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:48:29 2022

@author: Max-Louis

Pour eliminer les doublons il faut prendre en compte concernant la bdd:
    chaque ligne évoque le lien entre un mot et son synonyme, composé de 
    le modorgn, la nat du modorgn, le syno, la proximité sur 400.
    
    Le tableau final contiendra sur chaque colmn, IdN, natN, syno, natS, val800.
    
    le programme devra d'abord compartimenter la bdd en fction de la 
    colmn alphNb.
    
    pour améliorer la recherche d'un mot, la bdd a ete classe par ordre 
    alphabetique. La bdd dzAlphNb est classe sur la colmn IdNom [colmn 
     numero 0] et 
    dzInvalphNb sur la colmn syno [colmn numero 2].
    
    Une ligne peut avoir des modorgn identiques mais des syno différents, 
     peut avoir des synos identiques mais des modorgn diff,
     peut avoir un quasi doublon avec modorgn et syno permutables
     
     certains mots peuvent aussi apparaître exclusiement dans la colmn idN 
     comme dautres mots peuvent apparaître exclsvmt dns la colmn syno
     
     des compartiments de la bdd classe par ordre alphbtq selon la colmn idN
      ne disposent daucune lgn. Cela est le cas pour alphNb 0(majscl) et alphNb 27(carspec)
      
     pour les compartmnts IN sans lgn, les lgn du comprtimt SYN seront tout simplement recopié
    
    de façon lineaire et progressif la variable commençant par zero va 
    compter le nb de mot idtq consecutif dans idNom, ce nb de mot idtq 
     sil exst devra être contenu dns une df, ce mot sera ensuite recherche 
    dans la colmn listeSyno     
"""
import pandas as pd

dzlian = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzAlphNb.csv')
dzliinvan = pd.read_csv(r'C:/Users/Max-Louis/.spyder-py3/dzInvAlphNb.csv')

dzliinvan = dzliinvan[['listeSyno','NatNom','IdNom','val400','AlphNb']]

idN = []
natN = []
syno = []
natS = []
val800 = []

idNSnsDbl = []
natNSnsDbl = []
synoSnsDbl = []
natSSnsDbl = []
val800SnsDbl = []


stockTestDbl = []

varComp = 0

for loop in range(2):
    
    print(' --- varComp = ' + str(varComp))
    
    compSYN = dzliinvan[dzliinvan['AlphNb'] == varComp]
    compIN = dzlian[dzlian['AlphNb'] == varComp]
    
    prgrsv = 0
    
    nbLgnCmpIN = len(compIN)
    centreIN = int((nbLgnCmpIN - (nbLgnCmpIN % 2)) / 2)
    
    nbLgnCmpSYN = len(compSYN)
    centreSYN = int((nbLgnCmpSYN - (nbLgnCmpSYN % 2)) / 2)
    
    if varComp == 0 or varComp == 27:
        print('nbLgnCmpIN == 0')
        
        while prgrsv < nbLgnCmpSYN:
            
            idNSnsDbl.append(compSYN.iloc[prgrsv,0])
            natNSnsDbl.append(compSYN.iloc[prgrsv,1])
            synoSnsDbl.append(compSYN.iloc[prgrsv,2])
            natSSnsDbl.append('')
            val800SnsDbl.append(compSYN.iloc[prgrsv,3] * 2)
            prgrsv += 1
        
        prgrsv = 0
        
        
    elif varComp > 0 or varComp < 27:
        print('varComp > 0 or varComp < 27 \n')
        
        
        cIip0 = compIN.iloc[prgrsv, 0]
        print('cIip0 = compIN.iloc[prgrsv, 0]')
        print('cIip0 = ' + str(cIip0))
        #nbLtrCmpIN0 = len(cIip0)
        #print('nbLtrCmpIN0 = ' + str(nbLtrCmpIN0) + '\n')
        
        strCtn0IN = compIN[compIN['IdNom'].str.contains(cIip0)]
        print('strCtn0IN = compIN[compIN[\'IdNom\'].str.contains(cIip0)] \n')
        print('strCtn0IN = ')
        print(strCtn0IN)
        print('\n')
        
        fragment0IN = pd.DataFrame(strCtn0IN)
        print('fragment0IN = pd.DataFrame(strCtn0IN) : \n')
        print(fragment0IN)
        print('\n')
        
        print('recherche de cIip0 dans compSYN \n')
        
        strCtn0SYN = compSYN[compSYN['listeSyno'].str.contains(cIip0)]
        print('strCtn0SYN = compSYN[compSYN[\'listeSyno\'].str.contains(cIip0)] \n')
        print('strCtn0SYN = ')
        print(strCtn0SYN)
        print('\n')
        
        fragment0IN = pd.DataFrame(strCtn0IN)
        print('fragment0IN = pd.DataFrame(strCtn0IN) : \n')
        print(fragment0IN)
        print('\n')
        
        
        cIip2 = compIN.iloc[prgrsv, 2]
        print('cIip2 = compIN.iloc[prgrsv, 2]')
        print('ciIp2 = ' + str(cIip2))
        nbLtrCmpIN2 = len(cIip2)
        print('nbLtrCmpIN2 = ' + str(nbLtrCmpIN2) + '\n')
        
        strCtn2 = compIN[compIN['IdNom'].str.contains(cIip2)]
        print('strCtn2 = compIN[compIN[\'IdNom\'].str.contains(cIip2)] \n')
        print('strCtn2 = ')
        print(strCtn2)
        print('\n')
        
        fragment2 = pd.DataFrame(strCtn2)
        print('fragment2 = pd.DataFrame(strCtn2) : \n')
        print(fragment2)
        print('\n')
        
        print('test fragment0/fragment2 --- \n')
    
    
        cSip0 = compSYN.iloc[prgrsv, 0]
        print('cSip0 = ' + str(cSip0))
        nbLtrCmpSYN0 = len(cSip0)
        print('nbLtrCmpSYN0 = ' + str(nbLtrCmpSYN0) + '\n')
        
        
        cSip2 = compSYN.iloc[prgrsv, 2]
        print('csIp2 = ' + str(cSip2))
        nbLtrCmpSYN2 = len(cSip2)
        print('nbLtrCmpSYN2 = ' + str(nbLtrCmpSYN2) + '\n')
    
        """
        pb str.contains je ne sais pas comment il reagit sil trouve pas str
        ne pas oublier de compter le nb de letr puis rechercher parmi ts ls 
        mots idtq ceux qui ont pour modorgn le mm mot que le syno de compIN
        """
        
        
    varComp += 1
    
    