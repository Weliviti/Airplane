"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: 
 4. Date: 
****************************************************************************

"""
from graphics import *
import csv
import math

data_list = []

def load_csv(CSV_chosen):
    with open(CSV_chosen, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            data_list.append(row)

# ---------------------- TASK A FUNCTIONS -------------------------

def get_city_code():
    """Asks for and validates 3-letter airport code"""
    valid_codes = ["LHR","MAD","CDG","IST","AMS","LIS","FRA","FCO","MUC","BCN"]

    while True:
        code = input("Please enter a three-letter city code: ").upper()

        if len(code) != 3:
            print("Wrong code length - please enter a three-letter city code")
            continue
        
        if code not in valid_codes:
            print("Unavailable city code - please enter a valid city code")
            continue

        return code

def get_year():
    # ask user, validate, return year string
    pass

def build_filename(city, year):
    return city + year + ".csv"

# ---------------------- TASK B PROCESSING ------------------------

def calculate_outcomes():
    # loop through data_list and calculate all 10 outcomes
    # return them as a dictionary or list
    pass

def display_outcomes(outcomes):
    # print the formatted results exactly like the brief
    pass

# ---------------------- TASK C SAVE RESULTS ----------------------

def save_results(outcomes, airport_name, year):
    # append to results.txt
    pass

# ---------------------- TASK D HISTOGRAM -------------------------

def get_airline_code():
    # input + validation
    pass

def plot_histogram(airline_code, airport_name, year):
    # use graphics.py to draw histogram
    pass

# ---------------------- TASK E LOOPING ---------------------------

def main():
    while True:
        data_list.clear()

        city = get_city_code()
        year = get_year()
        filename = build_filename(city, year)
        load_csv(filename)

        outcomes = calculate_outcomes()
        display_outcomes(outcomes)

        save_results(outcomes, city, year)

        airline = get_airline_code()
        plot_histogram(airline, city, year)

        again = input("Do you want to select a new data file? Y/N: ").upper()
        if again == "N":
            print("Thank you. End of run")
            break

main()
