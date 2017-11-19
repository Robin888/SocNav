import numpy as np
from dm.State import State
from dm import risk_calculation


class Move(State):
    def __init__(self, code, move_name, move_type, IO_list,
                 ph, low_resources, med_resources,
                 high_resources, infrastructure, category):
        super().__init__(self.resources, infrastructure)
        self.category = category
        self.code = code
        self.move_name = move_name
        self.move_type = move_type
        self.IO = IO_list
        self.ph = ph
        self.resourcesCategories = {"low": low_resources,
                                    "med": med_resources,
                                    "high": high_resources}

        self.infrastructure = infrastructure
        self.probability = -1  # unassigned
        self.risk = -1  # unassigned
        self.one_hot = risk_calculation.resource_encoding(
            self.resourcesCategories)  # a one hot vector representation of teh resources
        self.sum = 0
        self.resources = self.one_hot
        for value in self.one_hot:
            self.sum += value

    def getPossibleState(self, curState):
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
