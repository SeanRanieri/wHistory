menu_items = ['1. Monthly Summary', '2. Yearly Summary', '3. Monthly Rank']

# Ask user for option, then return it
def get_option():
    option = ''

    print('wHistory (pronounced WI-st\u01dd-ree)')
    print('All data belongs to CustomWeather\n\n')

    for item in menu_items:
        print(item)

    print(str(len(menu_items)+1) + '. Quit')

    while (not option) or (not option.isnumeric()) or (int(option) < 1 or int(option) > len(menu_items)+1):
        option = input('\nEnter an option: ')

    return int(option)
