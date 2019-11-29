
#License: ThisIsMyStuffBitch

import sched
import time
from datetime import datetime, timedelta



class Pipeline:


	#loading the pipe processing modules 

	def __init__ (self,type_, extract, transform,load)
		
		self.extract = extract
		self.transform = transform
		self.load = load
		self.type = type_


	def get_batch(self):

		print('Issuing a new batch order.')
		
		if self.type == 'etl':
		
			self.load.run(self.transform.run(self.extract.run()))

		elif self.type == 'elt':

			self.transform.run(self.load.run(self.extract.run()))
		
		else:
			exit(0)


		print('done.')



	def run(self):
		while True:
			pass 
			#scheduling stuff



if __name__ == '__main__':
	pass