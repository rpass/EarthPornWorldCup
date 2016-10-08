# EarthPorn World Cup
Is a small project to answer the question: Which is the most beautiful country on Earth according to the wise redditors from /r/EarthPorn. The validity of the findings are questionable and the purpose of this project is equally to explore the Reddit API with PRAW as well as to come to an answer to the above question.

I'm open for criticism and advice so please give your thoughts willingly.

## Still To-Do
* Scrap a more complete list of country names
* Handle different spellings of country names
* Introduce multiple metrics for results (Most upvotes, Average upvotes in top 50 submissions, Upvotes of top submission, etc.)
* Persist metrics so as to not spam the Reddit API. A flat file will do.
* Introduce updating of the persisted results
* Transform the script into a cron-like script which can be left running and which will update over time