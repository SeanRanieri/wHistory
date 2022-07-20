import requests
from bs4 import BeautifulSoup

def request_month(city, year, month):
    URL = 'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=' + str(month) + '&year=' + str(year)
    page = requests.get(URL)
    return BeautifulSoup(page.content, 'html.parser')

# Check if data exists at a certain month and year
def data_exists(city, year, month):
    soup = request_month(city, str(year), str(month))
    header = soup.find_all(class_='headline-banner__title')[0].text
    if '2 Weeks' in header:
        return False
    return True

# Count number of digits in reading
def count_nums(str):
    nums = 0
    for i in range(0, 3):
        if str[i].isnumeric():
            nums += 1

    nums += 1 if '-' in str else 0
    return nums
