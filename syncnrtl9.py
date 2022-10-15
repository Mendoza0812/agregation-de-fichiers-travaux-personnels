# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 16:11:18 2022

@author: Max-Louis
"""

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

print("Input URL:")
url2 = input()
html2 = requests.get(url2).text
soup2 = BeautifulSoup(html2, 'html.parser')

vToolBar = soup2.find('div', id = 'vtoolbar').ul
liMot = vToolBar.find('li').text

form = soup2.find('form', id = 'reqform')
valForm = form.input['value'].upper()

debutUrl = "https://www.cnrtl.fr"

seq_listIdMot = []
seq_listNatMot = []
#Suite vérification onglet (liMot)/formulaire (valForm) de vToolBar
def testvfsvis():
    print("Test valForm / spanLM commence ---")
    nbrMot = -1
    for liMot in vToolBar:
        
        nbrMot += 1
        print(nbrMot)
        
        spanLM = liMot.span.text
        textLM = str(liMot.text)
        natMot = re.sub("[A-Z_À-ÿ\-, ]", "", textLM)
        seq_listIdMot.append(spanLM)
        seq_listNatMot.append(natMot)
        
        lmao = liMot.a['onclick']
        stringlmao = str(lmao)
        restrlmao = re.findall(r"'(.*?)'", stringlmao)
        srslmao = str(restrlmao)
        msrslmao = re.sub("\[|\'|\'|\]","",srslmao)
        
        if valForm == spanLM:
            
            print("TRUE Executer listeSyno du fichier cnrtl6")
            url3 = debutUrl + msrslmao
            print(url3)
            html3 = requests.get(url3).text
            soup3 = BeautifulSoup(html3, 'html.parser')
            lightFrame = soup3.find("table", class_ = "light_frame")
            tBody = lightFrame.find_all('tr')
            uneLigne = lightFrame.find('tr')
            nbrLigne = 0
            natMot1 = seq_listNatMot[nbrMot]
            if natMot1 == "":
                natMot1 = "Non renseigne"
            else:
                natMot1 = natMot1
            idMot1 = seq_listIdMot[nbrMot]
            
            for uneLigne in tBody :
                print("---------------------------------------------")
                print("Nature du mot d'origine : " + natMot1)
                print("Identité du mot d'origine : "+ idMot1)
                val = uneLigne.img['width']
                textSyn3 = uneLigne.text
                print("Proximité du synonyme : " + val + "/400")
                nbrLigne += 1
                strNbrLgn = str(nbrLigne)
                print("Place du synonyme : " + strNbrLgn)
                print("Dénomination du synonyme : " + textSyn3)
            
        elif valForm != spanLM:
            print("FALSE")
        else:
            print("ERROR")
    print("Test valForm / spanLM fin ---")
    
def traitmtLstMots():
    url = "https://www.cnrtl.fr/portailindex/SYNO//A/0"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    homeTab = soup.find('table', class_ = "hometab")
    lienSyn = homeTab.find_all('a')

    for link in lienSyn:
        url2 = "https://www.cnrtl.fr" + link.get('href')
        print(url2)
        motRef = link.text
        print("Ouverture du lien http vers :" + motRef)
        # motRef equiv textSyn1 dans syncnrtl1.py
 
def incorpPandas():
    #ici c'est pandas on stocke les données
    dataSyn = pd.DataFrame(
        {
            "idmot": 
                ["Identité du mot "],
            "natMot":
                ["La nature du mot "],
            "Synonyme":
                ["Synonyme du mot"],
            "Proximité/400":
                ["Proximité du synonyme"]
        }
 )

    print(dataSyn)

traitmtLstMots()
testvfsvis()
incorpPandas()