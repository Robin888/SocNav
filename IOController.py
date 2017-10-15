class IOController:
    def __init__(self, parameters):
        self.parameters = sorted(parameters, key= lambda param: param.weight, reverse=True) #params automatically sorted in ascending order

    def act(self):
        # obtain list of moves from database or elsewhere
        sortedList = []
        for param in self.parameters:
            #sort by distance from each given value:
            sortedList = sorted(sortedList, key = lambda element: abs(element.getIOValue(param.name) - param.value))

        # do other work, such as updating poles and such.
        return sortedList