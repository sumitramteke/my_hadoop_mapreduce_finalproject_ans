Here we have to list the students' activity for all questions. So for a given question, we will print the ID's of authors for the question itself, the answers and comments.

Approach: Group by question id.

Output from mapper: if it is a question we will output post_id, 0, author if it is an answer or comment we will output abs_parent_id, ans_id, author

Reducer: In reducer we can go through each line and lookout for the first param. It will be always a question id. We can detect using the second field if it's a question or answer. Whenever the question changes, we will output the answer. We will be maintaining a list of user ids associated with the particualr quesion/answer/node Also, we will have to take care that answers without questions are ignored.