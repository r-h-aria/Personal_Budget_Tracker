# Import datetime module
import datetime

# Import regular expression module for decimal handling
import re

# Import csv to use csv file logic
import csv

# Import calendar for easy use of monthrange function to do valid checking for us
import calendar

# Import decimal to ensure accurate floating point values (not rounding .00 to .0 especially)
from decimal import Decimal, ROUND_HALF_UP

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

# Creates and initializes expense csv for correct month with headers (if it doesnt exist already)
def autocreate_expense_csv(month):    # Use the proper month expense file name
    filename = f"expenses_{month}_2025.csv"

    # Headers for the file
    expense_csv_headers = ["Date", "Category", "Description", "Amount"]

    try:
    # Open in exclusive write mode when file is not created, and write the headers
        with open(filename, "x", newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(expense_csv_headers)
    
    except FileExistsError:
        pass

    return filename
    
# Finds and Populates expense file with expense in proper csv file
def populate_expense_csv(month, day, category, description, amount):

    expense_filename = autocreate_expense_csv(month)
    # Slice string to format the date nicely
    format_date = f"{month[:3]}-{day}"

    # Write the expense to appropriately named csv file in append mode
    # so it just adds to the end of the file which is sorted later
    with open(expense_filename, 'a', newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow([format_date, category, description, amount])
    
    print(f"Your expense breakdown was updated for the month of {month} in {expense_filename}.\n")

# Get valid choice of day from the user for expense logging
def get_day_choice(month):
    
    # Make a dictionary that matches the month name to its number
    month_number_dictionary = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                               "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    
    # Year to check for leap year, and max_day_value for 28, 30, or 31 being max amount of days for given month
    year = 2025
    # monthrange takes in the year and the month as an integer, but then returns a tuple
    # first value of tuple is the starting day of month as integer 0-6, and second max numbers in the month. We want the second value. so index the tuple [1]
    max_day_value = calendar.monthrange(year, month_number_dictionary[month])[1]

    valid_day = False
    while valid_day != True:
        try:
            day = int(input(f"Please enter the day of the expense (1-{max_day_value}) for the month of {month}: "))

            if day >= 1 and day <= max_day_value:
                valid_day = True
            else:
                print(f"Invalid day: Must be between 1 and {max_day_value} for the month of {month}.\n")

        except ValueError:
            print("Invalid day: Enter an integer value.\n")
    # return the day as a 2 digit value (if only one digit, adds 0 at the front)
    return f"{day:02d}"

# Get category of the expense (needs, wants, savings)
def get_expense_category():
    valid_category = False

    # List of possible categories
    category_list = ["Needs", "Wants", "Savings"]

    while valid_category != True:
        try:
            user_category_choice = input("Please enter a category for the expense (Needs, Wants, Savings): ").capitalize()

            if user_category_choice in category_list:
                valid_category = True
            else:
                print("Invalid input: Please enter either 'Needs', 'Wants' or 'Savings'.\n")
        
        except ValueError:
            print("Invalid input: Please enter a string value.\n")
    
    return user_category_choice

# Get the amount of the expense, formatted and validated
def get_expense_amount():
    valid_amount = False

    while valid_amount != True:
            expense_amount = input("Please enter the amount of the expense: ").strip()

            # check for positive input and use regex to do string format checking (only 2 decimal places)
            if float(expense_amount) > 0 and re.match(r"^\d+\.\d{2}$", expense_amount):
                valid_amount = True
            else:
                print("Invalid input: Please enter a positive float value with exactly 2 decimal places.\n")

    return float(Decimal(expense_amount))

# Driver function for menu option #3
def menu_option_3():

    # Begin by getting the month for which the user would like to log an expense
    user_month_choice = get_month_choice()

    # Get the day of the expense
    user_day_choice = get_day_choice(user_month_choice)
    
    # Get user to choose the appropriate category of transaction
    user_category_choice = get_expense_category()

    # Get user to enter a description for the expense
    expense_description = input("Please enter a description for the expense: ")

    # Get the amount of the expense from the user
    expense_amount = get_expense_amount()

    # Populate the csv file with the expense
    populate_expense_csv(user_month_choice, user_day_choice, user_category_choice, expense_description, expense_amount)
