

from scrapy.item import Field, item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExctractor
from scrapy.crawler import CrawlerProcess
from scrapy.loader.processors import MapCompose


#https://www.youtube.com/watch?v=YeB-jdrcfZA
	

class RedditComment(Item):
	
	id_ = field()
	body = Field()



class RedditSpider(CrawlSpider):

	name = self.name
	start_url = self.start_url
	allowed_domains = self.start_url

	#settings for allowed horizontal movement
	rules = [(LinkExtractor(), callback = parse)}



	def parse(self, response):
    		
        comments = response.css('.comments::text').extract()
        #Give the extracted content row wise
        for item in zip(titles,votes,times,comments):
          
            scraped_comment = item[0]

            yield scraped_info



if __name__ == "__main__":
	run_spider()