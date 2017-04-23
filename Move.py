import numpy as np
class Move:
    def __init__(self, pmesiiVars, probability, risk):
        self.pmesiiVars = pmesiiVars
        self.probability = probability
        self.risk = risk
    '''
    given by monte carlo - gets the state resulting from this move being made by sampling a distribution
    '''
    def getPossibleState(self, curState):
        # TODO:
        pass

    def compare(self, other):
        return np.sum([abs(self.pmesiiVars[i] - other.pmesiiVars[i]) for i in range(0, len(self.pmesiiVars))])
