
import sys
sys.path.append('/scrapers')
from spider_api import Swarm 
import pandas as pd

spiders_config_path = '/scrapers/config/spiders.txt'

"""
The extract module performs loading operations over an specified extraction domain. 

License: ThisIsMyStuffBitch

"""


def load_deploy_commands(path):
	
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

			global spiders_config_path
			extraction_commands = load_deploy_commands(scrapers_config_path)

		return extraction_commands



	def launch_swarm(self, extraction_commands, verbose = False):

		batch = pd.DataFrame()
		print('Deploying spiders swarm...\n')
		spider_swarm = Swarm(extraction_commands)
		spider_swarm.grip() 
		print('Retrieving all the obtained data.')
		batch = spider_swarm.retrieve_batch()
		print('\ndone.')
		return batch



	def run(self):

		print('\nPreparing extraction process...\n')
		extractors = self.prepare()
		data_batch = pd.DataFrame({})

		if self.params.source == 'WS':
			data_batch = launch_swarm(extractors)

		
		print('\nThe data stream is now inside the pipeline!')
		print('\nReady to perform preparation procedures...')
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