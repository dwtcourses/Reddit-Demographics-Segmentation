
#License: ThisIsMyStuffBitch

import sched
import time
from datetime import datetime, timedelta



class Pipeline:


	#loading the processing modules to the pipe
	def __init__ (self, extract, transform,load)
		
		self.extract = extract
		self.transform = transform
		self.load = load



	def get_batch(self):

		print('Initializing extraction session...')
		self.extract.run()
		self.transform.run() 
		self.load.run()
		print('done.')


	def schedule(self):
		pass




if __name__ == '__main__':
	pass