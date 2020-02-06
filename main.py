import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.basketball-reference.com/leagues/NBA_2020.html'

page = soup(requests.get(url).content, 'html.parser')
containers = page.findAll('div', {'id':'all_standings'})

obj = []

for i in containers:
    team_name = i.find('td', {'class': 'left'})
