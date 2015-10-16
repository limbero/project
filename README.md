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
Run `python cleaner.py`

Requires that you have files called corpus_el.txt, corpus_en.txt and corpus_sv.txt. Cleaning will create 3 files for each language, clean_lang, clean_lang_tokenized and dirty_lang. clean_lang removes lines that appear to be written in another language, and removes some cruft. clean_lang_tokenized splits word punctuation into their own words, but is otherwise the same as clean_lang.

#### Train the model

Run `ngram-count -text clean_lang_tokenized -lm model_lang -order n -write ngram_lang`

You will generally only be using model_lang, but ngram_lang is good to look at for understanding.

#### Generate posts

Run `ngram -order n -gen k -lm model_lang`

n is the order of the markov chain. k is the number of sentences you want to generate.
