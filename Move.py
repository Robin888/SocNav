import numpy as np
from utils import *

class Move:
	'Move class to express CAMEO moves in terms of Resources and Infrastructure'
	"""
	Attributes:
		resources: a dictionary expressing the change in resources caused by the move
		infrastructure: a dictionary expressing the change in infrastructure caused by the move
	"""
	def __init__(self, resources, infrastructure):
		self.resources = resources
		self.infrastructure = infrastructure

	"""
	Reads in the values of each resource measure and adds it to the resource dictionary
	"""
	def parseMeasures(self, filename):
		print ("WILL UPDATE ONCE I GET THE CSV FORMAT FROM THE SMRs")


	"""
	Used to get the measure of the resource or infrastructure from the respective dictionary
	'r' = resource
	'i' = infrastructure
	"""
	def getMeasure(self, measure, category = 'r'):
		measure = formatMeasure(measure)
		if category != 'r' and category != 'i':
			raise ValueError("Please input the category as either 'r', resources, or 'i', infrastructure")
		if category == "r" and measure not in self.resources:
			raise ValueError("'%s' not in resources" %measure)
		elif category == "i" and measure not in self.infrastructure:
			raise ValueError("%s not in infrastructure" %measure)

		else:
			if (category == "r"):
				return self.resources[measure]
			elif (category == "i"):
				return self.infrastructure[measure]

	"""
	Used to update the measure of the resource or infrastructure from the respective dictionary
	'r' = resource
	'i' = infrastructure
	"""
	def updateMeasure(self, measure, value, category = 'r'):
		measure = formatMeasure(measure)
		if category != 'r' and category != 'i':
			raise ValueError("Please input the category as either 'r', resources, or 'i', infrastructure")
		if category == "r" and measure not in self.resources:
			raise ValueError("'%s' not in resources" %measure)
		elif category == "i" and measure not in self.infrastructure:
			raise ValueError("%s not in infrastructure" %measure)
		else:
			if (category == "r"):
				self.resources[measure] = value
			elif (category == "i"):
				self.infrastructure[measure] = value


    '''
    given by monte carlo - gets the state resulting from this move being made by sampling a distribution
    '''
    def getPossibleState(self, curState):
        # TODO:
        pass

    def compare(self, other):
        return np.sum([abs(self.pmesiiVars[i] - other.pmesiiVars[i]) for i in range(0, len(self.pmesiiVars))])

'''
move = Move({"PDRLEG": 4}, {"Oil Refineries": 5})
print(move.getMeasure("Oil Refineries", category = "i"))
print("Updating Measure")
move.updateMeasure("Oil Refineries", 12, category = "i")
print(move.getMeasure("Oil Refineries", category = "i"))
test = "Hell OOOOOO World"
print(formatMeasure(test))
'''
