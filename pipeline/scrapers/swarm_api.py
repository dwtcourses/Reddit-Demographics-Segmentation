
import sys
import spider
import pandas as pd

#Wrapper for a swarm of scrapy spiders

class Swarm:


	def __init__(self, deploy_commands):

		self.crawlers = self.build(deploy_commands)
		self.yield_paths = deploy_commands.yield_paths
		

	def build(self, deploy_commands):

		crawlers = []
		
		for command in deploy_commands:

			crawlers.append(spider.factory(command))

		return crawlers


	def grip(self, verbose = False):

		print('Starting a new reactor process...')
		process = CrawlerProcess(settings={
    	'FEED_FORMAT': 'json',
    	'FEED_URI': 'items.json'
		})

		print('\nCrawling...')
		for spider in self.crawlers:
			process.crawl(spider)

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