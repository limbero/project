import praw
r = praw.Reddit('macosx:kth-ai-group55:v1.0 (by /u/limbero)')
submission = r.get_submission(submission_id='3ny9fl')
flat_comments = praw.helpers.flatten_tree(submission.comments)
for comment in flat_comments:
    print comment.body
