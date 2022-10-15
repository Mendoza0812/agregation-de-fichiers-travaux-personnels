import requests
from bs4 import BeautifulSoup

chose_synurl = "https://www.cnrtl.fr/synonymie/chose"
html_synchose = requests.get(chose_synurl).text
soupsynchose = BeautifulSoup(html_synchose, 'html.parser')

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

