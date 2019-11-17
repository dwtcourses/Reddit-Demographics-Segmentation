
import sys
sys.path.append('/scrapers')
from spider import *
from api import * as redit_api
import pandas as pd


"""
The extract module performs loading operations over an specified extraction domain. 

License: ThisIsMyStuffBitch

"""

dev_mode = True


def build_spiders():
	pass

def get_stream():
	pass
	

class Extractor:

	def __init__(self, params):
		pass


	#Will perform different extraction schemes depending on the ETL configuration
	def init_extractors(self):
		
		extractors = []
		
		if self.command.source == 'WS':
			extractors = build_spiders()

		elif self.command.source == 'API_1'
			extractors = get_stream()

		return extractors


	def extract_batch(extractors, self):

		batch = pd.DataFrame()

		for extractor in extractors:
			batch = extractor.grip() 
			#append operation (still figuring this out)

		return batch



	def run(self):
		
		extractors = self.init_extractors()
		data_batch = self.extract_batch(extractors)

		return data_batch





class Transforms:

	def __init__(self, params):

		self.transformations = command.transformations


	def map(self, operator):
		pass

	def run(self, data_batch):

		#applying all transforms over the extracted batch
		for transform in transforms:
			self.
		


class Loader:

	def __init__(self, params):
		pass

	def run(self):
		pass




if __name__ == '__main__':
	pass