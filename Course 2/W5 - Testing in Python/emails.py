#!/usr/bin/env python3

import sys
import csv

def populate_dictionary(filename):
    """Populate a dictionary with name/email pairs for easy lookup."""
    email_dict = {}
    with open(filename) as csvfile:
        lines = csv.reader(csvfile, delimiter = ',')
        for row in lines:
            name = str(row[0].lower())
            email_dict[name] = row[1]
    return email_dict

def find_email(argv):
    """ Return an email address based on the username given."""
    # Create the username based on the command line input.
    try:
        fullname = str(argv[1] + " " + argv[2])
        # Preprocess the data
        email_dict = populate_dictionary('/home/student-02-9ce27c095c34/data/user_emails.csv')
        # Find and print the email
        if email_dict.get(fullname.lower()):
            return email_dict.get(fullname.lower())
        else:
            return "No email address found"
    except IndexError:
        return "Missing parameters"

def main():
    print(find_email(sys.argv))

if __name__ == "__main__":
    main()
