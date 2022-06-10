import requests
from bs4 import BeautifulSoup as BS

source = ("https://store.epicgames.com/pt-BR/free-games")

site = requests.get(source).content

soup = BS(site, "html5lib")

print(soup.find_all(class_="css-1h2ruwl"))