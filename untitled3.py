# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:02:22 2022

@author: Max-Louis
"""

import requests

url = "https://www.google.fr"

http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://170.155.5.235:8080"
ftp_proxy   = "ftp://10.10.1.10:3128"

proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

r = requests.get(url, proxies=proxies)