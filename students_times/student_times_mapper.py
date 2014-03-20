#!/usr/bin/python
import sys
from datetime import datetime

AUTHOR_ID = 3 # field author_id > here student_id index number
ADDED_AT = 8 # field added_id index number
TZ_LEN = 3
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

def ignore_tz(t):
    return t[:-TZ_LEN]

def get_hour(d):
    d = ignore_tz(d) # ignore zone as not require
    try:
        dt = datetime.strptime(d, DATETIME_FORMAT)
        return dt.hour
    except ValueError:
        return None

def trim_doubleQuotes(qouted_string):
    return qouted_string.replace('\"','')

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) >= 9: # minimum field count require
	student_id = trim_doubleQuotes(data[AUTHOR_ID])
	added_at_hr = trim_doubleQuotes(data[ADDED_AT])
	added_at_hr = get_hour(added_at_hr)
	if added_at_hr:
        	print "{0}\t{1}".format(student_id, added_at_hr)