
import sys
sys.path.append('/data_source/spiders.py')

import spiders

import sched
import time
from datetime import datetime, timedelta


"""
The extract module performs loading operations over an specified extraction domain. 

License: ThisIsMyStuffBitch

"""

dev_mode = True


class Extractor:

	def __init__(self, command):

		self.cycle_time = command.schedule #how many hours have to pass between batch extractions
		self.last_batch = None #an hour of the day
		self.num_batches = command.num_batches

	
	#Will perform different extraction schemes depending on the ETL configuration
	def extractors_table(self):

		if self.command.source == 'WS':
			pass
		elif self.command.source == 'API_1'
			pass

	def run(self):
		pass


class Transforms:

	def __init__(self, command):
		self.transformations = command.transformations



	def run(self):
		pass
		


class Loader:

	def __init__(self, command):
		pass

	def run(self):
		pass



if __name__ == '__main__':
	pass