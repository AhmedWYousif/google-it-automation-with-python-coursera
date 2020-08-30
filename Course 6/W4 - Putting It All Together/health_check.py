#!/usr/bin/env python

import shutil
import psutil
import socket
import emails
import os

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free >= 20

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage <= 80

def check_ram_usage():
    values = psutil.virtual_memory()
    return (values.available / (1024.0 **2)) >= 500

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'



if __name__ == "__main__":
    system_has_issue = False
    subject = ""

    if not check_cpu_usage(): # If there's not enough disk, 
        system_has_issue = True
        subject = "Error - CPU usage is over 80%"
    elif not check_disk_usage('/'): # or not enough CPU, print an error
        system_has_issue = True
        subject = "Error - Available disk space is less than 20%"
    elif not check_localhost():
        system_has_issue = True
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
    elif not check_ram_usage():
        system_has_issue = True
        subject = "Error - Available memory is less than 500MB"

    if system_has_issue:
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        body = "Please check your system and resolve the issue as soon as possible."
        message = emails.generate_email(sender, receiver, subject, body)
        emails.send_email(message)
