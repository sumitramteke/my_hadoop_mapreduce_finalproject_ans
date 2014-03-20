#!/usr/bin/python

import sys
import re

#from mapper we will output the id, abs_parent_id, length
#we will output only questions and answers. For questions, abs_parent_id will be empty. For anwers and comments on questions abs_parent_id == parent_id.
#Length will be simple len() of string

ABS_PARENT_ID = 7
PARENT_ID = 6
AUTHOR_ID = 3
ID = 0
NODE_TYPE = 5

#a post-id will be either single digit between [1 to 9], followed by 0 or more digits from [0 to 9]
id_regexp = r"[1-9][0-9]*"

def remove_quotes(line):
    return line[1:-1]

def is_id(word):
    if re.match(id_regexp, word):
        return True
    return False

for line in sys.stdin:
    parts = line.strip().split("\t")

    if len(parts) < ABS_PARENT_ID:
        continue

    post_id = remove_quotes(parts[ID])
    author = remove_quotes(parts[AUTHOR_ID])
    parent_id = remove_quotes(parts[PARENT_ID])
    abs_parent_id = remove_quotes(parts[ABS_PARENT_ID])
    node_type = remove_quotes(parts[NODE_TYPE])

    #check if if it question or answer
    msg = ""
    if node_type == "question" and is_id(post_id):
        msg = "{0} {1} {2}".format(post_id, "0", author)
    #check for the odd lines of data, which don't have any post-id, the zeroth field itself is body.
    elif (node_type == "answer" or node_type == "comment") and is_id(parent_id) and is_id(abs_parent_id) and is_id(post_id):
        msg = "{0} {1} {2}".format(abs_parent_id, post_id, author)
    if len(msg) > 0:
        print msg