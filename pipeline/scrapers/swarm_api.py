
import sys
from spider import *
import pandas as pd

#Wrapper for a swarm of scrapy spiders

class Swarm:


	def __init__(self, deploy_commands):
		self.crawlers = self.build(deploy_commands)
		self.yield_paths = deploy_commands.yield_paths
		

	def build(self, deploy_commands):
		crawlers = []
		for command in deploy_commands
			pass
		return return spiders


	def grip(self, verbose = False):

		print('Starting a new reactor process...')
		process = CrawlerProcess(settings={
    	'FEED_FORMAT': 'json',
    	'FEED_URI': 'items.json'
		})
		print('\nCrawling...')
		process.crawl(MySpider)
		print('A new spider swarm has been deployed!\n')
		process.start() 
		print('\ndone.')


	def retrieve_batch(self):
		#collects the generated csv volumes and yields it to the caller
		for path in yield_paths:
			pass
		batch = pd.csv_read('placeholder')
		return batch


if __name__ == '__main__':
	pass