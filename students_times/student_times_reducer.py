#!/usr/bin/python

import sys

old_id = None

#this dictionary will contain the mapping of hour and number of posts for that hour e.g {14: 1, 15: 2, 2: 1}
count_dict = {}

#this is a list which contains tuples of hours with the highest number of comments e.g [(18, 5), (11, 5)]
highest = [(-1, -1)]

for line in sys.stdin:
    words = line.strip().split("\t")
    if len(words) < 2:
        continue

    student_id = words[0]
    hour = words[1]

    #check if a new id arrived
    if old_id and old_id != student_id:
        #print all the hours from highest for the the student id
        for h in highest:
            print "{0}\t{1}".format(old_id, h[0])
        count_dict = {}
        highest = [(-1, -1)]

    old_id = student_id

    #keep a record of the hours and corresponding number of posts
    if hour in count_dict:
        count_dict[hour] += 1
    else:
        count_dict[hour] = 1

   #Update the highest hours
    if count_dict[hour] > highest[0][1]:
        highest = [(hour, count_dict[hour])]
    elif count_dict[hour] == highest[0][1]:
        highest.append((hour, count_dict[hour]))