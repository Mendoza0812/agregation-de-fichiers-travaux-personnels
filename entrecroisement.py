# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 23:15:42 2022

@author: Max-Louis

suite de pbSynoChoix2.py
"""
import pandas as pd

deaaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')
#works
del deaaz['placeSyno']
chose = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\chose.csv')

print(chose)

trucmuche = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\trucmuche.csv')
bidule = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\bidule.csv')
patrimoine = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\patrimoine.csv')
fait = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\fait.csv')
machin = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\machin.csv')
evenement = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\événement.csv')
realite = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\réalité.csv')
bien = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\bien.csv')
truc = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\truc.csv')
objet = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\objet.csv')
possession = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\possession.csv')
affaire = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\affaire.csv')
capital = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\capital.csv')
propriete = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\propriété.csv')
circonstance = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\circonstance.csv')
richesse = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\richesse.csv')
batifolage = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\batifolage.csv')
esclave = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\esclave.csv')
bagatelle = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\bagatelle.csv')
phenomene = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\phénomène.csv')
instrument = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\instrument.csv')
fourbi = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\fourbi.csv')
rien = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\rien.csv')
condition = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\condition.csv')
sujet = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\sujet.csv')
bricole = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\bricole.csv')
babiole = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\babiole.csv')
action = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\action.csv')
