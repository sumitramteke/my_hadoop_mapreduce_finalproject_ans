#!/usr/bin/python

import sys
import re

#for reducer the input is abs_parent_id, post-id, author_id
#for question it is : 12345, 0, 46809
#for answer or comment it is : {12345, 1357, 34567}, {12345, 2468, 334455} and so on

LEN = 3

prev_q = None
current_q = None
valid_q = False
contrib_list = []

for line in sys.stdin:
#split by space since we outputted from mapper in that way
    parts = line.strip().split(" ")

    if len(parts) < LEN:
        continue

    current_q = parts[0]
    if prev_q != current_q:
        if valid_q:
            print "{0}\t{1}".format(prev_q, contrib_list)

        #ignore if newly arrived current_q is an answer or comment without a question
        if parts[1] != "0":
            valid_q = False
            continue

        #new question
        valid_q = True
        #initialize the new contributor's list
        contrib_list = []

    #add the question or answer or comment, to the contributors' list
    contrib_list.append(parts[2])
    prev_q = current_q

if valid_q:
    print "{0}\t{1}".format(prev_q, contrib_list)