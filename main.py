# Yearly Budget and Expense Tracker
from tracker_functions import *

# Prints out the welcome message for the user
print_welcome_message()

# Prints out an introductory message telling the user to use the menu
print_menu_instructions()

is_exit = False

# Loop the main menu continuously until the user hits 8 to exit
while is_exit != True:

    # Print out the menu to the user
    print_menu_options()

    user_menu_choice = get_menu_choice()
    # Create a switch/match statement that acts as the menu for the program
    match user_menu_choice:
        case 1:
            menu_option_1()
        case 2:
            menu_option_2()
        case 3:
            menu_option_3()
        case 4:
            menu_option_4()
        case 5:
            menu_option_5()
        case 6:
            menu_option_6()
        case 7:
            is_exit = True
        case _:
            print("N/A")