import scrape
from datetime import date

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


    if not scrape.data_exists(city, year, month):
        print('Data does not exist for this month. Please try a different month.\n')

    else:
        # Call request function in scrape.py module
        soup = scrape.request_month(city, year, month)

        table = soup.find('div', class_='dashb')

        data = table.find_all('td')

        print('\nSummary for ' + city + ' in ' + month + '/' + year)

        print(f'\nMax Temperature: {data[0].text}\nMax Humidity: {data[1].text}\nMax Pressure: {data[2].text}\n')
        print(f'\nMin Temperature: {data[3].text}\nMin Humidity: {data[4].text}\nMin Pressure: {data[5].text}\n')
        print(f'\nAvg Temperature: {data[6].text}\nAvg Humidity: {data[7].text}\nAvg Pressure: {data[8].text}\n')

        input('\nPress Enter to Continue...')

def rank():
    city = ''
    m_choice = 0
    months = []
    m_sort = None

    while not city:
        city = input('Enter a city: ')

    m_choice = input('What month do you want to rank? (1-12, leave blank to rank all months): ')

    print('Loading... (This could take a couple minutes)\n')

    if not (m_choice.isnumeric()) or (int(m_choice) > 12) or (int(m_choice) < 1):
        no_data = False
        for year in range(int(date.today().year)-1, 2008, -1):
            for month in range(12, 0, -1):
                if not scrape.data_exists(city, year, month):
                    no_data = True
                    break
                soup = scrape.request_month(city, year, month)
                table = soup.find('div', class_='dashb')
                data = table.find_all('td')

                months.append({f'{month}/{year}': data})
            if no_data:
                break

    else:
        for year in range(int(date.today().year)-1, 2008, -1):
            if not scrape.data_exists(city, year, m_choice):
                break

            soup = scrape.request_month(city, year, m_choice)
            table = soup.find('div', class_='dashb')
            data = table.find_all('td')

            months.append({f'{m_choice}/{year}': data})

    while True:

        type = '0'
        order = '0'

        while (not type.isnumeric()) or (int(type) < 1) or (int(type) > 4):
            type = input('What would you like to sort by?\n\n1) Temperature\n2) Humidity\n3) Pressure\n4) Quit\n: ')

        if type == '4':
            break

        while (not order.isnumeric()) or (int(order) < 1) or (int(order) > 2):
            order = input('How would you like to sort?\n\n1) Ascending\n2) Descending\n:')

        if type == '1':
            m_sort = lambda m: list(m.values())[0][6].text[0:scrape.count_nums(list(m.values())[0][6].text)]
            months.sort(reverse=(order=='2'), key=m_sort)
            for m in months:
                print(f'{list(m.keys())[0]}: {list(m.values())[0][6].text}')

        elif type == '2':
            m_sort = lambda m: list(m.values())[0][7].text[0:scrape.count_nums(list(m.values())[0][7].text)]
            months.sort(reverse=(order=='2'), key=m_sort)
            for m in months:
                print(f'{list(m.keys())[0]}: {list(m.values())[0][7].text}')

        else:
            m_sort = lambda m: float(list(m.values())[0][8].text[0:5])
            months.sort(reverse=(order=='2'), key=m_sort)
            for m in months:
                print(f'{list(m.keys())[0]}: {list(m.values())[0][8].text}')


    input('\nPress Enter to Continue...')
