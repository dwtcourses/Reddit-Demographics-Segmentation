
import sys
sys.path.append('/data_source/spiders.py')

import spiders


"""
The extract module performs loading operations over an specified extraction domain. 

License: ThisIsMyStuffBitch

"""

dev_mode = True


class Extractor:

	def __init__(self, command):
		pass

	"""
	Will perform different extraction schemes depending on the ETL configuration
	
	"""	
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

	
	def extract(self):
		pass

		

	def transform(self):
		pass



	def load(self):
		pass



if __name__ == '__main__':
	pass