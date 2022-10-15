# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 03:03:08 2022

@author: Max-Louis
"""

import requests
from bs4 import BeautifulSoup

premUrl = "https://www.cnrtl.fr/portailindex/SYNO//A/0"
debutUrl = "https://www.cnrtl.fr"
print(premUrl)
html2 = requests.get(premUrl).text
soup2 = BeautifulSoup(html2, 'html.parser')

letterHeader = soup2.find('table', class_ = 'letterHeader')
tdletterSelected = letterHeader.find("td")
trLetterHeader = letterHeader.find('tr')
nbrMot = 1

def has_no_a(flecheDroite1):
    return not flecheDroite1.find('a')
    
for tdLetterSelected in trLetterHeader:
    hrefLetter = tdLetterSelected.find("a").get('href')
    print(hrefLetter)
    premUrl = debutUrl + hrefLetter
    print(premUrl)
    while True:
        print(premUrl)
        html1 = requests.get(premUrl).text
        nbrMot += 80
        soup1 = BeautifulSoup(html1, 'html.parser')
        fleches1 = soup1.find('table', class_ = 'hometab').find_next_sibling('table')
        flecheDroite1 = fleches1.find('td').find_next_sibling('td')
        if has_no_a(flecheDroite1):
            print("It works")            
            break
    
        hrefPageSuiv1 = flecheDroite1.find('a').get('href')
        lienSuiv1 = debutUrl + hrefPageSuiv1
        premUrl = lienSuiv1
        
    homeTab = soup2.find('table', class_ = "hometab")
    lienSyn = homeTab.find_all('a')
    for link in lienSyn:
        nbrMot += 1
    
print(nbrMot)
    
            
    