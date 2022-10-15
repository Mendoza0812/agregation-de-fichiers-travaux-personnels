# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:30:31 2022

@author: Max-Louis

vItemSelected et spanVIS sont à intégrer dans elif nbMot > 1
"""

import requests
from bs4 import BeautifulSoup
import re


url2 = "https://www.cnrtl.fr/synonymie/faiblissant"
html2 = requests.get(url2).text
soup2 = BeautifulSoup(html2, 'html.parser')

# REGEX recherche guillemet simple nécessaire dans boucle for if for
char = "The rain in 'Spain'."
print("affichage char")
print(char)
print("FIN")

test = re.findall(r"'(.*?)'", char)
print("affichage test (regex dans char) avec .group qui permet ")
print("d'afficher le mot du début à la fin :")
print(test)
print("FIN")

# Mot pré-écrit dans la barre de recherche
form = soup2.find('form', id = 'reqform')
valForm = form.input['value'].upper()
print("Affichage valForm :")
print(valForm)
print("--- END ---")

print("Affichage du type valForm :")
print(type(valForm))
print("--- END ---")

vToolBar = soup2.find('div', id = 'vtoolbar').ul
print("Affichage vToolBar :")
print(vToolBar)
print("--- END ---")

liMot = vToolBar.find('li').text
print("Affichage liMot :")
print(liMot)
print("--- END ---")

print('Affichage type liMot :')
print(type(liMot))
print("--- END ---")


splitLM = liMot.split(", ")
print("affichage splitLM")
print(splitLM)
print(" --- END ---")

natMot = splitLM[1]
print("affichage natMot")
print(natMot)
print(" --- END ---")

idMot = splitLM[0]
print("affichage idMot")
print(idMot)
print(" --- END ---")

# Mot sélectionné sur la page
vItemSelected = vToolBar.find('li', id = "vitemselected")
print("Affichage vItemSelected :")
print(vItemSelected)
print("--- END ---")

print("Affichage du type vItemSelected :")
print(type(vItemSelected))
print("--- END ---")

# Modification du type de donnée en string pour comparaison avecvalForm
unicodeVIS = str(vItemSelected)
print("Affichage du type unicodeVIS :")
print(type(unicodeVIS))
print("--- END ---")

print("Affichage unicodeVIS:")
print(unicodeVIS)
print(" --- END ---")

spanVIS = vItemSelected.span.text
print("Affichage spanUVIS")
print(spanVIS)
print(" --- END ---")

print("Affichage du type spanVIS")
print(type(spanVIS))
print("--- END ---")

lowSVIS = spanVIS.lower()
print("Affichage de lowSVIS")
print(lowSVIS)
print("--- END ---")

#test similitude valForm / idMot
def testvfsvis():
    print("Test valForm / spanLM commence ---")
    nbrMot = 0
    for liMot in vToolBar:
        nbrMot += 1
        print(nbrMot)
        spanLM = liMot.span.text
        if valForm == spanLM:
            print("TRUE Executer listeSyno du fichier cnrtl6")
            
            lMA = liMot.a
            print("affichage lMA")
            print(lMA)
            print("FIN")
            
            """
            PROBLEME REGEX
            splitLMA = lMA.re.split("['-]")
            print("affichage splitlMA")
            print(splitLMA)
            print("FIN")
            
            url3 = ("https://www.cnrtl.fr" + lienLM.get('href'))
            html3 = requests.get(url3).text
            soup3 = BeautifulSoup(html3, 'html.parser')
            
            lightFrame = soup3.find("table", class_ = "light_frame")
            print("affichage lightFrame")
            print(lightFrame)
            print("FIN")
            uneLigne = lightFrame.find('tr')
            print(uneLigne)
            for uneLigne in lightFrame :
                print(uneLigne)
                print('/n')
                val = uneLigne.img['width']
                textSyn3 = uneLigne.text
                print(val)
                print(textSyn3)
            """
        elif valForm != spanLM:
            print("FALSE")
        else:
            print("ERROR")
    print("Test valForm / spanLM fin ---")
    
def nbOngletMot():
    print("Execution fonction nbOngletMot :")
    nbMot = 0
    for liMot in vToolBar:
        nbMot += 1
    print("nbMot =", nbMot)
    
    if nbMot < 1:
        print("Erreur nbMot")
    elif nbMot == 1:
        print("Executer listeSyno du fichier cnrtl6")
    elif nbMot > 1:
        print("Test similitude valForm / spanLM accordé :")
        testvfsvis() 
    else:
        print("Erreur imprevue dans vToolBar nbMot")
    print("--- END ---")

def idOngletMot():
    print("1Ici, on doit vérifier chaque mot dans l'onglet vToolBar \n")
    print("1S'ils sont strictement identiques comme p.ex être ou avoir. \n")
    
def natOngletMot():
    print("2S'ils sont strictement identiques \n")
    print("2On dissocie le mot par sa nature p.ex verbe adj etc.")

testvfsvis()
nbOngletMot()
idOngletMot()
natOngletMot()

print("--- END ---")

