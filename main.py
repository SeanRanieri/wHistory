import scrape
import menu
import monthly

# Main loop
while True:
    option = menu.get_option()

    if option == 1:
        monthly.summary()
    else:
        break
