Problem:
Here we need the top ten tags. The program top ten distinct tags.

Approach:
Create an index based on the tags, and count the number of questions associated with that question.

Output from Mapper:
We will confirm that the line we process is a question. We will separate out the tags using " " (space). The output will be tag, post_id. We ignore the questions with no tags.

Reducer:
We will maintain a list of tags. While insertingt he tags into the list, we will keep it sorted in descending order. While printing we print the distinct top 10 tags.