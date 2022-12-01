import requests
from bs4 import BeautifulSoup

# The URL I'm scraping is http://<IP_Address>/static/index.html
SCHEME = "http"
DOMAIN_NAME = "IP_Address" #Change this to your own attack IP
PORT = "80"
PATH_TO_FILE = "/static/index.html"

html = requests.get(SCHEME + "://" + DOMAIN_NAME + ":" + PORT + PATH_TO_FILE)

soup = BeautifulSoup(html.text, "lxml")

anchor_tags = soup.find_all("a", href=True)

for anchor in anchor_tags:
    if "api" in anchor["href"]:
        print(anchor)