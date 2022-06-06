import scrape

def summary():
    city = ''
    year = ''
    month = ''

    while not city:
        city = input('Enter a city: ')

    while (not year) or (not year.isnumeric()) or (int(year) < 2009):
        year = input('Enter a year (2009-): ')

    while (not month) or (not month.isnumeric()) or (int(month) < 1 or int(month) > 31):
        month = input('Enter a month: ')

    # Call request function in scrape.py module
    soup = scrape.request_month(city, year, month)

    table = soup.find('div', class_='dashb')

    data = table.find_all('td')

    print('\nSummary for ' + city + ' in ' + month + '/' + year)

    print(f'\nMax Temperature: {data[0].text}\nMax Humidity: {data[1].text}\nMax Pressure: {data[2].text}\n')
    print(f'\nMin Temperature: {data[3].text}\nMin Humidity: {data[4].text}\nMin Pressure: {data[5].text}\n')
    print(f'\nAvg Temperature: {data[6].text}\nAvg Humidity: {data[7].text}\nAvg Pressure: {data[8].text}\n')

    input('\nPress Enter to Continue...')
