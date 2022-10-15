# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 18:22:12 2022

@author: Max-Louis

synthèse des fichiers python cnrtl et syncnrtl (analyse débuté au 6)
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

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
  print(motRef)
  # motRef equiv textSyn1 dans syncnrtl1.py
 
def incorpPandas():
 #ici c'est pandas on stocke les données
 dataSyn = pd.DataFrame(
     {
         "idmot": 
             ["Identité du mot "],
         "natMot":
             ["La nature du mot "],
         "Synonyme": ["Synonyme du mot"],
         "Proximité/400": ["Proximité du synonyme"]
     }
 )

 print(dataSyn)

traitmtLstMots()
incorpPandas()

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html
"""
Pour les itérations, l exemple est en bas de cette page web:
    https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
"""