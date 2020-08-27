#!/usr/bin/env python


import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-hol-assets/gic215/employees-with-date.csv"

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

def get_data(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    
    # process data as dic
    reader = csv.reader(lines[1:])
    processedData = {}

    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        if row_date in processedData:
            processedData[row_date].append("{} {}".format(row[0], row[1]))
        else:
            processedData[row_date] = ["{} {}".format(row[0], row[1])]

    return processedData

def list_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    processedData = get_data(FILE_URL)
 
    min_date = start_date

    while min_date <= datetime.datetime.today():
        #print(min_date);
        #print(datetime.datetime.today())
        if min_date in processedData:
            print("Started on {}: {}".format(min_date.strftime("%b %d, %Y"), processedData[min_date]))
        elif min_date.date() == datetime.datetime.today().date():
            print("Started on {}: {}".format(min_date.strftime("%b %d, %Y"), []))
        # Now move the date to the next one
        min_date = min_date + datetime.timedelta(days=1)


def main():
    start_date = get_start_date()
    list_same_or_newer(start_date)

if __name__ == "__main__":
    main()

