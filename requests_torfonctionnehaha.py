# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 03:52:09 2022

@author: Max-Louis
"""

from requests_tor import RequestsTor

requestsTor = RequestsTor(tor_ports=(9050,), tor_cport=9051)

url = 'https://httpbin.org/anything'
requestsTorUrl = requestsTor.get(url)
print(requestsTorUrl .text)

urls = ['https://www.cnrtl.fr']
requestsTorUrls = requestsTor.get_urls(urls)
print(requestsTorUrls [-1].text)

requestsTorUrl.new_id()