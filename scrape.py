import requests
from bs4 import BeautifulSoup

def request_month(city, year, month):
    URL = 'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=' + month + '&year=' + year
    page = requests.get(URL)
    return BeautifulSoup(page.content, 'html.parser')
