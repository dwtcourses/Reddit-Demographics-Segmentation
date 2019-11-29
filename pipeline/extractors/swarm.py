
import sys
from spider import RedditSpider
import pandas as pd
from scrapy.crawler import CrawlerProcess

#Wrapper for a swarm object of webscrapers


class Swarm:



	def __init__(self,id_, deploy_commands):

		self.id = id_
		self.deploy_commands = self.unroll(deploy_commands)
		self.yield_paths = deploy_commands.yield_paths
		self.log = []
		log.append('Swarm id = ', id_)
		

	def unroll(self):
		pass


	def grip(self, verbose = False):

		log.append('Starting new reactor...')

		process = CrawlerProcess(settings={
    	'FEED_FORMAT': 'json',
    	'FEED_URI': 'items.json'
		})

		for commands in self.deploy_commands:

			process.crawl(RedditSpider, deploy_commands.name, deploy_commands.start_url, deploy_commands.allowed_domains)

		log.append('A new spider swarm has been deployed!\n')
		process.start() 
		log.append('\ndone.')



	def retrieve_batch(self):

		#collects the generated csv volumes and yields it to the caller
		for path in yield_paths:
			pass

		batch = pd.csv_read('placeholder')
		return batch



if __name__ == '__main__':
	pass