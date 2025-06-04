# Import datetime module
import datetime

# Credit to patorjk.com for an ASCII title art text generator
# Prints out the welcome message title art for the budget tracker
def print_welcome_message():
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
    "/$$$$$$$                                                             /$$       /$$$$$$$                  /$$                       /$$           /$$$$$$$$                           /$$                           \n"
    "| $$__  $$                                                           | $$      | $$__  $$                | $$                      | $$          |__  $$__/                          | $$                          \n"
    "| $$  \ $$ /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$ | $$      | $$  \ $$ /$$   /$$  /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$           | $$  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ \n"
    "| $$$$$$$//$$__  $$ /$$__  $$ /$$_____/ /$$__  $$| $$__  $$ |____  $$| $$      | $$$$$$$ | $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/           | $$ /$$__  $$|____  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$\n"
    "| $$____/| $$$$$$$$| $$  \__/|  $$$$$$ | $$  \ $$| $$  \ $$  /$$$$$$$| $$      | $$__  $$| $$  | $$| $$  | $$| $$  \ $$| $$$$$$$$  | $$             | $$| $$  \__/ /$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/\n"
    "| $$     | $$_____/| $$       \____  $$| $$  | $$| $$  | $$ /$$__  $$| $$      | $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$_____/  | $$ /$$         | $$| $$      /$$__  $$| $$      | $$_  $$ | $$_____/| $$      \n"
    "| $$     |  $$$$$$$| $$       /$$$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$| $$      | $$$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$  |  $$$$/         | $$| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      \n"
    "|__/      \_______/|__/      |_______/  \______/ |__/  |__/ \_______/|__/      |_______/  \______/  \_______/ \____  $$ \_______/   \___/           |__/|__/      \_______/ \_______/|__/  \__/ \_______/|__/      \n"
    "                                                                                                              /$$  \ $$                                                                                            \n"
    "                                                                                                             |  $$$$$$/                                                                                            \n"
    "                                                                                                              \______/                                                                                             \n"
    "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n")

# Prints out instruction prompt for using the main menu
def print_menu_instructions():
    print("Please choose an option from the menu below by entering the number associated with the option.\n")

# Prints out the actual menu options for the user
def print_menu_options():
    print(r"""
*******************************************
*        1) Enter monthly income          *
*        2) View budget breakdown         *
*        3) Log an expense                *  
*        4) Remove an expense             *
*        5) View expense history          *
*        6) Check remaining budget        *
*        7) Generate spending report      *
*        8) Exit                          *
*******************************************
                                           """)
    
# Obtains user's input for choice of menu option. Performs basic input validation and loops till user enters valid option
def get_menu_choice():
    # initial variable to act as loop termination
    valid_choice = False

    # If valid choice is input, breaks out of the loop and returns the integer 
    # Uses try and except to filter out invalid data types too
    while valid_choice != True:
        try:
            user_menu_choice = int(input("Please enter a number corresponding to an option: "))
            if user_menu_choice >= 0 and user_menu_choice <= 8:
                valid_choice = True
            else:
                print("Invalid integer: Input must be between 0 and 8 (inclusive).\n")
        except ValueError:
            print("Invalid input: Value must be an integer.\n")

    return user_menu_choice

# Re-usable function that asks the user to enter in a month
def get_month_choice():
    valid_month = False
    # list of months to easily check input
    month_list = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

    while valid_month != True:
        try:
            user_month_choice = input("Please enter the name of the month for which you would like to log an entry: ").lower() # .lower to allow mis-capitalization

            # check if what user entered is in the month_list - if it is then we break out of loop
            if user_month_choice in month_list:
                valid_month = True
            else:
                print("Invalid month name.\n")

        except ValueError:
            print("Invalid input: Value must be a string.\n")

    return user_month_choice
            

        
    



