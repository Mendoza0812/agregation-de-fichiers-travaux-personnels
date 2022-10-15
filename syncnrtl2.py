# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 18:30:18 2022

@author: Max-Louis
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.cnrtl.fr/portailindex/SYNO//A/0"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
    
htmlBody = soup.body
# cible toute la page en dehors de head

mainContent = htmlBody.find('div', id='main_content')

divContent = mainContent.find('div', id='content')

#Cible la table contenant les lettres de l'alphabet
letterHeader = soup.find('table', class_ = "letterHeader")

#Cible la table contenant tous les synonymes de la page
homeTab = soup.find('table', class_ = "hometab")

#Cible toutes les balises hyperliens correspondant à la liste
lienSyn = homeTab.a

#Cible le texte correspondant au premier mot de la liste
textSyn1 = homeTab.a.text

#Construit l'url du mot sur lequel il faudra parser
url2 = ("https://www.cnrtl.fr" + lienSyn.get('href'))
html2 = requests.get(url2).text

#Analyse la page du premier mot
soup2 = BeautifulSoup(html2, 'html.parser')

#Cible le texte du premier synonyme du premier mot
synoFormat = soup2.find("td", class_ = "syno_format").text
lightFrame = soup2.find("table", class_ = "light_frame")
print(lightFrame)

"""
jaugeVrtImg = soup2.find("table", class_ = "light_frame").img

pareil que 

lightFrame = soup2.find("table", class_ = "light_frame")
jaugeVrtImg = lightFrame.img

cela permet d'identifier clairement lightFrame pour cibler les syno
car la page web est différente entre url et url2 (syncnrtl4.py):
 - celle les listes de mots classés par ordre alphabétique (url)
     ici, lightFrame est équivalent de lienSyn
     
 - et celle des listes de synonymes correspondant au mot référencé
de la page et pas seulement à identifier le texte des syno (url2)
"""
jaugeVrtImg = lightFrame.img
print(jaugeVrtImg)
val400 = jaugeVrtImg['width']

#Une incrémentation sera nécessaire pour automatiser le sgbdr
increment = 0

#Définit la base de données pandas
dataSyn = pd.DataFrame(
    {
        "Mot":[textSyn1],
        "Synonyme":[synoFormat],
        "Proximité/400":[val400 + "/400"]
    }
)
print(dataSyn)

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html
"""
Pour les itérations, l exemple est en bas de cette page web:
    https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
"""