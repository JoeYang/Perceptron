import sys
import csv

class PerceptronModel:
  
  class TrainSplit:
    def __init__(self):
      self.train = []
      self.test = []
  class Instance:
  	def __init__(self, index, list_of_features):
  	  self.index	= index
  	  self.features = []
  	  for feature_index in range(3, len(list_of_features) -1):
  	  	try:
  	  	  self.features.append(float(list_of_features[feature_index]))
  	  	except:
  	  	  self.features.append(0)  
  	  self.real_tag = list_of_features[-1]  
  	def get_num_of_features(self):
  	  return len(self.features)
  class Klass:
  	def __init__(self, name):
  	  self.name = name
  	  self.new_weights = []
  	  self.weights = []
  	  self.average_weights = []
  	  self.num_interations = 0
  	  self.num_of_features = 1555
  	  for i in range(0, self.num_of_features):
  	  	self.weights.append(0) 
  	  	self.new_weights.append(0)
  	  	self.average_weights.append(0)
  	
  	def cleanup(self, flag):
  	  if flag == 1:
  	    for i in range(0, self.num_of_features):
  	  	  self.weights[i] = (self.weights[i]*self.num_interations + self.new_weights[i])/(self.num_interations+1)
  	  	  self.new_weights[i] = 0
  	  #print self.weights	  
  	  self.num_interations += 1	
  	def reset(self):  
  	  for i in range(0, self.num_of_features):
  	  	self.weights[i] = 0 
  	  	self.new_weights[i] = 0 
  	  	self.average_weights[i] = 0 
  
  def __init__(self):
  	self.instances = []
  	self.klasses = []
  	self.klasses.append(self.Klass("ad."))
  	self.klasses.append(self.Klass("nonad."))
  	self.num_of_folds = 10
  	self.num_of_features = 1555
  
  def readDate(self):
  	f = csv.reader(open("ad-dataset/ad.data", "r"), delimiter = ',')
  	index = 0
  	for line in f:
  	  self.instances.append(self.Instance(index, line))
  
  def crossValidationSplits(self):
  	splits = []
  	print  '-'*20, "building cross validation splits", '-'*20
  	for fold in range(0, self.num_of_folds): 		
  	  split = self.TrainSplit()
  	  length = len(self.instances)
  	  for i in range(0, length):
  	  	if i % self.num_of_folds == fold:
  	  	  split.train.append(self.instances[i])
  	  	else:
  	  	  split.test.append(self.instances[i])
  	  splits.append(split)
  	return splits
  def reset(self):
  	for klass in self.klasses:
  	  klass.reset()	
  
  def test(self, split):	
  	total = len(split.test)
  	TP = 0.0
  	FP = 0.0
  	FN = 0.0
  	for instance in split.test:
  	  klass = self.classify(instance)
  	  if klass.name == 'ad.':
  	  	if instance.real_tag == 'ad.':
  	  	  TP += 1.0
  	  	else:
  	  	  FN += 1.0
  	  if klass == "nonad.":
  	  	if instance.real_tag == "ad.":
  	  	  FP += 1
  	P = TP/(TP + FP)
  	R = TP/(TP + FN)
  	print "Accuracy", P,
	print "Recall  ", R,
	print "F-score ", 2*P*R/(P + R)
  
  def classify(self, instance):
  	best_score = -100000
  	maximum_likely_klass = self.klasses[0]
  	for klass in self.klasses:
  	  score = 0
  	  for i in range(0, self.num_of_features):
  	  	score += klass.weights[i] * instance.features[i]
  	  if score > best_score:
  	  	best_score = score
  	  	maximum_likely_klass = klass
  	return maximum_likely_klass
  
  def train(self, split):
  	iteration = 0
  	total = len(split.train)
  	while iteration < 20:
  	  error = 0
  	  for instance in split.train:
  	  	klass = self.get_correct_klass(instance.real_tag)
  	  	guess = self.classify(instance)
  	  	if guess.name != klass.name:
  	  	  error += 1	
  	  	  for i in range(0, self.num_of_features):
  	  	  	if iteration > 10:
  	  	  	  klass.new_weights[i] = klass.weights[i] + (klass.weights[i]-guess.weights[i])*instance.features[i]
  	  	  	else:
  	  	  	  klass.weights[i] = klass.weights[i] + instance.features[i]*0.1
  	  	  klass.cleanup(1)
  	  	else:
  	  	  klass.cleanup(0)
  	  #print "Iteration:", iteration,"--Accuracy", total, error  
  	  iteration += 1
  	 


  def get_correct_klass(self, name):
  	for klass in self.klasses:
  	  if klass.name == name:
  	  	return klass
  	return None  	


  def function_test(self):
  	instance = self.instances[0]
  	print instance.index, instance.features, instance.real_tag, instance.get_num_of_features()	

def main():
  pm = PerceptronModel()
  pm.readDate()
  splits = pm.crossValidationSplits()
  index = 1
  for split in splits:
  	print "Cross Validation", index, ":",
  	pm.train(split)
  	pm.test(split)
  	pm.reset()
  	index += 1

if __name__=="__main__":
  main()