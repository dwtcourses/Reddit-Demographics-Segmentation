from components import *
from configurators import *
from pipeline import Pipeline


ex_config_path = '/config/extractor.txt'
tr_config_path = '/config/transform.txt'
ld_config_path = '/config/load.txt'



#License:ThisIsMyStuffBitch



def build_pipeline(type_):

	#we get the schemes from the pipeline specs file
	print('Getting architecture Specs...')
	extract_params =  ExtractionConfigurator(ex_config_path)
	transform_params = TransformConfigurator(tr_config_path)
	load_params = LoadingConfigurator(ld_config_path)

	print('Building...\n')
	#we can now build the ETL components
	extractor = Extract(extract_params)
	transformator = Transform(transform_params)
	loader = Load(load_params)

	pipeline = Pìpleline(type_, extractor, transformator, loader)

	print('done.')

	return pipeline



def start(pipeline_model):
	print('Pipeline now running...\n')
 	pipeline_model.run()




if __name__ == '__main__':
	etl = build_pipeline('etl')
	start(etl)


