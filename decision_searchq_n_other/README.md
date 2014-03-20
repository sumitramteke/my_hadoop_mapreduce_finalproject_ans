A] For a active community site, we have to consider which factors are required to decide if we need to use Hadoop/MapReduce:

High volume, velocity and variety information assets define BigData. So wherever these 3Vs are on a high level basis, unstructured data is what obtained mostly for statistical purpose, hence, dealing with BigData. Hadoop is the core platform for structuring Big Data, and solves the problem of making it useful for analytics purposes.  Hence while dealing with BigData, Hadoop would be the best possible option to choose for statistical purpose.

B] The question is regarding improvement of the search functionality:  

We have an index of words by which we can directly get the post_id which contains that word. The index lookup can be made cleaner by leaving common words like a, the, an etc. Also, words filtered from the tags like "a", "p" can be excluded from the index. The input will have to be filtered accordingly to make the search more relevant.  We can keep an index of tags and the post-id so that tag-search is faster  An index of author_id against post_id can give us the activity of a particular use. Search by user-i/username could be efficient using this.


C] Other questions that could be answered by using mapreduce on this dataset:

1. Keeping track of inactive user for more than certain period who do neither comment nor score and nor even access forum. 
2. Obtain recently added post and its rate of response for its answers
