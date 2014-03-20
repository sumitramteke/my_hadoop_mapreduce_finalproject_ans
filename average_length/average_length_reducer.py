#!/usr/bin/python

import sys
import re

#for reducer the input is abs_parent_id, post-id, length
#for question it is : 12345, 0, 78
#for answer it is : {12345, 1357, 50}, {12345, 2468, 45} and so on

LEN = 3

prev_q = None
current_q = None
n_ans = 0
sum_n_ans = 0
q_len = -1

def calc_avg(total, n):
    if n == 0:
        return 0
    return float(total) / float(n)

for line in sys.stdin:
#split by space since we outputted from mapper in that way
    parts = line.strip().split(" ")

    if len(parts) < LEN:
        continue

    current_q = parts[0]
    if prev_q != current_q:
        if q_len != -1:
            print "{0}\t{1}\t{2}".format(prev_q, q_len, calc_avg(sum_n_ans, n_ans))
        #ignore if it is an answer without a question
        if parts[1] != "0":
            q_len = -1
            continue
        #new question
        n_ans = 0
        sum_n_ans = 0
        q_len = int(parts[2])
        prev_q = current_q
        continue

    #it is an answer, process it
    sum_n_ans += int(parts[2])
    n_ans += 1
    prev_q = current_q

if q_len != -1:
    print "{0}\t{1}\t{2}".format(prev_q, q_len, calc_avg(sum_n_ans, n_ans))