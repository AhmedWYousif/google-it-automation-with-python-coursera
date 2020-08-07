#!/usr/bin/env python
import operator
import re
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
match = re.search(r"ticky: (INFO|ERROR): ([\w ]*) \[.*\] \(([\w ]*)\)", line)
print (match[1],match[2],match[3])
###############################################################

fruit = {"oranges": (3,4), "apples": (5,4), "bananas": (7,3), "pears": (2,5)}
sorted(fruit.items())

print([(key, *val)for key, val in sorted(fruit.items(), key = operator.itemgetter(0))] )
#sort by key
sorted(fruit.items(), key=operator.itemgetter(0))
# sort by value
sorted(fruit.items(), key=operator.itemgetter(1))
# sort by value reversed 
sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)

