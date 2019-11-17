
import sys
from spider import *
import pandas as pd

#Wrapper for the scrapy spiders

class Spider:


	def __init__(self, deploy_command):
		self.crawler = self.build(deploy_command)
		

	def build(self, deploy_command):

		return WebCrawler()


	def grip(self):
		
		print('A new spider has been deployed!\n')

		process = CrawlerProcess(settings={
    	'FEED_FORMAT': 'json',
    	'FEED_URI': 'items.json'
		})
		print('\nCrawling...')
		process.crawl(MySpider)
		process.start() 



	def yield_batch(self):
		#collects the generated csv volumes and yields it to the caller
		batch = pd.csv_read('placeholder')
		return batch


if __name__ == '__main__':
	pass