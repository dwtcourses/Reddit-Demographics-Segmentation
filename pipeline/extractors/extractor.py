
#Wrapping all the designed extractors around the same interface 
from swarm import Swarm 
from reddit import RedditAPI



def create_extractor(type_, name, config):
	pass



class Extractor:


	def __init__(self, type_, name, config):
		
		self.log = []
		self.type = type_
		self.name = name
		self.config = config
		self.create()


	def create(self):
		pass


	def grip(self):
		pass


	def retrieve_batch(self):
		pass





if __name__ == '__main__':
	pass