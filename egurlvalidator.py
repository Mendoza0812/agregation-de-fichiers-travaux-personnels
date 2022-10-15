# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 22:53:55 2022

@author: Max-Louis
"""
import requests
from bs4 import BeautifulSoup
import validators
from validators import ValidationFailure

def is_string_an_url(url_string: str) -> bool:
    result = validators.url(url_string)

    if isinstance(result, ValidationFailure):
        return False

    return result

url = "https://www.cnrtl.fr/portailindex/SYNO//A/160"
debutUrl = "https://www.cnrtl.fr"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

fleches = soup.find('table', class_ = 'hometab').find_next_sibling('table')
flecheDroite = fleches.find('td').find_next_sibling('td')
hrefPageSuiv = flecheDroite.find('a').get('href')
lienSuiv = debutUrl + hrefPageSuiv

while is_string_an_url(lienSuiv) == True:
    html1 = requests.get(lienSuiv).text
    soup1 = BeautifulSoup(html1, 'html.parser')
    fleches1 = soup.find('table', class_ = 'hometab').find_next_sibling('table')
    flecheDroite1 = fleches1.find('td').find_next_sibling('td')
    hrefPageSuiv1 = flecheDroite1.find('a').get('href')
    print(lienSuiv)
    lienSuiv = debutUrl + hrefPageSuiv1