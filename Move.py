import numpy as np
from State import State

class Move(State):
    def __init__(self, resources, infrastructure, ioParams):
        super().__init__(resources, infrastructure)
        self.ioParams = ioParams
    '''
    given by monte carlo - gets the state resulting from this move being made by sampling a distribution
    '''
    def getPossibleState(self, curState):
        # TODO:
        pass

    def compare(self, other):
        return np.sum([abs(self.pmesiiVars[i] - other.pmesiiVars[i]) for i in range(0, len(self.pmesiiVars))])

    def getIOValue(self, name):
        for param in self.ioParams:
            if param.name == name:
                return param
        return None
'''
move = Move({"PDRLEG": 4}, {"Oil Refineries": 5})
print(move.getMeasure("Oil Refineries", category = "i"))
print("Updating Measure")
move.updateMeasure("Oil Refineries", 12, category = "i")
print(move.getMeasure("Oil Refineries", category = "i"))
test = "Hell OOOOOO World"
print(formatMeasure(test))
'''
