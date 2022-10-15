# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:38:22 2022

@author: Max-Louis
"""

from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os

torexe = os.popen(r'C:\Users\Max-Louis\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
profile = FirefoxProfile(r'C:\Users\Max-Louis\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
profile.set_preference("network.proxy.socks_remote_dns", False)
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile= profile, executable_path=r'C:/Users/Max-Louis/geckodriver-v0.31.0-win64/geckodriver.exe')
driver.get("http://check.torproject.org")