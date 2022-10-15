# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 02:09:55 2022

@author: Max-Louis

dTRAVAIL A CONTINUER -- IL FAUDRA COMPTER LE NOMBRE DE PAGE PARSE
"""

from scrapingbee import ScrapingBeeClient
import socket
from bs4 import BeautifulSoup
import random

liSessionId = []
questChangId = 0
numSessionId = 0
client = ScrapingBeeClient(api_key='4UCRHF6WBJDH8A5TOGFIL60YMKNV34YIPQQEIX158AS121AW1H8DRHLH7DTL9IIBB9LT8MMTL2AZDQ8G')

for random7 in range (100):
    random7 = random.randrange(10E7)
    print(random7)
    liSessionId.append(random7)
    if numSessionId == 700:
        questChangId += 1
        numSessionId = 0
    else:
        numSessionId = numSessionId
        response = client.get('https://www.cnrtl.fr',
                              params = {
                                  'session_id': liSessionId[numSessionId],
                                  }
                              )
        numSessionId += 1

soup2 = BeautifulSoup(response.text, 'html.parser')
print(soup2.title)
print('Response HTTP Status Code: ', response.status_code)
print('Response HTTP Response Body: ', response.content)
print(socket.gethostbyname(socket.gethostname()))
myHostName = socket.gethostname()
myIP = socket.gethostbyname(myHostName)
print("IP address of the localhost is {}".format(myIP))
