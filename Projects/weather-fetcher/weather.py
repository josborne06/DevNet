#!/usr/bin/env python3
import csv, argparse, requests, sys

API_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_weather(lat, lon):
    try:
        params = {"latitude": lat, "longitude": lon, "current_weather": True}
        r = requests.get(API_URL, params=params, timeout=5)
        r.raise_for_status()
        return r.json()["current_weather"]["temperature"]
    except (requests.RequestException, KeyError) as e:
        print(f"  ❌ Error fetching {lat},{lon}: {e}", file=sys.stderr)
        return None

def c_to_f(c):
    return c * 9/5 + 32

def main(csv_path):
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        print(f"{'City':<15} | {'Temp (°F)':>11}")
        print("-"*29)
        for row in reader:
            city, lat, lon = row["city"], row["lat"], row["lon"]
            c_temp = fetch_weather(lat, lon)
            if c_temp is not None:
                print(f"{city:<15} | {c_to_f(c_temp):>11.1f}")
            else:
                print(f"{city:<15} | {'N/A':>11}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("csv", help="Path to locations.csv")
    args = p.parse_args()
    main(args.csv)
