import sys
import csv
import json
from Klass import Klass
from Entity import Entity

class DataReader:
  def __init__(self):
  	self.title_file = "../data/comp5046-titles.txt"
  	self.label_file = "../data/comp5046-labels.tsv"
  	self.list_of_entities = []
  	self.klassLabels = []
  	self.readTitles()
  	self.readLabels()
  	self.test()

  def readTitles(self):
  	titleFile = open(self.title_file, "r")
  	for line in titleFile:
  	  newEntity = Entity(line.split()[0])
  	  self.list_of_entities.append(newEntity)
  
  def readLabels(self):
  	labelFile = csv.reader(open(self.label_file, "r"), delimiter = '	')
  	for label in labelFile:
  	  entity_name = label[0]
  	  label_name = label[1]
  	  entity = self.findEntity(entity_name)
  	  try:
  	  	entity.vote(label_name)
  	  except:
  	  	print "Warining:", entity_name, label_name, "NOT FOUND"
  	for entity in self.list_of_entities:
  	  entity.get_klass()  	

  def test(self):
  	entity = self.findEntity("127")
  	print entity.get_name(), entity.list_of_votes, entity.label, entity.json
  	
  def findEntity(self, entity_name):
  	for entity in self.list_of_entities:
  	  if entity.get_name() == entity_name:
  	  	return entity
  	return None  
  def get_list_of_entities(self):
  	return self.list_of_entities



