#!/usr/bin/python

import sys
import re

TAG = 2
ID = 0
TYPE = 5


def remove_quotes(line):
    return re.sub("\"", "", line)

for line in sys.stdin:
    parts = line.strip().split("\t")

    if len(parts) <= TYPE:
        continue

    post_id = remove_quotes(parts[ID])
    tags_list = remove_quotes(parts[TAG])
    node_type = remove_quotes(parts[TYPE])

    if node_type != "question" or tags_list == "":
        continue

    tags = tags_list.split(" ")
    for tag in tags:
        print "{0}\t{1}".format(tag, post_id)