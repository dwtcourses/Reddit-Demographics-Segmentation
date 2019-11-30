

import praw
import os
import pandas as pd

client_secret = os.environ.get('CLIENT_SECRET')
client_id = os.environ.get('CLIENT_ID')
username = os.environ.get('USERNAME')
password =  os.environ.get('PASSWORD')


class RedditAPI:


	def __init__(self):
		
		global client_secret
		global client_id
		global username
		global password

		self.reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, username = username, password = password, user_agent = 'ter')
		

	def hot_comments(self, topic, batch_size):
		
		sub_reddit = self.reddit.subreddit(topic)
		threads = sub_reddit.hot(limit = batch_size)

		batch = pd.DataFrame()

		for submission in threads:

			if submission.stickied == False:

				submission.comments.replace_more(limit = 0)

				for comment in submission.comments.list():
					
					batch = batch.append(pd.Series(comment.body), ignore_index = True)


		return batch



	def new_comments(self, topic, batch_size):
		
		sub_reddit = self.reddit.subreddit(topic)
		threads = sub_reddit.new(limit = batch_size)
		batch = pd.DataFrame()

		for submission in threads:

			if submission.stickied == False:

				submission.comments.replace_more(limit = 0)

				for comment in submission.comments.list():
				
					batch = batch.append(pd.Series(comment.body), ignore_index = True)


		return batch



	def hot_threads(self, topic, batch_size):
		pass


	def new_threads(self, topic, batch_size):
		pass




if __name__ == '__main__':
	api = RedditAPI()
	print(api.new_comments('python', 5))