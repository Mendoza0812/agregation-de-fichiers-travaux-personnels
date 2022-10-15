# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 23:49:53 2022

@author: Max-Louis
"""

import pandas as pd
#import matplotlib as mpl
import matplotlib.pyplot as plt
#import numpy as np

deaaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')
#works
chose800sv = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\chose800sv2.csv')
del deaaz['placeSyno']

val = chose800sv['val800']

synoChoix = chose800sv.iloc[0:4]
syno1 = synoChoix.iloc[0] #Trucmuche
syno2 = synoChoix.iloc[1] #bidule
syno3 = synoChoix.iloc[2] #patrimoine
syno4 = synoChoix.iloc[3] #fait
chose = 0
valinv = 800 - syno1[4], 800 - syno2[4], 800 - syno3[4], 800 - syno4[4]
montre = valinv[0], valinv[1], valinv[2] - (valinv[2]*2), valinv[3] - (valinv[3]*2)
trucmuche = montre[0]
bidule = montre[1]
patrimoine = montre[2]
fait = montre[3]
x = chose, 0, trucmuche, 0, patrimoine
y = chose, bidule, 0, fait, 0
plt.plot(x, y, 'bo')
plt.text(chose,chose,'chose')
plt.grid()
plt.axis([-1000, 1000, -1000, 1000])
plt.show()

# plt.savefig('TextTest02.png')