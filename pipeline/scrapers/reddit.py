

import praw

client_secret = 'BTDUTAyqlewMvJguZvo6ctXfkVU'
client_id = 'uOMVRzNTdw7LDg'
username = 'ter_dev'
password = 'fed150'


class RedditAPI:


	def __init__(self):
		
		global client_secret
		global client_id
		global username
		global password

		self.reddit = praw.Reddit(client_id, client_secret = client_secret, username, password, user_agent = 'ter')
		

	def get_comments(topic):
		
		sub_reddit = self.reddit.subrredit(topic)




if __name__ == '__main__':
	pass