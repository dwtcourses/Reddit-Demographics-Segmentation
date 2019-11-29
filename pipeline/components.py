
import sys
import json


from scrapers import scrapers as ext
import pandas as pd
from nltk.tokenize import MWETokenizer



"""
The extract module performs loading operations over an specified extraction domain. 

License: ThisIsMyStuffBitch

"""




class Extractor:


	def __init__(self, params):
		
		modality = params.modality
		self.log = []


	#Will perform different extraction schemes depending on the ETL configuration specified at the extractor configurator
	def prepare(self):
		
		extraction_commands = []
		
		extraction_commands = load_deploy_commands(scrapers_config_path)

		return extraction_commands



	def ingest(self, verbose = False):

		batch = pd.DataFrame({})
		self.log.append('Issuing a new extraction...\n')
		extractors = ext.create_scrapper('Reddit01',self.modality)
		extractor.grip() 
		self.log.append('Retrieving obtained data.')
		batch = spider_swarm.retrieve_batch()
		self.log.append('\ndone.')

		return batch



	def run(self):

		print('\n Issuing a new extraction...\n')
	
		data_batch = pd.DataFrame({})
		data_batch = self.ingest()

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