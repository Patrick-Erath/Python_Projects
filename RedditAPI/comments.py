import praw
import time

#Create reddit instance
reddit = praw.Reddit(client_id='wqrrsTJXlIrG7A',
					client_secret='g72L_jWvbJEduw2Ho_gnX1P4a1g', 
					password='PASSWORD',
					user_agent='Patrick', 
					username='USERNAME')

subreddit = reddit.subreddit('python')
hot_python = subreddit.hot(limit=3)
conversedict = {} # Empty dictionary 
boolio = True

for submission in hot_python:
	if not submission.stickied:

		submission.comments.replace_more(limit=0)
		for comment in submission.comments.list():
			if comment.id not in conversedict:
				conversedict[comment.id] = [comment.body[:30], {}]
				# conversedict = {post_id : [comment_body]}
				# conversedict[post_id][0] = comment_body
				if comment.parent() != submission.id:
					parent = str(comment.parent())
					# If current comment.parent = current comment.submission.id then PARENT IS CURRENT COMMENT, else update parent
					conversedict[parent][1][comment.id] = [comment.ups, comment.body]


# Iterate through dictionary
for post_id in conversedict:
	if x < 5:
		message = conversedict[post_id][0] # Returns message content
		replies = conversedict[post_id][1] # Returns reply object, {reply_id1:[votes, reply_content], reply_id2:[votes, reply_content]}
		if len(replies) > 1:
			print(35*'_')
			print('Original Message: {}'.format(message))
			print('Replies:')
			for reply in replies:
				print('-->')
				print(replies[reply][1][:20])


# Dictionary Format#
'''
conversedict = {post_id: [parent_content, {reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content]}],

                post_id: [parent_content, {reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content]}],
                                            
                post_id: [parent_content, {reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content]}],
                }


'''

