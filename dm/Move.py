import numpy as np
from State import State

class Move(State):
    def __init__(self, resources, infrastructure, ioValues, probability, category):
        super().__init__(resources, infrastructure)
        self.ioValues = ioValues
        self.probability = probability
        sum = 0
        for key, value in resources.items():
            sum += value
        self.sum = sum
        self.risk = probability * abs(sum)
        self.category = category
    '''
    given by monte carlo - gets the state resulting from this move being made by sampling a distribution
    '''
    def getPossibleState(self, curState):
        # TODO: DO THIS
        resources = {}
        for i in curState.resources:
            resources[i] = curState.resources[i] - self.resources[i]

        infrastructure = {}

        for i in curState.infrastructure:
            infrastructure[i] = curState.infrastructure[i] - self.infrastructure[i]
        return State(resources, infrastructure)

    def compare(self, other):
        return np.sum([abs(self.resources[i] - other.resources[i]) for i in range(0, len(self.resources))])


'''
move = Move({"PDRLEG": 4}, {"Oil Refineries": 5})
print(move.getMeasure("Oil Refineries", category = "i"))
print("Updating Measure")
move.updateMeasure("Oil Refineries", 12, category = "i")
print(move.getMeasure("Oil Refineries", category = "i"))
test = "Hell OOOOOO World"
print(formatMeasure(test))
'''
