"""
****************************************************************************
Additional info
 1. I declare that my work contains no examples of misconduct, such as
    plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID:
 4. Date:
****************************************************************************

This program analyses European airport departure data.
It loads a CSV file chosen by the user, validates inputs,
computes different outcomes, saves them to a results file,
draws a histogram using graphics.py, and allows repeated runs.
"""

from graphics import *
import csv
import os

# ------------------------------------------------------------------------
# GLOBAL VARIABLES
# ------------------------------------------------------------------------

# This list will store all rows from any loaded CSV file
data_list = []

# Valid airport codes and full airport names (from coursework table)
AIRPORTS = {
    "LHR": "London Heathrow",
    "MAD": "Madrid Adolfo Suárez-Barajas",
    "CDG": "Charles De Gaulle International",
    "IST": "Istanbul Airport International",
    "AMS": "Amsterdam Schiphol",
    "LIS": "Lisbon Portela",
    "FRA": "Frankfurt Main",
    "FCO": "Rome Fiumicino",
    "MUC": "Munich International",
    "BCN": "Barcelona International"
}

# Valid airlines and full airline names
AIRLINES = {
    "BA": "British Airways",
    "AF": "Air France",
    "AY": "Finnair",
    "KL": "KLM",
    "SK": "Scandinavian Airlines",
    "TP": "TAP Air Portugal",
    "TK": "Turkish Airlines",
    "W6": "Wizz Air",
    "U2": "easyJet",
    "FR": "Ryanair",
    "A3": "Aegean Airlines",
    "SN": "Brussels Airlines",
    "EK": "Emirates",
    "QR": "Qatar Airways",
    "IB": "Iberia",
    "LH": "Lufthansa"
}

# ------------------------------------------------------------------------
# BASIC FUNCTIONS
# ------------------------------------------------------------------------

def clear_data():
    """Clears the global data_list before loading a new CSV."""
    global data_list
    data_list = []


def load_csv(filename):
    """
    Loads a CSV file by name and fills data_list.
    The CSV must be in the same folder as this file.
    """
    clear_data()
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            if row:
                data_list.append(row)


# ------------------------------------------------------------------------
# INPUT VALIDATION FUNCTIONS
# ------------------------------------------------------------------------

def get_valid_airport_code():
    """Asks user for a valid 3-letter airport code."""
    while True:
        user_input = input("please enter a three-letter city code: ")
        if len(user_input) != 3:
            print("Wrong code length - please enter a three-letter city code:", end="")
            continue

        code = user_input.upper()
        if code not in AIRPORTS:
            print("Unavailable city code - please enter a valid citycode:", end="")
            continue

        return code


def get_valid_year():
    """Asks user for a valid year between 2000–2025."""
    while True:
        user_input = input("Please enter the year required in the format YYYY: ")

        if not (user_input.isdigit() and len(user_input) == 4):
            print("Wrong data type - please enter a four-digit year value:", end="")
            continue

        year = int(user_input)
        if not (2000 <= year <= 2025):
            print("Out of range - please enter a value from 2000 to 2025:", end="")
            continue

        return year


def get_valid_airline():
    """Asks user for a valid 2-letter airline code."""
    while True:
        user_input = input("Enter a two-character Airline code to plot a histogram: ")

        if len(user_input) != 2:
            print("Unavailable Airline code please try again:", end="")
            continue

        code = user_input.upper()
        if code not in AIRLINES:
            print("Unavailable Airline code please try again:", end="")
            continue

        return code


# ------------------------------------------------------------------------
# HELPER FUNCTIONS FOR ANALYSIS
# ------------------------------------------------------------------------

def extract_hour(time_string):
    """Return the hour part from a time like '09:15'."""
    try:
        return int(time_string.split(":")[0])
    except:
        return None


def extract_temperature(weather_string):
    """Extract a temperature like '18°C clear'."""
    try:
        temp = ""
        for char in weather_string:
            if char.isdigit() or char == "-":
                temp += char
        return int(temp)
    except:
        return None


# ------------------------------------------------------------------------
# ANALYSIS (TASK B)
# ------------------------------------------------------------------------

def analyse_data():
    """Calculates all Task B results and returns them in a dictionary."""
    results = {}

    total_flights = len(data_list)
    results["total_flights"] = total_flights

    terminal2 = 0
    under600 = 0
    air_france = 0
    temp_below_15 = 0
    ba_total = 0
    af_delayed = 0
    af_total = 0

    rain_hours = set()
    destination_count = {}

    for row in data_list:
        terminal = row[8]
        distance = int(row[5])
        airline = row[1][:2].upper()
        weather = row[10]
        scheduled = row[2]
        actual = row[3]
        destination = row[4]

        # Terminal 2
        if terminal == "2":
            terminal2 += 1

        # Distance under 600 miles
        if distance < 600:
            under600 += 1

        # Air France
        if airline == "AF":
            air_france += 1
            af_total += 1
            if scheduled != actual:
                af_delayed += 1

        # British Airways
        if airline == "BA":
            ba_total += 1

        # Temperature below 15
        temp = extract_temperature(weather)
        if temp is not None and temp < 15:
            temp_below_15 += 1

        # Rain
        if "rain" in weather.lower():
            hour = extract_hour(scheduled)
            if hour is not None:
                rain_hours.add(hour)

        # Destination counts
        destination_count[destination] = destination_count.get(destination, 0) + 1

    # BA averages
    results["terminal2"] = terminal2
    results["under600"] = under600
    results["air_france"] = air_france
    results["temp_below_15"] = temp_below_15

    results["avg_ba"] = round(ba_total / 12, 2)
    results["ba_percent"] = round((ba_total / total_flights) * 100, 2)

    if af_total > 0:
        results["af_delay_percent"] = round((af_delayed / af_total) * 100, 2)
    else:
        results["af_delay_percent"] = 0

    results["rain_hours"] = len(rain_hours)

    # Least common destination
    min_value = min(destination_count.values())
    least = [AIRPORTS.get(code, code) for code, count in destination_count.items() if count == min_value]
    results["least_destinations"] = least

    return results


# ------------------------------------------------------------------------
# OUTPUT FORMAT (TASK B)
# ------------------------------------------------------------------------

def display_results(filename, airport, year, results):
    """Prints all Task B results neatly."""
    print("****************************************************************************")
    print(f"File {filename} selected - Planes departing {AIRPORTS[airport]} {year}")
    print("****************************************************************************")

    print(f"The total number of flights from this airport was {results['total_flights']}")
    print(f"The total number of flights departing Terminal Two was {results['terminal2']}")
    print(f"The total number of departures on flights under 600 miles was {results['under600']}")
    print(f"There were {results['air_france']} Air France flights from this airport")
    print(f"There were {results['temp_below_15']} flights departing in temperatures below 15 degrees")
    print(f"There was an average of {results['avg_ba']} British Airways flights per hour from this airport")
    print(f"British Airways planes made up {results['ba_percent']}% of all departures")
    print(f"{results['af_delay_percent']}% of Air France departures were delayed")
    print(f"There were {results['rain_hours']} hours in which rain fell")
    print(f"The least common destinations are {results['least_destinations']}")


# ------------------------------------------------------------------------
# TASK C: SAVE RESULTS
# ------------------------------------------------------------------------

def save_results(filename, airport, year, results):
    """Appends results to results.txt."""
    with open("results.txt", "a") as f:
        f.write("****************************************************************************\n")
        f.write(f"File {filename} selected - Planes departing {AIRPORTS[airport]} {year}\n")
        f.write("****************************************************************************\n")
        f.write(f"The total number of flights from this airport was {results['total_flights']}\n")
        f.write(f"The total number of flights departing Terminal Two was {results['terminal2']}\n")
        f.write(f"The total number of departures on flights under 600 miles was {results['under600']}\n")
        f.write(f"There were {results['air_france']} Air France flights from this airport\n")
        f.write(f"There were {results['temp_below_15']} flights departing in temperatures below 15 degrees\n")
        f.write(f"There was an average of {results['avg_ba']} British Airways flights per hour from this airport\n")
        f.write(f"British Airways planes made up {results['ba_percent']}% of all departures\n")
        f.write(f"{results['af_delay_percent']}% of Air France departures were delayed\n")
        f.write(f"There were {results['rain_hours']} hours in which rain fell\n")
        f.write(f"The least common destinations are {results['least_destinations']}\n\n")


# ------------------------------------------------------------------------
# TASK D: HISTOGRAM (simple, neat)
# ------------------------------------------------------------------------

def draw_histogram(airline, airport, year):
    """Displays a simple horizontal histogram in a graphics window."""

    # Count flights per hour for chosen airline
    hourly_counts = [0] * 12
    hours_seen = [extract_hour(row[2]) for row in data_list]
    start_hour = min(hours_seen) if hours_seen else 0

    for row in data_list:
        if row[1][:2].upper() == airline:
            h = extract_hour(row[2])
            if h is not None:
                index = (h - start_hour) % 24
                if 0 <= index < 12:
                    hourly_counts[index] += 1

    max_value = max(hourly_counts)

    # Create window
    win = GraphWin("Histogram", 600, 500)
    title = Text(Point(300, 20), f"Departures per hour for {AIRLINES[airline]} ({AIRPORTS[airport]} {year})")
    title.draw(win)

    # Draw bars
    y = 60
    for i in range(12):
        bar_width = (hourly_counts[i] / max_value) * 400 if max_value > 0 else 0

        hour_label = Text(Point(80, y), f"{(start_hour + i)%24:02d}:00")
        hour_label.draw(win)

        bar = Rectangle(Point(120, y - 10), Point(120 + bar_width, y + 10))
        bar.setFill("lightblue")
        bar.draw(win)

        bar_text = Text(Point(130 + bar_width, y), str(hourly_counts[i]))
        bar_text.draw(win)

        y += 35

    # Close window on click
    close_msg = Text(Point(300, 480), "Click to close")
    close_msg.draw(win)
    win.getMouse()
    win.close()


# ------------------------------------------------------------------------
# MAIN PROGRAM LOOP (TASK E)
# ------------------------------------------------------------------------

def main():
    while True:

        airport = get_valid_airport_code()
        year = get_valid_year()
        filename = f"{airport}{year}.csv"

        load_csv(filename)

        results = analyse_data()
        display_results(filename, airport, year, results)
        save_results(filename, airport, year, results)

        airline = get_valid_airline()
        draw_histogram(airline, airport, year)

        again = input("Do you want to select a new data file? Y/N: ").strip().upper()
        if again != "Y":
            print("Thank you. End of run")
            break


if __name__ == "__main__":
    main()
