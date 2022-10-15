# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 01:56:09 2022

@author: Max-Louis
"""
from torrequest import TorRequest

# Choose a proxy port, a control port, and a password. 
# Defaults are 9050, 9051, and None respectively. 
# If there is already a Tor process listening the specified 
# ports, TorRequest will use that one. 
# Otherwise, it will create a new Tor process, 
# and terminate it at the end.
with TorRequest(proxy_port=9050, ctrl_port=9051, password="a1z2e3r4t5y6!!?") as tr:

  # Specify HTTP verb and url.
  resp = tr.get('http://google.com')
  print(resp.text)

  # Send data. Use basic authentication.
  resp = tr.post('https://api.example.com', 
    data={'foo': 'bar'}, auth=('user', 'pass'))
  print(resp.json)

  # Change your Tor circuit,
  # and likely your observed IP address.
  tr.reset_identity()

  # TorRequest object also exposes the underlying Stem controller 
  # and Requests session objects for more flexibility.

  print(type(tr.ctrl))            # a stem.control.Controller object
  tr.ctrl.signal('CLEARDNSCACHE') # see Stem docs for the full API

  print(type(tr.session))         # a requests.Session object
  c = cookielib.CookieJar()
  tr.session.cookies.update(c)    # see Requests docs for the full API