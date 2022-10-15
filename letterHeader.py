# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 01:58:50 2022

@author: Max-Louis
"""

import requests
from bs4 import BeautifulSoup

premUrl = "https://www.cnrtl.fr/portailindex/SYNO//A/4240"
debutUrl = "https://www.cnrtl.fr"
print(premUrl)
html2 = requests.get(premUrl).text
soup2 = BeautifulSoup(html2, 'html.parser')
letterHeader = soup2.find('table', class_ = 'letterHeader')
tdletterSelected = letterHeader.find("td")
trLetterHeader = letterHeader.find('tr')

for tdLetterSelected in trLetterHeader:
    hrefLetter = tdLetterSelected.find("a").get('href')
    print(hrefLetter)
    urlLetter = debutUrl + hrefLetter
    print(urlLetter)

