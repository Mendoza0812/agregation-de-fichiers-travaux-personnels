# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:12:03 2022

@author: Max-Louis
"""

import requests
from bs4 import BeautifulSoup

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
 html2 = requests.get(url2).text
 soup2 = BeautifulSoup(html2, 'html.parser')
 lightFrame = soup2.find("table", class_ = "light_frame")
 #lienSyno = lightFrame.find_all("a")
 #textSyno = lienSyno.text
 #print(textSyno)