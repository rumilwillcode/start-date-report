#!/usr/bin/env python3

import csv
import datetime
import requests

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"
employee_data = {}

def get_start_date():
    """Interactively get the start date to query for."""
    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def fetch_and_store_data(url):
    """Fetch the file from the given URL and store data in a dictionary."""
    response = requests.get(url)
    lines = response.text.splitlines()
    reader = csv.reader(lines[1:])
    
    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        row_name = row[0] + ' ' + row[1]
        if row_date in employee_data:
            employee_data[row_date].append(row_name)
        else:
            employee_data[row_date] = [row_name]

def list_newer(start_date):
    for date in sorted(employee_data):
        if date >= start_date:
            print(f"Started on {date.strftime('%b %d, %Y')}: {', '.join(employee_data[date])}")

def main():
    fetch_and_store_data(FILE_URL)
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()

