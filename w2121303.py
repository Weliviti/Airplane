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
    """Asks for and validates 4-digit year"""
    while True:
        year = input("Please enter the year required in the format YYYY: ")

        if not year.isdigit() or len(year) != 4:
            print("Wrong data type - please enter a four-digit year value")
            continue

        year_int = int(year)
        if year_int < 2000 or year_int > 2025:
            print("Out of range - please enter a value from 2000 to 2025")
            continue

        return year

def build_filename(city, year):
    return city + year + ".csv"

# ---------------------- TASK B PROCESSING ------------------------

def calculate_outcomes():
    """Process all 10 outcomes from the coursework"""
    # YOU will fill this part later
    outcomes = {
        "total_flights": 0,
        "terminal2": 0,
        "under600": 0,
        "airfrance": 0,
        "below15": 0,
        "ba_avg": 0,
        "ba_percent": 0,
        "af_delay_percent": 0,
        "rain_hours": 0,
        "least_common_destinations": []
    }
    return outcomes

def display_outcomes(outcomes):
    """Nicely prints the result in correct coursework format"""
    print("*********************************************************************************")
    print(f"File {filename} selected - Planes departing {airport_name} {year}")
    print("*********************************************************************************")

# ---------------------- TASK C SAVE RESULTS ----------------------

def save_results(outcomes, airport_name, year):
    """Appends current results to results.txt"""
    with open("results.txt", "a") as f:
        f.write(f"\nResults for {airport_name} - {year}\n")
        f.write("-------------------------------------\n")

# ---------------------- TASK D HISTOGRAM -------------------------

def get_airline_code():
    """Asks user for airline code and validates it"""
    valid_airlines = ["BA","AF","AY","KL","SK","TP","TK","W6","U2","FR","A3","SN","EK","QR","IB","LH"]

    while True:
        code = input("Enter a two-character Airline code to plot a histogram: ").upper()

        if code not in valid_airlines:
            print("Unavailable Airline code please try again.")
            continue

        return code
def plot_histogram(airline_code, airport_name, year):
    # use graphics.py to draw histogram
    pass

# ---------------------- TASK E LOOPING ---------------------------

def main():
    while True:
        data_list.clear()

        # Task A
        airport = get_airport_code()
        year = get_year()
        filename = build_filename(airport, year)

        load_csv(filename)

        # Task B
        outcomes = calculate_outcomes()
        airport_full_name = ""   # YOU will map code to full name later
        display_outcomes(outcomes, airport_full_name, year, filename)

        # Task C
        save_results(outcomes, airport_full_name, year)

        # Task D
        airline_code = get_airline_code()
        plot_histogram(airline_code, airport_full_name, year)

        # Task E
        again = input("Do you want to select a new data file? Y/N: ").upper()
        if again == "N":
            print("Thank you. End of run")
            break

main()

