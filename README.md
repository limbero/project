# AI Project - Text Generation

The project is about investigating how the use of different n-gram affects the performance of a language model for
different languages. In this particular project models for English, Swedish and Greek will be evaluated. 
The SRI Language Modeling Toolkit is used to create the language models, and the models are
trained on corpuses made of posts/comments from reddit.

Files included in this directory are:
* comments.py - retrieves posts from reddit and writes the data to a file
* cleaner.py - removes unwanted sentences from the corpus files, for example sentences in the wrong language
* Files for the language models and n-grams
* One corpus for each language

###Prerequisites
* Python 2.7
* Python Reddit API Wrapper
* SRI Language Modeling Toolkit

#### Create corpus
Run `python comments.py subreddit > corpus_file.txt` 

subreddit is the subreddit you want to retrieve posts from and corpus_file is the file you want to save the data to. comments.py is configured to retrieve the top 100 posts from the subreddit, but this can be changed.

#### Clean the corpus

#### Train the model

#### Generate posts
