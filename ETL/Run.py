from Components import *
from Commands import *
from ETL import *


#License:ThisIsMyStuffBitch



def build_pipeline():

	#we get the schemes from the pipeline specs file
	print('Getting achitecture Specs...')
	extract_params =  ExtractionCommand('placeholder')
	transform_params = TransformCommand('placeholder')
	load_params = LoadingCommand('placeholder')

	print('Building...\n')
	#we can now build the ETL components
	extract_comp = Extractor(extract_params)
	transform_comp = Transforms(transform_params)
	load_comp = Loader(load_params)

	pipeline = Pìpleline(extract_comp, transform_comp, load_comp))

	print('done.')

	return pipeline



def run(pipeline_model):

 	while True:
 		pipeline_model.get_batch()




if __name__ == '__main__':
	etl = build_pipeline()
	run(etl)


