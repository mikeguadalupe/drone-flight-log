#!/usr/bin/env python3
"""
Drone Flight Log
A simple command-line tool to log and review your drone flights.
Stores data in flights.csv in the same folder.
"""

import csv
import os
from datetime import datetime

LOG_FILE = "flights.csv"
FIELDS = ["date", "location", "duration_minutes", "purpose", "notes"]


def ensure_file():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()


def add_flight():
    date = input("Date (YYYY-MM-DD, blank = today): ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    location = input("Location: ").strip()
    duration = input("Duration (minutes): ").strip()
    purpose = input("Purpose (e.g. practice, real estate, inspection): ").strip()
    notes = input("Notes (optional): ").strip()

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow({
            "date": date,
            "location": location,
            "duration_minutes": duration,
            "purpose": purpose,
            "notes": notes,
        })
    print(f"\nLogged flight on {date} at {location}.\n")


def view_flights():
    ensure_file()
    with open(LOG_FILE, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("\nNo flights logged yet.\n")
        return

    total_minutes = 0
    print(f"\n{'Date':<12}{'Location':<20}{'Minutes':<10}{'Purpose':<15}Notes")
    print("-" * 70)
    for row in rows:
        print(f"{row['date']:<12}{row['location']:<20}{row['duration_minutes']:<10}{row['purpose']:<15}{row['notes']}")
        try:
            total_minutes += int(row["duration_minutes"])
        except ValueError:
            pass

    print("-" * 70)
    print(f"Total flights: {len(rows)}  |  Total flight time: {total_minutes} minutes ({total_minutes / 60:.1f} hours)\n")


def main():
    ensure_file()
    while True:
        print("Drone Flight Log")
        print("1. Log a new flight")
        print("2. View all flights")
        print("3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_flight()
        elif choice == "2":
            view_flights()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
