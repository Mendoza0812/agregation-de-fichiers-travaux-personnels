# -*- coding: utf-8 -*-
"""
Created on Tue May 31 00:47:08 2022

@author: Max-Louis
"""
import pandas as pd
listeSynoaz = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\lystazInit.csv')

variable = 0
variable1 = 1

initLysLys = listeSynoaz['InitLyS']

prec = ''
suiv = ''

while variable <= 382550:
    #a
        if initLysLys[variable] == 'a' :
            suiv = initLysLys[variable]
            variable += 1
    #b
        elif initLysLys[variable] == 'b' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('b ' +  str(variable))
                prec = suiv
            variable += 1
            
        elif initLysLys[variable] == 'c' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('b ' +  str(variable))
                prec = suiv
            variable += 1
        
        elif initLysLys[variable] == 'd' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('d ' +  str(variable))
                prec = suiv
            variable += 1
            
        elif initLysLys[variable] == 'e' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('e ' +  str(variable))
                prec = suiv
            variable += 1
            
        elif initLysLys[variable] == 'f' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('f ' +  str(variable))
                prec = suiv
            variable += 1
            
        elif initLysLys[variable] == 'g' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('b ' +  str(variable))
                prec = suiv
            variable += 1
        
        elif initLysLys[variable] == 'g' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('d ' +  str(variable))
                prec = suiv
            variable += 1
            
        elif initLysLys[variable] == 'h' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('e ' +  str(variable))
                prec = suiv
            variable += 1
            
        elif initLysLys[variable] == 'i' :
             suiv = initLysLys[variable]
             if prec != suiv:
                 print('i ' +  str(variable))
                 prec = suiv
             variable += 1
             
        elif initLysLys[variable] == 'j' :
             suiv = initLysLys[variable]
             if prec != suiv:
                 print('j ' +  str(variable))
                 prec = suiv
             variable += 1
         
        elif initLysLys[variable] == 'k' :
             suiv = initLysLys[variable]
             if prec != suiv:
                 print('k ' +  str(variable))
                 prec = suiv
             variable += 1
             
        elif initLysLys[variable] == 'l' :
             suiv = initLysLys[variable]
             if prec != suiv:
                 print('l ' +  str(variable))
                 prec = suiv
             variable += 1
             
        elif initLysLys[variable] == 'm' :
             suiv = initLysLys[variable]
             if prec != suiv:
                 print('m ' +  str(variable))
                 prec = suiv
             variable += 1
             
        elif initLysLys[variable] == 'n' :
             suiv = initLysLys[variable]
             if prec != suiv:
                 print('n ' +  str(variable))
                 prec = suiv
             variable += 1
         
        elif initLysLys[variable] == 'o' :
             suiv = initLysLys[variable]
             if prec != suiv:
                 print('o ' +  str(variable))
                 prec = suiv
             variable += 1
             
        elif initLysLys[variable] == 'p' :
             suiv = initLysLys[variable]
             if prec != suiv:
                 print('p ' +  str(variable))
                 prec = suiv
             variable += 1
             
        elif initLysLys[variable] == 'q' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('q ' +  str(variable))
                prec = suiv
            variable += 1
            
        elif initLysLys[variable] == 'r' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('r ' +  str(variable))
                prec = suiv
            variable += 1
        
        elif initLysLys[variable] == 's' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('s ' +  str(variable))
                prec = suiv
            variable += 1
            
        elif initLysLys[variable] == 't' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('t ' +  str(variable))
                prec = suiv
            variable += 1
            
        elif initLysLys[variable] == 'u' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('u ' +  str(variable))
                prec = suiv
            variable += 1
            
        elif initLysLys[variable] == 'v' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('v ' +  str(variable))
                prec = suiv
            variable += 1
        
        elif initLysLys[variable] == 'w' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('w ' +  str(variable))
                prec = suiv
            variable += 1
            
        elif initLysLys[variable] == 'x' :
            suiv = initLysLys[variable]
            if prec != suiv:
                print('x ' +  str(variable))
                prec = suiv
            variable += 1
            
        elif initLysLys[variable] == 'y' :
             suiv = initLysLys[variable]
             if prec != suiv:
                 print('y ' +  str(variable))
                 prec = suiv
             variable += 1
             
        elif initLysLys[variable] == 'z' :
             suiv = initLysLys[variable]
             if prec != suiv:
                 print('z ' +  str(variable))
                 prec = suiv
             variable += 1
        else :
            variable += 1