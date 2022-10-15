# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:35:47 2022

@author: Max-Louis

TEST REGEX pour testvToolBar où l'objectif est de récupérer l'url inscrit
dans l'attribut onClick de la balise a, écrit entre 2 apostrophes
"""

import requests
from bs4 import BeautifulSoup
import re


url2 = "https://www.cnrtl.fr/synonymie/faiblissant"
html2 = requests.get(url2).text
soup2 = BeautifulSoup(html2, 'html.parser')
vToolBar = soup2.find("div", id = "vtoolbar")

strSoup2 = str(soup2)
print("Affichage strSoup2: ")
print(strSoup2)
print("FIN")

vtbao = vToolBar.a['onclick']
print("Affichage vtbao")
print(vtbao)
print("FIN")

stringvtbao = str(vtbao)
print("affichage stringvtbao")
print(stringvtbao)
print("FIN")

print("affichage du type stringvtbao")
print(type(stringvtbao))
print("FIN")

restrvtbao = re.findall(r"'(.*?)'", stringvtbao)
print("affichage restrvtbao")
print(restrvtbao)
print("FIN")

srsvtbao = str(restrvtbao)
#Il faut enlever ces putins de crochets et de guillemets simples qui
#étaient la parce que c'était une valeur liste

msrsvtbao = re.sub("\[|\'|\'|\]","",srsvtbao)
print("Affichage msrsvtbao")
print(msrsvtbao)
print("FIN")

debutUrl = "https://www.cnrtl.fr"

# SOLUTION REGEX TROUVE ICI
url3 = debutUrl + msrsvtbao
print("affichage url3")
print(url3)
print("FIN")


print("Affichage vToolBar :")
print(vToolBar)
print("FIN")

# REGEX recherche guillemet simple nécessaire dans boucle for if for
char = "The rain in 'Spain'."
print("affichage char")
print(char)
print("FIN")

""" ceci ne marche pas 
regex = re.compile(r"'(.*?)'")
soupex = (char, "html.parser")
srex = soupex.find_all(regex)
print("affichage srex")
print(srex)
print("FIN")

"""
test = re.findall(r"'(.*?)'", strSoup2)
print("affichage test (regex dans char) avec .group qui permet ")
print("d'afficher le mot du début à la fin :")
print(test)
print("FIN")

hookups = soup2.find_all(text=re.compile(r"'(.*?)'"))
print("affichage hookups")
print(hookups)
print("FIN")
