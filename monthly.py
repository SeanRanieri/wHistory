import scrape

def summary():
    city = ''
    year = ''
    month = ''

    while not city:
        city = input('Enter a city: ')

    while (not year) or (not year.isnumeric()) or (int(year) < 2009):
        year = input('Enter a year: ')

    while (not month) or (not month.isnumeric()) or (int(month) < 1 or int(month) > 31):
        month = input('Enter a month: ')

    # calls request function in scrape.py module
    soup = scrape.request_month(city, year, month)

    table = soup.find('div', class_='dashb')

    data = table.find_all('td')

    print('\nSummary for ' + city + ' in ' + month + '/' + year)

    print(f'\nMax Temp: {data[0].text}\nMin Temp: {data[3].text}\nAvg Temp: {data[6].text}\n')

    input('\nPress Enter to Continue...')
