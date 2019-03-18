import praw
import time

# DO NOT PUSH YET!


#Create reddit instance
reddit = praw.Reddit(client_id='wqrrsTJXlIrG7A',
					client_secret='g72L_jWvbJEduw2Ho_gnX1P4a1g', 
					password='PASSWORD',
					user_agent='Patrick', 
					username='USERNAME')

subreddit = reddit.subreddit('news')

for comment in subreddit.stream.comments():
	try:
		print(30*'_')
		print()
		parent_id = str(comment.parent())
		submission = reddit.comment(parent_id)
		print('Parent:')
		print(submission.body)
		print('Comment:')
		print(comment.body)
	except praw.exceptions.PRAWException as e:
		pass
