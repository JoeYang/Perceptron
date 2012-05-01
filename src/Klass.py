

class Klass:  
  def __init__(self, klass_name):
  	self.name = klass_name
  	self.count = 0
  	self.type_1 = 0
  	self.type_2 = 0
  	self.weights = []
  
  def get_name(self):
  	return self.name

  def cal_precision(self):
  	return 0

  def cal_recall(self):
  	return 0

  def cal_f_score(self):
  	return 0				