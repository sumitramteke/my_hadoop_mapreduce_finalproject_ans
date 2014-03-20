Problem:
We need to find the hours during which a student has posted most number of posts (question / answer /comment)

Approach:
We can group by a student id.

Output from Mapper: The output will contain the student_id and the hour during which he/she posted.

Reducer: In reducer, we will keep a track as to which hour the student posts how many times. Also, we maintain a list of tuples which contains the highest hours for a student_id e.g (10099887, 14). This list will be updated based on every new line processed. When a new student_id is processed, we print the output.