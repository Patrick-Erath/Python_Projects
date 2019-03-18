import praw

#Create reddit instance
reddit = praw.Reddit(client_id='wqrrsTJXlIrG7A',
					client_secret='g72L_jWvbJEduw2Ho_gnX1P4a1g', 
					password='lolmaster',
					user_agent='Patrick', 
					username='me_using_reddit')

subreddit=reddit.subreddit('python')
hot_python = subreddit.hot(limit=3) # Returns submission objects

for submission in hot_python:
	if not submission.stickied:
		#print(submission.ups)
		print('Title: {}, UpVotes:{}, DownVotes:{}, Visited:{}'.format(submission.title,
																	   submission.ups,
																	   submission.downs,
																	   submission.visited))
	if submission.ups > 100:
		submission.downvote()

# GET : submission.title, .ups, .downs, .visited
# PUT : submission.upvote(), .clear_vote(), .downvote(), .reply()
#     : sureddit.subscribe(), .unsubscribe()