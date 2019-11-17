
import sys
sys.path.append('/scrapers')
from spider_api import Spider
import pandas as pd


"""
The extract module performs loading operations over an specified extraction domain. 

License: ThisIsMyStuffBitch

"""


def load_deploy_commands():
	
	deploy_commands = []

	"""
	grabs the dictionary with url seed, rules, domain and the number of spiders
	"""

	return deploy_commands



class Extractor:


	def __init__(self, params):
		pass


	#Will perform different extraction schemes depending on the ETL configuration specified at the extractor configurator
	def prepare(self):
		
		extraction_commands = []
		
		if self.params.source == 'WS':
			
			extraction_commands = load_deploy_commands()

		return extraction_commands



	def extract_batch(self, extraction_commands):

		batches = pd.DataFrame()

		
		for command in extraction_commands:

			extractor = Spider(command)
			extractor.grip() 
			batch = extractor.yield_batch()
			#append operation (still figuring this out)
			#batches.append(batch)

		return batches



	def run(self):
		
		extractors = self.prepare()
		data_batch = self.extract_batch(extractors)

		return data_batch





class Transforms:

	def __init__(self, params):

		self.transformations = params.transformations


	def map(self, operator):
		pass

	def run(self, data_batch):

		#applying all transforms over the extracted batch
		for transform in transforms:
			pass
		


class Loader:

	def __init__(self, params):
		pass

	def run(self):
		pass




if __name__ == '__main__':
	pass