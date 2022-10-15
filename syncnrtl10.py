# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 18:53:35 2022

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
lim = []
lnm = []
lpSyno = []
lSyno = []
lp4 = []
#Suite vérification onglet (liMot)/formulaire (valForm) de vToolBar
dataSyn = pd.DataFrame(columns={'idmot',
                        'natMot',
                        'placeSyno',
                        'Synonyme',
                        'Proximité/400'})
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
            idMot1 = seq_listIdMot[nbrMot]
            sim1 = str(idMot1)
            
            for uneLigne in tBody :
                print("---------------------------------------------")
                print("Identité du mot d'origine : " + sim1)
                sim1low = sim1.lower()
                lim.append(sim1low)
                print("Nature du mot d'origine : "+ natMot1)
                lnm.append(natMot1)
                val = uneLigne.img['width']
                textSyn3 = uneLigne.text
                print("Proximité du synonyme : " + val + "/400")
                lp4.append(val + "/400")
                print("Dénomination du synonyme : " + textSyn3)
                lSyno.append(textSyn3)
                nbrLigne += 1
                strNbrLgn = str(nbrLigne)
                print("Place du synonyme : " + strNbrLgn)
                lpSyno.append(nbrLigne)
                
        elif valForm != spanLM:
            print("FALSE")
        else:
            print("ERROR")
    print("Test valForm / spanLM fin ---")

testvfsvis()
    

print(seq_listNatMot)
print(seq_listIdMot)
print(lim)
print(lnm)
print(lp4)
print(lSyno)
print(lpSyno)
print(dataSyn)
products_list = (lim, lnm, lSyno, lp4, lpSyno)
df = pd.DataFrame (products_list).transpose()
df.columns = ['IdNom', 'NatNom', 'listeSyno', 'val400', 'placeSyno']

print (df)
#for col in df.columns:
 #   series = df[col]
    
