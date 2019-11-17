
import sys
sys.path.append('/scrapers')
from spider_api import Swarm 
import pandas as pd
from nltk.tokenize import MWETokenizer
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



	#template for what the transform table should eventually look like 
	def prepare_operators(operator_list):

		operators = []
		for operator_name in operator_list:

		
			if operator == "tokenize":

				tokenizer = lambda sentence : tokenize(sentence.split())  
				operators.append(tokenizer)


			elif operator == "trim":
				
				#just an example
				trimmer = lambda sentence: sentence
				operators.append(trimmer)

			else:
				print('Invalid operator')


		return operators



	def map(self,data_batch, operators):
		
		for operator in operators:
			operator(data_batch)

		return data_batch



	def run(self, data_batch):

		print('Preparing the issued transforms')
		operators = self.prepare_operators(self.params.transforms)
		print('Num mappings = ', len(operators))
		processed_data = self.map(data_batch, operators)
		print('done.')
		print('\nThe current batch is prepared for further processing.')
		input('\nPress enter to continue...')



class Loader:

	def __init__(self, params):
		pass

	def run(self):
		pass




if __name__ == '__main__':
	pass