#!/usr/bin/env python3
import csv
import argparse
import requests
import sys
import logging
import os
from datetime import datetime
import matplotlib.pyplot as plt

# --------------------
# CONFIGURATION
# --------------------
API_URL = "https://api.open-meteo.com/v1/forecast"
LOG_FILE = "weather.log"  # Log file to store each run's data

# --------------------
# SETUP LOGGING
# --------------------
# Ensure the log file exists and configure logging to append
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s,%(message)s',  # timestamp, data
    datefmt='%Y-%m-%d %H:%M:%S'
)

# --------------------
# FETCH WEATHER FUNCTION
# --------------------
def fetch_weather(lat, lon):
    """
    Call the weather API for given coordinates.
    Returns temperature in Celsius, or None on error.
    """
    try:
        params = {"latitude": lat, "longitude": lon, "current_weather": True}
        response = requests.get(API_URL, params=params, timeout=5)
        response.raise_for_status()
        # Extract temperature from JSON response
        return response.json()["current_weather"]["temperature"]
    except (requests.RequestException, KeyError) as e:
        print(f"❌ Error fetching {lat},{lon}: {e}", file=sys.stderr)
        return None

# --------------------
# TEMPERATURE CONVERSION
# --------------------
def c_to_f(celsius):
    """
    Convert Celsius to Fahrenheit.
    """
    return celsius * 9/5 + 32

# --------------------
# GRAPH GENERATOR
# --------------------
def generate_graph(log_file):
    """
    Read the log file and plot temperature history per city.
    Saves or displays a line graph of temp over time.
    """
    # Prepare data container: {city: [(timestamp, temp_f), ...]}
    data = {}
    with open(log_file) as f:
        for line in f:
            try:
                # Example log line: 2025-04-25 12:00:00,City,TempF
                timestamp_str, rest = line.strip().split(',', 1)
                city, temp_str = rest.split(',', 1)
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                temp = float(temp_str)
                data.setdefault(city, []).append((timestamp, temp))
            except ValueError:
                continue  # skip malformed lines

    # Plot each city's temperature history
    for city, records in data.items():
        records.sort(key=lambda x: x[0])
        times = [t for t, _ in records]
        temps = [temp for _, temp in records]
        plt.plot(times, temps, marker='o', label=city)

    plt.xlabel('Time')
    plt.ylabel('Temperature (°F)')
    plt.title('Temperature History')
    plt.legend()
    plt.tight_layout()
    plt.show()

# --------------------
# MAIN SCRIPT
# --------------------
def main(csv_path):
    # Read the CSV of locations
    with open(csv_path) as f:
        reader = csv.DictReader(f)

        # Print header for console output
        print(f"{'City':<15} | {'Temp (°F)':>11}")
        print('-' * 29)

        # Process each location
        for row in reader:
            city = row['city']
            lat = row['lat']
            lon = row['lon']

            # Fetch temperature in Celsius
            temp_c = fetch_weather(lat, lon)
            if temp_c is not None:
                # Convert to Fahrenheit
                temp_f = c_to_f(temp_c)
                # Print to console
                print(f"{city:<15} | {temp_f:>11.1f}")
                # Log to file: city,temperature
                logging.info(f"{city},{temp_f:.1f}")
            else:
                print(f"{city:<15} | {'N/A':>11}")

    # After logging, generate and display the temperature history graph
    if os.path.exists(LOG_FILE):
        generate_graph(LOG_FILE)

# --------------------
# ENTRY POINT
# --------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch temps and log + graph results')
    parser.add_argument('csv', help='Path to locations.csv')
    args = parser.parse_args()
    main(args.csv)
