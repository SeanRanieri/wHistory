import scrape

# Count number of digits in reading
def count_nums(str):
    nums = 0
    for i in range(0, 3):
        if str[i].isnumeric():
            nums += 1

    nums += 1 if '-' in str else 0
    return nums

# Return summary of yearly extremes
def summary():
    city = ''
    year = ''
    max_temp = '0  ';
    max_hum = '0  ';
    max_pres = '0  ';
    min_temp = '100';
    min_hum = '100';
    min_pres = '100';
    avg_temp = 0
    avg_hum = 0
    avg_pres = 0

    while not city:
        city = input('Enter a city: ')

    while (not year) or (not year.isnumeric()) or (int(year) < 2009):
        year = input('Enter a year (2009-): ')

    # Loop through 12 months of given year
    for i in range(1, 13):
        soup = scrape.request_month(city, year, str(i))
        table = soup.find('div', class_='dashb')
        data = table.find_all('td')

        # Check if weather reading is greater or less than that in variables
        max_temp = data[0].text if int(data[0].text[0:count_nums(data[0].text)]) > int(max_temp[0:count_nums(max_temp)]) else max_temp
        max_hum = data[1].text if int(data[1].text[0:count_nums(data[1].text)]) > int(max_hum[0:count_nums(max_hum)]) else max_hum
        max_pres = data[2].text if float(data[5].text[0:5]) > float(max_pres[0:5]) else max_pres
        min_temp = data[3].text if int(data[3].text[0:count_nums(data[3].text)]) < int(min_temp[0:count_nums(min_temp)]) else min_temp
        min_hum = data[4].text if int(data[4].text[0:count_nums(data[4].text)]) < int(min_hum[0:count_nums(min_hum)]) else min_hum
        min_pres = data[5].text if float(data[5].text[0:5]) < float(min_pres[0:5]) else min_pres

        avg_temp += int(data[6].text[0:count_nums(data[6].text)])
        avg_hum += int(data[7].text[0:count_nums(data[7].text)])
        avg_pres += int(data[8].text[0:count_nums(data[8].text)])

    avg_temp /= 12
    avg_hum /= 12
    avg_pres /= 12

    print('\nSummary for ' + city + ' in ' + year)

    print(f'\nMax Temperature: {max_temp}\nMax Humidity: {max_hum}\nMax Pressure: {max_pres}\n')
    print(f'\nMin Temperature: {min_temp}\nMin Humidity: {min_hum}\nMin Pressure: {min_pres}\n')
    print(f'\nAvg Temperature: {avg_temp: .2f} \u00b0F\nAvg Humidity: {avg_hum: .2f}%\nAvg Pressure: {avg_pres: .2f} "Hg\n')

    input('\nPress Enter to Continue...')
