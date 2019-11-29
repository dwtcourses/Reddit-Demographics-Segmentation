

import praw

client_secret = 
client_id = 
username = 
password = 
#bye dev account

class RedditAPI:


	def __init__(self):
		
		global client_secret
		global client_id
		global username
		global password

		self.reddit = praw.Reddit(client_id, client_secret = client_secret, username, password, user_agent = 'ter')
		

	def hot_comments(topic, batch_size):
		
		sub_reddit = self.reddit.subrredit(sub_name)
		threads = sub_reddit.hot(limit = batch_size)

		for submission in topic:
			pass


	def new_comments(topic, batch_size):
		
		sub_reddit = self.reddit.subrredit(sub_name)
		threads = sub_reddit.hot(limit = batch_size)

		for submission in topic:
			pass



	def hot_threads(topic, batch_size):
		pass


	def new_threads(topic, batch_size)
		pass




if __name__ == '__main__':
	pass