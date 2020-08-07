#!/usr/bin/env python3

import re
import operator
import csv

# number of different error messages
errors ={}
#each user (splitting between INFO and ERROR).
per_user = {}

with open("syslog.log") as file:
    logs = file.readlines()
    for log in logs:
        match = re.search(r"ticky: (INFO|ERROR) (.*) \((.*)\)", log.strip())
        if match != None:
            log_type = match.group(1)
            username = match.group(3).strip()
            message = match.group(2).strip()
            (old_info,old_error) = per_user.get(username,(0,0))
            if log_type == 'ERROR':
                errors[message] = errors.get(message,0)+1
                old_error +=1
            else:
                old_info +=1
      
            per_user[username] = (old_info,old_error)
file.close()    


errors = sorted(errors.items(), key = operator.itemgetter(1), reverse=True)
per_user = [(key,val[0],val[1])for key, val in sorted(per_user.items(), key = operator.itemgetter(0))] 

with open("error_message.csv", 'w+') as errors_file:   
    writer = csv.writer(errors_file)
    writer.writerow(("Error", "Count"))
    writer.writerows(errors)
errors_file.close()

with open("user_statistics.csv", 'w+') as users_file:   
    writer = csv.writer(users_file)
    writer.writerow(("Username", "INFO", "ERROR"))
    writer.writerows(per_user)
users_file.close()     
