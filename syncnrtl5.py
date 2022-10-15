# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:29:05 2022

@author: Max-Louis

Rien a été raté dans le programme précédent mais celui-ci a été créé 
pour voir s'il est possible d'aller plus vite dans le parsing avec
SoupStrainer comme cité dans la documentation. A regarder pour plus tard.
Cette technique est précisé à la fin de la documentation.
"""

from bs4 import SoupStrainer

only_a_tags = SoupStrainer("a")