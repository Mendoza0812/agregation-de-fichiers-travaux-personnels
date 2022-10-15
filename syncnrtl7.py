# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:21:54 2022

@author: Max-Louis
"""

import requests
from bs4 import BeautifulSoup
import re

print("Enter the url:")
url2 = input()
html2 = requests.get(url2).text
soup2 = BeautifulSoup(html2, 'html.parser')
"""
# Cible tous les synonymes listés de la page
lightFrame = soup2.find("table", class_ = "light_frame")

tBody = lightFrame.find_all('tr')
print("AFFICHAGE tBody")
print(tBody)
print("END")

uneLigne = lightFrame.find('tr')
print(uneLigne)
print("END")

def listeSyno() :
    for uneLigne in tBody :
        print(uneLigne)
        print('/n')
        val = uneLigne.img['width']
        textSyn3 = uneLigne.text
        print(val)
        print(textSyn3)
        """

#Vérifies la bonne direction de la page par à l'onglet et au formulaire
vToolBar = soup2.find('div', id = 'vtoolbar').ul
print("Affichage vToolBar :")
print(vToolBar)
print("--- END ---")

liMot = vToolBar.find('li').text
print("Affichage liMot :")
print(liMot)
print("--- END ---")



form = soup2.find('form', id = 'reqform')
valForm = form.input['value'].upper()
print("Affichage valForm :")
print(valForm)
print("--- END ---")

#Construit l'adresse url d'un onglet sélectionné

debutUrl = "https://www.cnrtl.fr"
"""
vtbao = vToolBar.a['onclick']
print("Affichage vtbao")
print(vtbao)
print("FIN")

stringvtbao = str(vtbao)
print("affichage stringvtbao")
print(stringvtbao)
print("FIN")

restrvtbao = re.findall(r"'(.*?)'", stringvtbao)
print("affichage restrvtbao")
print(restrvtbao)
print("FIN")

srsvtbao = str(restrvtbao)

msrsvtbao = re.sub("\[|\'|\'|\]","",srsvtbao)
print("Affichage msrsvtbao")
print(msrsvtbao)
print("FIN")

url3 = debutUrl + msrsvtbao
print("affichage url3")
print(url3)
print("FIN")
"""
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
        natMot = re.sub("[A-Z_À-ÿ, ]", "", textLM)
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
            
            for uneLigne in tBody :
                print("//Nature du mot d'origine : " + natMot1)
                print("Identité du mot d'origine : "+ idMot1)
                val = uneLigne.img['width']
                textSyn3 = uneLigne.text
                print("Proximité du synonyme : " + val + "/400")
                nbrLigne += 1
                print("Place du synonyme : " + nbrLigne)
                print("Dénomination du synonyme : " + textSyn3)
            
        elif valForm != spanLM:
            print("FALSE")
        else:
            print("ERROR")
    print("Test valForm / spanLM fin ---")
    
testvfsvis()

    
