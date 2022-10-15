import pandas as pd

moncsv1 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')

idNom = moncsv1['IdNom']

colByName100 = idNom[0:]

var0 = 0
var1 = 1
colPrec = colByName100[var0]
colSuiv = colByName100[var1]

h = 1

idNom = []
nbParu = []

for colSuiv in colByName100[1:] :
    colPrec = colByName100.iloc[var0]
    colSuiv = colByName100.iloc[var1]
    if colSuiv != colPrec :
        print(colPrec)
        print(h)
        
        idNom.append(colPrec)
        nbParu.append(h)
        
        h = 1
    elif colSuiv == colPrec :
        h += 1
    else :
        print('Innatendu')
    var0 += 1
    var1 += 1
    
products_list = (idNom, nbParu)
df = pd.DataFrame (products_list).transpose()
df.columns = ['IdNom', 'nbParu']