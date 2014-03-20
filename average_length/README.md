Here we are supposed to output the length of the question and the average length of answers for that question.

Approach: We will try grouping by the question id.

Output from mapper: if it is a question we will output post_id, 0, len(body) if it is an answer we will output abs_parent_id, ans_id, len(body)

Reducer: In reducer we can go through each line and lookout for the first param. It will be always a question id. We can detect using the second field if it's a question or answer. Whenever the question changes, we will output the answer. We will keep track of the sum and total answers. Also, we will have to take care that answers without questions are ignored.