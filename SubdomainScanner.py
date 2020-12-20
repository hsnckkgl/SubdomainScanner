import requests
import sys

#subdomains-10000.txt from https://github.com/rbsec/dnscan/blob/master/subdomains-10000.txt
sublist = open("subdomains10000.txt").read()
subs = sublist.splitlines()

for sub in subs:
    urltocheck = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(urltocheck)

    except requests.ConnectionError:
        pass
    else:
        print("Valid domain: ", urltocheck)