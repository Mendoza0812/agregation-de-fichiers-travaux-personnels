# -*- coding: utf-8 -*-
"""
Created on Wed May 11 00:13:34 2022

@author: Max-Louis
"""

import csv
import pandas
import requests
from bs4 import BeautifulSoup

r = csv.reader(open(r"out.csv")) # Here your csv file
for row in r:
    print(row)
print('END')

    
lire = pandas.read_csv(r"midterm.csv")
print(lire['URL80'][0])
print('END')

URL80 = str(lire['URL80'][0])
print(URL80)
print('END')

debutUrl = "https://www.cnrtl.fr"

html2 = requests.get(URL80).text
soup2 = BeautifulSoup(html2, 'html.parser')

letterHeader = soup2.find('table', class_ = 'letterHeader')
tdletterSelected = letterHeader.find("td")
trLetterHeader = letterHeader.find('tr')

liUrlAlphabet = []

rprNbSynoSr1Page = 0
rprAlphabet = 0
rprPage = 0
# Ces 3 dernières variables doivent être identiques et coïncider aux bdd

def checkUrlAlphabet():
    for tdLetterSelected in trLetterHeader:
        hrefLetter = tdLetterSelected.find("a").get('href')
        print(hrefLetter)
        urlAlphabet = debutUrl + hrefLetter
        print(urlAlphabet)
        liUrlAlphabet.append(urlAlphabet)
        
# La fonction ci-dessus renvoie toutes url chaque initiale alphabet
# Et sont intégrés dans liUrlAlphabet

def toutesPagesLettre():
    fleches1 = soup2.find('table', class_ = 'hometab').find_next_sibling('table')
    while True:        
        """
        ajouter ici ce qui permettra d'ajouter lienSuiv1 dans 
        la ligne suivante du fichier csv GFG1 colonne URL80.
        URL80 car 80 mots par page.
        C'est ce lien qui permettra d'ouvrir la page suivante de 
        tous les mots commençant par la même lettre
        Il doit être stocké dans le fichier csv pour ne pas perdre
        les progrès dans le scraping
        
        URL80 = lienSuiv1
        """
        flecheDroite1 = fleches1.find('td').find_next_sibling('td')
        hrefPageSuiv1 = flecheDroite1.find('a').get('href')
        lienSuiv1 = debutUrl + hrefPageSuiv1
        html1 = requests.get(lienSuiv1).text
        print(lienSuiv1)
        soup1 = BeautifulSoup(html1, 'html.parser')
        fleches1 = soup1.find('table', class_ = 'hometab').find_next_sibling('table')
        
def findAllLiensMot():
    homeTab = soup2.find('table', class_ = "hometab")
    lienMots = homeTab.find_all('a')
    for link in lienMots:
        url2 = debutUrl + link.get('href')
        print(url2)
        motRef = link.text
        print(motRef)
