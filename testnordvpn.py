# -*- coding: utf-8 -*-
"""
Created on Tue May 10 00:51:49 2022

@author: Max-Louis
"""

from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN

settings = initialize_VPN() 
rotate_VPN(settings) 
rotate_VPN(settings,google_check=1) 
terminate_VPN(settings)