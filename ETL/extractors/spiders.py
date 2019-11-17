

from scrapy.item import Field, item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExctractor


class RedditComment(Item):
	id = Field()
	body = Field()


class RedditCrawler(CrawlSpider):
	name = "RedditCrawler"
	start_url = ""
	allowed_domains = ['']

	rules = {

	}

	def parse_items(self, response):
		pass




if __init__ == '__main__':
	pass