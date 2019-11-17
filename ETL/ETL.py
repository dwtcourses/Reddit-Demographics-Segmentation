
import sys
sys.path.append('/data_source/spiders.py')

import spiders
import datetime


"""
The extract module performs loading operations over an specified extraction domain. 

License: ThisIsMyStuffBitch

"""

dev_mode = True


class Extractor:

	def __init__(self, command):

		self.cycle_time = command.schedule #how many hours have to pass between batch extractions
		self.last_batch = None #an hour of the day



	
	#Will perform different extraction schemes depending on the ETL configuration
	def extraction_source_table(self):

		if self.command.source == 'WS':
			pass
		elif self.command.source == 'API_1'
			pass




class Transforms:

	def __init__(self, command):
		pass





class Loader:
	def __init__(self, command):
		pass




class Pipeline:

	#loading the processing modules to the pipe
	def __init__ (self, extract, transform,load)
		self.extract = extract
		self.transform = transform
		self.load = load
		self.date = None

	
	def extract(self):
		pass

		
	def transform(self):
		pass


	def load(self):
		pass



	def get_batch(self):
		
		now = datetime.now()
		passed_time = now - self.extract.last_batch

		if passed_time >= self.extract.cycle_time:

			extract(self)
			transform(self) 
			load(self)

			self.extract.last_batch = datetime.now()






if __name__ == '__main__':
	pass