# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:38:34 2022

@author: Max-Louis

test page synonymes (url2)
"""

import requests
from bs4 import BeautifulSoup

url2 = "https://www.cnrtl.fr/synonymie/faiblissant"
html2 = requests.get(url2).text
soup2 = BeautifulSoup(html2, 'html.parser')


lightFrame = soup2.find("table", class_ = "light_frame")

mainContent = soup2.find("div", id = "main_content")
print(mainContent)
print("END------------------------------------------------------")

contentBox = soup2.find("div", id = "contentbox")
print(contentBox)
print("END")

lienSyn = lightFrame.find_all('a')
print(lienSyn)
print("END")

imgSyn = lightFrame.img["width"]
print(imgSyn)
print("END")

imgSyn2 = lightFrame.select('img[src="/images/portail/pbon.png"]')
print(imgSyn2)
print("END")

allImg = soup2.find_all('img')
for link3 in allImg:
    print(link3.get('width'))
print("END")

for link2 in lightFrame:
    textSyn = link2.text
    print(textSyn)
print("END")

"""
La solution a été trouvé en dessous
"""
tBody = lightFrame.find_all('tr')
print("AFFICHAGE tBody")
print(tBody)
print("END")

uneLigne = lightFrame.find('tr')
print(uneLigne)
print("END")

def listeSyno() :
    for uneLigne in tBody :
        print(uneLigne)
        print('/n')
        val = uneLigne.img['width']
        textSyn3 = uneLigne.text
        print(val)
        print(textSyn3)

listeSyno()
    
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/