# Import datetime module
import datetime

# Import regular expression module for decimal handling
import re

# Import csv to use csv file logic
import csv

# Import prettytable to print out nice tables in the terminal
from prettytable import PrettyTable

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
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    print()
    while valid_month != True:
        try:
            user_month_choice = input("Please enter the name of the month for which you would like to log an entry: ").capitalize() # .capitalize to set first letter to upper, rest lower
            # check if what user entered is in the month_list - if it is then we break out of loop
            if user_month_choice in month_list:
                valid_month = True
            else:
                print("Invalid month name.\n")

        except ValueError:
            print("Invalid input: Value must be a string.\n")

    return user_month_choice

# Gets user's income for a month
def get_month_income(month):
    valid_income = False

    while valid_income == False:
        try:

            user_month_income = int(input("Please enter your income for " + month + ": "))

            # check if the amount entered is a positive number and entered with 2 digits after the decimal (Credit to copilot for using regular expression to read string info)
            if user_month_income > 0:
                valid_income = True
            else:
                print("Please enter a positive income amount.\n")

        except ValueError:
            print("Please enter an integer value.\n")
    return user_month_income
    
# Populates the contents of a month row in the budget csv file
def populate_month_budget_csv(month, income, needs, wants, savings):
    # File name for the csv
    budget_csv_filename = "budget_2025.csv"

    # To find the correct area to populate, we open in read mode and populate a list first
    with open(budget_csv_filename, 'r') as infile:
        reader = csv.reader(infile)
        data = list(reader)

    # Loop through each row in the list
    for row in data:
        # Look at each column 0, and if we find matching month name, populate that rows columns appropriately and break out
        if row[0] == month:
            row[1] = income
            row[2] = needs
            row[3] = wants
            row[4] = savings
            break

    # Since we want to populate, we open in write mode and write in data list to update
    with open(budget_csv_filename, 'w', newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)
    
    # Let the user know the csv was successfully updated with the values
    print("Your income and budget category breakdown was updated in " + budget_csv_filename + "\n")

# Driver function for menu option #1
def menu_option_1():
    # Get user to choose month they'd like to log income for
    month_choice = get_month_choice()

    # Get user to enter their income for the month they chose
    month_income = get_month_income(month_choice)

    # Calculate budget categories breakdown for the month and store into separate variables - round to 2 dec places
    needs = round(month_income * 0.50)
    wants = round(month_income * 0.30)
    savings = round(month_income * 0.20)

    # Log to budget csv file under that month
    populate_month_budget_csv(month_choice, month_income, needs, wants, savings)

    # Ask to return to menu or quit
    menu_or_quit()

# Type menu to go back to the menu, or quit to quit the program
def menu_or_quit():
    is_menu = False

    while is_menu != True:
        try:
            user_choice = input("Please type 'menu' if you would like to go back to the menu, or 'quit' if you would like to quit the program: ")

            # If they enter menu, we can just break out of the loop and the while loop in main takes care of it
            # Otherwise, it quits the program
            if user_choice == "menu":
                is_menu = True
            elif user_choice == "quit":
                exit()
            else:
                print("Please enter either 'menu' or 'quit'\n")

        except ValueError:
            print("Please enter a string value containing either 'menu' or 'quit'\n")

# Generate and print table of budget breakdown
def print_budget_csv():

    # Header names for the table
    table = PrettyTable(["Month", "Income", "Needs", "Wants", "Savings"])

    # File name for the csv
    budget_csv_filename = "budget_2025.csv"

    # Read data into a list so we can use it
    with open(budget_csv_filename, 'r') as infile:
        reader = csv.reader(infile)
        data = list(reader)

    # For each row in the list starting from row 1, we write it to the table
    for row in data[1:]:
        table.add_row(row)
    
    print(table)

# Driver function for menu option #2
def menu_option_2():
    # Print the budget csv as a table in the terminal
    print_budget_csv()
    print()
    menu_or_quit()

