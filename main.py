import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.basketball-reference.com/leagues/NBA_2020.html'

page = soup(requests.get(url).content, 'html.parser')
tables = page.findAll('th', {"scope" : "row"})

obj = []

for i,t in enumerate(tables):
    print(i, ": ", t.text)
    obj.append(t.text)
for i in obj:
    print(i)
