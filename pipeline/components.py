
import sys
import json


from extractors import extractor as ext
import pandas as pd
from nltk.tokenize import MWETokenizer



"""
The extract module performs loading operations over an specified extraction domain. 

License: ThisIsMyStuffBitch

"""



class Extract:


	def __init__(self, config):
			
		self.log = []
		self.extractor_scheme = config.extractor_scheme



	def ingest(self, verbose = False):

		batch = pd.DataFrame({})
		if verbose == True: self.log.append('Issuing a new extraction...\n')

		extractor = ext.create_extractor('Reddit01',self.extractor_scheme)
		extractor.grip() 
		if verbose == True: self.log.append('Retrieving obtained data.')
	
		batch = extractor.retrieve_batch()
		if verbose == True: self.log.append('Batch specs = ', batch.describe())
		if verbose == True: for line in self.log: print(line)

		return batch



	def run(self):

		print('\nRunning...\n')

		data_batch = pd.DataFrame({})
		data_batch = self.ingest()

		print('\nThe data batch is now inside the pipeline!')
		print('\nReady to perform preparation procedures...')

		return data_batch





class Transform:


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



class Load:

	def __init__(self, params):
		pass

	def run(self):
		pass




if __name__ == '__main__':
	pass