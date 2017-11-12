import numpy as np
from State import State

class Move(State):
    def __init__(self, code, move_name, move_type, IO_list,
                 ph, low_resources, med_resources,
                 high_resources, infrastructure):

        self.probability = probability
        sum = 0
        for key, value in resources.items():
            sum += value

        self.sum = sum
        self.risk = probability * abs(sum)
        self.category = category

        self.code = code
        self.move_name = move_name
        self.move_type = move_type
        self.IO = IO_list
        self.ph = ph
        self.resources = {"low": low_resources,
        "med": med_resources,
        "high": high_resources}

        self.infrastructure = infrastructure
        self.probability = -1  # unassigned
        self.risk = -1  # unassigned
        self.one_hot = []  # a one hot vector representation of teh resources

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

    def get_IO(self):
        return self.IO

    def get_code(self):
        return self.code

    def get_move_name(self):
        return self.move_name

    def get_move_type(self):
        return self.move_type

    def get_resources(self):
        return self.resources

    def get_infrastructure(self):
        return self.infrastructure

    def to_dic(self):
        move_dic = {"code": self.code,
                    "IO": self.IO,
                    "move_name": self.move_name,
                    "move_type": self.move_type,
                    "ph": self.ph,
                    "resources": self.resources,
                    "infrastructure": self.infrastructure}
        return move_dic
