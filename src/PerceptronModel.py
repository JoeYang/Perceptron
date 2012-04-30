from DataReader import DataReader

class PerceptronModel:
  class TrainSplit:
    def __init__(self):
      self.train = []
      self.test = []
  
  def __init__(self):
  	self.reader = DataReader()
  	self.list_of_entities = []
  	self.list_of_klasses = []
  	self.num_of_folds = 10
  	
  def readTitles(self):
  	self.list_of_entities = self.reader.get_list_of_entities()

  def crossValidationSplits(self):
  	splits = []
  	for fold in range(0, self.num_of_folds): 		
  	  split = self.TrainSplit()
  	  length = len(self.list_of_entities)
  	  for i in range(0, length):
  	  	if i % self.num_of_folds == fold:
  	  	  split.train.append(self.list_of_entities[i])
  	  	else:
  	  	  split.test.append(self.list_of_entities[i])
  	  splits.append(split)
  	return splits
  
  def classify(self, entity):
  	pass

  def train(self, split):
  	pass

  def test(self, split):
  	pass	

