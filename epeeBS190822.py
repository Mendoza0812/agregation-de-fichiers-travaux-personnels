# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 00:56:14 2022

@author: Max-Louis
"""

import requests
from bs4 import BeautifulSoup
#from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN
import pandas as pd
import re

#settings = initialize_VPN() 

liMPl0CarSpec = pd.read_csv(r'C:/Users/Max-Louis/motPl0CarSpec.csv')

baseUrl = "https://www.cnrtl.fr"

liCarSpec = ['à','â','ä','é','è','ê','ë','î','ï','ô','ö','ù','û','ü','ÿ','ç','-','.','\'']
carSpec = 0
boolCarSpec = False

idN = []
natN = []
syno2 = []
natS = []
distance = []

#for incr in range (len(liMPl0CarSpec)):
for incr in range(2):
    
    #rotate_VPN(settings)
    
    motDeBase = 'église'
    
    html = requests.get(baseUrl + str('/synonymie/')+ motDeBase).text
    soup = BeautifulSoup(html, 'html.parser')

    vToolBar = soup.find('div', id = 'vtoolbar').ul
    liMot = vToolBar.find('li').text
    textLM = str(liMot)
    
    if len(textLM) == len(motDeBase):
        
        natMot = ''
    
    else:
        
        natMot = re.sub("[A-Z_À-ÿ\-, ]", "", textLM)
 
    lightFrame = soup.find('table', class_ = "light_frame")
    
    tBody = lightFrame.find_all('tr')
    uneLigne = lightFrame.find('tr')
    
    for uneLigne in tBody:
        
        val = uneLigne.img['width']
        lienHyT = uneLigne.a['href']
        texte = uneLigne.text
        
        url2 = baseUrl + lienHyT
        html2 = requests.get(url2).text
        soup2 = BeautifulSoup(html2, 'html.parser')
        
        vToolBar2 = soup2.find('div', id = 'vtoolbar').ul
        liMot2 = vToolBar2.find('li').text
        textLM2 = str(liMot2)
        
        if len(textLM2) == len(texte):
            
            natMot2 = ''
        
        else:
            
            natMot2 = re.sub("[A-Z_À-ÿ\-, ]", "", textLM2)
        
        lightFrame2 = soup2.find('table', class_ = "light_frame")
        tBody2 = lightFrame2.find_all('tr')
        uneLigne2 = lightFrame2.find('tr')
        
        for uneLigne2 in tBody2:
            
            texte2 = uneLigne2.text
            
            if texte2 == motDeBase:
                
                val2 = uneLigne2.img['width']
        
        val800 = int(val) + int(val2)
        
        string0 = motDeBase
        string2 = texte
        print(string2)
        
        boolCarSpec = False
        carSpec = 0
        
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
        natN.append(natMot)
        syno2.append(string2)
        natS.append(natMot2)
        distance.append(801 - val800)
    
#terminate_VPN(settings)

plist = (idN, natN, syno2, natS, distance)
dfRectif = pd.DataFrame(plist).transpose()
dfRectif.columns = ['idN','natN','syno2','natS','distance']
dfRectsv = dfRectif.sort_values('distance').reset_index(drop=True)
        