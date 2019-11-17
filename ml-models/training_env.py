

from randomforest import *
from svm import *
from rnn import *
from lstm import *

import pandas as pd



def load_dataset():
	pass


def train_scikit_model(dataset):
	pass


def train_torch_model(dataset):
	pass


def run_cross_validation(dataset):
	pass




if __name__ == 'main' ():

	dataset = load_dataset()
	model = ''

		
	if model == 'randomforest' || model == 'svm':
			
		train_scikit_model(dataset)


	elif model == 'lstm' || model == 'rnn':

		train_torch_model(dataset)