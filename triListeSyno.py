import pandas as pd

moncsv1 = pd.read_csv(r'C:\Users\Max-Louis\.spyder-py3\projet_concept\bdd_az\deaazCSV.csv')

trilisteSyno = moncsv1.sort_values(by=['listeSyno'])

colMonCsv1 = moncsv1['listeSyno']
colByName = trilisteSyno['listeSyno']

var0 = 0
var1 = 1
h = 1
# changer colByName[0:] en colMonCsv1[0:] apres
colByName100 = colMonCsv1[0:]
colPrec = colByName100[var0]
colSuiv = colByName100[var1]

listeSyno = []
nbParu = []

for colSuiv in colByName100[1:] :
    colPrec = colByName100.iloc[var0]
    colSuiv = colByName100.iloc[var1]
    if colSuiv != colPrec :
        print(colPrec)
        print(h)
        
        listeSyno.append(colPrec)
        nbParu.append(h)
        
        h = 1
    elif colSuiv == colPrec :
        h += 1
    else :
        print('Innatendu')
    var0 += 1
    var1 += 1
    
products_list = (listeSyno, nbParu)
df = pd.DataFrame (products_list).transpose()
df.columns = ['listeSyno', 'nbParu']