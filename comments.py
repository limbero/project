import praw
r = praw.Reddit('KTH AI project by group-55.')
submission = r.get_submission(submission_id='3ny9fl')
flat_comments = praw.helpers.flatten_tree(submission.comments)
for comment in flat_comments:
    print comment.body
