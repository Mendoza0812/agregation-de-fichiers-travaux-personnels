# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 18:30:18 2022

@author: Max-Louis
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.cnrtl.fr/synonymie/"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

# imprime tous les liens synonymes de la page web 
for url1 in soup.find("table", class_ = "hometab").find_all('a'):
    print(url1.get("href"))
    

#ici c'est pandas on stocke les données
dataSyn = pd.DataFrame(
    {
        "Synonyme 1": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Synonyme 2": [22, 35, 58],
        "Proximité": ["male", "male", "female"],
        "Syno1Syno2": ["haha-hoho", "hoho-haah", "HHAAAAA"]
    }
)

print (dataSyn)


# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html
"""
Pour les itérations, l exemple est en bas de cette page web:
    https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
"""