import sys, praw

r = praw.Reddit('macosx:kth-ai-group55:v1.0 (by /u/limbero)')

submissions = r.get_subreddit(sys.argv[1]).get_top(limit=sys.argv[2])

for submission in submissions:
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    for comment in flat_comments:
        print comment.body.encode("utf-8")
