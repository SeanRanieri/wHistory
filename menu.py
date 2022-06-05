menu_items = ['1. Monthly Temperature Summary']

# Ask user for option, then return it
def get_option():
    option = ''

    print('wHistory (pronounced WI-stə-ree)')
    print('All data belongs to CustomWeather\n\n')

    for item in menu_items:
        print(item)

    print(str(len(menu_items)+1) + '. Quit')

    while (not option) or (not option.isnumeric()) or (int(option) < 1 or int(option) > len(menu_items)+1):
        option = input('\nEnter an option: ')

    return int(option)
