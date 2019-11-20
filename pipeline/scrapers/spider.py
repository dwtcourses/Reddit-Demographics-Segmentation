

from scrapy.item import Field, item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExctractor
from scrapy.crawler import CrawlerProcess
from scrapy.loader.processors import MapCompose


#https://www.youtube.com/watch?v=YeB-jdrcfZA
	

class RedditComment(Item):
	
	body = Field()


def unwrap(arr):
	pass


class RedditSpider(CrawlSpider):

	name = self.name
	start_url = self.start_url
	allowed_domains = unwrap(self.allowed_domains)

	rules = ((LinkExtractor(), callback = parse_comment))


	def parse_items(self, response):
		pass

	def parse_comment(self):
		pass



if __init__ == '__main__':
	run_spider()