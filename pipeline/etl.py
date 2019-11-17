
#License: ThisIsMyStuffBitch

import sched
import time
from datetime import datetime, timedelta



class Pipeline:


	#loading the pipe processing modules 

	def __init__ (self, extract, transform,load)
		
		self.extract = extract
		self.transform = transform
		self.load = load


	def get_batch(self):

		print('Initializing extraction session...')
		
		
		self.load.run(self.transform.run(self.extract.run()))
		print('done.')


	def schedule(self):
		pass




if __name__ == '__main__':
	pass