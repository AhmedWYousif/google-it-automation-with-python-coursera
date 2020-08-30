#! /usr/bin/env python3

import os
import requests
import datetime
import reports
import emails

def process_data (directory):
    data =[]
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename)) as opened:
                lines = opened.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                data.append("name: {}<br/>weight: {}".format(name,weight))
    return "<br/><br/>".join(data)
            

if __name__ == "__main__":
    attachment = "/tmp/processed.pdf"
    title = "Processed Update on {}".format(datetime.datetime.today().date())
    paragraph = process_data("supplier-data/descriptions")
    reports.generate_report(attachment, title, paragraph)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)