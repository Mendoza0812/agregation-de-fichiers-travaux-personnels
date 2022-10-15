#  Install the Python Requests library:
# `pip install requests`
import requests
import socket

print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))

# Get the local host name

myHostName = socket.gethostname()

print("Name of the localhost is {}".format(myHostName))


# Get the IP address of the local host

myIP = socket.gethostbyname(myHostName)

print("IP address of the localhost is {}".format(myIP))

r = requests.get('https://github.com/')

#status code permet de savoir si l'url marche 
print(r.status_code)

hostName = "example.org"

ipAddress = socket.gethostbyname(hostName)

print("IP address of the host name {} is: {}".format(hostName, ipAddress))

