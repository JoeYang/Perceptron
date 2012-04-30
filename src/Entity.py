import collections
from Klass import Klass

class Entity:
  
  def __init__(self, name):
  	self.name = name
  	self.__dir__ = "../data/comp5406-articles/"
  	self.list_of_votes = collections.defaultdict(lambda:0)
  	self.label = None
  	self.txt = self.__dir__ + name + ".txt"
  	self.mw = self.__dir__ + name + ".mw"
  	self.json = self.__dir__ + name + ".json"
  
  def get_name(self):
  	return self.name

  def vote(self, category):
  	self.list_of_votes[category] += 1

  def get_klass(self):
  	num_votes = 0
  	best_label = None
  	for label in self.list_of_votes:
  	  if self.list_of_votes[label] > num_votes:
		num_votes = self.list_of_votes[label]
  	  	best_label = label
  	self.label = best_label	
  
  def readFile(self):
  	pass

  


