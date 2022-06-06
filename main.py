import menu
import monthly
import yearly

# Main loop
while True:
    option = menu.get_option()

    if option == 1:
        monthly.summary()
    elif option == 2:
        yearly.summary()
    else:
        break
