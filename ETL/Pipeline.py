
#License: ThisIsMyStuffBitch

class Pipeline:


	#loading the processing modules to the pipe
	def __init__ (self, extract, transform,load)
		
		self.extract = extract
		self.transform = transform
		self.load = load



	def get_batch(self):

		print('Initalizaing extraction session...')
		self.extract.run()
		self.transform.run() 
		self.load.run()
		print('done.')


	def scheduke(self):
		pass




if __name__ == '__main__':
	pass