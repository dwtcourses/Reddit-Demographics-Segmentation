
#Wrapping all the designed extractors around the same interface 

swarm_config_path = '/scrapers/config/swarm.txt'
api_config_path = '/scrapers/config/api_reddit.txt'



def load_deploy_commands(path):
    	
	deploy_commands = {}
	with open(path) as json_file:
   		deploy_commands = json.load(json_file)

	return deploy_commands



def create_scraper(type_, name):
	
	if type_ == 'swarm':
		pass

	elif type_ == 'praw':
		pass

	else:
		print('No scraper found with name = "', type_,'"')
		exit(0)



if __name__ == '__main__':
	pass