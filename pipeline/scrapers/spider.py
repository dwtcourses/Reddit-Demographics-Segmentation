

from scrapy.item import Field, item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExctractor
from scrapy.crawler import CrawlerProcess




class RedditComment(Item):
	id = Field()
	body = Field()


class RedditCrawler(CrawlSpider):
	
	name = "Crawler"
	start_url = ""
	allowed_domains = ['']

	rules = {

	}

	def parse_items(self, response):
		pass





if __init__ == '__main__':
	run_spider()