import random
import time
import praw
from praw_creds import client_id, client_secret, password, user_agent, username

reddit = praw.Reddit(client_id=client_id,
					client_secret=client_secret, 
					password=password,
					user_agent=user_agent, 
					username=username)

common_spammy_words = ['udemy','course','save','coupon','free','discount']

def find_spam_by_name(search_query):
	authors = []
	for submission in reddit.subreddit('all').search(search_query, sort='new', limit=11):
		print(submission.title, submission.author, submission.url)
		if submission.author not in authors:
			authors.append(submission.author)
	return authors

if __name__ == '__main__':
	while True:
		current_search_query = random.choice(common_spammy_words)
		spam_content = []
		trashy_users = {}
		smelly_authors = find_spam_by_name(current_search_query)
		for author in smelly_authors:
			user_trashy_urls = []
			sub_count = 0
			dirty_count = 0
			try:
				for sub in reddit.redditor(str(author)).submissions.new():
					submit_links_to = sub.url
					submit_id = sub.id
					submit_subreddit = sub.subreddit
					submit_title = sub.title
					dirty = False
					for w in common_spammy_words:
						if w in submit_title.lower():
							dirty = True
							junk = [submit_id, submit_title]
							if junk not in user_trashy_urls:
								user_trashy_urls.append([submit_id, submit_title, str(author)])
						if dirty:
							dirty_count+=1
						sub_count+=1

				try: 
					trashy_score = dirty_count/sub_count
				except: trashy_score = 0.0
				print('User {} has a trashy score of {}'.format(str(author), round(trashy_score,3)))

				if trashy_score >= 0.5:
					trashy_users[str(author)] = [trashy_score, sub_count]

					for trash in user_trashy_urls:
						spam_content.append(trash)

			except Exception as e:
				print(str(e))

		for spam in spam_content:
			spam_id = spam[0]
			spam_user = spam[2]
			submission = reddit.submission(id=spam[0])
			created_time = submission.created_utc
			if time.time()-created_time <= 86400:
				link = 'https://reddit.com'+submission.permalink
				message= """"*Beep Boop Beep Boop, 
Hello, my name is RedditAPI_Bot, and I detect reddit trash. My senses tell me that this post is spam. 
At least {} percent out of the {} submissions from /u/{} appear to be for Udemy affiliate links.
Don't let Reddit become spam ! Report this post!""".format(round(trashy_users[spam_user][0]*100,2), trashy_users[spam_user][1], spam_user)




