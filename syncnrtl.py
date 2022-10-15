import requests
from bs4 import BeautifulSoup
import pandas as pd

cnrtlSynUrl = "https://www.cnrtl.fr/synonymie/"
htmlSyn = requests.get(cnrtlSynUrl).text
soupSyn = BeautifulSoup(htmlSyn, 'html.parser')

# cible tous les liens synonymes de la page web
aSyn = soupSyn.find("table", class_ = "hometab").find_all('a')

for link in soupSyn.find("table", class_ = "hometab").find_all('a'):
    print(link.get("href"))

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