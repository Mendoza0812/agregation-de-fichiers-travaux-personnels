# -*- coding: utf-8 -*-
"""
Created on Sun May  8 18:12:55 2022

@author: Max-Louis
"""

from scrapingbee import ScrapingBeeClient
from bs4 import BeautifulSoup
import random
import re
import pandas as pd


lim = []
lnm = []
lpSyno = []
lSyno = []
lp4 = []

premUrl = "https://www.cnrtl.fr/portailindex/SYNO//A/0"
debutUrl = "https://www.cnrtl.fr"
print(premUrl)

client = ScrapingBeeClient(api_key='4UCRHF6WBJDH8A5TOGFIL60YMKNV34YIPQQEIX158AS121AW1H8DRHLH7DTL9IIBB9LT8MMTL2AZDQ8G')

html2 = client.get(premUrl).text
soup2 = BeautifulSoup(html2, 'html.parser')

letterHeader = soup2.find('table', class_ = 'letterHeader')
tdletterSelected = letterHeader.find("td")
trLetterHeader = letterHeader.find('tr')

def traitmtLstMots():
    
    url = premUrl
    
    random8 = random.randrange(10E7)
    
    debutUrl = "https://www.cnrtl.fr"
    html = client.get(url,
                     params ={
                         "session_id": random8}).text
    soup = BeautifulSoup(html, 'html.parser')

    homeTab = soup.find('table', class_ = "hometab")
    lienSyn = homeTab.find_all('a')
    
    for link in lienSyn:
        url2 = debutUrl + link.get('href')
        print(url2)
        motRef = link.text
        print(motRef)
        
        random9 = random.randrange(10E7)
        html2 = client.get(url2,
                           params= {
                               "session_id": random9}).text
        soup2 = BeautifulSoup(html2, 'html.parser')
        vToolBar = soup2.find('div', id = 'vtoolbar').ul
        liMot = vToolBar.find('li').text

        form = soup2.find('form', id = 'reqform')
        valForm = form.input['value'].upper()
        
        seq_listIdMot = []
        seq_listNatMot = []

        #Suite vérification onglet (liMot)/formulaire (valForm) de vToolBar
        nbrMot = -1
        for liMot in vToolBar:
        
            nbrMot += 1
            print(nbrMot)
            
            spanLM = liMot.span.text
            textLM = str(liMot.text)
            natMot = re.sub("[A-Z_À-ÿ\-, ]", "", textLM)
            seq_listIdMot.append(spanLM)
            seq_listNatMot.append(natMot)
        
            lmao = liMot.a['onclick']
            stringlmao = str(lmao)
#           restrlmao = re.findall(r"'(.*?)'", stringlmao)
            restrlmao = re.findall( "\(5\,'(.*?)'\)", stringlmao)
            srslmao = str(restrlmao)
            msrslmao = srslmao[2:-2]
        
            if valForm == spanLM:
            
                print("TRUE Executer listeSyno du fichier cnrtl6")
                url3 = debutUrl + msrslmao
                print(url3)
                
                random10 = random.randrange(10E7)
                
                html3 = client.get(url3,
                                   params = {
                                       "session_id": random10}).text
                
                soup3 = BeautifulSoup(html3, 'html.parser')
                lightFrame = soup3.find("table", class_ = "light_frame")
                tBody = lightFrame.find_all('tr')
                uneLigne = lightFrame.find('tr')
                nbrLigne = 0
                natMot1 = seq_listNatMot[nbrMot]
                idMot1 = seq_listIdMot[nbrMot]
                sim1 = str(idMot1)
            
                for uneLigne in tBody :
                    
                    sim1low = sim1.lower()
                    lim.append(sim1low)
                    
                    lnm.append(natMot1)
                    val = uneLigne.img['width']
                    textSyn3 = uneLigne.text
                    
                    lp4.append(val)
                    
                    lSyno.append(textSyn3)
                    nbrLigne += 1
                    lpSyno.append(nbrLigne)
                
            elif valForm != spanLM:
                print("FALSE")
            else:
                print("ERROR")
        print("Test valForm / spanLM fin ---")
        
def has_no_a(flecheDroite1):
    return not flecheDroite1.find('a')

        
for tdLetterSelected in trLetterHeader:
    hrefLetter = tdLetterSelected.find("a").get('href')
    print(hrefLetter)
    premUrl = debutUrl + hrefLetter
    print(premUrl)
    while True:
        
        random7 = random.randrange(10E7)
        html1 = client.get(premUrl,
                           params = {
                               'session_id': random7}).text
        soup1 = BeautifulSoup(html1, 'html.parser')
        traitmtLstMots()
        fleches1 = soup1.find('table', class_ = 'hometab').find_next_sibling('table')
        flecheDroite1 = fleches1.find('td').find_next_sibling('td')
        if has_no_a(flecheDroite1):
            print("It doesn't work")            
            break
    
        hrefPageSuiv1 = flecheDroite1.find('a').get('href')
        lienSuiv1 = debutUrl + hrefPageSuiv1
        premUrl = lienSuiv1
        


products_list = (lim, lnm, lSyno, lp4, lpSyno)
df = pd.DataFrame (products_list).transpose()
df.columns = ['IdNom', 'NatNom', 'listeSyno', 'val400', 'placeSyno']
print(df)