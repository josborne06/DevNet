#!/usr/bin/env python3
import csv
import argparse
import requests
import sys

API_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_weather(lat, lon):
    """Return current temperature for given coords, or None on error."""
    try:
        params = {"latitude": lat, "longitude": lon, "current_weather": True}
        r = requests.get(API_URL, params=params, timeout=5)
        r.raise_for_status()
        return r.json()["current_weather"]["temperature"]
    except (requests.RequestException, KeyError) as e:
        print(f"  ❌ Error fetching {lat},{lon}: {e}", file=sys.stderr)
        return None

def main(csv_path):
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        print(f"{'City':<15} | {'Temp (°C)':>9}")
        print("-"*27)
        for row in reader:
            city, lat, lon = row["city"], row["lat"], row["lon"]
            temp = fetch_weather(lat, lon)
            if temp is not None:
                print(f"{city:<15} | {temp:>9.1f}")
            else:
                print(f"{city:<15} | {'N/A':>9}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Fetch current temps from Open-Meteo")
    p.add_argument("csv", help="Path to locations.csv")
    args = p.parse_args()
    main(args.csv)
