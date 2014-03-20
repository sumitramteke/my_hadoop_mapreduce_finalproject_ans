#!/usr/bin/python

import sys
import re

LEN = 2
tag = None
n_tag = 0

top_ten = []

def insert_into_top_ten(tag_to_add, n_tag):
    i = 0
    for tag in top_ten:
        if n_tag < tag[1]:
            i += 1
            continue
        else:
            break
    top_ten.insert(i, (tag_to_add, n_tag))

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) < LEN:
        continue

    current_tag, current_q_id = parts
    if tag and current_tag != tag:
        insert_into_top_ten(tag, n_tag)
        tag = current_tag
        n_tag = 1
        continue

    n_tag += 1
    tag = current_tag

#print top_ten
#print out the top ten
n_distinct = 0
i = 0
while n_distinct < 10:
    print top_ten[i]
    i += 1
    if top_ten[i][1] != top_ten[i-1][1]:
        n_distinct += 1