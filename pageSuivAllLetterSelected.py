# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 00:01:49 2022

@author: Max-Louis
"""
import requests
from bs4 import BeautifulSoup
import validators
from validators import ValidationFailure

premUrl = "https://www.cnrtl.fr/portailindex/SYNO//A/0"
debutUrl = "https://www.cnrtl.fr"
print(premUrl)
html2 = requests.get(premUrl).text
soup2 = BeautifulSoup(html2, 'html.parser')
allLetterSelected = soup2.find_all('a', class_ = 'letterSelected')

def is_string_an_url(url_string: str) -> bool:
    result = validators.url(url_string)

    if isinstance(result, ValidationFailure):
        return False

    return result

def has_no_a(flecheDroite1):
    return not flecheDroite1.find('a')
    

    
while True:
    print(premUrl)
    html1 = requests.get(premUrl).text
    soup1 = BeautifulSoup(html1, 'html.parser')
    fleches1 = soup1.find('table', class_ = 'hometab').find_next_sibling('table')
    flecheDroite1 = fleches1.find('td').find_next_sibling('td')
    if has_no_a(flecheDroite1):
        print("It works")            
        break
    hrefPageSuiv1 = flecheDroite1.find('a').get('href')
    lienSuiv1 = debutUrl + hrefPageSuiv1
    premUrl = lienSuiv1
    